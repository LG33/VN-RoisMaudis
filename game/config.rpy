image decor noir = "#000"
image decor intro:
    "backgrounds/intro.png"
image decor chambre:
    "backgrounds/bedroom.png"
image decor grande_salle:
    "backgrounds/bigroom.png"
image decor entree:
    "backgrounds/entry.png"
image decor village:
    "backgrounds/village.png"
image decor chateau:
    "backgrounds/fontainebleau.png"
image decor water:
    "backgrounds/water.png"
    zoom 0.5
image decor eglise:
    "backgrounds/eglise.png"

image helene normal:
    "characters/helene/Helene_Normale.png"
image helene masque:
    "characters/helene/Helene_Masque.png"
image helene inquiete:
    "characters/helene/Helene_Panique.png"
image helene serieuse:
    "characters/helene/Helene_Panique.png"
image helene souriante:
    "characters/helene/Helene_Sourire.png"

image helene_demon normal:
    "characters/helene_demon/Helene_Demon_Evil.png"
image helene_demon souriante:
    "characters/helene_demon/Helene_Demon_Smirk.png"
image mort_de_helene = "backgrounds/CG_Helene.png"

image gaston normal:
    "characters/gaston/Gaston_Normal.png"
image gaston masque:
    "characters/gaston/Gaston_Masque.png"
image gaston serieux:
    "characters/gaston/Gaston_Serieux.png"
image gaston souriant:
    "characters/gaston/Gaston_Sourire.png"
image gaston panique:
    "characters/gaston/Gaston_Panique.png"
image cadavre_gaston = "backgrounds/CG_Gaston.jpg"

image anne normal:
    "characters/anne/Anne_Normale.png"
image anne masque:
    "characters/anne/Anne_Masque.png"
image anne panique:
    "characters/anne/Anne_Panique.png"
image anne serieuse:
    "characters/anne/Anne_Serieuse.png"
image anne souriante:
    "characters/anne/Anne_Sourire.png"

image charles normal:
    "characters/charles/Charles_Normal.png"
image charles masque:
    "characters/charles/Charles_Masque.png"
image charles panique:
    "characters/charles/Charles_Panique.png"
image charles serieux:
    "characters/charles/Charles_Serieux.png"
image charles dague:
    "characters/charles/Charles_Dague.png"

image arm_0:
    "backgrounds/bras/bras_0.png"
image arm_1:
    "backgrounds/bras/bras_1.png"
image arm_2:
    "backgrounds/bras/bras_2.png"
image arm_3:
    "backgrounds/bras/bras_3.png"
image arm_4:
    "backgrounds/bras/bras_4.png"
image arm_gant:
    "backgrounds/bras/bras_gant.png"

# image test = im.MatrixColor("characters/bras_leon_fin.png",im.matrix.saturation(0.1))

define leon = Character('Léon', window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define helene = Character('Hélène', image="helene", window_top_padding=22, window_background="gui/ingame/dialogue_box.png")
define helene_demon = Character('Hélène', image="helene_demon", window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define gaston = Character('Gaston', image="gaston", window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define anne = Character('Anne', image="anne", window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define charles = Character('Charles', image="charles", window_top_padding=22, window_background="gui/ingame/dialogue_box.png")
#define charles = Character('Charles', image="charles", outlines=[(1, "#aa7700", 0, 0)], window_top_padding=22, window_background="gui/dialogue_box.png")

define inconnu = Character('???', window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define jacques_inconnu = Character("???", what_color="#8888ff", what_italic=True, what_slow_cps=15, window_top_padding=22, window_background="gui/ingame/dialogue_box.png")
define jacques = Character("Jacques De Molay", what_color="#8888ff", what_italic=True, what_slow_cps=20, window_top_padding=22, window_background="gui/ingame/dialogue_box.png")

define self = Character(None, what_italic=True, what_color="#ffdd55", window_top_padding=90, window_background="gui/ingame/narrative_box.png")

transform left: 
    xalign 0.2 
    yalign 1
    zoom 1.3
    
transform right: 
    xalign 0.8
    yalign 1
    zoom 1.3
    
transform center: 
    xalign 0.5 
    yalign 1
    zoom 1.3
    
transform left_zoom: 
    xalign 0.2 
    yalign 0.3
    zoom 2
    
transform right_zoom: 
    xalign 0.8
    yalign 0.3
    zoom 2
    
transform center_zoom: 
    xalign 0.5 
    yalign 0.3
    zoom 2

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
    renpy.music.register_channel('menu', loop=False)
    renpy.music.set_volume(0.5, 0, channel='menu')