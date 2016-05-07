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

transform left: 
    xalign -0.2 
    yalign 1.0
    zoom 3.0
    
transform right: 
    xalign 1.5 
    yalign 1.0
    zoom 3.0
    
transform center: 
    xalign 0.5 
    yalign 1.0
    zoom 3.0

init python:
    choix1 = 0

# The game starts here.
label start:
    # play music "illurock.ogg"

    scene bg black with fade

    "???" "Eh ! Tu m'entends ??"

    scene bg intro with fade

    show helene normal at center with dissolve

    "???" "Tu as reçu un sérieux coup apparement, on verra ça une fois à la planque, suis moi, c'est pas comme si on se faissait poursuivre !"

    menu:
        "Qui êtes-vous ?":
            $ choix1 = 1
            jump intro_2
        "Qui suis-je ?":
            $ choix1 = 2
            jump intro_2

label intro_2:
    # show helene panic
    
    "???" "Quoi !!!"
    
    # show helene normal

    "???" "Aller lève-toi, d'autres gardes vont arriver."
    "???" "Tiens, attrape ma main !"
    
    jump reveil

label reveil:
    scene bg bedroom
    with fade
    
    show helene normal at center with dissolve
    
    "???" "Ca y est, tu es réveillé ?"
    "???" "..."
    "???" "Hier on s'est fait attaquer et... tu as chuté du haut d'un escalier."
    "???" "..."
    "???" "Tu ne te rappelles vraiment plus de rien ?!"

    menu:
        "Non":

            "(Elle commence à pleurer)"
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
    "???" "Tu t'appelles Léon, et je suis Hélène"
    
    jump arrivee_anne
                    
label presentation_lieu:

    "???" "Nous sommes dans une planque souterraine, proche du chateau de Fontainebleau."
    "???" "On est un petit groupe de résistant."
    
    jump arrivee_anne
                    
label arrivee_anne:

    "(Autres explications)"
    
    show anne normal at right with dissolve
    
    anne "Salut Léon !"
    anne "Désolé de vous couper mais Charles nous convoque dans la grande salle."
    helene "OK, on arrive."
    
    hide anne with dissolve
    
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
    
    scene bg bigroom with fade
    
    show charles normal at left with dissolve
    
    charles "Bonjours Léon. Hélène m'a dit ce qu'il t'était arrivé, j'en suis vraiment désolé. Plus on te parlera de tout rapidement, mieux ça sera pour toi."
    charles "Tu connais déjà Hélène, je vais te présenter Gaston et Anne."
    
    show gaston normal at right with dissolve
    
    gaston "Salut mon pote, content de te voir debout"
    
    hide gaston with dissolve
    
    show anne normal at right with dissolve
    
    anne "Salut, moi c'est Anne."
    anne "--Explications sur Charles--"

    menu:
        "S'agenouiller":
            jump agenouiller
        "Demander s'il faut s'agenouiller":
            jump agenouiller
        
label agenouiller:
    anne "Anne éclate de rire et lui explique que les status n'ont plus d'importance au sein de l'ordre."
    "Suite de la conversation où ils mentionnent que l'attaque précédente leur a permis de mettre la main sur un document indiquant que Jacques de Molay, grand maître des Templiers, partira à la chasse des la forêt de Fontainebleau le lendemain du jour présent, occasion en or pour tenter un assassinat. Léon a finalement des nausées et ressent une douleur au bras et demande à ce qu’on le laisse se reposer."

label retour_chambre:
    scene bg bedroom with fade
    
    "De retour dans sa chambre, il tire sa manche et aperçoit une marque étrange sur le bras. Il se passe de l'eau dessus via un sceau d'eau avoisinant. Il aperçoit alors son visage dans le reflet de l'eau."
    jump vision_01

label vision_01:
    scene bg black with fade
    
    "???" "Léon, il y a plusieurs choses que tu dois savoir sur les démons."
    jump gaston_manche

