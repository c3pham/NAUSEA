# Splash screen

init offset = -1

label splashscreen:
    scene black
    with Pause(1)

    show text "Celine's stufff" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return