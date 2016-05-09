# Declare images used by this game.
image bg black = "#000"
image bg intro = "backgrounds/intro.jpg"
image bg bedroom = "backgrounds/bedroom.jpg"
image bg bigroom = "backgrounds/bigroom.jpg"
image bg entry = "backgrounds/entry.jpg"
image bg village = "backgrounds/village.jpg"

image helene normal = "characters/helene/helene_normal.png"
image helene triste = "characters/helene/helene_trise.png"
image helene pleure = "characters/helene/helene_pleure.png"
image helene surprise = "characters/helene/helene_surprise.png"
image helene confidente = "characters/helene/helene_confidente.png"
image helene pense = "characters/helene/helene_pense.png"
image helene arriere = "characters/helene/helene_arriere.png"
image helene souriante = "characters/helene/helene_souriante.png"
image helene inquiete = "characters/helene/helene_inquiete.png"
image helene demoralisee = "characters/helene/helene_demoralisee.png"

image gaston normal = "characters/gaston_normal.png"

image anne normal = "characters/anne_normal.png"

image charles normal = "characters/charles_normal.png"

image bras_leon debut = "characters/bras_leon_debut.png"
    
image bras_leon mid = "characters/bras_leon_mid.png"
image bras_leon fin = "characters/bras_leon_fin.png"

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
    
transform enter_right:
    on show:
        xalign 3.0
        linear 0.5 xalign 1.5
    on hide:
        xalign 1.5
        linear 0.5 xalign 3.0
    
transform enter_left:
    on show:
        xalign -3.0
        linear 0.5 align -0.2
    on hide:
        xalign -0.2
        linear 0.5 xalign -3.0
    
transform bras_transform:
    xalign 0.25
    zoom 2.0
    on show:
        yalign 2.0
        linear 0.5 yalign 1.2
    on hide:
        yalign 1.2
        linear 0.5 yalign 2.0

init python:
    choix1 = 0

# The game starts here.
label start:
    # play music "illurock.ogg"

    scene bg black with fade

    "???" "Eh ! Tu m'entends ??"

    scene bg intro with fade

    show helene normal at center with dissolve

    "???" "Tu as pris un sérieux coup apparement, on verra ça une fois à la planque, là on a pas le temps."
    
    menu:
        "Qui êtes-vous ?":
            $ choix1 = 1
            jump intro_2
        "Qui suis-je ?":
            $ choix1 = 2
            jump intro_2

label intro_2:
    show helene surprise at center
    
    "???" "Quoi !!!"
    
    show helene inquiete

    "???" "Aller lève-toi, d'autres gardes vont arriver."
    "???" "Tiens, attrape ma main !"
    
    jump reveil

label reveil:
    scene bg bedroom with fade
    
    show helene normal at left with dissolve
    
    "???" "Ca y est, tu es réveillé ?"
    "???" "..."
    show helene demoralisee at left
    "???" "Hier on s'est fait attaquer et... tu as fait une grosse chute."
    "???" "..."
    "???" "Tu ne te rappelles vraiment plus de rien ?!"

    menu:
        "Non":
            show helene pleure at left
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
    show helene demoralisee at left
    
    "???" "C'est vrai, commençons par ça."
    "???" "Je m'appelle Hélène."
    helene "On se connait depuis de nombreuses années."
    helene "J'étais noble avant le début du Royaume des Templiers, comme toi d'ailleurs."
    helene "Et nous voilà dans l'Ordre du Lys à mener des attaques terroristes."
    
    jump arrivee_anne
                    
label presentation_leon:
    "???" "Oui évidemment, tu dois même plus connaître ton nom."
    "???" "Tu t'appelles Léon, tu étais un fils de noble quand on s'est connu."
    "???" "Lors de la prise de pouvoir des Templiers, on a rejoint ensemble l'Ordre du Lys."
    "???" "Ah oui j'oubliais : je m'appelle Hélène."
    
    jump arrivee_anne
                    
