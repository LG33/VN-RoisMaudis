# commentaires généraux.
# 01 - Fuite
label start:
    # play sound ["music/AttaqueMagique.mp3" , "music/ChuteHomme.mp3"] fadein 1.0
    
    play gui "music/BoutonSelection.mp3"
    
    stop music fadeout 1.0
    scene decor noir with long_dissolve

    inconnu "Léon ! Léon !!"
    pause 1.0
    play cloche "music/SonCloche.mp3" fadein 4.0 loop
    play sound "music/BruitageChien.mp3" fadein 2.0 loop

    self "Que... {w=0.2}qu’est-ce qu’il se passe ?"

    scene decor intro with long_dissolve

    pause 0.5

    inconnu "Tu t’es évanoui. Dépêche-toi, il faut fuir !"
    self "Je... {w=0.2}je ne comprends rien..."

    menu:
        "\"Où sommes-nous ?\"":
            leon "Où sommes-nous ?"
            jump fuite_fin
        "\"Qui êtes-vous ?\"":
            leon "Qui êtes-vous ?"
            jump fuite_fin
    
label fuite_fin:
    inconnu "QU... {w=0.2}QUOI ?!"
    
    pause 2.0
    
    inconnu "Il ne manquait plus que ça ! "
    inconnu "Léon... {w=0.2}tu...{w=0.2} qu’est-ce qu’il t’arrive ?"
    inconnu "..."
    inconnu "On n’a pas le temps. Suis-moi !"
    leon "Ah... {w=0.2}ma tête..."
    with shake
    play sound "music/FlashSound.mp3"

    scene decor noir with long_dissolve

    stop cloche fadeout 1.5

    inconnu "LÉON !!!"

    stop sound fadeout 1.5
    stop music fadeout 1.5

    pause 3.0

    jump reveil_start
# END FILE 01 - Fuite

# 02 - Réveil

label reveil_start:
    play music "music/planque_dialogue.mp3" fadein 1.0 loop
    pause 3.0

    scene decor chambre with long_dissolve

    pause 3.0

    show helene inquiete at center with long_dissolve

    inconnu "Ça y est, tu es réveillé ?"
    leon "..."    
    inconnu "J’étais vraiment inquiète, tu sais !"
    self "Cette voix... {w=0.2}c’est la fille au masque ?"

    show helene normal
    
    pause 1.0

    inconnu "L’assaut d’hier ne s’est pas passé comme prévu et on t’a retrouvé évanoui après s’être séparés."

    show helene inquiete

    inconnu "Ils étaient mieux préparés que ce que nous avions anticipé... Certains avaient même des armes magiques."

    show helene normal

    inconnu "Mais ne t’inquiète pas, Gaston t’a porté et on s’en est tous sortis indemnes."
    leon "Un assaut ? Gaston ?"

    show helene inquiete
    pause 2.0

    inconnu "Je m’en doutais... {w=0.2}Tu ne te rappelles vraiment plus de rien..."

    helene normal "Tu ne te souviens même plus de moi... {w=0.2}Hélène..."

    menu:
        "\"Où est ce qu’on est ?\"":
            jump reveil_1_1
        "\"Qu’est-ce qui s’est passé ?\"":
            jump reveil_1_2

label reveil_1_1:
    leon "Où est ce qu’on est ?"
    helene "Nous sommes dans des souterrains. Tu peux voir ça comme la base secrète de l’Ordre du Lys."
    jump reveil_1_end

label reveil_1_2:
    leon "Qu’est-ce qui s’est passé ?"
    helene "Nous avons attaqué une église au nom de l’Ordre du Lys, mais ça ne s’est pas passé parfaitement et tu as fini dans cet état..."
    jump reveil_1_end

label reveil_1_end:
    leon "L’Ordre du Lys ?"

    pause 0.3
    play sound "music/door_opening.ogg"
    pause 0.5
    show helene at left with move
    show anne normal at right with long_dissolve

    inconnu "Hélène, Charles demande à nous voir."

    pause 1.0
    show anne souriante

    inconnu "Ah, Léon, tu es enfin réveillé !"
    inconnu "Tu as dormi comme un loir, tu sais. Ne nous fais plus de frayeurs comme ça !"

    show helene inquiete

    helene "Anne... {w=0.2}Il a perdu la mémoire..."

    show anne serieuse

    anne "Oh..."

    pause 2.0

    show anne souriante

    anne "Je suis Anne, nous sommes amis. "
    anne normal "Charles nous attend. Léon, tu devrais venir avec nous."

    stop music fadeout 2.0
    play sound "music/door_close.ogg"

    jump reunion_start
# END FILE 02 - Réveil


# 03 - Réunion
label reunion_start:
    scene decor noir with long_dissolve
    pause 3.0

    self "Où est-ce qu’ils m’emmènent..."
    
    play cloche "music/grande_salle.ogg" fadein 1.0 loop

    pause 3.0

    scene decor grande_salle
    show charles normal at left
    show gaston normal at right
    with long_dissolve

    self "Ces personnes... {w=0.2}leur visage ne me dit rien."

    hide gaston with dissolve
    show charles normal at center with move
    
    inconnu "Léon aurait donc perdu la mémoire..."
    charles "Je m'appelle Charles. Je suis fondateur et dirigeant de l'Ordre du Lys."
    
    hide charles with dissolve
    show gaston souriant at center with dissolve

    gaston "Moi, c'est Gaston. T'as intérêt à vite retrouver la mémoire !"
    leon "L'Ordre du Lys... {w=0.2}qu’est-ce que c'est ?"

    hide gaston with dissolve
    show charles normal at center with dissolve

    charles "Tu te souviens de la situation de la France actuellement ?"
    leon "Non..."
    charles "De quoi te rappelles-tu ?"
    leon "Pas de grand chose... {w=0.2}Je sais juste que nous sommes en France et il me semble que nous sommes en 1313."
    charles serieux "C’est tout ?"
    charles "..."
    charles normal  "On va devoir reprendre depuis le début."
    charles "La France est dirigée par les Templiers, un groupe de religieux fanatiques catholiques."
    charles serieux "Ils ont mit la main il y a plus de 50 ans sur le Missel Satanique durant la septième croisade."
    charles normal "Jusqu’à récemment, ils ne s’étaient pas montrés menaçants."
    charles serieux "Cependant…"
    charles "Jacques de Molay, le grand maître des Templiers, a réussi à déchiffrer ce manuscrit."
    charles "Il s’en est alors servi afin d’invoquer des démons, les Disciples de Baphomet, en pratiquant des rites occultes."
    charles "Ce sont des créatures immondes à six bras et la peau calcinée."
    charles "Ils peuvent maudire leurs ennemis ce qui provoque une mort douloureuse."
    self "Des... {w=0.2}des démons ?! Vraiment ?!"

    hide charles with dissolve
    show gaston serieux at center with dissolve

    gaston "Ces chiens ont utilisé leur pouvoir pour tuer un grand nombre d’innocents."

    hide gaston with dissolve
    show charles normal at center with dissolve
    
    charles "Il y a six ans, les Templiers ont terrassé les armées du roi Philippe le Bel avec ces démons."
    charles serieux "Ils se sont emparés du pouvoir en à peine un mois et ont exécuté les membres de la famille royale."
    charles "Depuis, ils dirigent le pays en imposant leurs dogmes."
    charles "Ils projettent de renverser les différents royaumes européens pour que seul l'Église gouverne."
    charles "Actuellement, ils convoient les terres du rois Édouard II d’Angleterre et de l’empereur Henri VIII de Germanie."
    charles "..."
    charles normal "En tant que prince héritier, il était de ma responsabilité de fonder l’Ordre du Lys."
    charles "C’est un groupe de résistants qui luttent contre les Templiers."
    self "Un... {w=0.2}un prince ?!"

    menu:
        "\"Excusez mon impolitesse, votre altesse. Je ne savais pas.\"":
            jump reunion_1_1
        "\"Mais tu n'es plus un prince maintenant que les Templiers ont pris le pouvoir, non ?\"":
            jump reunion_1_2

