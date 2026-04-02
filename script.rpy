# The script of the game goes in this file.

transform move_right:
    linear 0.6 xalign + 0.3
transform move_right_iris:
    xalign 0.4
    linear 0.6 xalign +0.7
transform move_right_again:
    linear 0.6 xalign + 0.7
transform move_right_again_iris:
    linear 0.6 xalign + 1.1

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
        zoom 0.9
        yalign 0.18
    unknown_leo "Hi, is this where the game club meets?"
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
    unknown_iris "Um… Actually… I’m also here?"
    show iris sad behind leo with dissolve:
        yalign -0.1
        xalign 0.4
    "You notice a small girl standing behind Leo"
    you "Oh! Sorry, I didn’t see you there."
    unknown_iris "It’s okay, I’m used to it."
    you "So you’re here for the game club, right?"
    "At the mention of the game club, the girl visibly brightens up."
    show iris happy
    iris "Yes… I’m Iris by the way."
    you "Great, so-"
    "You don't get to finish the sentence, when the door opens with a bang."
    play sound "audio/door_opens.mp3"
    show alex happy with dissolve:
        yalign 1
        zoom 0.5
    show leo neutral at move_right
    show iris happy at move_right_iris
    unknown_alex "Hey losers, heard there was a nerd congregation happening over here!-"
    #wpadanie sfx
    #alex shocked
    "Apparently karma IS a bitch. The guy gets tackled to the floor by someone running at full speed through the entrance."
    show alex angry at move_right:
        yalign 1
        zoom 1
    show leo neutral at move_right_again
    show iris happy at move_right_again_iris
    unknown_alex "Ow! What the hell???"
    show fern pokerface with dissolve:
        zoom 0.6
        yalign 1
    unknown_fern "Oh my god I’m so, SO sorry! Are you okay?"
    show alex freaky
    unknown_alex "Yeah, yeah. Not that I mind a little bit of homicide, but damn, for a small guy you hit me pretty hard."
    "Both of them get off the floor with only their egos bruised a bit. And thank god for that, you can't afford to lose any members."
    you "I'm guessing you're here for the club too?"
    alex "Yup, I'm Alex"
    fern "And I'm Fern, great to meet you all." #Uśmiech
    you "Well, it looks like we're almost all here, we're still waiting for one person. Meanwhile the five of us can-"
    alex "Five of us?"
    "You think longingly about the last time you got to finish a sentence."
    alex "I'm not the best at math but I'm pretty sure there are six people in this room."
    "You look around, and that's when you notice a girl sitting in the corner of the room, nose in a book. When she sees you've noticed her, she stands up and joins the rest of you."
    show zoe neutral with dissolve:
        zoom 0.22
        xalign 0.75
    you "W-wait, how long have you been here?"
    unknown_zoe "Long enough."
    "She gives you a pointed look. You're sure she's seen worse things than someone walking in circles and muttering to themselves like a crazy person."
    you "A-alright, well that means we don't have to wait for anyone anymore!"
    show alex happy:
        yalign 1
        zoom 0.5
    alex "Wow you're real good at this."
    #LEO SMILE
    leo "I think it's great you're trying to run this club."
    #ALEKS ŚMIECH (NIE UŚMIECH)
    alex "Trying, Huh? And I thought I was rude."
    #LEO IRRITAED
    leo "Ah, you know that's not what I meant."
    alex "I don’t know, do I?"
    leo "You are purposely making me look bad-"
    alex "Just kidding~"
    "You can see whatever this is starting to escalate."
    menu:
        "How about we stop fighting and make up, huh?":
            $alex_aff -=1
            $leo_aff -=1
            jump stop_fighting
        "Don’t worry, I get the joke, no hard feelings":
            $alex_aff +=1
            jump get_the_joke
        "Don’t entertain this nonsense, ask the girl what’s her name.":
            $alex_aff -=1
            $leo_aff +=1
            $zoe_aff +=1
            jump nonsense
        "{i}Turn to Leo{/i} I didn’t think you were making fun of me, and thank you":
            $leo_aff +=1
            $iris_aff +=1
            jump thank_you

label stop_fighting:
    alex "Sure, remind me again, are you running a preschool?"
    #LEO UŚMIECH
    leo "Nobodys fighting, just a… civilized discussion, let’s forget about this and move on right…?"
    "He says that but you can tell he’s tensed up a bit. Now it’s awkward, good job. Fortunately for you Fern comes in with a save."
    fern "So! What’s your name, mystery girl?"
    "There’s a look of disdain on the girl's face."
    zoe "My name is Zoe. Please tell me you will not give everyone a nickname."
    jump section4

label get_the_joke:
    alex "See? They get it, loosen up a bit."
    leo "Sure.."
    "He says that but you can tell he’s tensed up a bit. Now it’s awkward, good job. Fortunately for you Fern comes in with a save."
    fern "So! What’s your name, mystery girl?"
    "There’s a look of disdain on the girl's face."
    zoe "My name is Zoe. Please tell me you will not give everyone a nickname."
    jump section4

label nonsense:
    you "So, what’s your name?"
    fern "Yeah, who are you mystery girl?"
    "There’s a look of disdain on the girl's face."
    zoe "My name is Zoe. Please tell me you will not give everyone a nickname."
    jump section4

label thank_you:
    leo "Great, glad we cleared that up."
    "{i}Leo gives you an appreciative smile.{/i}"
    alex "Yeah, yeah, you guys are so cute and boring, let’s focus on more important things."
    fern "Yeah! Who are you mystery girl?"
    zoe "My name is Zoe. Please tell me you will not give everyone a nickname."
    jump section4

label section4:
    iris "{i}Oh, that’s a cute idea.{/i}"
    alex "Oh yeah? I know what Mr. Stickuphisass is going to-"
    you "WOW, AHAHahaha I’m so glad you guys are getting along so well already. How about we all settle in, and we can talk more about the club."
    fern "Wait, what would your nickname be?"
    "It’s like you didn’t say a thing."
    fern "They’re probably going to boss us around, right? How about… master?"
    alex "Kinky, I like it."
    "Oh GOD, why are they like this? Can someone please kill you now? This is some kind of karmic punishment for sure. Sorry God but you just had to be born a League player."
    "You can physically feel yourself turning red. Alex, of course, is trying not to burst out laughing, and even though Fern is looking at you innocently, you can see a hint of malice in his eyes."