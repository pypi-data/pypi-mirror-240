"""
Define a data structure to exchange basic font information
between database, sources files and binary fonts
"""
from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any, Iterable

import yaml
from otSpec.table import OS2, head
from otSpec.table import name as ot_name

if TYPE_CHECKING:
    from fontTools.ttLib import TTFont
    from collections.abc import KeysView

__version__ = "0.1.1"

log = logging.getLogger(__name__)

NoneType = type(None)
positive_number = lambda i: i >= 0
int_or_None = (int, NoneType)
str_or_None = (str, NoneType)

# Map TTFont (fontTools font) attributes to FontInfo attributes
ttfont_to_info_mapping = {
    "head": {"unitsPerEm": "UPM"},
    "hhea": {
        "ascender": "hheaAscender",
        "descender": "hheaDescender",
        "lineGap": "hheaLineGap",
    },
    "OS/2": {
        "sCapHeight": "CapHeight",
        "sxHeight": "xHeight",
        "sTypoAscender": "TypoAscender",
        "sTypoDescender": "TypoDescender",
        "sTypoLineGap": "TypoLineGap",
        "yStrikeoutSize": "StrikeoutSize",
        "yStrikeoutPosition": "StrikeoutPosition",
        "ySubscriptXSize": "SubscriptXSize",
        "ySubscriptYSize": "SubscriptYSize",
        "ySubscriptXOffset": "SubscriptXOffset",
        "ySubscriptYOffset": "SubscriptYOffset",
        "ySuperscriptXSize": "SuperscriptXSize",
        "ySuperscriptYSize": "SuperscriptYSize",
        "ySuperscriptXOffset": "SuperscriptXOffset",
        "ySuperscriptYOffset": "SuperscriptYOffset",
        "usWidthClass": "OS2widthClass",
        "usWeightClass": "OS2weightClass",
        "usWinAscent": "WinAscender",
        "usWinDescent": "WinDescender",
    },
    "post": {
        "italicAngle": "ItalicAngle",
        "underlineThickness": "UnderlineSize",
        "underlinePosition": "UnderlinePosition",
        "isFixedPitch": "FixedPitch",
    },
    "name": {
        ot_name.ID_COPYRIGHT: "Copyright",
        ot_name.ID_FAMILY: "FamilyName",
        ot_name.ID_SUBFAMILY: "StyleName",
        ot_name.ID_FONT_IDENTIFIER: "FontIdentifier",
        ot_name.ID_FULL_NAME: "FullName",
        ot_name.ID_VERSION: "VersionString",
        ot_name.ID_POSTSCRIPT_NAME: "PostScriptName",
        ot_name.ID_TRADEMARK: "Trademark",
        ot_name.ID_MANUFACTURER: "Manufacturer",
        ot_name.ID_DESIGNER: "Designer",
        ot_name.ID_DESCRIPTION: "FontDescription",
        ot_name.ID_VENDOR_URL: "VendorURL",
        ot_name.ID_DESIGNER_URL: "DesignerURL",
        ot_name.ID_LICENSE: "LicenseText",
        ot_name.ID_LICENSE_URL: "LicenseURL",
        ot_name.ID_TYPOGRAPHIC_FAMILY: "OTfamilyName",
        ot_name.ID_TYPOGRAPHIC_SUBFAMILY: "OTstyleName",
        ot_name.ID_COMPATIBLE_FULL_NAME: "OTmacName",
        ot_name.ID_WWS_FAMILY: "WWSfamilyName",
        ot_name.ID_WWS_SUBFAMILY: "WWSstyleName",
    },
}