label reunion_1_1:
    leon "Excusez mon impolitesse, votre altesse. Je ne savais pas."
    charles serieux "Ne t'inquiète pas pour ça, j'ai horreur de ce genre de formalités."

    hide charles with dissolve
    show anne souriante with dissolve

    anne "Charles est le seul survivant de la famille royale."
    anne serieuse "Lors de la prise du pouvoir des Templiers, son père, Philippe le bel, ainsi que le reste de sa famille ont été exécutés."
    leon "Avec un prince à sa tête, L’Ordre du Lys doit être plus puissant que je ne pensais."
    jump reunion_1_end

label reunion_1_2:
    leon "Mais tu n'es plus un prince maintenant que les Templiers ont pris le pouvoir, pas vrai ?"
    charles serieux "..."
    charles "Tu as raison."
    charles normal "Cependant, je suis le seul survivant de la famille royale. Mon devoir est de diriger l'Ordre et rétablir la monarchie."

    hide charles with dissolve
    show anne serieuse with dissolve

    anne "Lors de la prise du pouvoir des Templiers, son père, Philippe le Bel, ainsi que le reste de sa famille ont été exécutés."
    leon "L’Ordre du Lys a l'air d’être plus puissant que je ne pensais..."

    jump reunion_1_end

label reunion_1_end:

    anne "..."

    hide anne with dissolve
    show charles serieux with dissolve

    charles "..."
    charles "Tu as tous les membres de l'ordre devant toi."
    leon "Que... quoi ?!" with little_shake
    leon "Et vous pensez vaincre avec cinq personnes seulement ?!"
    self "Ils se moquent de moi ?!"

    hide charles with dissolve
    show anne serieuse at center with dissolve

    anne serieuse "Eh, nous ne sommes peut-être pas nombreux, mais le peuple est de notre côté."
    anne "Nous agissons au nom de tous ceux qui n’ont pas la force de s’opposer aux Templiers."
    anne "Et nous avons de nombreux alliés !"

    hide anne with dissolve
    show gaston serieux with dissolve

    gaston "Nous avons le soutien d’Édouard II, le roi d’Angleterre. Il nous fourni des informations et une aide financière précieuse."

    hide gaston with dissolve
    show charles normal with dissolve

    charles "L’Ordre du Lys était bien plus puissant jadis."
    charles "Nous avions toute une armée. Nous étions bien plus nombreux que nos ennemis."
    charles serieux "..."
    charles "Nous avons été massacrés par une malédiction démoniaque, le Feu de Géhenne, introduite dans nos rangs."
    charles "Nous sommes les seuls survivants avec encore la volonté de se battre."
    charles "..."
    charles "Cette malédiction est pire que la mort."
    charles normal "Une marque noire apparaît sur le corps et s’étend partout peu à peu."
    charles "Après quelques jours, le corps est entièrement recouvert."
    charles serieux "Le maudit perd alors la raison et se déchaîne sur son entourage." 
    charles "Il fini par mourir, épuisé mentalement."
    self "Un phénomène pareil existe réellement ?"
    charles normal "De plus, le Feu de Géhenne est contagieux et se transmet par contact..."
    charles "...et il n’y a pas de remède."
    charles serieux "Par conséquent, les maudits sont exécutés sur le champ."
    charles "Certains templiers possèdent même une griffe de Disciple de Baphomet, ce qui leur permet de lancer cette malédiction."
    leon "Vous avez été massacrés et vous souhaitez encore vous battre, à cinq ?!"

    hide charles with dissolve
    show anne normal with dissolve

    anne "Nous avons encore une chance."
    anne "Toute la puissance des Templiers repose sur un seul individu."
    anne serieuse "Jacques de Molay, leur grand maître."
    anne "C’est lui qui est à l’origine de tout."
    anne "Il est également le seul à pouvoir utiliser le Missel Satanique et contrôler les disciples de Baphomet."
    anne "Si nous le tuons, tout le reste s’écroulera."
    anne normal "Quand ça arrivera, les Templiers seront à nouveau faibles et nous reprendrons la France avec l’aide du roi d’Angleterre."
    self "Ce raisonnement semble bien optimiste..."

    hide anne with dissolve
    show charles normal with dissolve

    charles "Bref, tout ne doit pas être très clair pour toi, mais le temps presse."
    charles "Je vous ai demandé à tous de venir pour une raison précise."
    pause 1.5
    self "Tout le monde semble si sérieux d’un coup..."
    charles "Le but de notre attaque de cette nuit était de soutirer des informations à un officier templier proche de Jacques de Molay."
    charles serieux "Malgré ce qui est arrivé à Léon, ce fut un succès."
    charles normal "Ainsi, nous avons réussi à connaître l’emploi du temps du grand maître pour les jours à venir."
    leon "Il l’a simplement révélé ?!"

    hide charles with dissolve
    show gaston serieux at center with dissolve

    gaston "Léon... {w=0.2}Nous l’avons torturé puis égorgé."
    self "...Quoi ?!" with little_shake
    self "Mais c’est horrible !"
    self "Je fais vraiment partie d’un groupe pareil ?!"

    hide gaston with dissolve
    show charles normal at center with dissolve

    charles "Quoi qu’il en soit, nous savons que Jacques de Molay se trouve maintenant au Château de Fontainebleau."
    charles "Il quittera le château ce soir pour Paris."
    charles "D’ici là, il n’aura pas le temps d’apprendre la mort de son officier."
    charles "Autrement dit, il ne se doutera de rien et ne changera pas son emploi du temps."
    charles serieux "Nous ne pouvons pas laisser passer une occasion pareille."
    charles "Nous allons tendre une embuscade et l’assassiner au départ de son trajet."
    charles "Léon, repose-toi pendant que nous nous occupons des préparatifs. Il faut que tu sois en forme ce soir."
    self "...moi ?!"
    self "Ils croient que je vais combattre ?!"

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "Charles, tu n’es pas sérieux ?"
    helene "Hors de question que Léon participe à cet assaut dans cet état !"

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "Léon est de loin le plus doué au combat parmi. Nous avons besoin de lui."

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "C’est ridicule, il a perdu la mémoire ! On ne sait même pas s’il saura se battre !" with little_shake

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "C’est Jacques de Molay que nous attaquons, Hélène. Nous ne pouvons pas nous permettre de nous séparer d’un membre du groupe."
    charles "Nous attendons ce jour depuis si longtemps, nous devons mettre toutes les chances de notre côté."
    charles "Il viendra avec nous, la discussion est close."
    self "Je n’ai même pas mon mot à dire..."

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "..."

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "Nous avons peu de temps. Nous devons dès maintenant nous prépar{nw}"
    
    scene decor noir with flash_blanc
    scene decor noir with shake
    play sound "music/FlashSound.mp3"
    pause 2.0
    
    scene decor grande_salle
    show helene inquiete at center
    with long_dissolve

    helene "Léon ! Tu vas bien ?!"
    leon "...J’ai un énorme mal au crâne..."
    leon "..."
    leon "Je peux retourner dans ma chambre ?"

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "..."
    charles "Bien sûr. Repose-toi bien."

    stop cloche fadeout 2.0

    jump retour_chambre