label gaston_manche:
    scene bg bedroom with fade
    
    "On entend quelqu'un rentrer. Léon retrousse rapidement sa manche."
    
    show gaston normal at right with dissolve
    
    gaston "Salut ! Quesque tu nous cache sous cette manche mon gars ? T'inquiète, j'suis ton pote ! C'est une blessure c'est ça ?"
    
    menu:
        "Montrer la blessure":
            jump gaston_blessure
        "Ne pas lui montrer la blessure":
            gaston "Allez ! Montre !"
            "Gaston tire la manche !"
            jump gaston_blessure

label gaston_blessure:
    gaston "Je suis vraiment désolé, je voulais pas..."
    gaston "C'est un mauvais coup, je voulais pas te toucher l'autre soir.."
    
    menu:
        "Demander quels sont les effets de la blessure":
            gaston "Je ne sais même pas moi même. J'avais récupéré artefact avec lequel tu as été blessé lors d'une bataille"
            gaston "Je ne connais pas ses effets."
        "S'énerver contre Gaston":
            gaston "Je comprend ta colère et j'en suis désolé."
            gaston "J'avais récupéré artefact avec lequel tu as été blessé lors d'une bataille"
            gaston "Je ne connais pas ses effets."
            
    gaston "Il lui demande de ne pas parler de la blessure aux autres pour l’instant avant l’attaque prévue le lendemain car cette annonce pourquoi avoir un impact moral important au sein du groupe et Gaston ne souhaite pas mettre en danger l’attaque."
    
    menu:
        "Rester silencieux":
            gaston "Je sais que c'est difficile pour toi. Encore une fois je suis vraiment désolé."
        "Contester et demander pourquoi faire ça pour lui":
            gaston "Je sais que c'est difficile pour toi. Encore une fois je suis vraiment désolé."
    
    "Gaston souhaite se racheter auprès de Léon, alors il lui promet de le protéger vu qu'il est très vulnérable du fait de son amnésie. Il n'a jamais dit ça à quelqu'un mais il lui dit qu'il ne doit pas faire trop confiance à Hélène. Il conseille à Léon de faire attention."
    
    show anne normal at left with dissolve
    
    anne "Gaston ? Charles voudrait te parler."
    gaston "Ah ? J'y vais de ce pas. A tout à l'heure Léon !"
    
    hide gaston with dissolve
    
    "Anne explique à Léon que Gaston peut être dur parfois mais qu'il a un passé difficile. En effet, il avait une relation cachée avec une noble malgré le fait qu'il soit paysan et celle-ci a été tuée lors de l'attaque des templiers."
    "Anne dit qu'elle a une idée, il devraient en parler à Charles."
    
    jump grande_salle
    
label grande_salle:
    
    show bg bigroom with fade
    
    show charles normal at right with dissolve
    show anne normal at left with dissolve   
    
    "Anne dit que si Léon voit un peu les environs ça peut l'aider à se rappeler de certaines choses. Charles dit que c'est dangereux, et que seul Hélène pourrait aller avec lui car son visage n'est pas connu contrairement au leur. Léon se sent subitement mal."
    
    hide anne
    hide charles
    show bg black
    with fade
    "???" "Les démons peuvent prendre une forme humaine."

    show bg bigroom
    with fade
    show charles normal at right with dissolve
    show anne normal at left with dissolve

    "Léon reprend conscience. Anne et Charles le regarde très inquiets."
    
    menu:
        "Dire que tout va bien":
            charles "Léon, non tout ne va pas bien, tu viens de t'écrouler sur le sol au milieu de la conversation !"
        "Dire qu'on se sent mal":
            charles "En effet tout ne va pas bien, tu viens de t'écrouler sur le sol au milieu de la conversation !"
    
    charles "Anne ? Pourrais tu nous laisser, je dois m'entretenir avec Léon. Merci"
    anne "Très bien, je dois de toute façon préparer les armes pour l'assaut de demain."
    hide anne with dissolve
    show charles at center with dissolve
    charles "Bon. Qu'est-ce qui ne va pas? Tu peux me le dire tu sais, je n'en parlerai à personne."
    
    menu:
        "Lui montrer la blessure au bras en expliquant l'erreur de Gaston":
            charles "Oh?! C'est Gaston qui t'as fait ça ? Le pauvre bougre n'a surement pas fait exprès. Bon, j'en parlerai avec lui pour savoir comment te soigner au plus vite."
        "Dire que tout va bien":
            charles ".. Très bien, c'est comme tu veux mais sache que je suis là si tu as besoin d'en parler."
            
    charles "Au fait, voici une dague, prend la, tu sera heureux de l'avoir quand tu en aura besoin crois moi !"
    charles "Bon. Je dois retourner travailler, prend soin de toi Léon."
        
    menu:
        "Lui demander si les démons peuvent prendre forme humaine":
            charles "Hein? Non, d'où te viens des idées pareilles, je ne pense pas que ce soit possible, c'est même completement n'importe quoi !"
        "Le laisser partir":
            "..."
    hide charles with dissolve
        
    "Charles laisse Léon seul. Léon regarde alors son bras."
        
    jump planque_entree
    
