# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ivar = Character("Ivar")
image line = "character backround.png"
image ivar = "Ivar.png"
image forest = "Forest.png"
image village hub = "Village (Hub).png"
image village1 = "Village (Hub) - (1).png"
define gui.text_font = "Aclonica-Regular.ttf"  
define gui.name_text_font = "Aclonica-Regular.ttf"
define gui.interface_text_font = "EagleLake-Regular.ttf" 
define gui.button_text_font = "EagleLake-Regular.ttf"
define gui.choice_button_text_font = "EagleLake-Regular.ttf"
define gui.choice_button_text_color = '#000000'
define gui.text_color = '#000000'
define gui.name_text_color = '#000000'
# The game starts here.

label start:
    scene line
    show ivar at center with moveinleft
    play music "<loop 0>Calm.mp3"
    ivar "Welcome!"
    ivar "I heard you have came from far away to explore here."
    ivar "Follow me through this forest, I'll show you the way to our village."
    ivar "And traveler, what is your name may I ask?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()


    ivar "Pleased to meet you, %(player_name)s!"
    
    scene forest with pixellate
    play music "<loop 0>Forest (Vikings).mp3"
    menu:
        "Where do you want to go?"
        "The Village":
             jump village

label village:
    ivar "So, you want to go to the village?"
    scene village hub with pixellate
    play music "<loop 0>Arbondor.mp3"
    ivar "This is our village, Arbondor."
    ivar "You are welcome to stay here as long as you'd like."
    ivar "Arbondor keeps going on north, would you like to see the rest?"
    menu:
        "Would you like to explore the rest of the Arbondor?"
        "Yes":
            jump village1
        "No":
            ivar "I guess you can stay here then."
    return

label village1:
    ivar "Let's go to the north of Arbondor then."
    scene village1 with pixellate

    return