# END FILE 03 - Réunion

# 04 - Chambre
label retour_chambre:
    
    scene decor chambre with ellipse

    #play music "music/planque_dialogue.mp3" fadein 1.0 loop

    pause 4.0

    self "J’ai la tête qui tourne... {w=0.2}et mon bras..."

    scene arm_gant with long_dissolve

    self "Ca me brûle..."

    scene arm_1 with long_dissolve

    self "{cps=*2}...!{/cps}"
    self "{cps=*2}Qu... {w=0.1}Qu’est-ce que c’est que ça !{/cps}" with little_shake
    self "{cps=*2}Merde ! Ça ne peut pas être ça !{/cps}" with little_shake
    self "{cps=*2}C’était déjà là quand je me suis réveillé ?{/cps}"
    self "{cps=*2}D’après Charles, des griffes magiques peuvent infliger ça...{/cps}"
    self "Je vois..."
    self "J’ai sans doute chopé ça hier, quand j’ai perdu la mémoire..."
    self "{cps=*2}Que-va-t-il m’arriver si les autres le découvrent ?{/cps}"
    self "{cps=*2}Ah ! De l’eau !{/cps}"
    pause 0.5
    play sound "music/BruitEau.wav"
    pause 1.0
    self "{cps=*2}Ça veut pas partir...{/cps}"
    self "{cps=*2}Oh !{/cps}"

    scene decor water with long_dissolve
    #play music "music/planque_dialogue.mp3" fadein 1.0 loop
    pause 2.0

    self "Alors c’est à ça que je ressemble... {w=0.2}Je tire une de ces têtes..."
    self "D’ailleurs, je n’ai idée de l’âge que j’ai..."
    self "J’ai l’air vieux..."

    scene decor noir with flash_blanc
    #stop music fadeout 2.0
    pause 1.0

    jacques_inconnu "L{w=0.0}é{w=0.0}o{w=0.0}n{w=0.0},{w=0.0} {w=0.0}à{w=0.0} {w=0.0}p{w=0.0}r{w=0.0}o{w=0.0}p{w=0.0}o{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0}.{w=0.0}.{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc
    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    self "Que... {w=0.2}quoi ?!" with shake
    self "C’était quoi, ça ?!"
    self "Une hallucination ?! Un souvenir ?!"


    pause 0.5
    play sound "music/door_opening.ogg"
    pause 2.0
    show anne normal at center with dissolve
    pause 1.0

    anne "Léon, tu vas mieux ?"
    self "C’était limite mais j’ai pu couvrir mon bras à temps..."
    anne "Eh, tu m’écoutes ?"
    leon "Ne... {w=0.2}ne t’inquiète pas, c’est juste un coup de fatigue, rien de bien grave."
    anne serieuse "..."
    anne "Te réveiller au milieu d’inconnus doit être dur à vivre..."
    leon "Je ne me souviens d’aucun d’entre vous..."
    leon "Je suppose que vous devez tous être d’importants personnages si Charles est un prince."
    anne souriante "Absolument pas !"
    anne "Je n’étais qu’une servante avant."
    anne normal "Depuis le début, l’origine des membres de l’Ordre étaient très variés."
    anne "Gaston, lui, n’était qu’un paysan."
    anne souriante "Quant à Hélène et toi, vous étiez un couple de nobles."
    leon "Un... {w=0.2}un couple ?!" with little_shake
    leon "Vraiment ?!"
    anne normal "Oh... {w=0.2}elle ne t’en a pas parlé ?"
    anne serieuse "Je vois... {w=0.2}ton amnésie doit être très dure à vivre pour elle aussi."
    anne souriante "Vous étiez ensemble bien avant d’intégrer l’Ordre."
    leon "Elle ne m’en a pas dit un mot..."
    leon "..."
    leon "Argh…"
    with flash_blanc
    stop music fadeout 2.0

    anne serieuse "Léon ?!"
    anne "Tu vas bien ?!"
    leon "…"
    leon "Mon mal de tête est de plus en plus fort…"
    anne "..."
    anne normal "Il faut te soigner. Je vais aller parler à Charles, rejoins-moi dans cinq minutes."

    play sound "music/door_close.ogg"
    
    jump grande_salle
# END FILE 04 - Chambre