label presentation_lieu:
    "???" "Nous sommes dans une planque souterraine, proche du chateau de Fontainebleau."
    "???" "Ca fait quelques mois qu'on est ici."
    
    jump arrivee_anne
                    
label arrivee_anne:
    "--Autres explications / 2nd lot de question à poser--"
    
    show anne normal at left, enter_right
    
    anne "Salut Léon !"
    anne "Désolé de vous couper mais Charles nous convoque dans la grande salle."
    helene "OK, on arrive."
    
    hide anne
    
    helene "Tu penses que ça ira ?"
    
    menu:
        "Oui":
            show helene arriere at center
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
    anne "Quant à Charles, c'est le troisième fils de Phillipe Le Bel."
    menu:
        "S'agenouiller":
            jump agenouiller
        "Demander s'il faut s'agenouiller":
            jump agenouiller
        
label agenouiller:
    show helene souriante at center
    anne "T'inquiète pas, les statuts n'ont plus d'importance au sein de l'ordre."
    "Suite de la conversation où Charles mentionne une maladie contagieuse incurable que les démons infligent et que l'attaque précédente leur a permis de mettre la main sur un document indiquant que Jacques de Molay, grand maître des Templiers, partira à la chasse des la forêt de Fontainebleau le lendemain du jour présent, occasion en or pour tenter un assassinat. Léon a finalement des nausées et ressent une douleur au bras et demande à ce qu’on le laisse se reposer."

label retour_chambre:
    scene bg bedroom with fade
    
    "De retour dans sa chambre, il tire sa manche et aperçoit une marque étrange sur le bras."
    
    show bras_leon debut at bras_transform
    
    "Il se passe de l'eau dessus via un sceau d'eau avoisinant. Il aperçoit alors son visage dans le reflet de l'eau."
    
    hide bras_leon debut at bras_transform
    
    jump vision_01

label vision_01:
    scene bg black with fade
    
    "???" "Léon, il y a plusieurs choses que tu dois savoir sur les démons."
    jump gaston_manche

label gaston_manche:
    scene bg bedroom with fade
    
    "On entend quelqu'un rentrer. Léon retrousse rapidement sa manche."
    
    show gaston normal at right with dissolve
    
    gaston "Salut Léon ! Dis, j'ai quelque chose à te dire."
    gaston "Je suis pas sûr mais... j'ai peur que ce qui t'es arrivé soit du à l'artefact démoniaque que je portais."
    
    menu:
        "Comment ça ?!":
            gaston "Je suis vraiment désolé..."
        "Pourquoi tu penses ça ?":
            gaston "J'ai sentis l'artefact s'activer puis tu es tombé."

label gaston_blessure:
    
    menu:
        "Demander quels sont les effets de cet artefact":
            gaston "Je ne sais même pas moi même. J'avais récupéré artefact avec lequel tu as été blessé lors d'une bataille"
            gaston "Je ne connais pas ses effets."
        "S'énerver contre Gaston":
            gaston "Je comprend ta colère et j'en suis désolé."
            gaston "J'avais récupéré artefact avec lequel tu as été blessé lors d'une bataille"
    
    "Gaston souhaite se racheter auprès de Léon, alors il lui promet de le protéger vu qu'il est très vulnérable du fait de son amnésie. Il n'a jamais dit ça à quelqu'un mais il lui dit qu'il ne doit pas faire trop confiance à Hélène. Il conseille à Léon de faire attention."
    
    show anne normal at right
    
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
    
    show bg black with fade
    
    "???" "Les démons peuvent prendre une forme humaine."

    show bg bigroom
    show charles normal at right
    show anne normal at left
    with fade

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
    charles "Bon. Qu'est-ce qui ne va pas ? Tu peux me le dire tu sais, je n'en parlerai à personne."
    
    menu:
        "Lui montrer la blessure au bras en expliquant l'erreur de Gaston":
            show bras_leon debut at bras_transform
            charles "Oh ?! C'est Gaston qui t'as fait ça ? Le pauvre bougre n'a surement pas fait exprès. Bon, j'en parlerai avec lui pour savoir comment te soigner au plus vite."
            hide bras_leon debut at bras_transform
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
    show bg entry with fade
    
    show helene normal at center with dissolve
    helene "Allons au village, ça te fera du bien de prendre l'air."
    jump village
    
