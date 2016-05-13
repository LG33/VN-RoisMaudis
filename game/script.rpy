image decor noir = "#000"

image decor intro:
    "backgrounds/intro.jpg"
    zoom 1
    
image decor chambre:
    "backgrounds/bedroom.jpg"
    zoom 2
    
image decor grande_salle:
    "backgrounds/bigroom.jpg"
    zoom 2
    
image decor entree:
    "backgrounds/entry.jpg"
    zoom 2
    
image decor village:
    "backgrounds/village.jpg"
    zoom 0.6
    
image decor fontainebleau:
    "backgrounds/fontainebleau.jpg"
    zoom 0.6


image helene normal = "characters/helene/helene_normal.png"
image helene masque = "characters/helene/helene_masque.png"
image helene inquiete = "characters/helene/helene_inquiete.png"
image helene serieuse = "characters/helene/helene_serieuse.png"
image helene souriante = "characters/helene/helene_souriante.png"

image helene_demon normal = "characters/helene_demon/helene_demon_normal.png"
image helene_demon souriante = "characters/helene_demon/helene_demon_souriante.png"

image gaston normal = "characters/gaston/gaston_normal.png"
image gaston masque = "characters/gaston/gaston_masque.png"
image gaston serieux = "characters/gaston/gaston_serieux.png"
image gaston souriant = "characters/gaston/gaston_souriant.png"
image gaston panique = "characters/gaston/gaston_panique.png"

image anne normal = "characters/anne/anne_normal.png"
image anne masque = "characters/anne/anne_masque.png"
image anne choquee = "characters/anne/anne_choquee.png"
image anne serieuse = "characters/anne/anne_serieuse.png"
image anne souriante = "characters/anne/anne_souriante.png"

image charles normal = "characters/charles/charles_normal.png"
image charles masque = "characters/charles/charles_masque.png"
image charles panique = "characters/charles/charles_panique.png"
image charles serieux = "characters/charles/charles_serieux.png"

image bras_leon debut = "characters/bras_leon_debut.png"
image bras_leon mid = "characters/bras_leon_mid.png"
image bras_leon fin = "characters/bras_leon_fin.png"


define leon = Character('Léon', outlines=[(1, "#008800", 0, 0)], window_top_padding=20, window_background="gui/dialogue_box.png")
define helene = Character('Hélène', outlines=[(1, "#ff00ff", 0, 0)], window_top_padding=20, window_background="gui/dialogue_box.png")
define gaston = Character('Gaston', color="#9999ff", window_top_padding=20, window_background="gui/dialogue_box.png")
define anne = Character('Anne', color="#eeeeee", window_top_padding=20, window_background="gui/dialogue_box.png")
define charles = Character('Charles', outlines=[(1, "#aa7700", 0, 0)], window_top_padding=20, window_background="gui/dialogue_box.png")
define inconnu = Character('???', window_top_padding=20, window_background="gui/dialogue_box.png")
define self = Character(None, color="#ffff99", what_italic=True, what_color="#ffdd55", window_top_padding=90, window_background="gui/narrative_box.png")
define jacques = Character("jacques_name", dynamic=True, what_color="#8888ff", what_italic=True, what_slow_cps=10, window_top_padding=20, window_background="gui/dialogue_box.png")

transform left: 
    xalign -0.2 
    yalign 1.0
    zoom 5.0
    
transform right: 
    xalign 1.5
    yalign 1.0
    zoom 5.0
    
transform center: 
    xalign 0.5 
    yalign 1.0
    zoom 5.0
    
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
    zoom 4.0
    on show:
        yalign 2.0
        linear 0.5 yalign 1.2
    on hide:
        yalign 1.2
        linear 0.5 yalign 2.0

init python:
    choix1 = 0
    jacques_name = "???"
    helene_side = Character('',color="#ff99ff",window_left_padding=288,window_top_padding=40,show_side_image=Image("side_image/lucy_surprized.png", xalign=100, yalign=0.87), )

    
define ellipse = Fade(0.5, 1.0, 0.5)
define long_dissolve = Dissolve(1.0)

# init python:
#    def beepy_voice(event, interact=True, **kwargs):
#        if not interact:
#            return
#
#        if event == "show_done":
#            renpy.sound.play("melodic1_click.wav", loop=True)
#        elif event == "slow_done":
#            renpy.sound.stop()
#
#define pike = Character("Christopher Pike", callback=beepy_voice)