label planque_entree:
    show bg entry
    with fade
    
    show helene normal with dissolve
    helene "Allons au village, ça te fera du bien de prendre l'air."
    jump village
    
label village:
    show bg village
    with fade
    show helene normal with dissolve
    
    "Ils arrivent au village. Hélène reparle de leur ancienne relation. Elle lui dit que malgré qu'il a perdu la mémoire, il n'a pas changé. Elle lui raconte de joyeux souvenirs qu'ils ont eu ensemble dans ce village. "
    helene "Comment va-tu depuis ta perte de mémoire ? Je suis désolée de pas pouvoir t'aider plus mais nous devons tous préparer l'assaut de demain."
    
    menu:
        "Je lui dit que tout va bien, que tout le monde essaye de m'aider":
            $ showBlessureToHelene = 0
            helene "ok.. Si tu le dis"
        "Je lui parle de la blessure au bras":
            $ showBlessureToHelene = 1
            "Je lui montre la blessure et lui dit que Gaston en est le responsable. Hélène prend une mine terne et ne répond rien."
    helene "Bon. Retournons à la planque, la nuit commence à tomber."
    jump grande_salle_suite

label grande_salle_suite:
    show bg bigroom with fade
    show charles normal with dissolve
    show helene normal at right with dissolve
    show anne normal at left with dissolve 
    
    charles "Si je vous convoque tous ici, c'est pour l'organisation de l'assaut de demain"
    "Tout le monde est dans la grande salle. Charles parle de l'organisation de l'attaque : infiltration dans les jardins de fontainebleau. Gaston demande s'il est sage de faire participer Léon vu son état. Anne attaque alors Léon par surprise, mais il parvient à contrer aisément. Anne en conclu qu'il a toutes ses capacités. Charles laisse à Léon le choix de les accompagner ou non."
    charles "Veux-tu venir ?"
    
    menu:
        "Dire que oui, je souhaite venir":
            charles "Très bien, tu es toujours aussi courageux car ce ne sera pas simple et très dangeureux."
        "Dire que non, je ne préfère pas venir":
            charles "Oui tu as raison, ce ne serait pas prudent. Il n'y a pas de problème, tu restera à la planque surveiller"
    "Tout le monde va se coucher."  
    
    hide charles with dissolve
    hide anne with dissolve
    hide helene with dissolve
    
    jump chambre_soir
    
label chambre_soir:
    show bg bedroom 
    with fade
    "Léon est seul dans sa chambre et regarde sa blessure."
    "Hélène entre brusquement dans la chambre, voit la blessure de Léon, et s'en va froidement."
    "Avant de s'endormir, la blessure de Léon se ravive."
    
    jump last_vision

label last_vision:
    show bg black with fade
    "???" "Les démons sous forme humaine... On peut les reconnaître à leurs yeux"
    jump chambre_nuit

label chambre_nuit:
    show bg bedroom 
    with fade
    "La nuit passe"
    "Léon est seul dans sa chambre et regarde sa blessure."