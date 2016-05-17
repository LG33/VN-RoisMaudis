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

image bras_leon_flashback = im.MatrixColor("characters/bras_leon_fin.png",im.matrix.saturation(0.1))

define leon = Character('Léon', outlines=[(1, "#008800", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define helene = Character('Hélène', image="helene", outlines=[(1, "#ff00ff", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define gaston = Character('Gaston', image="gaston", color="#9999ff", window_top_padding=40, window_background="gui/dialogue_box.png")
define anne = Character('Anne', image="anne", color="#eeeeee", window_top_padding=40, window_background="gui/dialogue_box.png")
define charles = Character('Charles', image="charles", outlines=[(1, "#aa7700", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define inconnu = Character('???', window_top_padding=40, window_background="gui/dialogue_box.png")
define self = Character(None, color="#ffff99", what_italic=True, what_color="#ffdd55", window_top_padding=90, window_background="gui/narrative_box.png")
define jacques = Character("jacques_name", dynamic=True, what_color="#8888ff", what_italic=True, what_slow_cps=10, window_top_padding=40, window_background="gui/dialogue_box.png")

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

define ellipse = Fade(0.5, 1.0, 0.5)
define long_dissolve = Dissolve(1.0)

init python:
    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)
    
    shake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    flash = Fade(.25, 0, .25, color="#ff0000")
    
    choix1 = 0
    jacques_name = "???"
    helene_side = Character('',color="#ff99ff",window_left_padding=288,window_top_padding=40,show_side_image=Image("side_image/lucy_surprized.png", xalign=100, yalign=0.87), )
    
    #config.empty_window = renpy.curry(extend)("", interact=False)

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
    show helene masque at center
    
    inconnu "Léon ! Léon !!"
    
    with flash
    
    self "Que… qu’est-ce qu’il se passe ?"
    
    scene decor intro
    show helene masque at center
    with long_dissolve
    
    pause 0.5
    
    inconnu "Tu t’es évanoui. Dépêche-toi, il faut fuir !"
    self "Je… je ne comprends rien…"

    menu:
        "Demander qui je suis":
            leon "Qui suis-je ?"
            jump fuite_fin
        "Demander qui elle est":
            leon "Qui êtes-vous ?"
            jump fuite_fin
    
label fuite_fin:
    inconnu "QU… {w=0.7}QUOI ?!"
    
    pause 2.0
    
    inconnu "On n’a pas le temps, suis-moi !"
    leon "Ah… ma tête…"
    
    with shake

    scene decor noir with dissolve

    inconnu "LEON !!!"

    pause 5.0

    jump reveil_start

label reveil_start:
    scene decor chambre
    show helene inquiete at left
    with dissolve

    inconnu "Ça y est, t'es réveillé ?"
    leon "..."    
    inconnu "J’étais vraiment inquiète, tu sais!"
    self "Cette voix… c’est la fille au masque ?"

    show helene normal
    
    inconnu "L’attaque d’hier ne s’est pas passée comme prévu mais ne t’inquiète pas, Gaston t’as porté et on s’en est tous sortis indemnes."
    leon "Une attaque ? Gaston ?"

    show helene inquiete
    pause 1.0

    inconnu "Je m’en doutais… Tu ne te souviens vraiment plus de rien…"

    #show helene normal at left

    helene normal "Tu ne te souviens même plus de moi… je m’appelle Hélène."

    menu:
        "Demander qui je suis":
            jump reveil_1_1
        "Demander où nous sommes":
            jump reveil_1_2
        "Demander ce qu’était l’attaque d’hier":
            jump reveil_1_3

label reveil_1_1:
    leon "Qui suis-je ?"
    helene "Tu t’appelles Léon. Comme nous tous, tu es un membre de l’Ordre du Lys"
    jump reveil_1_end

label reveil_1_2:
    leon "Où est-ce qu’on est ?"
    helene "Nous sommes dans des souterrains. Tu peux voir ça comme la base secrète de l’Ordre du Lys"
    jump reveil_1_end

label reveil_1_3:
    leon "De quelle attaque tu parles ?"
    helene "Nous avons attaqué une église templière au nom de l’Ordre du Lys"
    jump reveil_1_end

label reveil_1_end:
    leon "L’ordre du Lys ?"

    pause 0.3
    "*bruits de pas et porte qui s’ouvre*"
    pause 0.5
    show anne normal at right with dissolve

    inconnu "Hélène, Charles demande à nous voir."

    pause 1.0
    show anne souriante

    inconnu "Ah, Léon, tu es enfin réveillé !"
    inconnu "Tu as dormi comme un loir, tu sais! Ne nous fais plus de frayeurs comme ça !"

    show helene inquiete

    helene "Anne… Il a perdu la mémoire…"

    show anne serieuse

    anne "Oh…"

    pause 2.0

    show anne souriante

    anne "Je suis Anne, nous sommes amis. J’espère que tu retrouveras rapidement la mémoire !"

    show anne normal

    anne "Charles nous attend. Léon, tu devrais venir avec nous."
    
    jump reunion_start
    
label reunion_start:
    scene decor noir with dissolve
    pause 2.0
    "*bruits de pas multiples*"
    self "Les couloirs étrois et humides... ça ne me met pas vraiment à l'aise"
    
    scene decor grande_salle with dissolve
    show charles normal at left
    show gaston normal at right
    
    pause 2.0
    show charles at center with move
    
    inconnu "Alors comme ça, tu as perdu la mémoire..."
    charles "Je suppose qu'on doit se présenter du coup. Tu peux m'appeler Charles. Je suis le fondateur et dirigeant de l'Ordre du Lys"
    
    show charles at left with move
    show gaston at center with move
    
    gaston souriant "Moi, c'est Gaston. T'as intérêt à vite retrouver la mémoire mon gars !"
    
    hide charles
    hide gaston
    show helene serieuse at center with dissolve
    
    helene "Gaston!"
    
    hide helene
    show gaston normal at center with dissolve
    
    gaston "Oh ça va je plaisante!"
    leon "Vous parliez de l'Ordre du Lys.. vous pouvez m'expliquez ce que c'est ?"
    hide gaston
    
    show charles normal at center
    charles "Nous sommes un groupe de résistants qui nous battons désespérément pour libérer le pays des Templiers."
    
    menu:
      "Demander pourquoi le combat est désespéré":
           jump reunion_1_1
      "Demander qui sont les Templiers":
           jump reunion_1_2

label reunion_1_1:
    leon "Comment ça, désespérément?"
    jump reunion_1_end

label reunion_1_2:
    leon "Comment ça, les Templiers?"

    hide charles
    show helene inquiete at center with dissolve

    helene "Tu ne te souviens vraiment plus de rien…"

    hide helene
    jump reunion_1_end
    
label reunion_1_end:

    show charles serieux at center with dissolve

    charles "Il y a une dizaine d’années, les Templiers, un groupe religieux maléfique, a eu recours à des rites démoniaques."

    hide charles
    show gaston serieux at center with dissolve

    gaston "Ces salopards ont invoqué des démons et ont utilisé leurs pouvoirs pour tuer un grand nombre d’innocents."

    hide gaston
    show charles serieux at center with dissolve
    
    charles "Ces démons ont écrasé le Royaume en seulement quelques jours et terrorisent maintenant le peuple en lançant une malédiction à tous ceux qui agiront d’une façon qui leur déplait."
    charles "Une marque noire apparaît sur le corps de la personne maudite et s’étend peu à peu sur tout son corps. Après quelques jours, quand le corps est entièrement recouvert, la personne meurt dans d’atroces souffrances. Comme si ça ne suffisait pas, les personnes affectées sont généralement rejetées par leurs proches, par peur."
    leon "Ça n’a pas l’air plaisant..."

    hide charles
    show anne serieuse at center with dissolve

    anne "L’Ordre du Lys a été crée dans le but de lutter contre ce règne de terreur. Nous sommes tous les cinq de bons combattants. On se manifeste pour l’instant surtout en assassinant des haut gradés Templiers, mais notre véritable objectif est de renverser entièrement les Templiers."
    menu:
        "Annoncer que je ferais tout mon possible":
           jump reunion_2_1
        "Demander si c’est vraiment un objectif réaliste":
           jump reunion_2_2

label reunion_2_1:
    leon "Je vais faire tout mon possible pour vous aider!"

    show anne souriante

    anne "Ravie de l’entendre ! Et ne t’inquiète pas, le peuple aussi est de notre côté ! D’ailleurs, bien qu’ils ne souhaitent pas s’impliquer directement dans la lutte, on a de nombreux alliés qui nous fournissent en fonds ou en informations. "
    jump reunion_2_end

label reunion_2_2:
    leon "Vaincre les Templiers… C’est vraiment à notre portée ? Nous ne sommes que cinq..."
    anne "Mais le peuple est de notre côté ! D’ailleurs, bien qu’ils ne souhaitent pas s’impliquer directement dans la lutte, on a de nombreux alliés qui nous fournissent en fonds ou en informations. "

    show anne souriante

    jump reunion_2_end

label reunion_2_end:

    anne "Charles était un prince de l’ancien royaume et est le seul survivant de la famille Royale. L’avoir de notre côté aide pour notre image."

    hide anne
    show charles normal at center with dissolve

    self "Un… un prince ?!"
 
    menu:
        "S’agenouiller":
           jump reunion_3_1
        "Demander ce qu’un prince fait ici":
           jump reunion_3_2

label reunion_3_1:
    leon "Excusez-moi, mon altesse. Je ne savais pas."

    pause 2.0
    hide charles
    show gaston souriant at center with dissolve

    gaston "Ha ha ha! Tu devrais voir ta tête !"

    hide gaston
    show anne normal at center with dissolve

    "Anne semble aussi se retenir de rire…"
    anne "Gaston! Ne te moque pas, tu avais réagi exactement de la même façon la première fois que tu as rencontré Charles toi aussi."

    show anne souriante

    anne "On a décidé que les statuts auraient peu d’importance au sein de l’ordre. D’ailleurs, j’étais une servante à l’origine!"

    jump reunion_3_end

label reunion_3_2:

    leon "Un prince devrait vraiment se battre parmi un groupe pareil ?"

    hide charles
    show anne souriante

    anne "Son simple nom permet de nous rendre plus crédible auprès de nos alliés. Et puis on a décidé qu’au sein de l’ordre les statuts auraient peu d’importance. D’ailleurs, j’étais servante à l’origine !"

    jump reunion_3_end

label reunion_3_end:

    hide anne
    show gaston souriant at center with dissolve

    gaston "Et moi, j’étais paysan. Dur à croire, hein !"

    hide gaston
    show helene normal at center with dissolve

    helene "Quand à nous, nous étions des nobles."

    hide helene
    show charles normal at center with dissolve

    charles "Bien. Je sais que tout ne doit pas être encore très clair pour toi, mais je vous  ai tous demandé à venir pour une raison précise."
    "Tout le monde semble si sérieux d’un coup…"
    charles "L’attaque d’hier, dont le but était d’assassiner un officier Templier, a été menée avec succès."

    show charles serieux

    charles "Enfin, si on omet ce qui est arrivé à Léon, bien entendu."

    show charles normal

    charles "Comme à notre habitude, nous avons rapidement pris les documents qui traînaient sur place avec nous, juste au cas où."
    charles "Nous avons entre autres ramassé cette lettre. Anne, peux-tu la lire ? Tu vas comprendre où je veux en venir."

    hide charles
    show anne normal at center with dissolve

    anne "Voyons voir… oh, c’est une lettre écrite par Jacques de Molay !"
    leon "Jacques de Molay ?"

    hide anne
    show helene normal at center with dissolve

    helene "C’est le grand Maître des Templiers. Il n’y a personne au dessus de lui"
    leon "Je vois…"

    hide helene
    show anne normal at center with dissolve

    anne "Elle s’adresse au Templier qu’on a assassiné. Ils semblaient plutôt proche, mais il n’y a rien de bien intéressant jusque là… OH !"

    show anne serieuse

    anne "Charles ! On ne peut pas passer à côté d’une occasion pareille !"

    hide anne
    show gaston serieux at center with dissolve

    gaston "Qu’est ce qu’il y a ?"

    hide gaston
    show anne serieuse at center with dissolve

    anne "Je vous lis ce qu’il y a d’écrit"
    anne "\"Mon âge me permet de moins en moins à partir à la chasse, mais ça m’arrive encore de temps en temps. D’ailleurs, j’ai prévu de partir chasser dans la forêt de Fontainebleau à l’occasion de l’Ascension, dans la matinée. J’ai hâte !\""

    hide anne
    show gaston serieux at center with dissolve

    gaston "Mais… C’est demain !"

    hide gaston
    show charles serieux at center with dissolve

    charles "C’est exact. Vous voyez où je veux en venir. Jacques de Molay ne sort quasiment plus du château, ce genre d’occasion est très rare. Nous allons évidemment nous préparer à"
    hide charles
    show helene inquiete at center
    helene "Léon ! Tu vas bien ?!"
    leon "…pas vraiment… je peux me reposer dans ma chambre ?"

    hide helene
    show charles serieux at center

    charles "Bien sûr. Repose-toi bien."

    jump retour_chambre

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