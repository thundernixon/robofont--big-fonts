
from mojo.UI import SetCurrentLayerByName
from mojo.events import addObserver, removeObserver
                     
class ShowHideLayers():
    
    """
    Startup Script:
        Assigns the "h" key to show/hide layer outlines across all open fonts.
        -- Modified from https://github.com/andyclymer/RoboFont-StartupScripts
    """

    def __init__(self):
        addObserver(self, "keyDown", "keyDown")
        
    def showHideOption(self, displayOptionKey, currentDisplayOptionValue):
        af = AllFonts()
        for f in af:
            for layerName in f.layerOrder:
                if not layerName == "foreground":
                    f.getLayer(layerName).setDisplayOption(displayOptionKey, not currentDisplayOptionValue)

    def keyDown(self, info):
        event = info["event"]
        characters = event.characters()
        modifierFlags = event.modifierFlags()
        if characters == "h":
            f = CurrentFont()
            if len(f.layerOrder) > 1:
                nextLayer = f.layerOrder[1]
                # Get the current display status for the first non-foreground layer
                currentDisplayOption = f.getLayer(nextLayer).getDisplayOption()["Stroke"]
                # show/hide stroke and points
                self.showHideOption("Stroke", currentDisplayOption)
                self.showHideOption("Points", currentDisplayOption)
                
                
ShowHideLayers()