label start:

    # pike "So, hanging out on Talos IV, minding my own business, when..."
    # play music "illurock.ogg"
    # $ jacques_name = "Jacques de Molay"

    scene decor noir with dissolve
    
    inconnu "Léon ! Léon !!"
    self "Que… qu’est-ce qu’il se passe ?"
    
    scene decor intro
    show helene masque at center
    with long_dissolve
    
    pause 0.5

    inconnu "Tu t’es évanoui, dépêche-toi, il faut fuir !"
    self "Je… je ne comprends rien…"

    menu:
        "Demander qui je suis":
            leon "Qui suis-je ?"
            jump fuite_fin
        "Demander qui elle est":
            leon "Qui êtes-vous ?"
            jump fuite_fin
    
label fuite_fin:
    inconnu "QU… {p=1.0}QUOI ?!"
    
    pause 2.0
    
    inconnu "On n’a pas le temps, suis-moi !"
    leon "Ah… ma tête…"

    scene decor noir 
    hide helene
    with dissolve

    inconnu "LÉON!!!"

    pause 5.0

    jump reveil_start

label reveil_start:
    scene decor chambre
    show helene normal at left
    with ellipse
     
    inconnu "Ça y est, t'es réveillé ?"
    inconnu "..."
    
    inconnu "Hier on s'est fait attaquer et... tu as fait une grosse chute."
    inconnu "..."
    
    inconnu "Tu ne te rappelles vraiment plus de rien ?!"
    
    menu:
        "Non.":
            inconnu "OK…"
    
    pause 1.0

    inconnu "Du coup, j’imagine que t’as beaucoup de questions."
    
    menu:
        "Qui suis-je ?":
            jump presentation_leon
        "Où sommes-nous ?":
            jump presentation_lieu
        "Tu m'a toujours pas dis qui tu es." if choix1 == 1:
            jump presentation_helene
                    
label presentation_helene:
    inconnu "C'est vrai, commençons par ça."
    inconnu "Je m'appelle Hélène."
    helene "On se connait depuis de nombreuses années."
    helene "J'étais noble avant le début du Royaume des Templiers, comme toi d'ailleurs."
    helene "Et nous voilà dans l'Ordre du Lys à mener des attaques terroristes."
    
    jump arrivee_anne
                    
label presentation_leon:
    inconnu "Oui évidemment, tu dois même plus connaître ton nom."
    inconnu "Tu t'appelles Léon, tu étais un enfant noble quand on s'est connu."
    inconnu "Lors de la prise de pouvoir des Templiers, on a rejoint ensemble l'Ordre du Lys."
    inconnu "Ah oui j'oubliais : je m'appelle Hélène."
    
    jump arrivee_anne
                    
label presentation_lieu:
    inconnu "Nous sommes dans une planque souterraine, proche du chateau de Fontainebleau."
    inconnu "Ca fait quelques mois qu'on est ici."
    
    jump arrivee_anne
                    
label arrivee_anne:
    "--Autres explications / 2nd lot de question à poser--"
    
    show anne normal at right
    
    anne "Salut Léon !"
    anne "Désolé de vous couper mais Charles nous convoque dans la grande salle."
    helene "OK, on arrive."
    
    hide anne
    
    helene "Tu penses que ça ira ?"
    
    menu:
        "Oui":
            show helene souriante at left
            helene "Allons-y alors."
            jump meeting_1
        "Je sais pas":
            helene "Je comprends, ça doit faire très bizarre de tomber au milieu d'un groupe terroriste sans rien savoir. Mais ici tout le monde te connait bien et personne te veut du mal."
            show helene souriante at left
            helene "Aller, allons-y, ça sert à rien de les faire attendre."
            jump meeting_1
                    
