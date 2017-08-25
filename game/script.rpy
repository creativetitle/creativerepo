label main_menu:
    return

#Define variables.

define newscene = Fade(1.5,1.5,1.5)
define chleft = xalign .25
define chright = xalign .75

#Define characters.

define ley = Character("Leyna", image = "leyna")
define ldurs = Character("Durs??")

#Define sprites

#Game start.

label start:

    scene bg_river with newscene
    
    play music "dividingwinds.mp3"

    pause 2.5
    
    show leyna normal with dissolve
    
    ley "Hi, welcome to Ambassador."    
    ley "This is a story about a man who travels the world to teach others the lost art of dancing."
    ley oh "The journey will be full of sick moves hip tunes that will drive your body and soul in ways you could never have imagined."
    ley normal "So put on your dancing shoes and raise your expectations high as we dive-"

    show leyna normal at chleft
    with move
    
    show loathingdurs

    ldurs "ROOOAAAR!"
           
return