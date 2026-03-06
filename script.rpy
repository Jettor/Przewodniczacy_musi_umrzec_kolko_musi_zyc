# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Maksym")
define c = Character("Ziomek", color="#f19ced")
# The game starts here.
label start:
    play music "music background.mp3"
    #call screen mapScreen
    scene bg classroom1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show razel

    # These display lines of dialogue.

    c "Meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow."

    show zacarias at left

    c "Meow meow meow meow!"

menu:
    "Meow meow":
        jump meow2

    "Meow meow meow":
        jump meow3

label meow2:
    scene bg torino
    with fade
    show maksym smug at center
    m "Meow meow meow meow meow meow meow meow meow meow me"
    m "Meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow."
    jump end

label meow3:
    scene bg ww2
    with fade
    show maksym serious at center
    pause 1
    show bg ww2_2 
    with fade
    pause 2
    show bg ww2_3 
    with fade
    m "Meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow."
    m "Meow meow meow meow meow meow meow meow meow meow."

label end:
    scene bg wsti1
    with fade
    show maksym silly at right
    with dissolve
    m "Meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow."
    m "Meow meow meow meow meow."

    return


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


   