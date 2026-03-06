label mapMenu:

    screen mapScreen:
        add "map towers.png"

        #Rim
        imagebutton:
            xpos 950
            ypos 120
            idle "rim idle.png"
            hover "rim hover.png"
            action Jump("room_rim")

        #Parter
        imagebutton:
            xpos 520
            ypos 970
            idle "parter idle.png"
            hover "parter hover.png"
            #action Jump("room_parter")

        #18.16
        imagebutton:
            xpos 930
            ypos 190
            idle "18_16 idle.png"
            hover "18_16 hover.png"
            action Jump("room_1816")
        
        #4 pietro/dziekanat
        imagebutton:
            xpos 1360
            ypos 750
            idle "4p idle.png"
            hover "4p hover.png"
            action Jump("room_dziekanat")