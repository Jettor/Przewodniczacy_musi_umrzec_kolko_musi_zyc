# The script of the game goes in this file.

transform move_right_leo:
    xalign 0.0
    linear 0.6 xalign 0.3
transform move_right_iris:
    xalign 0.4
    linear 0.6 xalign 0.7

label start:
    play music "music background.mp3"
    scene bg classroom pink
        
    "So now you're here. Two weeks later, the first day of your second year, trying to keep your beloved video game club alive."
    "Well… it's not like you can blame the school for wanting to disband it. Last year ended on a really bad note."
    "Infighting basically left the club with no members… except for you. And as the only member, you've got yourself the role of the club president."    
    "The problem is, a measly five people signed up, and now you've got to convince them not to quit the second they figure out you have no idea what you're doing."
    "Speaking of… They will probably be here soon, so better get your shit together and make a good first impression."
    play sound "audio/door_opens.mp3"
    "As soon as you finish the thought, there's a light knocking on the door."
    show leo neutral with dissolve:
        yalign 0.18
    "???" "Hi, is this where the game club meets?"
    you "Hi! Yes, you’re in the right place. I’m \"Y/N\", the club president, nice to meet you."
    leo "My name is Leo, nice to meet you too."
    you "So how are you finding the school? Any cool people in your group?"
    "God, you sound like his mom."
    leo "It’s alright so far, I actually just got chosen as the group president, so I guess I must have made an okay impression, haha."
    menu:
        "Wow, you must be amazing!":
            $leo_aff -= 1
            jump amazing
        "That seems like a lot of pressure":
            $leo_aff +=1
            jump pressure

label amazing:
    #leo zakłopotanie
    leo "Thank you..."
    jump section2
label pressure:
    #leo surprised
    leo "Yeah, I guess you could say that."
    jump section2

label section2:
    "He looks around the empty room, and raises an eyebrow."
    leo "Is there anyone else coming?"
    "Quick! Distract him from the fact that he might be the only one to come."
    menu:
        "You're the first one here":
            jump first_one_here
        "{i}Show your dominance. Stay silent{/i}":
            $leo_aff -=1
            $zoe_aff +=1
            jump silent
        "Wow! You're so hot!":
            $leo_aff +=1
            jump hot

label first_one_here:
    you "You’re the first one here, ther-"
    jump section3

label silent:
    you "..."
    leo "..."
    jump section3

label hot:
    #show leo happy
    you "Wow! You’re so ho-"
    jump section3

label section3:
    "???" "Um… Actually… I’m also here?"
    show iris sad behind leo with dissolve:
        yalign -0.1
        xalign 0.4
    "You notice a small girl standing behind Leo"
    you "Oh! Sorry, I didn’t see you there."
    "???" "It’s okay, I’m used to it."
    you "So you’re here for the game club, right?"
    "At the mention of the game club, the girl visibly brightens up."
    #Iris happy
    iris "Yes… I’m Iris by the way."
    you "Great, so-"
    "You don't get to finish the sentence, when the door opens with a bang."
    play sound "audio/door_opens.mp3"
    show alex happy with dissolve:
        yalign 1
    show leo neutral at move_right_leo
    show iris sad at move_right_iris
    "???" "Hey losers, heard there was a nerd congregation happening over here!-"
    #wpadanie sfx
    #alex shocked
    "Apparently karma IS a bitch. The guy gets tackled to the floor by someone running at full speed through the entrance."
    show fern pokerface with dissolve:
        zoom 0.6
        yalign 1
    show alex angry
    alex "Ow! What the hell???"
    fern "Ayo sybau, loser."


   