label village:
    show bg village with fade
    
    show helene souriante at center with dissolve
    
    "Ils arrivent au village. Hélène reparle de leur ancienne relation. Elle lui dit que malgré qu'il a perdu la mémoire, il n'a pas changé. Elle lui raconte de joyeux souvenirs qu'ils ont eu ensemble dans ce village. "
    
    show helene demoralisee at center
            
    helene "Comment va-tu depuis ta perte de mémoire ? Je suis désolée de pas pouvoir t'aider plus mais nous devons tous préparer l'assaut de demain."
    
    menu:
        "Je lui dit que tout va bien, que tout le monde essaye de m'aider":
            $ showBlessureToHelene = 0
            helene "ok.. Si tu le dis"
            show helene normal at center
        "Je lui parle de la blessure au bras":
            $ showBlessureToHelene = 1
            show helene surprise at center
            "Je lui montre la blessure et lui dit que Gaston en est le responsable. Hélène prend une mine terne et ne répond rien."
            show helene demoralisee at center
            
    helene "Bon. Retournons à la planque, la nuit commence à tomber."
    
    jump grande_salle_suite

label grande_salle_suite:
    show bg bigroom with fade
    
    show charles normal at center with dissolve
    show helene demoralisee at right with dissolve
    show anne normal at left with dissolve 
    
    charles "Si je vous convoque tous ici, c'est pour l'organisation de l'assaut de demain"
    "Tout le monde est dans la grande salle. Charles parle de l'organisation de l'attaque : infiltration dans les jardins de fontainebleau. Gaston demande s'il est sage de faire participer Léon vu son état. Anne attaque alors Léon par surprise, mais il parvient à contrer aisément. Anne en conclu qu'il a toutes ses capacités. Charles laisse à Léon le choix de les accompagner ou non."
    charles "Veux-tu venir ?"
    
    menu:
        "Dire que oui, je souhaite venir":
            $ wantToGoToBattle = 1
            charles "Très bien, tu es toujours aussi courageux car ce ne sera pas simple et très dangeureux."
        "Dire que non, je ne préfère pas venir":
            $ wantToGoToBattle = 0
            charles "Oui tu as raison, ce ne serait pas prudent. Il n'y a pas de problème, tu restera à la planque surveiller"
    "Tout le monde va se coucher."  
    
    hide charles with dissolve
    hide helene with dissolve
    hide anne with dissolve
    
    jump chambre_soir
    
label chambre_soir:
    show bg bedroom with fade
    
    "Léon est seul dans sa chambre et regarde sa blessure."
    
    show bras_leon debut at bras_transform
    
    if showBlessureToHelene == 0:
        "Hélène entre brusquement dans la chambre, voit la blessure de Léon, et s'en va froidement."
    
    "Avant de s'endormir, la blessure de Léon se ravive."
    
    jump last_vision

label last_vision:
    show bg black with fade
    
    "???" "Les démons sous forme humaine... On peut les reconnaître à leurs yeux"
    jump chambre_nuit

label chambre_nuit:
    show bg bedroom with fade
    
    "La nuit passe"
    
    show bras_leon debut at bras_transform
    
    "Léon est seul dans sa chambre et regarde sa blessure."
    
    if showBlessureToHelene == 0:
        if wantToGoToBattle == 1:
            jump final_03
        else:
            jump final_02 
    elif showBlessureToHelene == 1:
        jump final_01
        
        
