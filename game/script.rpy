﻿# commentaires généraux.
# 01 - Fuite
label start:
    # play sound ["music/AttaqueMagique.mp3" , "music/ChuteHomme.mp3"] fadein 1.0
    show screen menu_button
    stop music fadeout 3.0
    scene decor noir with long_dissolve

    inconnu "Léon ! Léon !!"
    pause 1.0
    play cloche "music/SonCloche.mp3" fadein 4.0 loop
    play sound "music/BruitageChien.mp3" fadein 2.0 loop

    self "Que... {w=0.5}qu’est-ce qu’il se passe ?"
    
    scene decor intro with long_dissolve
    
    pause 0.5
    
    inconnu "Tu t’es évanoui. Dépêche-toi, il faut fuir !"
    self "Je... {w=0.5}je ne comprends rien..."

    menu:
        "\"Où sommes nous ?\"":
            leon "Où sommes nous ?"
            jump fuite_fin
        "\"Qui êtes-vous\"":
            leon "Qui êtes-vous ?"
            jump fuite_fin
    
label fuite_fin:
    inconnu "QU... {w=0.5}QUOI ?!"
    
    pause 2.0
    
    inconnu "Il manquait plus que ça ! "
    inconnu "Léon... {w=0.5}tu..."
    inconnu "..."
    inconnu "On n’a pas le temps. Suis-moi !"
    leon "Ah... {w=0.5}ma tête..."
    play sound "music/FlashSound.mp3"
    
    with shake

    scene decor noir with long_dissolve

    inconnu "LÉON !!!"

    stop sound fadeout 1.5
    stop music fadeout 1.5
    stop cloche fadeout 1.5

    pause 4.0

    jump reveil_start
# END FILE 01 - Fuite

# 02 - Réveil
label reveil_start:
    scene decor chambre

    # Stop the old music and play the new one in loop
    stop music fadeout 1.0
    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    show helene inquiete at center
    with long_dissolve

    inconnu "Ça y est, tu es réveillé ?"
    leon "..."    
    inconnu "J’étais vraiment inquiète, tu sais !"
    self "Cette voix... {w=0.5}c’est la fille au masque ?"

    show helene normal
    
    inconnu "L’assaut d’hier ne s’est pas tout à fait passée comme prévu et on t’a retrouvé évanoui après s’être séparés."

    show helene inquiete

    inconnu "Ils étaient mieux préparés que ce que nous ne l’avions anticipé... Certains avaient même des armes magiques."

    show helene normal

    inconnu "Mais ne t’inquiète pas, Gaston t’as porté et on s’en est tous sortis indemnes."
    leon "Un assaut ? Gaston ?"

    show helene inquiete
    pause 1.0

    inconnu "Je m’en doutais... {w=0.5}Tu ne te souviens vraiment plus de rien..."

    helene normal "Tu ne te souviens même plus de moi... {w=0.5}je m’appelle Hélène."

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

    helene "Anne... {w=0.5}Il a perdu la mémoire..."

    show anne serieuse

    anne "Oh..."

    pause 2.0

    show anne souriante

    anne "Je suis Anne, nous sommes amis. "
    anne normal "Charles nous attend. Léon, tu devrais venir avec nous."

    play sound "music/door_close.ogg"

    jump reunion_start
# END FILE 02 - Réveil


