# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ivar = Character("Ivar")
image line = "Untitled.png"

# The game starts here.

label start:
    scene line
    ivar "Welcome!"
    ivar "I heard you have came from far away to explore here."
    
    return

    