# 05 - Dialogue Charles
label grande_salle:
    
    scene decor noir with long_dissolve
    pause 2.5
    play cloche "music/grande_salle.ogg" fadein 1.0 loop
    pause 1.0

    scene decor grande_salle
    show anne serieuse at left
    show charles normal at right
    with long_dissolve
 
    anne "Non Charles, il ne se sent vraiment pas bien."
    anne souriante "Et puis, prendre l’air lui fera du bien !"
    charles serieux "Anne, nous n’avons pas de temps à perdre... {w=0.2}tu es consciente de l’importance de l’attaque de ce soir...?"
    anne "Justement ! À ce rythme, il ne tiendra même plus debout ce soir !"
    charles "..."
    charles "Il ne se souvient même plus du chemin…"
    helene "J’irai avec lui !"
    anne souriante "Ah, tu es là !"

    hide anne
    hide charles 
    with dissolve
    show helene souriante at center with long_dissolve

    helene "Si j’y vais avec lui, il n’y a plus de problème, pas vrai ? Vous préparerez l’attaque tous les trois."

    hide helene with dissolve
    show charles normal at center with dissolve

    charles "Même toi tu t’y mets..."
    charles "..." 
    charles "Très bien. Ne prenez pas trop de temps."
    self "Visiblement, mon avis n’intéresse personne..."
    leon "Et… {w=0.2}On va où exactement ?"

    hide charles with dissolve
    show anne souriante with dissolve

    anne "Au village de Montigny-sur-Loing, voir Léothéric. C’est un herboriste de talent qui est fidèle à l’Ordre."
    anne "Il pourra calmer tes douleurs avec sa potion au genévrier."
    leon "Je vois… ah !"
    pause 0.5
    leon "Ah !{nw}"

    stop cloche fadeout 3.0

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "L{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}v{w=0.0}e{w=0.0}n{w=0.0}t{w=0.0} {w=0.0}p{w=0.0}r{w=0.0}e{w=0.0}n{w=0.0}d{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}u{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0}."

    pause 1.0
    scene decor grande_salle with flash_blanc

    play cloche "music/grande_salle.ogg" fadein 1.0 loop

    show helene inquiete at center with dissolve

    helene "Léon ! Tu vas bien ?!"
    self "Ah... {w=0.2}encore ça ?!"
    helene "Léon ?!"
    leon "Ah, oui… j’ai juste des vertiges..."
    helene "..."

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "Effectivement, tu avais raison Anne, il faut vraiment qu’il se soigne."
    pause 1.0
    charles "Ah, une dernière chose..."
    charles "Anne, Hélène, pourriez-vous nous laissez seuls un instant ?"

    hide charles with dissolve
    show anne serieuse at right
    show helene inquiete at left
    with dissolve

    anne "Très bien."

    hide anne
    hide helene 
    with long_dissolve
    show charles normal at center with dissolve

    self "Pourquoi veut-il me parler ?"
    self "Il ne serait quand même pas au courant pour mon bras ?!"
    charles "Léon..."
    leon "...Oui ?"
    show charles dague at center_dague
    charles "Cette dague est à toi, reprends-la."
    leon "..."
    charles "Tu risques d’en avoir besoin pour te défendre. On ne sait jamais, un templier peut te tomber dessus n’importe quand."
    charles "Je te la rends."
    leon "Ah, merci."
    show charles normal at center
    self "Je me suis inquiété pour rien…"
    charles "Bien. Va retrouver Hélène. Revenez vite."
    leon "Ah ! Je..."
    charles "Oui ?"

    menu:
        "\"Est-ce que les démons peuvent prendre une forme humaine ?\"":
           jump dialogue_charles_1_1
        "Ne rien demander":
           jump dialogue_charles_1_2

label dialogue_charles_1_1:

    leon "Est-ce que les démons peuvent prendre une forme humaine ?"
    charles serieux "Où as-tu entendu une chose pareille ?"
    leon "Nulle part... {w=0.2}je me posais juste la question."
    charles normal "Ne te pose pas des questions aussi insensées. Évidemment qu’ils ne peuvent pas."
    charles "..."
    charles "Bon, allez-y et ne tardez pas."

    jump dialogue_charles_1_end

label dialogue_charles_1_2:

    leon "Non... {w=0.2}rien."
    charles "..."
    charles "Bon, allez-y et ne tardez pas."

    jump dialogue_charles_1_end
    
label dialogue_charles_1_end:

    hide charles with long_dissolve
    stop cloche fadeout 2.0

    pause 1.0
    scene decor noir with long_dissolve
    pause 1.0

    self "Tout à l’heure... {w=0.2}mon bras..."

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_2 with long_dissolve

    self "La marque... {w=0.2}elle s’est étendue..."

    jump village_start
    #jump sortie_start
# END FILE 05 - Dialogue Charles

# 06 - Sortie
label sortie_start:
    scene decor noir with dissolve

    stop music fadeout 3.0
    stop cloche fadeout 3.0

    pause 1.5
    scene decor entree
    show helene normal at center
    with long_dissolve

    helene souriante "Ah, te voila !"
    helene normal "De quoi avez-vous parlé avec Charles ?"
    leon "Rien d’important…"
    helene "..."

    #menu:
        #"\"Il m’a donné une dague\"":
           #helene "Quoi ? Et il fallait que nous sortions pour ça ?"
        #"\"Rien d’important…\"":
           #helene "..."

    helene souriante "Bien, allons-y !"

    jump village_start
# END FILE 06 - Sortie

# 07 - Village
label village_start:

    scene decor noir with long_dissolve
    pause 4
    play music "music/village.mp3" fadein 1.0 loop
    pause 2
    scene decor village
    show helene inquiete at center
    with long_dissolve

    helene "Alors, tu vas mieux ?"
    leon "Cette potion au genévrier n’a vraiment pas bon goût, mais elle a le mérite d’être efficace."
    helene souriante "Tant mieux !"
    leon "On devrait se dépêcher de rentrer maintenant, non ? Ils doivent nous attendre…"
    helene inquiete "Puisque tu te sens bien, pourquoi ne pas rester encore un peu ?"
    helene "Je peux te montrer les endroits qu’on avait l’habitude de fréquenter !"
    leon "..."
    self "C’est vrai que je me sens plus à l’aise à l’air libre plutôt que dans ces souterrains étroits…"
    leon "Ça me va."
    helene souriante "Parfait !"
    self "Elle semble particulièrement enthousiaste…"
    helene normal "Ah, cet étal là-bas ! C’est là qu’on achète habituellement nos légumes."
    helene souriante "Ils vendent les meilleurs choux du coin !"
    helene normal "Par contre, leurs navets sont écoeurants..."
    helene "Ne va pas le répéter au marchand, il est persuadé du contraire."
    helene souriante "Tu n’aimes déjà pas les navets, alors imagine quand ils sont mauvais."
    leon "Je n’aime pas les navets ?"
    helene normal "En général, tu n’es pas difficile avec la nourriture, mais alors pour les navets par contre... !"
    helene souriante "Une fois, Anne en avait mis dans une soupe de légumes et tu as agis comme un gamin ! Tu as fini par aller te coucher en boudant sans rien manger."
    leon "Vraiment ? C’est embarrassant..."
    helene "C’est ce qui fait ton charme !"
    leon "..."
    helene "..."
    helene normal "..."
    helene "Léon..."
    leon "Oui ?"

    show helene normal at center_zoom
    helene "Je n’ai pas vraiment trouvé le moment pour t’en parler plus tôt, mais..."
    helene "Toi et moi... {w=0.2}nous sommes amants."

    menu:

        "\"Oui... Anne l’a déjà mentionné.\"":
           jump village_1_1
        "\"Vraiment ?! Je n’en avais aucune idée...\"":
           jump village_1_2

