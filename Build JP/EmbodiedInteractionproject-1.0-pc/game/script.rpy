# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Edvard")

image bg room = im.Scale("bg room.jpg", 1920, 1080)
image bg text = im.Scale("bg text.png", 1920, 1080)
image bg cut = im.Scale("bg cut.jpg", 1920, 1080)
image bg wax = im.Scale("bg wax.jpg", 1920, 1080)

transform move_to_left_from_middle:
    xalign 0.5
    linear 1.0 xalign 0.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show edvard happy:
        xalign 0.5 yalign 0.4

    # These display lines of dialogue.

    e "Hi! I'm Edvard, your Guide to the hidden details in the famous {i}Scream{/i} painting by Edvard Munch."

    show edvard happy:
        move_to_left_from_middle
    e "Let's start at the top and work our way down!"

    scene bg text
    with Fade(0.5, 1.0, 0.5)

    show edvard happy:
        xalign 0.5 yalign 0.4
        move_to_left_from_middle

    e "Near the top right corner of the painting, some text was discovered."

    e "The text says {i}\"Kan kun være malet af en gal mand!\"{/i}, which translates to {i}Can only have been painted by a madman!{/i}"

    e "Experts suspect this was written by Munch himself, as the handwriting matches his."

    e "The text is suspected to have been added after an art student condemned the painting for being the work of a mentally ill person."

    scene bg cut
    with Fade(0.5, 1.0, 0.5)

    show edvard happy:
        xalign 0.5 yalign 0.4
        move_to_left_from_middle

    e "On the right side of the painting, a cut has been made."

    e "The cut is approximately 5 cm from the edge of the painting, and was not made all the way through."

    e "It is theorized Munch made the cut to make the composition more narrow, but after making the cut it did not fit the frame he had on hand."

    e "Therefore, he added it back, and painted it mostly red to try and hide the cut."

    e "The cut is still visible though, especially around the middle of the painting, right next to the figure."

    scene bg wax
    with Fade(0.5, 1.0, 0.5)

    show edvard happy:
        xalign 0.5 yalign 0.4
        move_to_left_from_middle

    e "Near the bottom right corner, some white stains can be seen."

    e "Initially, these were thought to be bird droppings, as Munch often painted outdoors."

    e "However, after analysis of the material, it was found to be candle wax."

    e "It is suspected Munch knocked over a candle either while working on the painting or in his storage, and accidentally spilled the candle wax on the painting."

    scene bg room
    with Fade(0.5, 1.0, 0.5)

    show edvard happy:
        xalign 0.5 yalign 0.4

    e "Thank you for partaking in the {i}Scream{/i} experience! Now you know some fun facts about the painting!"

    e "Goodbye!"

    # This ends the game.

    return