# 03 - Réunion
label reunion_start:
    scene decor noir with long_dissolve
    pause 3.0

    self "Où est-ce qu’ils m’emmènent..."
    pause 1.0
    
    stop music fadeout 2.0
    play cloche "music/grande_salle.ogg" fadein 1.0 loop

    scene decor grande_salle
    show charles normal at left
    show gaston normal at right
    with long_dissolve

    self "Ces personnes... {w=0.5}évidemment, leur visage ne me dit rien."

    hide gaston with dissolve
    show charles normal at center with move
    
    inconnu "Léon aurait donc perdu la mémoire..."
    charles "Je m'appelle Charles. Je suis fondateur et dirigeant de l'Ordre du Lys."
    
    hide charles with dissolve
    show gaston souriant at center with dissolve

    gaston "Moi, c'est Gaston. T'as intérêt à vite retrouver la mémoire !"
    leon "L'Ordre du Lys... {w=0.5}qu’est-ce que c'est ?"

    hide gaston with dissolve
    show charles normal at center with dissolve

    charles "Te souviens-tu de la situation dans laquelle la France se trouve actuellement ?"
    leon "Non..."
    charles "De quoi tu te souviens ?"
    leon "Pas de grand chose... {w=0.5}Je sais juste que nous sommes en France et il me semble que nous sommes en 1313."
    charles serieux "C’est tout ?"
    charles "..."
    charles normal  "On va devoir reprendre depuis le début."
    charles "La France est actuellement dirigée par les Templier, un groupe religieux extrémiste"
    charles serieux "Ils se sont procurés durant la dernière croisade un artefact démoniaque."
    charles "Ils s’en sont servi afin d’invoquer des démons en pratiquant des rites occultes."
    self "Des... {w=0.5}des démons ?! Vraiment ?!"

    hide charles with dissolve
    show gaston serieux at center with dissolve

    gaston "Ces chiens ont utilisés les pouvoirs des démons pour tuer un grand nombre d’innocents."

    hide gaston with dissolve
    show charles normal at center with dissolve
    
    charles "Il y a 6 ans, ils ont terrassé les armées de la monarchie en utilisant la puissance de ces démons."
    charles serieux "Ils se sont emparés du pouvoir en à peine un mois et ont assassiné le roi Philippe le Bel."
    charles "Ils dirigent depuis le pays en imposant leurs dogmes religieux."
    charles "Ils convoitent mêmes les terres des pays voisins à présent."
    charles "..."
    charles normal "En tant qu’ancien prince, il était de ma responsabilité de fonder l’Ordre du Lys."
    charles "C’est un groupe de résistants qui lutte face aux Templiers."
    leon "Un... {w=0.5}un prince ?!"

    hide charles with dissolve
    show anne souriante with dissolve

    anne "Charles était un prince de l’ancien royaume"
    anne serieuse "Lors de la prise du pouvoir des Templiers, son père, Phillippe le Bel, ainsi que le reste de sa famille ont été executés."
    anne "Charles est le seul survivant de la famille royale."
    leon "Un prince... {w=0.5}L’Ordre du Lys doit être bien plus grand que ce que j’imaginais."
    anne "..."

    hide anne with dissolve
    show charles serieux with dissolve

    charles "..."
    charles "Tous les membres de l’Ordre sont actuellement présents."
    leon "Que... quoi ?!"
    with shake
    leon "Vous comptez les vaincre avec seulement cinq personnes ?!"
    with shake
    self "Ils se moquent de moi ?!"

    hide charles with dissolve
    show anne serieuse at center with dissolve

    anne serieuse "Eh, nous ne sommes peut-être pas nombreux, mais le peuple est de notre côté."
    anne "Nous agissons au nom de tous ceux qui n’ont pas le courage de faire face aux Templier."
    anne "Nous avons de nombreux alliés qui nous aident financièrement ou qui nous fournissent des informations."

    hide anne with dissolve
    show charles normal with dissolve

    charles "L’Ordre du Lys était bien plus puissant autrefois."
    charles "Nous avions toute une armée. Nous étions bien plus nombreux que les templiers."
    charles serieux "..."
    charles "Nous avons été décimés à cause d’une malédiction démoniaque qu’ils ont introduit parmi nos rangs."
    charles "Les personnes dans cette pièce sont les seuls survivants qui ont encore la volonté de se battre."
    charles "..."
    charles "Cette malédiction est pire que la mort."
    charles normal "Une marque noire aparaît sur le corps de la personne maudite et s’étend peu à peu sur son corps."
    charles "Le corps est entièrement recouvert après quelques jours."
    charles serieux "La personne maudite perd alors la raison. Elle se met à se déchaîner sans distinction sur les gens qui l’entourent." 
    charles "Elle finit alors par mourir une fois épuisée mentalement."
    self "Un phénomène pareil existe réellement ?"
    charles normal "Cette malédiction est contagieuse. Elle se transmet simplement par le toucher."
    charles "Il n’y a pas de remède une fois que quelqu’un a été affecté par la malédiction."
    charles serieux "Par conséquent, les personnes affectées sont condamnées à être exécutées sur le champs."
    charles "Certains Templiers possèdent même une arme crée par des démons qui peut infliger cette malédiction alors qu’ils n’ont aucun pouvoir magique."
    leon "L’Ordre du Lys s’est fait massacré alors qu’il avait une armée et souhaite toujours se battre avec une poignée de personnes ?!"

    hide charles with dissolve
    show anne normal with dissolve

    anne "Nous avons toujours une chance."
    anne "Le règne des Templiers est centré autour d’une seule et unique personne."
    anne serieuse "Jacques de Molay."
    anne normal "Il est le grand maître des Templiers. C’est lui qui est à l’origine de toutes les atrocités commises par les Templiers."
    anne serieuse "Si nous le tuons tout le reste s’écroulera."
    self "Ce raisonnement semble bien optimiste..."

    hide anne with dissolve
    show charles normal with dissolve

    charles "Bref. Je sais que tout ne doit pas être encore très clair pour toi, mais le temps presse."
    charles "Je vous ai tous demandé de venir pour une raison précise."
    self "Tout le monde semble si sérieux d’un coup..."
    charles "Le but de notre attaque de cette nuit était de soutirer des informations à un officier Templier proche de Jacques de Molay."
    charles serieux "Malgré ce qui est arrivé à Léon, c’était un succès."
    charles normal "Suite à ça, nous avons réussi à connaître l’emploi du temps de Jacques de Molay pour les jours à venir."
    leon "Ce Templier l’a simplement révélé ?!"

    hide charles with dissolve
    show anne serieuse at center with dissolve

    anne "Léon... {w=0.5}Nous l’avons torturé puis égorgé."
    self "...Quoi ?!"
    self "Mais c’est horrible !"
    self "Je fais vraiment partie d’un groupe qui suit ce genre de pratiques ?!"

    hide anne with dissolve
    show charles normal at center with dissolve

    charles "Quoi qu’il en soit, nous savons que Jacques de Molay se trouve actuellement au Château de Fontainebleau."
    charles "De plus, il quittera le château ce soir pour un déplacement vers Paris."
    charles "Le délai est trop court pour qu’il prenne connaissance de la mort de l’officier Templier. Autrement dit, il ne se doutera de rien et ne changera pas son emploi du temps."
    charles serieux "..."
    charles "Évidemment, nous ne pouvons pas laisser passer une occasion pareille."
    charles "Nous allons l’attendre à la sortie du château et l’assassiner."
    charles "Bref. Léon, repose-toi pendant que nous nous occupons des préparatifs. Il faut que tu sois en forme ce soir."
    self "...moi ?!"
    self "Ils comptent me faire combattre dans mon état ?!"

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "Charles, tu n’es pas sérieux ?"
    helene "Il est hors de question que Léon participe à cet assaut dans son état."

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "Léon est de loin le plus doué parmi nous cinq pour le combat. Nous avons besoin de lui."

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "C’est ridicule, il a perdu la mémoire ! On ne sait même pas s’il saura se battre !"

    with shake

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

    $ charles("B{w=0.0}r{w=0.0}e{w=0.0}f{w=0.0},{w=0.0} {w=0.0}n{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}a{w=0.0}v{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0} {w=0.0}d{w=0.0}e{w=0.0} {w=0.0}t{w=0.0}e{w=0.0}m{w=0.0}p{w=0.0}s{w=0.0}.{w=0.0} {w=0.0}N{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}e{w=0.0}v{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}è{w=0.0}s{w=0.0} {w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}t{w=0.0}e{w=0.0}n{w=0.0}a{w=0.0}n{w=0.0}t{w=0.0} {w=0.0}n{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}r{w=0.0}é{w=0.0}p{w=0.0}a{w=0.0}r", interact=False)
    pause 2.4

    play sound "music/FlashSound.mp3"    
    with flash_blanc
    
    hide charles
    show helene inquiete at center

    helene "Léon ! Tu vas bien ?!"
    leon "...J’ai subitement un énorme mal de crâne..."
    leon "..."
    leon "Je peux me reposer dans ma chambre ?"

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "..."
    charles "Bien sûr. Repose-toi bien."

    jump retour_chambre