label village_1_1:

    leon "Oui... {w=0.2}Anne l’a déjà mentionné."
    helene normal "Vraiment ? Décidément, elle ne sait pas tenir sa langue !"
    helene "J’aurais préféré te l’annoncer moi-même..."
    helene "C’est aussi de ma faute, je n’ai pas eu le courage de t’en parler avant..."
    helene "Quoi qu’il en soit..."

    jump village_1_end

label village_1_2:

    leon "Vraiment ?! Je n’en avais aucune idée..."
    helene normal "Oui. Nous étions déjà ensemble bien avant de rejoindre l’Ordre."
    helene "Désolée... {w=0.2}Je n’ai pas trouvé le courage de t’en parler plus tôt."
    
    jump village_1_end
    
label village_1_end:

    helene souriante "Tu es très important pour moi."
    helene normal "Et tu sais, je te connais mieux que quiconque."
    helene normal "..."
    helene "Léon."
    helene "Tu me caches quelque chose d’important, pas vrai ?"
    self "{cps=*2}Que...{/cps}"
    self "{cps=*2}Elle est au courant pour mon bras ?!{/cps}" with little_shake
    self "Non... {w=0.2}Ce n’est pas possible..."
    self "Elle se doute juste de quelque chose..."
    self "Qu’est-ce que je dois faire ? Je dois lui en parler ?"
    self "C’est la seule à qui je peux me confier..."
    self "Mais ce que Charles a dit au sujet de ceux qui ont cette marque..."
    self "Non. C’est probablement une mauvaise idée de lui en parler. {w=0.2}Ça ne peut que mal finir."
    self "Mais... {w=0.2}Elle m’aime, pas vrai ?"
    self "Mais même si je lui en parle... {w=0.2}elle ne pourrait sûrement rien faire pour m’aider..."

    menu:

        "Lui parler de la marque au bras":
           jump village_2_1
        "Ne pas lui en parler":
           jump village_2_2

label village_2_1:

    leon "Hélène... {w=0.2}Mon bras..."
    helene normal "Oui ?"
    leon "Je m’en suis rendu compte un peu plus tôt..."
    leon "..."
    leon "...Regarde."

    pause 2.0
    show helene serieuse
    stop music fadeout 2.0
    pause 2.0

    helene "..."
    helene "..."
    helene "..."
    helene "Nous rentrons."

    leon "H... Hélène, je t’assu{nw}"
    helene "Nous rentrons."
    leon "Je ne voulais pa{nw}"
    helene "Nous rentrons."
    leon "..."    
   
    jump briefing_endingC_start


label village_2_2:

    leon "Je ne comprends pas de quoi tu parles. {w=0.2}Je ne te cache rien."
    helene inquiete "Je vois... {w=0.2}tu ne me fais pas encore confiance, pas vrai ?"
    helene "Je ne peux pas t’en vouloir puisque tu as tout oublié."
    leon "..."
    helene normal "Peu importe."
    helene souriante "Si un jour tu dois me parler de quelque chose, tu sais que je serai là pour t’écouter."
    helene normal "Bon, et si on allait voir d’autres endroits ?"
    leon "Oui, allons-y !"
    stop music fadeout 4.0
     
    jump briefing_endingAB_start
# END FILE 07 - Village


# 08 - Ending A/B - Briefing
label briefing_endingAB_start:

    scene decor grande_salle
    #play music "music/planque_dialogue.mp3" fadein 1.0 loop
    play cloche "music/grande_salle.ogg" fadein 1.0 loop

    stop music fadeout 2.0

    show anne normal at center
    with ellipse

    anne "Ah, vous êtes revenus !"

    hide anne with dissolve
    show charles serieux at center with dissolve

    charles "Vous en avez mis, du temps."

    hide charles with dissolve
    show helene souriante at center with dissolve

    helene "Vraiment ? On s’est dépêchés, pourtant."

    hide helene with dissolve
    show charles normal at center with dissolve

    charles "..."
    charles "Peu importe."
    charles "Maintenant que tout le monde est là, je vais vous expliquer le plan d’attaque de ce soir. Écoutez attentivement."

    scene decor noir with long_dissolve
    pause 3.0
    scene decor grande_salle
    show charles normal at center
    with long_dissolve

    charles "Et donc, une fois notre cible éliminée, on fuira par là où on est venu."
    self "C’était interminable..."
    self "Pourtant, si on résume, on s’infiltre juste dans la forêt de Fontainebleau et on tend une embuscade à Jacques de Molay à son passage, rien de plus."
    self "Ça paraît un peu simple, mais ça a le mérite d’être efficace."
    charles "Nous en avons fini. Nous partons dans moins d’une heure. Léon, profites-en pour bien te reposer. Il faut que tu sois en forme."

    hide charles with long_dissolve
    show anne normal at left
    with dissolve

    anne "Gaston, viens m’aider à préparer les armes."
    show gaston normal at right with move
    gaston "J’arrive."

    hide anne
    hide gaston
    with long_dissolve

    show helene normal at center

    self "Il ne reste que nous deux..."
    helene "Léon..."
    helene inquiete "Tu as vraiment envie de participer à cet assaut ?"
    leon "..."
    helene "Charles ne t’a pas laissé le choix, mais si vraiment tu ne te sens pas prêt..."
    helene normal "Tu peux toujours t’enfuir."
    leon "Pour aller où ?"
    leon "Ce n’est pas vraiment comme si j’avais quelque part où aller. L’Ordre du Lys est le seul endroit où on peut m’aider."
    helene "Tu as juste à te cacher jusqu’à notre départ."
    helene "L’attaque ne peut pas être repoussée, on serait obligé de partir sans toi. Tu n’auras qu’à attendre notre retour."
    leon "Charles serait furieux..."
    helene "Ne t’inquiète pas, je m’occuperai de lui expliquer."
    helene "Je pourrais même lui dire que c’est moi qui t’ai forcé à ne pas venir."
    helene "Vouloir te faire participer est déjà une erreur de toutes façon."
    leon "..."
    helene "..."
    helene "Je dois finir de me préparer. Réfléchis-y."

    hide helene with dissolve

    self "..."

    jump soir_endingAB_start
# END FILE 08 - Ending A/B - Briefing