# Map UFO font attributes to FontInfo attributes
ufo_to_info_mapping = {
    "versionMajor": "VersionMajor",
    "versionMinor": "VersionMinor",
    "unitsPerEm": "UPM",
    "capHeight": "CapHeight",
    "xHeight": "xHeight",
    "italicAngle": "ItalicAngle",
    # "postscriptSlantAngle": "SlantAngle",
    "copyright": "Copyright",  #                            ID  0
    "styleMapFamilyName": "FamilyName",  #                  ID  1
    "styleMapStyleName": "StyleName",  #                    ID  2
    "openTypeNameUniqueID": "FontIdentifier",  #            ID  3
    "postscriptFullName": "FullName",  #                    ID  4
    "openTypeNameVersion": "VersionString",  #              ID  5
    "postscriptFontName": "PostScriptName",  #              ID  6
    "trademark": "Trademark",  #                            ID  7
    "openTypeNameManufacturer": "Manufacturer",  #          ID  8
    "openTypeNameDesigner": "Designer",  #                  ID  9
    "openTypeNameDescription": "FontDescription",  #        ID 10
    "openTypeNameManufacturerURL": "VendorURL",  #          ID 11
    "openTypeNameDesignerURL": "DesignerURL",  #            ID 12
    "openTypeNameLicense": "LicenseText",  #                ID 13
    "openTypeNameLicenseURL": "LicenseURL",  #              ID 14
    "openTypeNamePreferredFamilyName": "OTfamilyName",  #   ID 16
    "familyName": "OTfamilyName",  #                        ID 16
    "openTypeNamePreferredSubfamilyName": "OTstyleName",  # ID 17
    "styleName": "OTstyleName",  #                          ID 17
    "openTypeNameCompatibleFullName": "OTmacName",  #       ID 18
    "openTypeNameWWSFamilyName": "WWSfamilyName",  #        ID 21
    "openTypeNameWWSSubfamilyName": "WWSstyleName",  #      ID 22
    "openTypeHheaAscender": "hheaAscender",
    "openTypeHheaDescender": "hheaDescender",
    "openTypeHheaLineGap": "hheaLineGap",
    "openTypeOS2TypoAscender": "TypoAscender",
    "openTypeOS2TypoDescender": "TypoDescender",
    "openTypeOS2TypoLineGap": "TypoLineGap",
    "openTypeOS2WinAscent": "WinAscender",
    "openTypeOS2WinDescent": "WinDescender",
    "openTypeOS2SubscriptXSize": "SubscriptXSize",
    "openTypeOS2SubscriptYSize": "SubscriptYSize",
    "openTypeOS2SubscriptXOffset": "SubscriptXOffset",
    "openTypeOS2SubscriptYOffset": "SubscriptYOffset",
    "openTypeOS2SuperscriptXSize": "SuperscriptXSize",
    "openTypeOS2SuperscriptYSize": "SuperscriptYSize",
    "openTypeOS2SuperscriptXOffset": "SuperscriptXOffset",
    "openTypeOS2SuperscriptYOffset": "SuperscriptYOffset",
    "openTypeOS2StrikeoutSize": "StrikeoutSize",
    "openTypeOS2StrikeoutPosition": "StrikeoutPosition",
    "openTypeOS2WidthClass": "OS2widthClass",
    "openTypeOS2WeightClass": "OS2weightClass",
    "postscriptIsFixedPitch": "FixedPitch",
    "postscriptUnderlineThickness": "UnderlineSize",
    "postscriptUnderlinePosition": "UnderlinePosition",
}


