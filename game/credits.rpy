label end_credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with long_dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend with long_dissolve
    show cred at Move((0.5, 2.1), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with long_dissolve
    hide thanks
    with Pause(5)
    with long_dissolve
    return

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    hide theend with long_dissolve
    show cred at Move((0.5, 2.1), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with long_dissolve
    hide thanks
    with Pause(5)
    with long_dissolve
    return

init python:
    credits = ('Game Designer', 'Sven Barray'), ('Game Designer', 'David Birgé-Cotte'), ('Game Designer', 'Louis Gaillard'), ('Game Designer', 'Joseph Reichenbach'), ('Graphistes', 'Coline Bertrand'), ('Graphistes', 'Julia Blarda'), ('Graphistes', 'Philipine Briard'), ('Graphistes', 'Alice Leclerc'), ('Graphistes', 'Alexandre Mahmoudi'), ('Graphistes', 'Nina Yang'),
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=80}{font=gui/century.ttf}" + c[0] + "\n"
        credits_s += "{size=40}{font=gui/century.ttf}" + c[1] + "\n"
        c1=c[0]
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5, font="gui/century.ttf")
    image theend = Text("{size=80}The end", text_align=0.5, font="gui/century.ttf")
    image thanks = Text("{size=80}Merci d'avoir joué !", text_align=0.5, font="gui/century.ttf")