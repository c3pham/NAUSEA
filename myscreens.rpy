# where I'll put all of my screens
# things happening in rooms

# image buttons to transport the scene
screen main_room:
    imagemap:
        ground "bg room.jpg"
        hotspot(1073, 212, 221, 598) action Jump("mirror")
        hotspot(294, 102, 463, 698) action Jump("closet")
        hotspot(1220, 762, 698, 282) action Jump("desk")

screen unicorn:
    imagebutton:
        xpos 660
        ypos 1
        idle "unicorn.png"
        hover "unicorn hover.png"
        action Jump("escapism")


# drag pictures
screen drag_objects:
    draggroup:
        drag:
            drag_name "obj1"
            child "obj1.png"
            xpos 0.25
            ypos 0.75
            draggable True
            droppable False
            drag_raise True
        drag:
            drag_name "obj2"
            child "obj2.png"
            xpos 0.35
            ypos 0.75
            draggable True
            droppable False
            drag_raise True
        drag:
            drag_name "obj3"
            child "obj3.png"
            xpos 0.45
            ypos 0.75
            draggable True
            droppable False
            drag_raise True
        drag:
            drag_name "obj4"
            child "obj4.png"
            xpos 0.55
            ypos 0.75
            draggable True
            droppable False
            drag_raise True
        drag:
            drag_name "obj5"
            child "obj5.png"
            xpos 0.65
            ypos 0.75
            draggable True
            droppable False
            drag_raise True
        drag:
            drag_name "obj6"
            child "obj6.png"
            xpos 0.75
            ypos 0.75
            draggable True
            droppable False
            drag_raise True