class FontInfo:
    attributes = {
        # "name" : (type, validator)
        "VersionMajor": (int, None),
        "VersionMinor": (int, None),
        "Copyright": (str_or_None, None),
        "FamilyName": (str_or_None, None),
        "StyleName": (str_or_None, None),
        "FontIdentifier": (str_or_None, None),
        "FullName": (str_or_None, None),
        "VersionString": (str_or_None, None),
        "PostScriptName": (str_or_None, None),
        "Trademark": (str_or_None, None),
        "Manufacturer": (str_or_None, None),
        "Designer": (str_or_None, None),
        "FontDescription": (str_or_None, None),
        "VendorURL": (str_or_None, None),
        "DesignerURL": (str_or_None, None),
        "LicenseText": (str_or_None, None),
        "LicenseURL": (str_or_None, None),
        "OTfamilyName": (str_or_None, None),
        "OTstyleName": (str_or_None, None),
        "OTmacName": (str_or_None, None),
        "WWSfamilyName": (str_or_None, None),
        "WWSstyleName": (str_or_None, None),
        "UPM": (int, positive_number),
        "CapHeight": (int, positive_number),
        "xHeight": (int, positive_number),
        "ItalicAngle": (float, None),
        # "SlantAngle": (float, None),
        "TypoAscender": (int, positive_number),
        "TypoDescender": (int, None),
        "TypoLineGap": (int, positive_number),
        "hheaAscender": (int, positive_number),
        "hheaDescender": (int, None),
        "hheaLineGap": (int, positive_number),
        "WinAscender": (int, positive_number),
        "WinDescender": (int, positive_number),
        "UnderlineSize": (int, positive_number),
        "UnderlinePosition": (int, None),
        "StrikeoutSize": (int, positive_number),
        "StrikeoutPosition": (int, positive_number),
        "SubscriptXSize": (int, positive_number),
        "SubscriptYSize": (int, positive_number),
        "SubscriptXOffset": (int, None),
        "SubscriptYOffset": (int, None),
        "SuperscriptXSize": (int, positive_number),
        "SuperscriptYSize": (int, positive_number),
        "SuperscriptXOffset": (int, None),
        "SuperscriptYOffset": (int, None),
        "OS2widthClass": (int, lambda c: 0 < c < 10),
        "OS2weightClass": (int, lambda c: 0 < c < 1001),
        "FixedPitch": (bool, None),
        "IsItalic": (bool, None),
        "IsBold": (bool, None),
        "UseTypoMetric": (bool, None),
    }

    def __init__(self, **kwargs):
        object.__setattr__(self, "_data", {})
        for name, value in kwargs.items():
            self.__setattr__(name, value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} with {len(self)} attributes>"

    def __str__(self) -> str:
        return self.yaml

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self.attributes:
            raise AttributeError(f"FontInfo attribute '{name}' not allowed.")
        attrType, valid = self.attributes[name]
        if isinstance(value, attrType):
            _value = value
        else:
            try:
                _value = attrType(value)
            except ValueError:
                raise ValueError(
                    f"Value '{value}' for FontInfo attribute '{name}' can't be converted to {attrType}."
                )
        if valid is None or valid(_value):
            self._data[name] = _value
        else:
            raise ValueError(
                f"Invalid value '{_value}' for FontInfo attribute '{name}'."
            )

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"FontInfo attribute '{name}' not defined.")

    def __delattr__(self, name: str):
        if name in self._data:
            del self._data[name]

    def __setitem__(self, key: str, value: Any):
        self.__setattr__(key, value)

    def __getitem__(self, key: str) -> Any:
        return self._data[key]

    def __delitem__(self, key: str):
        del self._data[key]

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterable[str]:
        return self._data.__iter__()

    def __contains__(self, key) -> bool:
        return key in self._data

    def keys(self) -> KeysView:
        return self._data.keys()

    def has_key(self, name: str) -> bool:
        return name in self._data

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    @classmethod
    def from_TTFont(cls, ttfont: TTFont) -> FontInfo:
        info = cls()
        for tableTag, mapping in ttfont_to_info_mapping.items():
            table = ttfont[tableTag]
            if tableTag == "name":
                for nameID in mapping:
                    # try Win-Unicode first
                    namerecord = table.getName(
                        nameID, ot_name.PLATFORM_WIN, ot_name.WIN_UNI
                    )
                    if not namerecord:
                        # try Mac-Roman if Win-Unicode is not available
                        namerecord = table.getName(
                            nameID, ot_name.PLATFORM_MAC, ot_name.MAC_ROMAN
                        )
                    if namerecord:
                        info[mapping[nameID]] = namerecord.toStr()
            else:
                for attribute in mapping:
                    info[mapping[attribute]] = getattr(table, attribute)
                if tableTag == "head":
                    info.VersionMajor = int(table.fontRevision // 1)
                    info.VersionMinor = round(table.fontRevision % 1 * 1000)
                elif tableTag == "post":
                    info.ItalicAngle = round(table.italicAngle, 1)
                elif tableTag == "OS/2":
                    info.IsBold = bool(table.fsSelection & OS2.fsSelection_BOLD)
                    info.IsItalic = bool(table.fsSelection & OS2.fsSelection_ITALIC)
                    info.UseTypoMetric = bool(
                        table.fsSelection & OS2.fsSelection_USE_TYPO_METRICS
                    )
        return info

    def to_TTFont(self, ttfont: TTFont) -> None:
        for tableTag, mapping in ttfont_to_info_mapping.items():
            table = ttfont[tableTag]
            if tableTag == "name":
                for nameID, info_attr in mapping.items():
                    if info_attr in self:
                        if self[info_attr] is None:
                            table.removeNames(nameID)
                        else:
                            if nameID not in (ot_name.ID_COMPATIBLE_FULL_NAME,):
                                table.setName(
                                    self[info_attr],
                                    nameID,
                                    ot_name.PLATFORM_WIN,
                                    ot_name.WIN_UNI,
                                    ot_name.WIN_ENGLISH,
                                )
                            table.setName(
                                self[info_attr],
                                nameID,
                                ot_name.PLATFORM_MAC,
                                ot_name.MAC_ROMAN,
                                ot_name.MAC_ENGLISH,
                            )
            else:
                for ttfont_attr, info_attr in mapping.items():
                    if info_attr in self:
                        setattr(table, ttfont_attr, self[info_attr])
                if tableTag == "head":
                    if "VersionMajor" in self and "VersionMinor" in self:
                        table.fontRevision = round(
                            self.VersionMajor + self.VersionMinor / 1000, 3
                        )
                    if "IsItalic" in self:
                        if self.IsItalic and not (
                            table.macStyle & head.macStyle_ITALIC
                        ):
                            table.macStyle |= head.macStyle_ITALIC
                        elif not self.IsItalic and (
                            table.macStyle & head.macStyle_ITALIC
                        ):
                            table.macStyle -= head.macStyle_ITALIC
                    if "IsBold" in self:
                        if self.IsBold and not (table.macStyle & head.macStyle_BOLD):
                            table.macStyle |= head.macStyle_BOLD
                        elif not self.IsBold and (table.macStyle & head.macStyle_BOLD):
                            table.macStyle -= head.macStyle_BOLD
                elif tableTag == "OS/2":
                    if table.version < 3:
                        table.version = 3
                    if self.UseTypoMetric:
                        table.fsSelection |= OS2.fsSelection_USE_TYPO_METRICS
                        table.version = 4
                    else:
                        table.fsSelection &= ~OS2.fsSelection_USE_TYPO_METRICS
                    # if not self.WWSfamilyName and not self.WWSstyleName:
                    #     table.fsSelection |= OS2.fsSelection_WWS
                    if "IsItalic" in self:
                        if self.IsItalic and not (
                            table.fsSelection & OS2.fsSelection_ITALIC
                        ):
                            table.fsSelection |= OS2.fsSelection_ITALIC
                            table.fsSelection &= ~OS2.fsSelection_REGULAR
                        elif not self.IsItalic and (
                            table.fsSelection & OS2.fsSelection_ITALIC
                        ):
                            table.fsSelection -= OS2.fsSelection_ITALIC
                    if "IsBold" in self:
                        if self.IsBold and not (
                            table.fsSelection & OS2.fsSelection_BOLD
                        ):
                            table.fsSelection |= OS2.fsSelection_BOLD
                            table.fsSelection &= ~OS2.fsSelection_REGULAR
                        elif not self.IsBold and (
                            table.fsSelection & OS2.fsSelection_BOLD
                        ):
                            table.fsSelection -= OS2.fsSelection_BOLD

    @classmethod
    def from_UFO(cls, ufofont) -> FontInfo:
        """Creates fontinfo object from UFO

        :param ufofont: UFO font source
        :type ufofont: defcon.Font or simmilar
        :return: fontinfo instance
        :rtype: FontInfo
        """
        info = cls()
        ufoInfo = ufofont.info
        for ufo_attr, info_attr in ufo_to_info_mapping.items():
            if hasattr(ufoInfo, ufo_attr):
                value = getattr(ufoInfo, ufo_attr)
                if value is not None:
                    if ufo_attr == "styleMapStyleName":
                        info[info_attr] = value.title()
                        info["IsItalic"] = "italic" in value
                        info["IsBold"] = "bold" in value
                    else:
                        info[info_attr] = value
        if hasattr(ufoInfo, "openTypeOS2Selection") and isinstance(
            ufoInfo.openTypeOS2Selection, (list, tuple)
        ):
            info.UseTypoMetric = 7 in ufoInfo.openTypeOS2Selection
        else:
            info.UseTypoMetric = False
        return info

    def to_UFO(self, ufofont) -> None:
        """Apply fontinfo from self to UFO font

        :param ufofont: UFO font target
        :type ufofont: defcon.Font or simmilar
        """
        ufoInfo = ufofont.info
        for ufo_attr, info_attr in ufo_to_info_mapping.items():
            log.debug("ufo: %r, info: %r", ufo_attr, info_attr)
            if info_attr in self:
                value = self[info_attr]
                log.debug(value)
                if ufo_attr == "styleMapStyleName":
                    setattr(ufoInfo, ufo_attr, value.lower())
                else:
                    setattr(ufoInfo, ufo_attr, value)
            elif (
                ufo_attr in ("familyName", "openTypeNamePreferredFamilyName")
                and "FamilyName" in self
            ):
                setattr(ufoInfo, ufo_attr, self["FamilyName"])
            elif (
                ufo_attr in ("styleName", "openTypeNamePreferredSubfamilyName")
                and "StyleName" in self
            ):
                setattr(ufoInfo, ufo_attr, self["StyleName"])
        # set openTypeOS2Selection
        if self.UseTypoMetric:
            if ufoInfo.openTypeOS2Selection is None:
                ufoInfo.openTypeOS2Selection = [7]
            elif 7 not in ufoInfo.openTypeOS2Selection:
                ufoInfo.openTypeOS2Selection.append(7)
        elif (
            not self.UseTypoMetric
            and ufoInfo.openTypeOS2Selection is not None
            and 7 in ufoInfo.openTypeOS2Selection
        ):
            ufoInfo.openTypeOS2Selection.remove(7)
        if (
            ("WWSfamilyName" in self and self.WWSfamilyName)
            or ("WWSstyleName" in self and self.WWSstyleName)
        ) and 8 in ufoInfo.openTypeOS2Selection:
            ufoInfo.openTypeOS2Selection.remove(8)
        elif (
            ("WWSfamilyName" not in self or not self.WWSfamilyName)
            and ("WWSstyleName" not in self or not self.WWSstyleName)
            and 8 not in ufoInfo.openTypeOS2Selection
        ):
            ufoInfo.openTypeOS2Selection.append(8)

    @property
    def yaml(self) -> str:
        """
        :return: yaml representation of font info
        :rtype: str
        """
        return yaml.dump(self._data)

    @property
    def json(self) -> str:
        """
        :return: json representation of font info
        :rtype: str
        """
        return json.dumps(self._data, indent=4)

    def save(self, path: str, format: str = "") -> None:
        """Save fontinfo to file

        :param path: path to save at
        :param format: json or yaml, defaults to empty string. If not provided format is extracted from path.
        """
        _format = ""
        if format:
            if format.upper() == "JSON":
                _format = "json"
            elif format.upper() == "YAML":
                _format = "yaml"
        else:
            if path.upper().endswith(".JSON"):
                _format = "json"
            elif path.upper().endswith(".YAML"):
                _format = "yaml"
            else:
                _format = "json"
        with open(path, "wb") as infoFile:
            if _format == "json":
                infoFile.write(self.json.encode("utf-8"))
            elif _format == "yaml":
                infoFile.write(self.yaml.encode("utf-8"))

    def difference(self, other, selfLabel="self", otherLabel="other"):
        assert isinstance(other, FontInfo)
        result = {}
        for attr in self.attributes:
            if attr in self or attr in other:
                _self = self.get(attr)
                _other = other.get(attr)
                if _self != _other:
                    result[attr] = {selfLabel: _self, otherLabel: _other}
        return result