# 08 - Ending C - Briefing
label briefing_endingC_start:

    scene decor grande_salle
    stop music fadeout 2.0
    play cloche "music/grande_salle.ogg" fadein 1.0 loop
    show anne normal at center
    with ellipse

    anne "Ah, vous êtes revenus !"

    hide anne with dissolve
    show charles serieux at center with dissolve

    charles "Vous en avez mis du temps, tout va bien ?"

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "..."
    helene "Oui."
    self "..."
    self "Je n’ai pas réussi à lui faire dire un seul mot depuis notre départ du village…"

    hide helene with dissolve
    show charles normal at center with dissolve

    charles "..."
    charles "Peu importe."
    charles "Maintenant que tout le monde est là, je vais vous expliquer le plan d’attaque de ce soir. Écoutez attentivement."

    scene decor noir with dissolve
    pause 2.0
    scene decor grande_salle
    show charles normal at center
    with long_dissolve

    charles "Et donc, une fois notre cible éliminée, on fuira par là où on est venu."
    self "C’était interminable..."
    self "Pourtant, si on résume, on s’infiltre juste dans la forêt de Fontainebleau et on tend une embuscade à Jacques de Molay à son passage, rien de plus."
    self "Ça paraît un peu simple, mais ça a le mérite d’être efficace."
    charles "Nous en avons fini. Nous partons dans moins d’une heure. Léon, profites-en pour bien te reposer. Il faut que tu sois en forme."

    hide charles with long_dissolve
    show anne normal at left
    show gaston normal at right
    with dissolve

    anne "Gaston, viens m’aider à préparer les armes."
    gaston "J’arrive."


    hide anne
    hide gaston
    with long_dissolve

    show helene normal at center

    self "Il ne reste que nous deux..."
    leon "Hélène, je..."
    helene "Je vais me préparer."

    hide helene with long_dissolve

    self "..."
    self "Si elle m’aimait vraiment, elle ne réagirait pas comme ça…"

    jump soir_endingC_start
# END FILE 08 - Ending C - Briefing

    
# 09 - Ending A/B - Soir
label soir_endingAB_start:

    stop cloche fadeout 2.0
    scene decor chambre with ellipse

    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    self "..."
    self "Me cacher avant leur départ..."
    self "C’est vraiment raisonnable ?"

    stop music fadeout 1.0
    pause 0.5
    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_3 with long_dissolve

    self "..."
    self "Ça s’est encore propagé..."
    play sound "music/door_opening.ogg"
    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    pause 0.5
    scene decor chambre
    show helene normal at center
    with dissolve

    helene "Léon, à propos de..."
    helene serieuse "..."
    self "...Merde !" with little_shake
    self "Elle a eu le temps de le voir ?!"
    helene "À plus tard."

    play sound "music/door_close.ogg"

    hide helene with dissolve

    leon "Hélène ! Je... {w=0.2}Ah...!"

    scene decor noir with flash_blanc
    stop music fadeout 1.0
    pause 1.0

    jacques_inconnu "O{w=0.0}n{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}t{w=0.0} {w=0.0}r{w=0.0}e{w=0.0}c{w=0.0}o{w=0.0}n{w=0.0}n{w=0.0}a{w=0.0}î{w=0.0}t{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}c{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}s{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}à{w=0.0} {w=0.0}l{w=0.0}e{w=0.0}u{w=0.0}r{w=0.0}s{w=0.0} {w=0.0}y{w=0.0}e{w=0.0}u{w=0.0}x{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc
    play cloche "music/planque_dialogue.mp3" fadein 1.0 loop

    self "Encore ce truc..."
    self "Plus important... {w=0.2}Hélène !"
    self "Elle a manifestement vu mon bras..."
    self "Elle ne va pas en parler aux autres... {w=0.2}pas vrai ?"
    self "Nous sommes en couple... {w=0.2}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère..."
    self "..."
    self "Qu’est-ce que je dois faire..."

    menu:

        "Participer à l’assaut":
           jump soir_2_1
        "Se cacher avant le départ":
           jump soir_2_2

label soir_2_1:

    self "..."
    self "Cette attaque est trop importante. Je me sentirais coupable de ne pas y aller avec eux."
    self "Je ferais mieux de me reposer jusqu’à notre départ."

    jump massacre_endingA_start

label soir_2_2:

    self "..."
    self "Et puis merde !"
    self "Je veux pas risquer ma vie pour des personnes dont je n’ai aucun souvenir."
    self "Je me planque !"    

    jump massacre_endingB_start




# END FILE 09 - Ending A/B - Soir


# 10 - Ending A - Massacre
label massacre_endingA_start:

    $ ending = "A"

    scene decor chambre
    show anne serieuse at center
    with ellipse

    anne "Léon, il est l’heure. Je t’attends à l’entrée."
    hide anne with long_dissolve

    play sound "music/door_close.ogg"

    self "Je suis stressé et excité à la fois."
    self "..."
    self "Hélène..."
    self "Elle m’évite depuis tout à l’heure..."
    self "Vu que les autres agissent normalement, je ne pense pas qu’elle leur ait parlé de mon bras. C’est déjà un soulagement."

    stop cloche fadeout 2.0
    stop music fadeout 2.0

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_4 with long_dissolve

    self "J’ai l’impression que ça va de plus en plus vite..."
    self "..."
    self "Ce grand maître des Templiers..."
    self "Peut-être qu’il connaît un moyen de supprimer cette malédiction ?"
    self "Ce n’est pas grand chose, mais c’est ma seule piste."
    self "Je vais devoir miser dessus..."

    scene decor noir with long_dissolve
    pause 3.0

    play sound "music/sf_decapitation.mp3"
    with shake

    charles "Bien. Nous avons réussi à franchir les gardes en les éliminant."
    charles "Nous ne leur avons pas non plus laissé l’occasion de donner l’alerte."
    charles "Tout se passe comme prévu."

    scene decor chateau
    stop music fadeout 2.0
    stop cloche fadeout 2.0
    play music "music/action.mp3" fadein 1.0 loop

    show charles masque
    with long_dissolve

    charles "Nous n’avons plus qu’à attendre le passage de Jacques de Molay."

    hide charles with dissolve
    show anne masque at left
    show gaston masque at right
    with dissolve

    gaston "On va lui faire sa fête !"
    anne "Il ne devrait plus tarder, n’est-ce pas ?"

    hide gaston
    hide anne
    with dissolve
    show charles masque at center with dissolve

    charles "Enlevez vos masques. Il ne feront que nous gêner à partir de maintenant. Aujourd’hui, ce sera nous ou eux de toutes façons."

    hide charles with long_dissolve
    show charles serieux with long_dissolve

    charles "Bien. Nous n’avons plus qu’à l’attendre."
    charles "Ah, des chevaux, au loin !"
    charles "Restez sur vos gardes, c’est peut-être lui."

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "..."
    helene "J’aurais préféré ne pas avoir à en arriver là aussi tôt."

    hide helene with dissolve
    show anne normal at center with dissolve

    anne "Qu’est-ce que tu veux dire pa{nw}"

    play sound "music/sf_decapitation.mp3"
    hide anne with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center
    with long_dissolve

    inconnu "Et de un."
    self "...!"
    self "Cette chose... {w=0.2}Ce collier... {w=0.2}C’est Hélène ?!"

    show helene_demon at left with move
    show charles panique at right with dissolve

    charles "Anne... {w=0.2}non... {w=0.2}ce n’est pas possible !"
    self "Qu... {w=0.2}qu’est-ce qu’il se passe ?!"

    hide charles with dissolve
    show gaston panique at right with dissolve

    gaston "Ah !"
    gaston "Espèce de monstre ! Meurs !"
    helene_demon souriante "Tu es ridicule."

    play sound "music/sf_decapitation.mp3"
    hide gaston with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 0.5

    self "C’est un cauchemar !"

    hide helene_demon with dissolve
    show charles panique at center with dissolve

    charles "Anne...! Dis quelque chose !"

    play sound "music/BruitDattaque.mp3"
    hide charles with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 0.5

    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Elle me rattraperait sans difficulté..."

    show helene_demon normal with dissolve

    helene_demon "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donnée !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon "On dirait que ma mission se termine prématurément."
    self "Elle se rapproche de plus en plus... Je n’ai plus le choix !"
    helene_demon "Je m’attendais à plus de résistance... {w=0.2}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending A - Massacre

