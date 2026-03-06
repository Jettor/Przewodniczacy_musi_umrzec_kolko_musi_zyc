# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maksym")
define c = Character("Ziomek", color="#f19ced")
# The game starts here.

label start:
    play music "music background.mp3"
    call screen mapScreen

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


   