label meeting_1:
    scene decor grande_salle
    show charles normal at center
    show gaston normal at left
    show anne normal at right
    with ellipse

    charles "Content de te voir debout Léon, tu nous auras fais une grosse frayeur, surtout à Hélène. Mais ne perdons pas de temps, tu dois te poser beaucoup de questions !"
    charles "Je parle, je parle mais je ne me suis toujours pas présenté ! Je m’appelle Charles IV fils de Philippe Le Bel et dernier descendant direct des Capétiens."

    menu:
        "S’agenouiller":
            show gaston souriant at left
            show anne souriante at right
            gaston "Ha ha ha!"
            anne "Ne rigole pas trop Gaston, souviens toi, tu as réagis de la même manière lors de votre première rencontre !"
            
            show charles serieux at center
            
            charles "Arrêtez un peux vous deux !"
            
            show gaston serieux at left
            show anne serieuse at right
            
            show charles normal at center
            
            charles "Relèves toi Léon, pas besoin d’un tels protocole, nous sommes tous égaux dans ce groupe, et puis la monarchie a disparut depuis bien longtemps"
        "Ne pas s’agenouiller":
            pause 0.0
    
    charles "Le monarchie a disparu depuis bien longtemps, je ne suis maintenant plus qu’un prince déchus. Nous sommes dorénavant tous égaux dans ce groupe contre un ennemi commun"
    
    menu:
        "La monarchie a disparu ?":
            charles "Oui… C'est maintenant les Templiers qui gouvernent. Nous étions à deux doigts de mettre fin à leurs pratique de la magie noire. Mais ils ont commencé à (...)"
        "Qui est l’ennemi commun ?":
            charles "Les templiers… Nous étions à deux doigts de mettre fin à leurs pratique de la magie noire. Mais ils ont commencé à (...)"

    "Suite de la conversation où Charles mentionne une maladie contagieuse incurable que les démons infligent et que l'attaque précédente leur a permis de mettre la main sur un document indiquant que Jacques de Molay, grand maître des Templiers, partira à la chasse des la forêt de Fontainebleau le lendemain du jour présent, occasion en or pour tenter un assassinat. Léon a finalement des nausées et ressent une douleur au bras et demande à ce qu’on le laisse se reposer."

label retour_chambre:
    scene decor chambre with ellipse
    
    "De retour dans sa chambre, il tire sa manche et aperçoit une marque étrange sur le bras."
    
    show bras_leon debut at bras_transform
    
    "Il se passe de l'eau dessus via un sceau d'eau avoisinant. Il aperçoit alors son visage dans le reflet de l'eau."
    
    "Tout d'un coup, son bras se met à lui faire très mal."
    
    jump vision_01

label vision_01:
    scene decor noir with ellipse
    
    "--Réminéscence : Un souvenir flou revient à l'esprit de Léon. Il distinque la silouhette d'un homme--"
    inconnu "Léon, il y a plusieurs choses que tu dois savoir sur les démons."
    jump gaston_manche

label gaston_manche:
    scene decor chambre with ellipse
    
    "On entend quelqu'un rentrer. Léon retrousse rapidement sa manche."
    
    show gaston normal at right with dissolve
    
    gaston "Salut Léon ! T'as un petit moment ? J'ai quelque chose à te dire."
    
    show gaston serieux at right
    
    gaston "Pendant l'attaque, je me suis servis d'un artéfact démoniaque et... tu as été touché."
    
    menu:
        "S'énerver":
            gaston "Je suis vraiment désolé..."
        "Demander plus de précisions":
            pause 0.0
    
    gaston "Je l'avais trouvé après une attaque. On s'est dit que ça pourrait nous protéger contre les démons."
    gaston "Je savais que ça faisait tombé la personne dans les pommes, mais je savais pas que ça leur faisait aussi perdre la mémoire."
    
    pause 2.0
    
    gaston "Je m'en veut énormément tu sais ! Je sais à quel point ça t'as fait du mal."
    gaston "Crois-moi, je vais tout faire pour me racheter."
    gaston "A ce propos, il faut que je te dise quelque chose que j'ai jamais osé te dire avant : fais attention à Hélène. Je sais à quel point vous vous aimez tous les deux mais..."

    menu:
        "S'exclamer et demander plus d'info":
            gaston "Comment ça ? Elle t'as rien dit ?!"
            gaston "Tu vois, c'est pour ça que je te dis de te méfier d'elle. A mon avis elle joue un double jeu."
            gaston "Ta perte de mémoire, c'est peut-être l'occasion de remettre votre relation en question."
        "Ne rien dire":
            gaston "...je la suspecte de jouer un double jeu."
    
    show anne normal at left with dissolve
    
    anne "Gaston ? Charles voudrait te parler."
    gaston "Ah ? J'y vais de ce pas. A tout à l'heure Léon !"
    
    hide gaston with dissolve
    
    anne "T'en fais une drôe de tête !"
    anne "T'inquiète pas, Gaston peut être dur parfois mais qu'il a un passé difficile. Il avait une relation cachée avec une noble et elle a été tuée lors de l'attaque des templiers."
    anne "Dis, j'ai un truc à te proposer, mais faut qu'on en parle à Charles."
    
    jump grande_salle
    
