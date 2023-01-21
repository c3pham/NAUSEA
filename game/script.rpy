# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

label splashscreen:
    scene black
    with Pause(1)

    show text "Celine's stufff" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return
    
# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene testimage

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    call screen drag_sample2


    show screen drag_sample3
    if droppable == "The Left Circle":
        $ xpos_var = 150
    elif droppable == "The Right Circle":
        $ xpos_var = 790
    else:
        $ xpos_var = 640
    if draggable == "circle":
        show circle:
            xpos xpos_var ypos 460
    elif draggable == "triangle":
        show triangle:
            xpos xpos_var ypos 460
    elif draggable == "square":
        show square:
            xpos xpos_var ypos 460
    e "{color=#000}The [draggable] was put in [droppable]"
    

    "I don't bother opening my eyes."

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return




screen drag_sample2:
    draggroup:
        drag:
            drag_name "circle"
            child "circle.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "triangle"
            child "triangle.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "square"
            child "square.png"
            xpos 700
            ypos 100
            draggable True
            droppable True
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "spot.png"
            draggable False
            droppable True
        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "spot.png"
            draggable False
            droppable True
            

screen drag_sample3:
    draggroup:
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "spot.png"
            draggable False
            droppable False
        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "spot.png"
            draggable False
            droppable False