# 10 - Ending B - Massacre
label massacre_endingB_start:

    $ ending = "B"

    scene decor noir with long_dissolve
    pause 3.0
    scene decor entree with long_dissolve

    self "Dans la précipitation, je n’ai pas trouvé de meilleure cachette..."
    self "..."
    self "Je me sens stupide à rester immobile derrière un amas de débris..."
    self "Ah, je les entends."
    charles "Dans un moment pareil !"
    charles "Trouvez où il est ! S’il est encore ici, on le trouvera rapidement !"
    helene "Charles, calme-toi !"
    charles "La ferme !"
    anne "Charles, on n’a plus le temps !"
    anne "On va devoir se débrouiller sans lui."
    charles "..."
    charles "Si on revient vivants, je lui ferai regretter !"
    charles "Allons-y."
    self "..."
    self "Ils sont partis..."
    self "Hélène a vu mon bras... {w=0.2}Est-ce que je ne devrais pas m’enfuir pour de bon ?"
    self "..."
    self "Je ne saurais même pas où aller..."
    self "Je n’ai pas d’autre choix que de les attendre et espérer qu’elle n’en parle à personne..."

    scene decor chambre with ellipse

    self "Ça fait déjà un moment... {w=0.2}J’espère que ça ne se passe pas mal."

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_4 with long_dissolve

    self "J’ai l’impression que ça va de plus en plus vite..."
    self "Au final, je ne fais que leur causer des problèmes..."
    self "...?!"

    scene decor chambre with dissolve

    self "J’ai entendu quelque chose !"
    inconnu "...Léon !"
    self "Ça vient de l’entrée !"

    scene decor entree
    show gaston panique
    with long_dissolve

    stop music fadeout 2.0
    stop cloche fadeout 2.0
    play music "music/action.mp3" fadein 1.0 loop

    gaston "Dieu merci, tu es bien là ! Dépêche-toi, on dégage en vitesse !"
    leon "Qu’est-ce qui se passe ?!"
    gaston "C’est Hélène ! C’est une saloperie de démon !"
    leon "Qu... {w=0.2}quoi ?!"
    gaston "Elle a tué Anne et Charles et si on ne se grouille pas, on est les suivants !"
    leon "Qu’est-ce que tu racontes ?!"
    gaston "Magne-toi, putain, on n’a pas le temps ! Elle va nou{nw}"

    play sound "music/sf_decapitation.mp3"
    hide gaston with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center with dissolve

    inconnu "Qu’est-ce qu’il est bruyant, celui-là."
    self "...!"
    self "...Gaston !"
    show helene_demon souriante with dissolve
    inconnu "Cet imbécile avait une chance de s’échapper mais il a préféré revenir ici pour te prévenir."
    self "Cette chose... {w=0.2}Ce collier… {w=0.2}C’est vraiment Hélène ?!"
    self "C’est vraiment elle ?!"
    helene_demon normal "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Impossible, elle bloque l’entrée... {w=0.2}et elle me rattraperait sans difficulté."
    helene_demon "On dirait que ma mission se termine prématurément."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donnée !"
    helene_demon souriante "J’ai commencé par attaquer Anne dans le dos, par surprise. C’était la plus dangereuse des trois, après tout !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon normal "Elle est morte en un instant. Charles était complètement figé, je l’ai tué dans la foulée sans qu’il ne bouge d’un pouce."
    self "Elle se rapproche de plus en plus... {w=0.2}Je n’ai plus le choix !"
    helene_demon "Je m’attendais à plus de résistance... {w=0.2}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending B - Massacre

# 10 - Ending C - Massacre

label soir_endingC_start:

    $ ending = "C"

    scene decor noir with dissolve
    pause 3.0
    scene decor chambre with dissolve

    self "..."
    self "Je ne peux qu’attendre, maintenant..."
    self "Ah !"

    stop music fadeout 2.0
    stop cloche fadeout 2.0

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "O{w=0.0}n{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}t{w=0.0} {w=0.0}r{w=0.0}e{w=0.0}c{w=0.0}o{w=0.0}n{w=0.0}n{w=0.0}a{w=0.0}î{w=0.0}t{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}c{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}s{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}à{w=0.0} {w=0.0}l{w=0.0}e{w=0.0}u{w=0.0}r{w=0.0}s{w=0.0} {w=0.0}y{w=0.0}e{w=0.0}u{w=0.0}x{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc

    self "Encore ce truc..."
    self "Mon bras me brûle..."

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_3 with long_dissolve

    self "..."
    self "La façon dont Hélène m’évite depuis qu’elle a vu mon bras..."
    self "Elle ne va pas en parler aux autres... {w=0.2}pas vrai ?"
    self "Elle est censée m’aimer... {w=0.2}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère..."

    scene decor chambre with dissolve

    self "..."
    self "Qu’est-ce que je peux faire..."

    pause 1.0
    stop music fadeout 1.0
    play sound "music/door_opening.ogg"
    pause 1.0

    gaston "L… Léon… On doit…"
    play sound "music/FlashSound.mp3"

    self "!!!"
    play music "music/action.mp3" fadein 1.0 loop
    leon "{cps=*2}Aah... {w=0.1}AAAAAH !{/cps}" with little_shake

    scene cadavre_gaston with long_dissolve
    pause 2.0

    self "{cps=*2}Qu’est-ce que...!{/cps}"
    leon "{cps=*2}Gaston ! Tu m’entends ?!{/cps}" with little_shake
    self "{cps=*2}Il n’a plus de pouls... {w=0.1}merde !{/cps}"
    self "{cps=*2}C’est quoi ce bordel ! Je dois me barrer d’ici !{/cps}"
     
    scene decor noir with dissolve
    pause 1.0
    scene decor grande_salle
    show helene normal at center
    with dissolve

    leon "{cps=*2}Ah ! Hélène !{/cps}"
    leon "{cps=*2}On doit partir d’ici !{/cps}"
    helene normal "..."
    leon "{cps=*2}Dépêche-toi ! Gaston… {w=0.1}il...{/cps}"
    charles "Qu’est-ce qu’il se passe, ici ?"

    hide helene with dissolve
    show charles serieux at center

    charles "Quelque chose ne va pas ?"
    leon "{cps=*2}C’est Gaston… {w=0.1}il est...{/cps}"
    self "Attends..."
    self "C’est forcément l’un d’entre eux qui a fait ça !"
    self "Je ne peux faire confiance à personne !"
    self "Je dois partir d’ici le plu{nw}"

    play sound "music/BruitDattaque.mp3"
    hide charles with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center with dissolve

    self "...!"
    self "...Charles !"
    show helene_demon souriante with dissolve
    inconnu "Et de deux."
    self "Cette chose... {w=0.2} Ce collier... {w=0.2}C’est Hélène ?!"
    anne "Vous en faites, du bruit !"

    hide helene_demon with dissolve
    show anne normal at center with dissolve

    anne "Qu’est-ce qu... {w=0.2}Aah... {w=0.2}Non..."
    anne panique "AAAAAAAAH !" with little_shake
    anne "Charles ! Charles !!"
    anne "Dis quelque cho{nw}"

    play sound "music/sf_decapitation.mp3"

    hide anne with flash_rouge
    with shake
    pause 0.5
    play sound "music/FlashSound.mp3"
    pause 1.0

    show helene_demon souriante at center

    self "C’est un cauchemar !"
    helene_demon "Les humains sont si faibles !"
    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Elle me rattraperait sans difficulté..."
    helene_demon normal "J’aurais préféré garder ma couverture plus longtemps."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donnée !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon "On dirait que ma mission se termine prématurément."
    self "Elle se rapproche de plus en plus... Je n’ai plus le choix !"
    helene_demon "Je m’attendais quand même à plus de résistance... {w=0.2}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending C - Massacre

