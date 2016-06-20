# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.95
        
        $i = 0
        $hSpacing = 20
        $vSpacing = 20
            
        hbox:
            spacing hSpacing
            vbox:
                style "menu"
                spacing vSpacing 
                 
                for caption, action, chosen in items:
                    $i += 1
                    if i % 2 == 1:
                        if action:
                             
                            button:
                                action action
                                style "menu_choice_button"                       
                               
                                text caption style "menu_choice"
                             
                        else:
                            text caption style "menu_caption"
                   
                if i % 2 == 0:
                    $i = 1
                else:
                    $i = 1               
                           
            vbox:
                style "menu"
                spacing vSpacing
                 
                for caption, action, chosen in items:
                    $i += 1
                    if i % 2 == 1:
                        if action:
                             
                            button:
                                action action
                                style "menu_choice_button"                     
                               
                                text caption style "menu_choice"
                             
                        else:
                            text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default
    
    #le texte
    style menu_choice is button_text:
        color "#fff"
        size 28
        drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ] 
        outlines [(1, "#231906", 0, 0)]
        hover_outlines [(1, "#000000", 0, 0)]
        selected_outlines [(1, "#000000", 0, 0)]
        selected_hover_outlines [(1, "#000000", 0, 0)]
        font "gui/century.ttf"
    
    # la boite de texte
    style menu_choice_button is button:
        xminimum 700
        xmaximum 700
        yminimum 90
        ymaximum 90
        ypadding 10
        xpadding 10
        background "#000000dd"
        hover_background "#231906dd"
        mouse "hover"
        

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■

screen main_menu:
    tag menu
    
    add "gui/accueil/background.jpg"
    
    imagebutton auto "gui/accueil/nouveau_%s.png" xpos 0 ypos 0 focus_mask True action [Start(), Play("menu", "music/BoutonNavigation.mp3")]  mouse "hover"

    imagebutton auto "gui/accueil/charger_%s.png" xpos 0 ypos 0 focus_mask True action [ShowMenu('charger'), Show("load"), Play("menu", "music/BoutonNavigation.mp3")]  mouse "hover"
    
    imagebutton auto "gui/accueil/quitter_%s.png" xpos 0 ypos 0 focus_mask True action [Quit(confirm=False), Play("menu", "music/BoutonNavigation.mp3")]  mouse "hover"

            
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
    
    soundOn = True
        
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    
    $ x1=x+337
    $ y1=y+22
    add FileScreenshot(number) xpos x1 ypos y1
    $ x2=x+30
    $ y2=y+30
    text file_text xpos x2 ypos y2 size 20
    

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
    
screen charger:
    tag menu
    
    add "gui/charger/background.png"
    
    if soundOn:
        use sound_On
    else:
        use sound_Off
    
    if _preferences.fullscreen:
        use fullscreen_On
    else:
        use fullscreen_Off
    
    use nav_buttons
    
screen sauvegarder:
    tag menu
    
    add "gui/charger/background.png"
    
    use save
    
    if soundOn:
        use sound_On
    else:
        use sound_Off
    
    if _preferences.fullscreen:
        use fullscreen_On
    else:
        use fullscreen_Off
    
    use nav_buttons
    