# END FILE 03 - Réunion

# 04 - Chambre
label retour_chambre:
    
    scene decor chambre with ellipse

    stop cloche fadeout 2.0
    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    self "J’ai la tête qui tourne... {w=0.5}et mon bras..."

    scene arm_gant with long_dissolve

    self "Ca me brûle sous ce gant..."

    scene arm_1 with long_dissolve

    self "{cps=*2}...!{/cps}"
    self "{cps=*2}Qu... {w=0.3}Qu’est-ce que c’est que ça !{/cps}"
    with shake
    self "{cps=*2}Ce ne serait quand même pas... {w=0.3}non, ça ne peut pas être ça !{/cps}"
    with shake
    self "{cps=*2}C’était déjà là quand je me suis réveillé ?{/cps}"
    self "{cps=*2}C’est arrivé pendant l’assaut d’hier ?!{/cps}"
    self "{cps=*2}Charles a dit que des armes magiques pouvaient infliger ça...{/cps}"
    self "{cps=*2}Qu’est ce qu’il va m’arriver si les autres le découvrent ?{/cps}"
    self "{cps=*2}Ah ! De l’eau !{/cps}"
    self "{cps=*2}Ça veut pas partir...{/cps}"
    self "{cps=*2}Oh !{/cps}"

    scene decor water with dissolve
    pause 2.0

    self "Alors c’est à ça que je ressemble... {w=0.5}Je tire une de ces têtes..."
    self "D’ailleurs, j’ai aucune idée de l’âge que j’ai..."
    self "J’ai l’air plus vieux que je l’aurais espéré..."

    play sound "music/FlashSound.mp3"
    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "I{w=0.0}l{w=0.0} {w=0.0}y{w=0.0} {w=0.0}a{w=0.0} {w=0.0}p{w=0.0}l{w=0.0}u{w=0.0}s{w=0.0}i{w=0.0}e{w=0.0}u{w=0.0}r{w=0.0}s{w=0.0} {w=0.0}c{w=0.0}h{w=0.0}o{w=0.0}s{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}q{w=0.0}u{w=0.0}e{w=0.0} {w=0.0}t{w=0.0}u{w=0.0} {w=0.0}d{w=0.0}o{w=0.0}i{w=0.0}s{w=0.0} {w=0.0}s{w=0.0}a{w=0.0}v{w=0.0}o{w=0.0}i{w=0.0}r{w=0.0} {w=0.0}s{w=0.0}u{w=0.0}r {w=0.0}l{w=0.0}e{w=0.0}s {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc

    self "Que... {w=0.5}quoi ?!"
    with shake
    self "C’était quoi, ça ?!"
    self "Une hallucination ?! Un souvenir ?!"

    pause 0.5
    play sound "music/door_opening.ogg"
    show anne normal at center with dissolve

    anne "Léon, tu vas mieux ?"
    self "C’était limite mais j’ai pu remettre mon gant à temps..."
    anne "Eh, tu m’écoutes ?"
    leon "Ne... {w=0.5}ne t’inquiète pas, c’est juste un coup de fatigue, rien de bien grave."
    anne serieuse "..."
    anne "Te réveiller au milieu d’inconnus doit être dur à vivre..."
    leon "Je n’ai des souvenirs d’aucun d’entre vous..."
    leon "Je suppose que vous devez tous être des personnes importantes si Charles est un prince."
    anne souriante "Absolument pas !"
    anne "Je n’étais qu’une servante avant la prise du pouvoir par les Templiers."
    anne normal "Depuis le début, les statuts sociaux des membres de l’Ordre étaient très variés."
    anne "Gaston, lui, n’était qu’un paysan."
    anne souriante "Quand à Hélène et toi, vous étiez un couple de nobles."
    leon "Un... {w=0.5}un couple ?!"
    with shake
    leon "Vraiment ?!"
    anne normal "Oh... {w=0.5}elle ne t’en a pas parlé ?"
    anne serieuse "Je vois... ton amnésie doit être très dure à vivre pour elle aussi."
    anne souriante "Hélène et toi êtes en couple depuis bien avant que vous n'ayez intégré l’Ordre."
    leon "Elle ne m’en a pas dit un mot..."
    anne normal "..."
    anne serieuse "Tu as vraiment mauvaise mine."
    anne normal "J’ai quelque chose à proposer. Allons voir Charles."

    play sound "music/door_close.ogg"
    
    jump grande_salle
# END FILE 04 - Chambre

