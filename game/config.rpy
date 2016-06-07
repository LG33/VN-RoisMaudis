image decor noir = "#000"
image decor intro:
    "backgrounds/intro.png"
    zoom 0.5
image decor chambre:
    "backgrounds/bedroom.png"
    zoom 0.5
image decor grande_salle:
    "backgrounds/bigroom.png"
    zoom 0.5
image decor entree:
    "backgrounds/entry.png"
    zoom 0.5
image decor village:
    "backgrounds/village.jpg"
    zoom 0.5
image decor chateau:
    "backgrounds/fontainebleau.png"
    zoom 0.5
image decor water:
    "backgrounds/water.png"
    zoom 0.5
image decor eglise:
    "backgrounds/eglise.jpg"

image helene normal:
    "characters/helene/helene_normal.png"
    zoom 0.45
image helene masque:
    "characters/helene/helene_masque.png"
    zoom 0.45
image helene inquiete:
    "characters/helene/helene_panique.png"
    zoom 0.45
image helene serieuse:
    "characters/helene/helene_serieuse.png"
    zoom 0.45
image helene souriante:
    "characters/helene/helene_sourire.png"
    zoom 0.45

image helene_demon normal:
    "characters/helene_demon/helene_demon_normal.png"
    zoom 0.45
image helene_demon souriante:
    "characters/helene_demon/helene_demon_souriante.png"
    zoom 0.45

image gaston normal:
    "characters/gaston/gaston_normal.png"
    zoom 0.4
image gaston masque:
    "characters/gaston/gaston_masque.png"
    zoom 0.4
image gaston serieux:
    "characters/gaston/gaston_serieux.png"
    zoom 0.4
image gaston souriant:
    "characters/gaston/gaston_souriant.png"
    zoom 0.4
image gaston panique:
    "characters/gaston/gaston_panique.png"
    zoom 0.4

image anne normal:
    "characters/anne/anne_normal.png"
    zoom 5
image anne masque:
    "characters/anne/anne_masque.png"
    zoom 5
image anne choquee:
    "characters/anne/anne_choquee.png"
    zoom 5
image anne serieuse:
    "characters/anne/anne_serieuse.png"
    zoom 5
image anne souriante:
    "characters/anne/anne_souriante.png"
    zoom 5

image charles normal:
    "characters/charles/charles_normal.png"
    zoom 0.4
image charles masque:
    "characters/charles/charles_masque.png"
    zoom 0.4
image charles panique:
    "characters/charles/charles_panique.png"
    zoom 0.4
image charles serieux:
    "characters/charles/charles_serieux.png"
    zoom 0.4
image charles dague:
    "characters/charles/charles_dague.png"
    zoom 0.4

image arm_0:
    "backgrounds/bras/bras_0.png"
    zoom 0.5
image arm_1:
    "backgrounds/bras/bras_1.png"
    zoom 0.5
image arm_2:
    "backgrounds/bras/bras_2.png"
    zoom 0.5
image arm_3:
    "backgrounds/bras/bras_3.png"
    zoom 0.5
image arm_4:
    "backgrounds/bras/bras_4.png"
    zoom 0.5
image arm_gant:
    "backgrounds/bras/bras_gant.png"
    zoom 0.5

# image test = im.MatrixColor("characters/bras_leon_fin.png",im.matrix.saturation(0.1))

define leon = Character('Léon', outlines=[(1, "#008800", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")

define helene = Character('Hélène', image="helene", outlines=[(1, "#ff00ff", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")
define helene_demon = Character('Hélène', image="helene_demon", outlines=[(1, "#ff00ff", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")

define gaston = Character('Gaston', image="gaston", color="#9999ff", window_top_padding=40, window_background="gui/dialogue_box.png")

define anne = Character('Anne', image="anne", color="#eeeeee", window_top_padding=40, window_background="gui/dialogue_box.png")

define charles = Character('Charles', image="charles", outlines=[(1, "#aa7700", 0, 0)], window_top_padding=40, window_background="gui/dialogue_box.png")

define inconnu = Character('???', window_top_padding=40, window_background="gui/dialogue_box.png")

define jacques_inconnu = Character("???", what_color="#8888ff", what_italic=True, what_slow_cps=10, window_top_padding=40, window_background="gui/dialogue_box.png")
define jacques = Character("Jacques De Molay", what_color="#8888ff", what_italic=True, what_slow_cps=20, window_top_padding=40, window_background="gui/dialogue_box.png")

define self = Character(None, color="#ffff99", what_italic=True, what_color="#ffdd55", window_top_padding=90, window_background="gui/narrative_box.png")

transform left: 
    xalign 0.2 
    yalign 1.2
    
transform right: 
    xalign 0.8
    yalign 1.2
    
transform center: 
    xalign 0.5 
    yalign 1.2

define ellipse = Fade(0.5, 2.0, 0.5)
define long_dissolve = Dissolve(0.5)
define dissolve = Dissolve(0.2)

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
    
    flash_rouge = Fade(.25, 0, .25, color="#ff0000")
    flash_blanc = Fade(.25, 0, .25, color="#ffffff")
    
    choix1 = 0
	
    # Channels
    renpy.music.register_channel('cloche')
	