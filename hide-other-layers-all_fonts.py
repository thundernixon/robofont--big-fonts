# Hide other layers for all open fonts

currentLayerName = CurrentLayer().name


print(CurrentLayer().getDisplayOption())

for f in AllFonts():
    for layer in f.layers:
        if layer.name != currentLayerName:
            
            # layer.setDisplayOption('all', False)
            
            layer.setDisplayOption('Fill', False) 
            layer.setDisplayOption('Stroke', True)
            layer.setDisplayOption('Points', True)
            layer.setDisplayOption('Coordinates', False) 
            layer.setDisplayOption('all', False)

            
            # do I need something like this?
            layer.changed()
            
            
            print(CurrentLayer().getDisplayOption())
