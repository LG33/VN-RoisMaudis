# Declare images used by this game.
image bg black = "#000"
image bg intro = "backgrounds/intro.jpg"
image bg bedroom = "backgrounds/bedroom.jpg"
image bg bigroom = "backgrounds/bigroom.jpg"
image bg entry = "backgrounds/entry.jpg"
image bg village = "backgrounds/village.jpg"

image helene normal = "characters/helene_normal.png"

image gaston normal = "characters/gaston_normal.png"

image anne normal = "characters/anne_normal.png"

image charles normal = "characters/charles_normal.png"

# Declare characters used by this game.
define helene = Character('Hélène', color="#ff99ff")
define gaston = Character('Gaston', color="#9999ff")
define anne = Character('Anne', color="#eeeeee")
define charles = Character('Charles', color="#ffff99")

transform left: xalign 0.1 yalign 1.0

init python:
    choix1 = 0

# The game starts here.
label start:
    # $ bl_game = False

    # play music "illurock.ogg"

    scene bg black
    with fade

    "???" "Eh ! Tu m'entends ??"

    scene bg intro
    with fade

    show helene normal
    with dissolve

    "???" "Tu as reçu un sérieux coup apparement. Désolé de te brusquer mais on doit vraiment fuir."

    menu:
        "Qui êtes-vous ?":
            $ choix1 = 1
            jump intro_2
        "Qui suis-je ?":
            $ choix1 = 2
            jump intro_2

label intro_2:

    # show helene panic
    
    "???" "!!!"
    
    # show helene normal

    "???" "Aller lève-toi, d'autres gardes vont arriver."
    "???" "Tiens, attrape ma main !"
    
    jump reveil

label reveil:

    scene bg bedroom
    with fade
    
    show helene normal
    with dissolve
    
    "???" "Ca y est, tu es réveillé ?"
    "???" "..."
    "???" "Hier on s'est fait attaquer et... tu as chuté du haut d'un escalier."
    "???" "..."
    "???" "Tu ne te rappelles vraiment plus de rien ?!"

    menu:
        "Non":

            "(Hélène commence à pleurer)"
            "???" "Désolé..."
            "???" "J'arrive pas à le croire... Tu étais tout pour moi et..."
            "???" "Désolé, je suis là à pleurer alors que tu te poser énormément de questions."
            
            menu:
                "Qui suis-je ?":
                    jump presentation_leon
                "Où sommes-nous ?":
                    jump presentation_lieu
                "Tu m'a toujours pas dis qui tu es." if choix1 == 1:
                    jump presentation_helene
                    
label presentation_helene:

    "???" "C'est vrai, commençons par ça."
    "???" "Je m'appelle Hélène."
    helene "On se connait depuis de nombreuses années."
    
    jump arrivee_anne
                    
label presentation_leon:

    "???" "Oui évidemment, tu dois même plus connaître ton nom."
    "???" "Tu t'appelles Léon."
    
    jump arrivee_anne
                    
label presentation_lieu:

    "???" "Nous sommes dans une planque souterraine, proche du chateau de Fontainebleau."
    "???" "On est un petit groupe de résistant."
    
    jump arrivee_anne
                    
label arrivee_anne:

    "(Autres explications)"
    
    show anne normal
    with dissolve
    
    anne "Salut Léon !"
    anne "Désolé de vous couper mais Charles nous convoque dans la grande salle."
    helene "OK, on arrive."
    
    hide anne
    with fade
    
    helene "Tu penses que ça ira ?"
    
    menu:
        "Oui":
            helene "Allons-y alors."
            jump meeting_1
        "Je sais pas":
            helene "Je comprends, ça doit faire très bizarre de tomber au milieu d'un groupe terroriste sans rien savoir. Mais ici tout le monde te connait bien et personne te veut du mal."
            helene "Aller, allons-y, ça sert à rien de les faire attendre."
            jump meeting_1
                    
label meeting_1:
    
    scene bg bigroom
    with fade
    
    show charles normal
    with dissolve
    
    charles "Bonjours Léon. Hélène m'a dit ce qu'il t'était arrivé, j'en suis vraiment désolé. Plus on te parlera de tout rapidement, mieux ça sera pour toi."
    charles "Tu connais déjà Hélène, je vais te présenter Gaston et Anne."
    
    show gaston normal
    with dissolve
    
    gaston "Salut mon pote, content de te voir debout"
    
    hide gaston
    with fade
    
    show anne normal
    with dissolve
    
    anne "Salut, moi c'est Anne."