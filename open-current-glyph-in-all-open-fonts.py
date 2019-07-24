from mojo.UI import OpenGlyphWindow

g = CurrentGlyph()
    
for font in AllFonts():
    print(font)
    fontG = font[g.name]
    if fontG is not None:
        OpenGlyphWindow(fontG, newWindow=True)