# 05 - Dialogue Charles
label grande_salle:
    
    scene decor grande_salle

    stop music fadeout 2.0
    play cloche "music/grande_salle.ogg" fadein 1.0 loop

    show anne normal at left
    show charles normal at right
    with ellipse
 
    charles "Au village ?"
    anne "Oui. Je pense que Léon devrait sortir acheter des herbes médicinales. Ça calmera ses douleurs si jamais il doit participer à l’assaut de ce soir."
    anne souriante "Ça ne peut que lui faire du bien de prendre l’air !"
    charles "Il ne se souvient plus du chemin."
    anne normal "Hélène peut l’accompagner, ils y allaient toujours ensemble pour faire des provisions."
    anne "Après tout, leurs visages ne sont pas connus des Templiers, contrairement à ceux du reste de l’Ordre"

    charles "Anne... {w=0.5}tu es consciente de l’importance de l’attaque de demain...?"
    charles "Léon ne peut pas vraiment nous aider à préparer quoi que ce soit dans son état, mais Hélène n’a pas de temps à perdre à gambader au village."
    helene "Je veux y aller !"
    anne souriante "Ah, tu es là !"

    hide anne
    hide charles 
    with dissolve
    show helene souriante at center with long_dissolve

    helene "S’il ne manque que moi, vous devriez pouvoir vous débrouiller à tout préparer, pas vrai ?"

    hide helene with dissolve
    show charles normal at center with dissolve

    charles "Même toi tu t’y mets..."
    charles "..." 
    charles "Tâchez de revenir rapidement."
    self "Visiblement, mon avis n’intéresse personne..."
    self "De toute façon, je ne me sens pas vraiment à l’aise dans ce trou à rat. Ça ne peut que me faire du bien de sortir un peu."

    leon "Agh..."

    scene decor noir with flash_blanc
    play sound "music/FlashSound.mp3"
    pause 1.0

    jacques_inconnu "L{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}v{w=0.0}e{w=0.0}n{w=0.0}t{w=0.0} {w=0.0}p{w=0.0}r{w=0.0}e{w=0.0}n{w=0.0}d{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}u{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0}."

    pause 1.0
    scene decor grande_salle with flash_blanc

    self "Ah... {w=0.5}encore ça ?!"

    show helene inquiete at center with dissolve

    helene "Léon ! Tu vas bien ?!"
    leon "Ce n’est rien, j’ai juste des vertiges."
    helene "..."

    hide helene with dissolve
    show charles serieux at center with dissolve

    charles "..."
    charles "Anne, Hélène, laissez-nous seuls un instant."

    hide charles with dissolve
    show anne serieuse at left
    show helene inquiete at right
    with dissolve

    anne "Très bien."

    hide anne
    hide helene 
    with long_dissolve
    show charles normal at center with dissolve

    charles "Léon... {w=0.5}tu es certain que tout va bien ? N’essaye pas de ma faire croire que tu as juste de simples vertiges."
    charles "Tu peux nous en parler, tu sais."
    self "Je ne peux pas le laisser savoir ce que j’ai au bras..."
    leon "Je t’assure. Je suis juste un peu fatigué mais je ne me sens pas particulièrement mal."
    charles serieux "..."
    charles normal "Peu importe."
    charles "Ah, j’allais oublier !"
    play sound "music/BoutonSelection.mp3"
    charles dague "Cette dague, tu t’en sers toujours pour le combat."
    charles "Tu avais l’habitude de ne jamais t’en séparer."
    charles "Je te la rends."
    leon "Ah, merci."

    show charles normal

    play sound "music/BoutonNavigation.mp3"
    self "Effectivement, elle rentre parfaitement dans le fourreau que j’ai à la taille."
    charles "Bien. Va retrouver Hélène. Revenez vite."
    leon "Ah! Je..."
    charles "Oui ?"

    menu:
        "\"Demander si les démons peuvent prendre une forme humaine\"":
           jump dialogue_charles_1_1
        "Ne rien demander":
           jump dialogue_charles_1_2

label dialogue_charles_1_1:

    leon "Est-ce que les démons peuvent prendre une forme humaine ?"
    charles serieux "Où a-tu entendu une chose pareille ?"
    leon "Nulle part... {w=0.5}je me posais juste la question."
    charles normal "Ne te pose pas des questions aussi insensées. Évidemment qu’ils ne peuvent pas."
    charles "Bref. Ne tardez pas."

    jump dialogue_charles_1_end

label dialogue_charles_1_2:

    leon "Non... {w=0.5}rien."
    charles "..."
    charles "Bref, ne tardez pas."

    jump dialogue_charles_1_end
    
label dialogue_charles_1_end:

    hide charles with long_dissolve

    self "Tout à l’heure... {w=0.5}mon bras..."

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_2 with long_dissolve

    self "La marque... {w=0.5}elle est plus étendue que tout à l’heure..."

    jump sortie_start
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
    leon "Rien d’important..."
    helene "..."
    helene souriante"Bien, allons-y !"

    jump village_start
# END FILE 06 - Sortie

# 07 - Village
label village_start:

    scene decor village

    # On reprend la musique à l’arrivée au village
    play music "music/village.mp3" fadein 1.0 loop

    show helene normal at center
    with ellipse

    helene "... et c’est à cet étal qu’on achète habituellement nos légumes."
    self "On a déjà acheté les herbes... {w=0.5}on ne devait pas se dépêcher de rentrer ?"
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
    leon "On devrait rentrer maintenant qu’on a les herbes, non ? Ils doivent nous attendre."
    helene "On peut bien traîner un peu, ce sont pas dix minutes que vont changer quoi que ce soit."
    helene "..."
    helene normal "..."
    helene serieuse "Léon..."
    leon "Oui ?"

    show helene normal at center_zoom
    helene "Je n’ai pas vraiment trouvé le moment pour t’en parler plus tôt, mais..."
    helene "Toi et moi... {w=0.5}nous formons un couple."

    menu:

        "\"Oui... Anne l’a déjà mentionné.\"":
           jump village_1_1
        "\"Vraiment ?! Je n’en avais aucune idée...\"":
           jump village_1_2

label village_1_1:

    leon "Oui... {w=0.5}Anne l’a déjà mentionné."
    helene normal "Vraiment ? Décidément, elle ne sait pas tenir sa langue !"
    helene "J’aurais préféré te l’annoncer moi-même..."
    helene "C’est aussi de ma faute, je n’ai pas eu le courage de t’en parler avant..."
    helene "Quoi qu’il en soit..."

    jump village_1_end

label village_1_2:

    leon "Vraiment ?! Je n’en avais aucune idée..."
    helene normal "Oui. Nous étions déjà ensemble bien avant de rejoindre l’Ordre."
    helene "Désolée... {w=0.5}Je n’ai pas trouvé le courage de t’en parler plus tôt."
    
    jump village_1_end
    