label grande_salle:
    scene decor grande_salle with ellipse
    
    show charles normal at right with dissolve
    show anne normal at left with dissolve   
    
    "Anne dit que si Léon voit un peu les environs ça peut l'aider à se rappeler de certaines choses. Charles dit que c'est dangereux, et que seul Hélène pourrait aller avec lui car son visage n'est pas connu contrairement au leur."
    "Léon se sent subitement mal."
    
    scene decor noir with dissolve
    
    inconnu "Les démons peuvent prendre une forme humaine."

    scene decor grande_salle
    show charles serieux at right
    show anne serieuse at left
    with dissolve
    
    anne "Léon ! T'es sur que ça va ?"

    menu:
        "Dire que tout va bien":
            charles "Comment ça ?! Tu viens de t'écrouler sur le sol au milieu de la conversation !"
        "Dire qu'on se sent mal":
            charles "Je vois ça oui ! Tu viens de t'écrouler sur le sol au milieu de la conversation !"
    
    charles "Anne, pourrais tu nous laisser, je dois m'entretenir avec Léon. Merci"
    anne "Très bien, je dois de toute façon préparer les armes pour l'assaut de demain."
    hide anne with dissolve
    
    charles "J'ai quelque chose à te donner. C'est une dague. Prends là, tu seras heureux de l'avoir quand tu en auras besoin, crois moi !"
    charles "Bon. Je dois retourner travailler, prends soin de toi Léon."
        
    menu:
        "Lui demander si les démons peuvent prendre forme humaine":
            charles "Hein? Non, d'où te viens des idées pareilles, je ne pense pas que ce soit possible, c'est même completement n'importe quoi !"
        "Le laisser partir":
            pause 0.0
    
    hide charles with dissolve
    show bras_leon mid at bras_transform
    
    pause 3.0
        
    jump planque_entree
    
label planque_entree:
    scene decor entree with ellipse
    
    show helene normal at center with dissolve
    helene "Allons au village, ça te fera du bien de prendre l'air."
    jump village
    
label village:
    scene decor village with ellipse
    
    show helene souriante at center with dissolve
    
    "Ils arrivent au village."
    
    "--Léon peut demander des explications à Hélène quant à leur relation--"
    
    "Elle lui dit que malgré qu'il a perdu la mémoire, il n'a pas changé. Elle lui raconte de joyeux souvenirs qu'ils ont eu ensemble dans ce village. "
    
    show helene inquiete at center
            
    helene "Comment va-tu depuis ta perte de mémoire ? Je suis désolée de pas pouvoir t'aider plus mais nous devons tous préparer l'assaut de demain."
    
    menu:
        "Je lui dit que tout va bien, que tout le monde essaye de m'aider":
            $ showBlessureToHelene = 0
            helene "Ok.. Si tu le dis"
            show helene normal at center
        "Je lui parle de la blessure au bras":
            $ showBlessureToHelene = 1
            show helene inquiete at center
            "Léon lui montre la blessure et lui dit que Gaston en est le responsable. Hélène prend une mine terne et ne répond rien."
            
    helene "Bon. Retournons à la planque, la nuit commence à tomber."
    
    jump grande_salle_suite

label grande_salle_suite:
    scene decor grande_salle
    show charles normal at center
    show helene inquiete at right
    show anne normal at left
    with ellipse
    
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

    jump chambre_soir
    
label chambre_soir:
    scene decor chambre with ellipse
    
    "Léon est seul dans sa chambre et regarde sa blessure."
    
    show bras_leon fin at bras_transform
    
    if showBlessureToHelene == 0:
        "Hélène entre brusquement dans la chambre, voit la blessure de Léon, et s'en va froidement."
    
    "Avant de s'endormir, la blessure de Léon se ravive."
    
    jump last_vision

label last_vision:
    scene decor noir with ellipse
    
    inconnu "Les démons sous forme humaine... On peut les reconnaître à leurs yeux"
    "--Hélène a les yeux vairons, c'est au joueur de faire le rapprochement--"
    jump chambre_nuit

label chambre_nuit:
    scene decor chambre with ellipse
    
    "La nuit passe"
    
    if showBlessureToHelene == 0:
        if wantToGoToBattle == 1:
            jump final_03
        else:
            jump final_02 
    elif showBlessureToHelene == 1:
        jump final_01
        
        
