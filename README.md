# Work with complex fonts in RoboFont

The RoboFont docs have some good advice for working with big fonts.

This repo contains a few scripts which are slightly adapted for a workflow to work with many masters at once.

## Usage

Run `open-fonts-in-SimpleFontWindow.py` to select UFOs to open in simple font windows. These don't contain thumbnail previews of glyphs, and that speeds up editing significantly. This also opens up glyph `A` in all fonts, to make it easy to use editThatNextMaster.

The regular "Save All" function doesn't always work with simple font windows, so you can use `save-allfonts-in-simplefontwindows.py` to save all fonts at once.

Run `layersShowhideHotkey.py` to activate a hotkey `h`, which will show/hide background layers in all fonts. Currently, you need to run this each time you restart RoboFont, but that may change in the future.

## Recommendations

- Install the RoboFont extension [editThatNextMaster](https://github.com/LettError/editThatNextMasterRoboFontExtension) so you can cycle through glyphs easily.