label village_1_end:

    helene souriante "Tu es très important pour moi."
    helene normal "Et tu sais, je te connais mieux que quiconque."
    helene normal "..."
    helene serieuse "Léon."
    helene "Tu me caches quelque chose d’important, pas vrai ?"
    self "{cps=*2}Que...{/cps}"
    self "{cps=*2}Elle est au courant pour mon bras ?!{/cps}"
    with shake
    self "Non... {w=0.5}Ce n’est pas possible..."
    self "Elle se doute juste de quelque chose..."
    self "Qu’est-ce que je dois faire ? Je dois lui en parler ?"
    self "Nous étions en couple... {w=0.5}C’est probablement la seule à qui je peux me confier..."
    self "Mais ce que Charles a dit au sujet de ceux qui ont cette marque..."
    self "Non. C’est probablement une mauvaise idée de lui en parler."
    self "Ça ne peut que mal finir."
    self "Mais... {w=0.5}Elle m’aime, pas vrai ?"
    self "Mais même si je lui en parle... {w=0.5}elle ne pourrait sûrement rien faire pour m’aider..."

    menu:

        "Lui parler de la marque au bras":
           jump village_2_1
        "Ne pas lui en parler":
           jump village_2_2

label village_2_1:

    leon "Hélène... {w=0.5}Mon bras..."
    helene normal "Oui ?"
    leon "Je m’en suis rendu compte un peu plus tôt..."
    leon "..."
    leon "...Regarde par toi-même."

    pause 2.0
    show helene serieuse
    pause 2.0

    helene "..."
    helene "..."
    helene "..."
    helene "Nous rentrons."

    $ leon("{w=0.0}H{w=0.0}.{w=0.0}.{w=0.0}.{w=0.0} {w=0.0}H{w=0.0}é{w=0.0}l{w=0.0}è{w=0.0}n{w=0.0}e{w=0.0},{w=0.0} {w=0.0}j{w=0.0}e{w=0.0} {w=0.0}t{w=0.0}’{w=0.0}a{w=0.0}s{w=0.0}s{w=0.0}u", interact=False)
    pause 0.7
    helene "Nous rentrons."
    $ leon ("{w=0.0}J{w=0.0}e{w=0.0} {w=0.0}n{w=0.0}e{w=0.0} {w=0.0}v{w=0.0}o{w=0.0}u{w=0.0}l{w=0.0}a{w=0.0}i{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}a", interact=False)
    pause 0.6
    helene "Nous rentrons."
    leon "..."    
   
    jump briefing_endingC_start


label village_2_2:

    leon "Je ne comprends pas de quoi tu parles. Je ne te cache rien."
    helene inquiete "Je vois... {w=0.5}tu ne me fais pas encore confiance, pas vrai ?"
    helene "Je ne peux pas t’en vouloir puisque tu as tout oublié."
    leon "..."
    helene normal "Peu importe."
    helene souriante "Si un jour tu dois me parler de quelque chose, tu sais que je serai là pour t’écouter."
    helene normal "Il commence à se faire tard. Nous devrions rentrer."

    # On stoppe la musique dans cette scène là, en même temps que la transition visuelle
    stop music fadeout 3.0
     
    jump briefing_endingAB_start
# END FILE 07 - Village


# 08 - Ending A/B - Briefing
label briefing_endingAB_start:

    scene decor grande_salle
    #play music "music/planque_dialogue.mp3" fadein 1.0 loop
    play music "music/grande_salle.ogg" fadein 1.0 loop

    show anne normal at center
    with ellipse

    anne "Ah, vous êtes revenus !"

    hide anne with dissolve
    show charles serieux at center with dissolve

    charles "Vous en avez mis, du temps."

    hide charles with dissolve
    show helene normal at center with dissolve

    helene "Vraiment ? On s’est dépêchés, pourtant."

    hide helene with dissolve
    show charles normal at center with dissolve

    charles "..."
    charles "Peu importe."
    charles "Maintenant que tout le monde est là, je vais vous expliquer le plan d’attaque de ce soir. Écoutez attentivement."

    scene decor noir with long_dissolve
    pause 2.0
    scene decor grande_salle
    show charles normal at center
    with long_dissolve

    charles "Une fois notre cible éliminée, on fuira en repassant par le chemin de notre venue puisqu’il sera déjà nettoyé."
    self "En gros, on s’infiltre en tuant les gardes Templiers sur notre chemin et on se cache dans la forêt jusqu’au passage de Jacques de Molay..."
    self "Ça paraît un peu simpliste, mais je suppose que le manque de temps et d’information que nous avons nous empêche d’être mieux préparés..."
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
    helene "Léon..."
    helene inquiete "Tu as vraiment envie de participer à cet assaut ?"
    leon "..."
    helene "Charles ne t’a pas laissé le choix, mais si vraiment tu ne te sens pas prêt..."
    helene serieuse "Tu peux toujours t’enfuir."
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
    play music "music/planque_dialogue.mp3" fadein 1.0 loop
    show anne normal at center
    with ellipse

    anne "Ah, vous êtes revenus !"

    hide anne with dissolve
    show charles serieux at center with dissolve

    charles "Vous en avez mis, du temps."

    hide charles with dissolve
    show helene serieuse at center with dissolve

    helene "..."

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

    charles "Une fois notre cible éliminée, on fuira en repassant par le chemin de notre venue puisqu’il sera déjà nettoyé."
    self "En gros, on s’infiltre en tuant les gardes Templiers sur notre chemin et on se cache dans la forêt jusqu’au passage de Jacques de Molay..."
    self "Ça paraît un peu simpliste, mais je suppose que le manque de temps et d’informations que nous avons nous empêche d’être mieux préparés..."
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

    jump soir_endingC_start