label final_01:
    scene decor chambre with ellipse
    
    "Léon se réveille et sort de sa chambre"
    
    scene decor grande_salle with dissolve 
    
    "Léon découvre le cadavre de Gaston, paniqué."
    "Léon cours sans se poser de question et tombe sur Hélène dans la grande salle, paniquée, qui lui dit que Charles est devenu fou et a tué Gaston."
    "Charles arrive et demande ce qui se passe, Léon marche à reculon, paniqué, sous l'incompréhension de Charles. Charles se fait alors soudainement transpercer le coeur par Hélène, sous forme démoniaque."
    "Anne arrive et hurle de terreur en voyant le cadavre de Charles, puis Hélène la transperce également à son tour."
    "Hélène s'approche alors de Léon en disant qu'elle aurait préféré ne pas avoir à montrer son véritable visage aussi tôt."
    jump end
    

label final_02:
    scene decor chambre with ellipse
    
    "Silence..."
    
    menu:
        "Aller voir dans la grande salle":
        
            show decor grande_salle with dissolve
    
            "Bruit de quelqu'un arrivant en panique"
    
    "Gaston arrive en courant, paniqué."
    
    show gaston normal at left
    
    gastion "Helène ! Elle a tué tout le monde !!! Viens, faut qu'on se tire !"
    
    "Hélène apparait sous forme démoniaque..."
    
    show helene_demon normal at right
    
    "...et transperce immédiatement Gaston dans le dos"
    
    helene "Enfin, on est tranquille. Si Gaston n'avait pas eu la merveilleuse idée de venir te chercher, t'aurais peut-être eu la vie sauve..."
    
    jump end
    
label final_03:
    scene decor chambre with ellipse
    
    "Toc-Toc-Toc"
    
    show helene souriante at center with dissolve
    
    helene "Aller, c'est l'heure de partir à l'attaque !"
    
    scene decor fontainebleau with ellipse
    
    "Le groupe s'infiltre dans le Jardin de Fontainebleau en assassinant furtivement des gardes."
    "Ils se camouflent dans de la verdure sur le terrain de chasse, chemin par lequel Jacques de Molay devrait passer."
    "Hélène annonce alors qu'elle n'a plus le choix et qu'elle n'aurait pas voulu en arriver là si tôt, puis Anne pousse un hurlement."
    "Elle a été transpercée dans le coeur par Hélène qui a alors pris une forme démoniaque."
    "Gaston sort son artefact, paniqué mais Hélène se précipite sur lui et le transperce à son tour pendant que Léon est figé par la peur et Charles figé par la mort d'Anne."
    "Hélène s'approche alors lentement de Charles qui ne tente rien et elle le transperce à son tour."
    "Hélène s'approche finalement de Léon en lui disant que c'est dommage qu'elle doive en arriver là."
    jump end
    
label end:
    "Hélène face à lui et dos au mur, Léon sort alors son poignard et transperce Hélène dans le coeur."
    "Hélène mourrante, Léon retrouve alors ses souvenirs dans un long flashback."
    
    scene decor noir with dissolve
    
    "--Scènes de flashback--"
    "Léon est en réalité un Templier."
    "Les visions que Léon avait ces derniers jours étaient en fait des souvenirs d'une conversation qu'il a eu avec Jacques de Molay, grand maître des Templiers, qui lui parle des démons alors que Léon est sur le point de lui-même faire une invocation."
    "C'est ainsi que Léon invoque Hélène."
    "Léon asassinera alors le roi Philippe le Bel de ses propres mains, et accomplira par le temps plusieurs missions en compagnie deHélène visant à neutraliser la résistance."
    "Pendant ces années, il tissera également des liens amoureux avec Hélène."
    "Un jour, Jacques de Molay demande à Léon et Hélène, en qui il a une entière confiance, d'infiltrer l'Ordre du Lys, principal atout de la résistance que l'Empire Templier a été capable de trouver, afin de récolter le plus d'information possible sur les alliés de l'ordre en leur disant qu'ils pouvaient les décimer si nécéssaire."
    "C'est ainsi que Léon et Hélène ont intégrés l'Ordre."
    
    if wantToGoToBattle == 1:
        show decor fontainebleau with dissolve
    else:
        show decor grande_salle with dissolve
    
    "Hélène, prononçant ses derniers mots, constate que Léon en sanglots se souvient de tout et est heureuse de le revoir étant lui-même, lui dit que sa blessure au bras était fatale et que son seul moyen de le sauver était de lui transmettre son énergie vitale, impliquant sa propre mort."
    "Hélène meurt alors dans les bras de Léon, le sourire aux lèvres."
    
    "FIN"
    
    return