# 11 - Mort de Hélène
label mort_de_helene_start:

    play sound "music/BruitDattaque.mp3"
    
    # on stoppe la musique car moment drama
    stop music fadeout 1.0

    if ending == "A":
        scene mort_de_helene_A with flash_rouge
    if ending == "B":
        scene mort_de_helene_B with flash_rouge
    if ending == "C":
        scene mort_de_helene_C
    with flash_rouge

    pause 2.0
    helene_demon "L... {w=0.2}Léon."
    self "...Ça a marché ? Une simple dague ?"
    helene_demon "Tu dois... {w=0.2}vivre..."
    self "Qu’est-ce qu’elle raconte ?"
    helene_demon "Je suis vraiment heureuse... {w=0.2}de t’avoir rencontré..."
    helene_demon "Je ne regrette rien..."
    self "Elle débloque !"

    scene decor noir with dissolve
    play sound "music/FlashSound.mp3"
    with shake
    self "..."
    self "...elle ne respire plus."
    self "...!"
    self "Je me sens si apaisé tout d’un coup... {w=0.2}Qu’est-ce que ?!"

    scene arm_gant with dissolve
    pause 0.8
    scene arm_3 with dissolve

    self "...!"

    scene arm_2 with dissolve
    pause 0.5
    scene arm_1 with dissolve
    pause 0.5
    scene arm_0 with dissolve

    self "Comment est-ce que..."
    self "Ah ! Ma mémoire !"
    self "..."
    self "Je me souviens..."
    self "Je me souviens de tout..."

    jump flashback_start
# END FILE 11 - Mort de Hélène

# 12 - Flashback
label flashback_start:

    pause 1.0
    scene decor noir
    show text "{font=gui/MorrisRomanBlack.ttf}{size=80}Huit mois plus tôt" at truecenter
    with long_dissolve
    pause 3.0
    scene decor noir with long_dissolve

    leon "Vous m'avez demandé ?"
    jacques_inconnu "Ah, Léon, te voila."
    jacques_inconnu "J'ai une mission à te confier. Une mission que toi seul peut remplir."
    leon "Je vous écoute, grand maître."

    scene decor eglise with dissolve
    play music "music/eglise_calme.mp3" fadein 1.0 loop
    pause 2.0

    jacques "Tu connais l'Ordre du Lys, n'est-ce pas ?"
    leon "Bien sûr. C'est un groupe de terroristes fanatiques qui s'opposent à votre règne divin."
    leon "Ceux-ci ont déjà été terrassés il y a quelques années."
    jacques "Pas tout à fait. Une poignée de membres, dont Charles IV, ont survécu et continuent de voiloir se battre."
    jacques "Ils sont insignifiants et nous savons actuellement où leur base se trouve."
    leon "Souhaitez-vous que je les extermine tous, grand maître ?"
    jacques "Pas tout à fait."
    jacques "Il se trouve que Charles IV est en contact avec Édouard II, le roi d'Angleterre."
    jacques "..."
    jacques "Je veux que tu intègres l'Ordre du Lys en te faisant passer pour l'un des leurs."
    jacques "Ta mission est de récolter des informations sur le royaume d'Angleterre, afin de préparer notre future conquête."
    leon "Bien, grand maître."
    jacques "Hélène ira avec toi."
    jacques "Les démons peuvent prendre une forme humaine."
    jacques "Elle utilisera cette forme et rejoindra également l'Ordre."
    jacques "Cependant, comme tu le sais..."
    jacques "On peut reconnaître ces démons sous forme humaine à leurs yeux."
    jacques "Ceux-ci ont les yeux vairons, soit deux yeux de couleur différente."
    jacques "Tu ne peux pas laisser nos ennemis le découvrir ou la couverture d'Hélène tomberait."
    leon "Je comprends."
    jacques "..."
    jacques "Léon, à propos des démons..."
    jacques "Lorsqu'un démon et un humain ont une relation aussi... intime... que la votre, un lien d'énergie vitale se créé."
    jacques "Hélène a le pouvoir de contrôler de flux de force vitale."
    jacques "Théoriquement, elle peut s'en servir pour te transmettre sa propre vitalité et te soigner d'une blessure mortelle."
    jacques "Le prix à payer serait sa propre vie, elle n'a donc aucun intérêt à faire ça."
    jacques "En revanche, elle a également le pouvoir d'aspirer la tienne ce qui causerait ta mort sans que tu n'ais la moindre chance de te défendre."
    jacques "Sois prudent. Elle a un contrôle absolu sur ton existence."
    leon "Ne vous inquiétez pas, grand maître."
    leon "Je lui accorde une confiance totale. Je l’aime tellement..."
    leon "Je ne peux pas imaginer un monde sans Hélène."

    pause 2.0

    show screen end_credits
    with long_dissolve

    pause 1000


# END 12 - Flashback