# END FILE 08 - Ending C - Briefing

    
# 09 - Ending A/B - Soir
label soir_endingAB_start:

    scene decor chambre with ellipse

    stop music fadeout 1.0
    play music "music/planque_dialogue.mp3" fadein 1.0 loop

    self "..."
    self "Me cacher avant leur départ..."
    self "C’est vraiment raisonnable ?"

    pause 0.5
    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_3 with long_dissolve

    self "..."
    self "Ça s’est encore propagé..."
    play sound "music/door_opening.ogg"

    scene decor chambre
    show helene normal at center
    with dissolve

    helene "Léon, à propos de..."
    helene serieuse "..."
    self "...Merde !"
    with shake
    self "Elle a eu le temps de le voir ?!"
    helene "À plus tard."

    play sound "music/door_close.ogg"

    hide helene with dissolve

    leon "Hélène ! Je... {w=0.5}Ah...!"

    scene decor noir with flash_blanc
    play sound "music/FlashSound.mp3"
    pause 1.0

    jacques_inconnu "{w=0.0}O{w=0.0}n{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}t{w=0.0} {w=0.0}r{w=0.0}e{w=0.0}c{w=0.0}o{w=0.0}n{w=0.0}n{w=0.0}a{w=0.0}î{w=0.0}t{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}c{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}s{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}à {w=0.0}l{w=0.0}e{w=0.0}u{w=0.0}r{w=0.0}s{w=0.0} {w=0.0}y{w=0.0}e{w=0.0}u{w=0.0}x{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc

    self "Encore ce truc..."
    self "Plus important... {w=0.5}Hélène !"
    self "Elle a manifestement vu mon bras..."
    self "Elle ne va pas en parler aux autres... {w=0.5}pas vrai ?"
    self "Nous sommes en couple... {w=0.5}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère..."
    self "..."
    self "Qu’est ce que je dois faire..."

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
    self "Je veux pas risquer ma vie pour des personnes dont je n’ai aucun souvenir"
    self "Je me planque !"

    jump massacre_endingB_start




# END FILE 09 - Ending A/B - Soir


# 10 - Ending A - Massacre
label massacre_endingA_start:

    scene decor chambre
    show anne serieuse at center
    with ellipse

    anne "Léon, il est l’heure. Je t’attends à l’entrée."

    play sound "music/door_close.ogg"

    self "Je suis stressé et excité à la fois."
    self "..."
    self "Hélène..."
    self "Elle m’évite depuis tout à l’heure..."
    self "Vu que les autres agissent normalement, je ne pense pas qu’elle leur ait parlé de mon bras. C’est déjà un soulagement."

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

    with shake

    play sound "music/sf_decapitation.mp3"
    charles "Bien. Nous avons réussi à franchir les gardes en les éliminant."
    charles "Nous ne leur avons pas non plus laissé l’occasion de donner l’alerte."
    charles "Tout se passe comme prévu."

    scene decor chateau
    stop music fadeout 1.0
    play music "music/action.mp3" fadein 1.0 loop

    show charles masque
    with dissolve

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

    $ anne("{w=0.0}Q{w=0.0}u{w=0.0}’{w=0.0}e{w=0.0}s{w=0.0}t{w=0.0}-{w=0.0}c{w=0.0}e{w=0.0} {w=0.0}q{w=0.0}u{w=0.0}e{w=0.0} {w=0.0}t{w=0.0}u{w=0.0} {w=0.0}v{w=0.0}e{w=0.0}u{w=0.0}x{w=0.0} {w=0.0}d{w=0.0}i{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}p{w=0.0}a", interact=False)
    pause 0.95

    with flash_rouge
    play sound "music/sf_decapitation.mp3"
    hide anne with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center
    with long_dissolve

    helene_demon "Et de un."
    self "...!"
    self "Cette chose... {w=0.5}C’est Hélène ?!"

    show helene_demon at left with move
    show charles panique at right with dissolve

    charles "Anne... {w=0.5}non... {w=0.5}ce n’est pas possible !"
    self "Qu... {w=0.5}qu’est-ce qu’il se passe ?!"

    hide charles with dissolve
    show gaston panique at right with dissolve

    gaston "Ah !"
    gaston "Espèce de monstre ! Meurs !"
    helene_demon souriante "Tu es ridicule."

    #self "*bruit de coeur transpercé*"
    with flash_rouge
    play sound "music/sf_decapitation.mp3"
    hide gaston with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 0.5

    self "C’est un cauchemar !"

    hide helene_demon with dissolve
    show charles panique at center with dissolve

    charles "Anne...! Dis quelque chose !"

    play sound "music/BruitDattaque.mp3"
    with flash_rouge
    hide charles with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 0.5

    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Elle me rattraperait probablement sans difficulté..."

    show helene_demon normal with dissolve

    helene_demon "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donné !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon "Je devais récolter autant d’informations que possible sur les alliés de la résistance... {w=0.5}On dirait que ma mission se termine prématurément."
    self "Elle se rapproche de plus en plus... Je n’ai plus le choix !"
    helene_demon "Je m’attendais à plus de résistance... {w=0.5}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending A - Massacre

