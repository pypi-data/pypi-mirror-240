from fontinfo import FontInfo

def test_basic_instance():
    info = FontInfo()
    assert isinstance(info, FontInfo)