label final_01:
    "Léon se réveille et sort de sa chambre"
    "Léon découvre le cadavre de Gaston, paniqué."
    "Léon cours sans se poser de question et tombe sur Hélène dans la grande salle, paniquée, qui lui dit que Charles est devenu fou et a tué Gaston."
    "Charles arrive et demande ce qui se passe, Léon marche à reculon, paniqué, sous l'incompréhension de Charles. Charles se fait alors soudainement transpercer le coeur par Hélène, sous forme démoniaque."
    "Anne arrive et hurle de terreur en voyant le cadavre de Charles, puis Hélène la transperce également à son tour."
    "Hélène s'approche alors de Léon en disant qu'elle aurait préféré ne pas avoir à montrer son véritable visage aussi tôt."
    jump end
    

label final_02:
    "Léon se réveille et consate que les autres sont déjà partis. Il entent alors du bruit à l'entrée et va voir ce qui s'y passe."
    "Gaston s'y trouve, paniqué, et dis à Léon qu'Helène a tué les autres et qu'il faut vite qu'ils s'enfuissent. "
    "Hélène, sous forme démoniaque, transperce alors Gaston dans le dos."
    "Elle se rapproche alors de Léon en disant qu'elle a effectivement tué les deux autres et que si Gaston n'avait pas décidé de revenir à la planque pour prévenir Léon, il aurait eut une meilleure chance de s'enfuir."
    jump end
    
label final_03:
    "Hélène réveille Léon. Ils partent à l'attaque."
    "Le groupe s'infiltre dans le Jardin de Fontainebleau en assassinant furtivement des gardes."
    "Ils se camouflent dans de la verdure sur le terrain de chasse, chemin par lequel Jacques de Molay devrait passer."
    "Hélène annonce alors qu'elle n'a plus le choix et qu'elle n'aurait pas voulu en arriver là si tôt, puis Anne pousse un hurlement. Elle a été transpercée dans le coeur par Hélène qui a alors pris une forme démoniaque."
    "Gaston sort son artefact, paniqué mais Hélène se précipite sur lui et le transperce à son tour pendant que Léon est figé par la peur et Charles figé par la mort d'Anne."
    "Hélène s'approche alors lentement de Charles qui ne tente rien et elle le transperce à son tour."
    "Hélène s'approche finalement de Léon en lui disant que c'est dommage qu'elle doive en arriver là."
    jump end
    
label end:
    "Hélène face à lui et dos au mur, Léon sort alors son poignard et transperce Hélène dans le coeur."
    "Hélène mourrante, Léon retrouve alors ses souvenirs dans un long flashback."
    
    "Léon est en réalité un Templier. Les visions que Léon avait ces derniers jours étaient en fait des souvenirs d'une conversation qu'il a eu avec Jacques de Molay, grand maître des Templiers, qui lui parle des démons alors que Léon est sur le point de lui-même faire une invocation. C'est ainsi que Léon invoque Hélène. Léon asassinera alors le roi Philippe le Bel de ses propres mains, et accomplira par le temps plusieurs missions en compagnie deHélène visant à neutraliser la résistance. Pendant ces années, il tissera également des liens amoureux avec Hélène. Un jour, Jacques de Molay demande à Léon et Hélène, en qui il a une entière confiance, d'infiltrer l'Ordre du Lys, principal atout de la résistance que l'Empire Templier a été capable de trouver, afin de récolter le plus d'information possible sur les alliés de l'ordre en leur disant qu'ils pouvaient les décimer si nécéssaire. C'est ainsi que Léon et Hélène ont intégrés l'Ordre."
    "Hélène, prononçant ses derniers mots, constate que Léon en sanglots se souvient de tous et heureuse de le revoir étant lui-même, lui dit que sa blessure au bras était fatale et que son seul moyen de le sauver était de lui transmettre son énergie vitale, impliquant sa propre mort. Hélène meurt alors dans les bras de Léon, le sourire aux lèvres."
    
    "FIN"
    
    return