# 10 - Ending B - Massacre
label massacre_endingB_start:

    scene decor entree with long_dissolve
    pause 3.0

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
    self "Hélène a vu mon bras... {w=0.5}Est-ce que je ne devrais pas m’enfuir pour de bon ?"
    self "..."
    self "Je ne saurais même pas où aller..."
    self "Je n’ai pas d’autre choix que de les attendre et espérer qu’elle n’en parle à personne..."

    scene decor chambre with ellipse

    self "Ça fait déjà un moment... {w=0.5}J’espère que ça ne se passe pas mal."

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

    stop music fadeout 1.0
    play music "music/action.mp3" fadein 1.0 loop

    gaston "Dieu merci, tu es bien là ! Dépêche-toi, on dégage en vitesse !"
    leon "Qu’est-ce qui se passe ?!"
    gaston "C’est Hélène ! C’est une saloperie de démon !"
    leon "Qu... {w=0.5}quoi ?!"
    gaston "Elle a tué Anne et Charles et si on ne se grouille pas, on est les suivants !"
    leon "Qu’est-ce que tu racontes ?!"
    $ gaston("M{w=0.0}a{w=0.0}g{w=0.0}n{w=0.0}e{w=0.0}-{w=0.0}t{w=0.0}o{w=0.0}i{w=0.0},{w=0.0} {w=0.0}p{w=0.0}u{w=0.0}t{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0},{w=0.0} {w=0.0}o{w=0.0}n{w=0.0} {w=0.0}n{w=0.0}’{w=0.0}a{w=0.0} {w=0.0}p{w=0.0}a{w=0.0}s{w=0.0} {w=0.0}l{w=0.0}e{w=0.0} {w=0.0}t{w=0.0}e{w=0.0}m{w=0.0}p{w=0.0}s{w=0.0} {w=0.0}!{w=0.0} {w=0.0}E{w=0.0}l{w=0.0}l{w=0.0}e{w=0.0} {w=0.0}v{w=0.0}a{w=0.0} {w=0.0}n{w=0.0}o{w=0.0}u", interact=False)
    pause 1.75

    #self "*bruit de coeur transpercé*"
    with flash_rouge
    play sound "music/sf_decapitation.mp3"
    hide gaston with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center with dissolve

    helene_demon "Qu’est-ce qu’il est bruyant, celui-là."
    self "...!"
    self "...Gaston !"
    helene_demon souriante "Cet imbécile avait une chance de s’échapper mais il a préféré revenir ici pour te prévenir."
    self "Cette chose... {w=0.5}C’est Hélène ?!"
    self "C’est vraiment elle ?!"
    helene_demon normal "J’aurais préféré garder ma couverture plus longtemps, mais l’attaque se déroulait trop bien et je ne pouvais pas risquer la vie du grand maître."
    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Impossible, elle bloque l’entrée... {w=0.5}et elle me rattraperait probablement sans difficulté."
    helene_demon "Je devais récolter autant d’informations que possible sur les alliés de la résistance... {w=0.5}On dirait que ma mission se termine prématurément."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donné !"
    helene_demon souriante "J’ai commencé par attaquer Anne dans le dos, par surprise. C’était la plus dangereuse des trois, après tout !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon normal "Elle est morte en un instant. Charles était complètement figé, je l’ai tué dans la foulée sans qu’il ne bouge d’un pouce."
    self "Elle se rapproche de plus en plus... {w=0.5}Je n’ai plus le choix !"
    helene_demon "Je m’attendais à plus de résistance... {w=0.5}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending B - Massacre

# 10 - Ending C - Massacre

label soir_endingC_start:

    scene decor noir with dissolve
    pause 3.0
    scene decor chambre with dissolve

    self "..."
    self "Je ne peux qu’attendre, maintenant..."
    self "Ah !"

    scene decor noir with flash_blanc
    pause 1.0

    jacques_inconnu "{w=0.0}O{w=0.0}n{w=0.0} {w=0.0}p{w=0.0}e{w=0.0}u{w=0.0}t{w=0.0} {w=0.0}r{w=0.0}e{w=0.0}c{w=0.0}o{w=0.0}n{w=0.0}n{w=0.0}a{w=0.0}î{w=0.0}t{w=0.0}r{w=0.0}e{w=0.0} {w=0.0}c{w=0.0}e{w=0.0}s{w=0.0} {w=0.0}d{w=0.0}é{w=0.0}m{w=0.0}o{w=0.0}n{w=0.0}s{w=0.0} {w=0.0}s{w=0.0}o{w=0.0}u{w=0.0}s{w=0.0} {w=0.0}f{w=0.0}o{w=0.0}r{w=0.0}m{w=0.0}e{w=0.0} {w=0.0}h{w=0.0}u{w=0.0}m{w=0.0}a{w=0.0}i{w=0.0}n{w=0.0}e{w=0.0} {w=0.0}à {w=0.0}l{w=0.0}e{w=0.0}u{w=0.0}r{w=0.0}s{w=0.0} {w=0.0}y{w=0.0}e{w=0.0}u{w=0.0}x{w=0.0}."

    pause 1.0
    scene decor chambre with flash_blanc

    self "Encore ce truc..."
    self "Mon bras me brûle..."

    scene arm_gant with long_dissolve
    pause 0.8
    scene arm_3 with long_dissolve

    self "..."
    self "La réaction qu’elle a eu quand elle a vu mon bras..."
    self "Elle ne va pas en parler aux autres... {w=0.5}pas vrai ?"
    self "Nous sommes en couple... {w=0.5}Elle ne ferait pas ça !"
    self "..."
    self "Enfin, j’espère..."
    self "..."
    self "Il faut que j’aille lui parler !"

    pause 0.5
    play sound "music/door_opening.ogg"
    stop music fadeout 1.0
    play music "music/action.mp3" fadein 1.0 loop
    pause 0.5

    self "!!!"
    leon "{cps=*2}Aah... {w=0.3}AAAAAH !"
    with shake

    scene cadavre_gaston with dissolve

    self "{cps=*2}Qu’est-ce que...!{/cps}"
    leon "{cps=*2}Gaston ! Tu m’entends ?!{/cps}"
    with shake
    self "{cps=*2}Il n’a plus de pouls... {w=0.5}merde !{/cps}"
    self "{cps=*2}Nous sommes en danger ici ! On doit se barrer !{/cps}"
     
    scene decor noir with dissolve
    pause 1.0
    scene decor grande_salle
    show helene normal at center
    with dissolve

    leon "{cps=*2}Ah ! Hélène !{/cps}"
    leon "{cps=*2}On doit partir d’ici !{/cps}"
    helene inquiete "Qu’est-ce que tu racontes ?{/cps}"
    leon "{cps=*2}Dépêche-toi !{/cps}"
    charles "Qu’est-ce qu’il se passe, ici ?"

    hide helene with dissolve
    show charles serieux at center

    charles "Quelque chose ne va pas ?"
    leon "C’est Gaston, il..."
    self "Attends..."
    self "C’est forcément l’un d’entre eux qui a fait ça !"
    self "Je ne peux faire confiance à personne !"
    $ self("{w=0.0}J{w=0.0}e{w=0.0} {w=0.0}d{w=0.0}o{w=0.0}i{w=0.0}s{w=0.0} {w=0.0}p{w=0.0}a{w=0.0}r{w=0.0}t{w=0.0}i{w=0.0}r{w=0.0} {w=0.0}d{w=0.0}’{w=0.0}i{w=0.0}c{w=0.0}i{w=0.0} {w=0.0}l{w=0.0}e{w=0.0} {w=0.0}p{w=0.0}l{w=0.0}u", interact=False)
    pause 1.0

    #self "*bruit de coeur transpercé*"
    with flash_rouge
    play sound "music/BruitDattaque.mp3"
    hide charles with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 1.5
    show helene_demon normal at center
    with dissolve

    self "...!"
    self "...Charles !"
    helene_demon souriante "Et de deux."
    self "Cette chose... {w=0.5}C’est Hélène ?!"
    anne "Vous en faites, du bruit !"

    hide helene_demon with dissolve
    show anne normal at center with dissolve

    anne "Qu’est ce qu... {w=0.5}Aah... {w=0.5}Non..."
    anne panique "AAAAAAAAH !"
    with shake
    anne "Charles ! Charles !!"
    $ anne("D{w=0.0}i{w=0.0}s{w=0.0} {w=0.0}q{w=0.0}u{w=0.0}e{w=0.0}l{w=0.0}q{w=0.0}u{w=0.0}e{w=0.0} {w=0.0}c{w=0.0}h{w=0.0}o", interact=False)
    pause 0.6

    #self "*bruit de coeur transpercé*"
    with flash_rouge
    play sound "music/sf_decapitation.mp3"
    hide anne with dissolve
    pause 0.5
    with shake
    play sound "music/FlashSound.mp3"
    pause 1.0

    show helene_demon souriante at center

    self "C’est un cauchemar !"
    helene_demon "Les humains sont si faibles !"
    self "Qu’est-ce que je dois faire ? Fuir ?"
    self "Elle me rattraperait probablement sans difficulté..."
    helene_demon normal "J’aurais préféré garder ma couverture plus longtemps."
    self "Me battre ? Ah, j’ai la dague que Charles m’a donné !"
    self "Est-ce que ça va vraiment marcher sur une créature pareille ?"
    helene_demon "Je devais récolter autant d’informations que possible sur les alliés de la résistance... {w=0.5}On dirait que ma mission se termine prématurément."
    self "Elle se rapproche de plus en plus... Je n’ai plus le choix !"
    helene_demon "Je m’attendais quand même à plus de résistance... {w=0.5}C’en est presque décevant."

    jump mort_de_helene_start
