label mirror:
    hide screen main_room
    hide screen drag_objects
    scene bg mirror
    "mirror"
    "..."
    "..."
    "I look like a mess no matter what I do."
    pause
    "???" "...come here..."
    "???" "...we're waiting..."
    jump adventure

# screen mirror

label desk:
    hide screen drag_objects
    "desk"
    jump start
label closet:
    hide screen drag_objects
    hide screen main_room
    scene bg closet
    "closet"
    scene bg closeup closet
    pause
    "hi"
    jump start
label bed:
    hide screen drag_objects
    "bed"
    jump start
label adventure:
    "adventure"
    show magic girl at left
    "???" "Welcome back!"
    "???" "We've been waiting for you."
    "???" "Oh, that's right. {w} You must've forgotten my name. {w} It's Bungee"
    m "Come back to our side."
    call screen unicorn
label escapism:
    "escapism"
    jump start