screen save:
    image "gui/charger/sauvegarder_selected_idle.png" xpos 0.22 ypos 0.1
    imagebutton auto "gui/charger/charger_%s.png" xpos 0.1 ypos 0.1 focus_mask True action [Hide("save"), Show("load"), Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    
    use save_load_slots
    
screen load:
    image "gui/charger/charger_selected_idle.png" xpos 0.1 ypos 0.1
    imagebutton auto "gui/charger/sauvegarder_%s.png" xpos 0.22 ypos 0.1 focus_mask True action [Hide("load"), Show("save"), Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    
    use save_load_slots
    
screen save_load_slots:
    $ y=295
    for i in range(0, 3):
        imagebutton auto "gui/charger/fileslot_%s.png" xpos 195 ypos y focus_mask True action [FileAction(i), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"
        use load_save_slot(number=i, x=195, y=y)
        $ y+=188
    
    $ y=295
    for i in range(3, 6):
        imagebutton auto "gui/charger/fileslot_%s.png" xpos 755 ypos y focus_mask True action [FileAction(i), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"
        use load_save_slot(number=i, x=755, y=y)
        $ y+=188
        
screen nav_buttons:
    imagebutton auto "gui/charger/retour_%s.png" xpos 0.1 ypos 0.8 action [Return(), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/main_menu_%s.png" xpos 0.22 ypos 0.8 action [MainMenu(), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/credits_%s.png" xpos 0.7 ypos 0.8 action [ShowMenu('text_history'), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/credits_%s.png" xpos 0.6 ypos 0.8 action [Jump('credits'), Hide("save"), Hide("load"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("menu", "music/BoutonNavigation.mp3")]
    
screen sound_Off: 
    imagebutton auto "gui/charger/sound_off_%s.png" xpos 1475 ypos 275 focus_mask True action [ToggleVariable("soundOn"), SetMute("music",False), SetMute("sfx",False), SetMute("menu",False), Hide("sound_Off"), Show("sound_On"), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"
    
screen sound_On: 
    imagebutton auto "gui/charger/sound_on_%s.png" xpos 1475 ypos 275 focus_mask True action [ToggleVariable("soundOn"), SetMute("music",True), SetMute("sfx",True), SetMute("menu",True), Hide("sound_On"), Show("sound_Off"), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"
    
screen fullscreen_Off:
    imagebutton auto "gui/charger/windowed_%s.png" xpos 1480 ypos 510 focus_mask True action [Preference('display', 'fullscreen'), Hide("fullscreen_Off"), Show("fullscreen_On"), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"
    
screen fullscreen_On: 
    imagebutton auto "gui/charger/fullscreen.png" xpos 1480 ypos 510 focus_mask True action [Preference('display', 'window'), Hide("fullscreen_On"), Show("fullscreen_Off"), Play("menu", "music/BoutonSelection.mp3")] mouse "hover"

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show"
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 0.35 ypos 0.8 action [yes_action, Play("menu", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/yesno_no_%s.png" xpos 0.65 ypos 0.8 action [no_action, Play("menu", "music/BoutonNavigation.mp3")]  mouse "hover"
    
    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno_main_menu.png"

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos


## ■██▓▒░ THE TEXTBOX ░▒▓███████████████████████████████████■
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:
    default side_image = None
    window:
        id "window"
        has vbox:
            style "say_vbox"
        if who:
            text who id "who"
        text what id "what"              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Which quick menu should we use? We use 5 different quick menues for presentation purposes in the script.

## ■██▓▒░ TEXTBOX DROP SHADOW ░▒▓███████████████████████████■
## This block is responsible for the text drop shadow effect for the textbox dialogue.
init python:
    style.say_dialogue.drop_shadow = (2, 2)
    style.say_dialogue.drop_shadow_color = "#000"
    
    style.say_dialogue.font = "gui/century.ttf"
    style.say_dialogue.size = 40
    
    #style.say_dialogue.color = "#231906"

## ■██▓▒░ QUICK MENU ░▒▓████████████████████████████████████■
## Screens for the quick menus above the textbox. We use several different quick menus for presentation purposes.

screen menu_button:
    imagebutton auto "gui/ingame/menu_%s.png" action [ShowMenu('sauvegarder'), Play("menu", "music/BoutonNavigation.mp3")]  xpos 0.75 ypos 0 focus_mask True mouse "hover"

screen ingame_menu:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') focus_mask True at option mouse "hover"
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() focus_mask True at home mouse "hover"
    imagebutton auto "gui/ingame_menu_%s.png" action [Show('menu_button'), Hide('ingame_menu')] xpos 0.85 ypos 0 focus_mask True mouse "hover"
    
init -2:
    transform option:
        xpos 0.85
        ypos -150
        easein_bounce 0.5 ypos 75
        on hide:
            ypos 75
            linear 0.3 ypos -150
    transform home:
        xpos 0.85
        ypos -75
        easein_bounce 0.5 ypos 150
        on hide:
            ypos 150
            linear 0.3 ypos -75
            