# END FILE 10 - Ending C - Massacre

# 11 - Mort de Hélène
label mort_de_helene_start:

    play sound "music/BruitDattaque.mp3"
    with flash_rouge
    # on stoppe la musique car moment drama
    stop music fadeout 1.0
    pause 3.0
    scene mort_de_helene with dissolve

    helene_demon "L... {w=0.5}Léon."
    self "...Ça a marché ? Une simple dague ?"
    helene_demon "Tu dois... {w=0.5}vivre..."
    self "Qu’est-ce qu’elle raconte ?"
    helene_demon "Je suis vraiment heureuse... {w=0.5}de t’avoir rencontré..."
    helene_demon "Je ne regrette rien..."
    self "Elle débloque !"

    scene decor noir with dissolve
    with shake
    play sound "music/FlashSound.mp3"
    self "..."
    self "...elle ne respire plus."
    self "...!"
    self "Je me sens si apaisé tout d’un coup... {w=0.5}Qu’est-ce que ?!"

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
    scene decor noir with dissolve
    

    jacques_inconnu "{cps=*1.3}Demain, c’est le grand jour...{/cps}"
    jacques_inconnu "{cps=*1.3}Nous allons enfin pouvoir nous débarrasser de cette monarchie exécrable qui règne depuis bien trop longtemps.{/cps}"
    jacques_inconnu "{cps=*1.3}N’es-tu pas excité, Léon ?{/cps}"
    jacques_inconnu "{cps=*1.3}Tu t’es préparé tellement longtemps pour ce jour.{/cps}"
    jacques_inconnu "{cps=*1.3}Plus que n’importe qui d’autre.{/cps}"
    jacques_inconnu "{cps=*1.3}...{/cps}"
    jacques_inconnu "{cps=*1.3}Il y a plusieurs choses que tu dois savoir sur les démons.{/cps}"

    scene decor eglise with dissolve
    # on attend la CG pour mettre la musique
    play music "music/eglise_calme.mp3" fadein 1.0 loop
    pause 1.0

    jacques "Les démons peuvent prendre une forme humaine."
    jacques "C’est vraiment pratique, ils deviennent totalement méconnaissables."
    jacques "Attention, cependant..."
    jacques "On peut reconnaître ces démons sous forme humaine à leurs yeux."
    jacques "Ceux-ci sont vairons, c’est à dire que chaque oeil a une couleur différente."
    jacques "Fais en sorte que nos ennemis ne s’en rendent jamais compte."
    jacques "Autre chose. Un démon et son invocateur peuvent se transférer leur énergie vitale."
    jacques "Un démon peut même allonger la durée de vie de son invocateur de cette façon."
    jacques "Cependant, cela lui coûterait sa propre espérance de vie. "
    jacques "Un démon pourrait même aller jusqu’à sacrifier sa vie pour sauver celle de l’invocateur s’il est en danger de mort."
    jacques "Enfin, il n’a pas vraiment d’intérêt à faire ça."
    jacques "Mais tout cela est sans importance pour le moment."
    jacques "Nous sommes sur le point de vivre un moment historique !"
    jacques "Je suppose que tu te souviens de toutes les étapes du rituel ?"
    leon "Oui, grand maître."
    jacques "Parfait. Tu vas pouvoir passer à l’invocation de ton démon."
    jacques "Tu lui as déjà choisi un nom ?"
    leon "Oui, grand maître."
    leon "Si c’est un mâle, je l’appellerai Horace." # horace oh desespoir !
    leon "Et si c’est une femelle, je l’appellerai..."
    pause 0.5
    leon "Hélène."
    pause 1.0

    jump end_credits

# END 12 - Flashback
