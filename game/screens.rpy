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
        size 35
        font "gui/century.ttf"
    
    # la boite de texte
    style menu_choice_button is button:
        xminimum 907
        xmaximum 907
        yminimum 207
        ymaximum 207
        xpadding 150
        ypadding 10
        background "gui/ingame/choice_idle.png"
        hover_background "gui/ingame/choice_hover.png"
        mouse "hover"
        

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■

screen main_menu:
    tag menu
    
    add "gui/accueil/background.jpg"
    
    imagebutton auto "gui/accueil/nouveau_%s.png" xpos 0 ypos 0 focus_mask True action [Start(), Play("gui", "music/BoutonNavigation.mp3")]  mouse "hover"

    imagebutton auto "gui/accueil/charger_%s.png" xpos 0 ypos 0 focus_mask True action [ShowMenu('load'), Play("gui", "music/BoutonNavigation.mp3")]  mouse "hover"
    
    imagebutton auto "gui/accueil/quitter_%s.png" xpos 0 ypos 0 focus_mask True action [Quit(confirm=False), Play("gui", "music/BoutonNavigation.mp3")]  mouse "hover"

    

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
    
screen load:
    tag menu
    
    add "gui/charger/background.png"
    
    add "gui/charger/charger_selected_idle.png" xpos 540 ypos 165
    imagebutton auto "gui/charger/sauvegarder_%s.png" xpos 174 ypos 175 focus_mask True action [Show("save"), Hide("load"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    
    use save_load_slots
    
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
    tag menu
    
    add "gui/charger/background.png"
    
    add "gui/charger/sauvegarder_selected_idle.png" xpos 155 ypos 165
    imagebutton auto "gui/charger/charger_%s.png" xpos 559 ypos 175 focus_mask True action [Show("load"), Hide("save"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    
    use save_load_slots
    
    if soundOn:
        use sound_On
    else:
        use sound_Off
    
    if _preferences.fullscreen:
        use fullscreen_On
    else:
        use fullscreen_Off
    
    use nav_buttons
    
screen save_load_slots:
    $ y=295
    for i in range(0, 3):
        imagebutton auto "gui/charger/fileslot_%s.png" xpos 195 ypos y focus_mask True action [FileAction(i), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"
        use load_save_slot(number=i, x=195, y=y)
        $ y+=188
    
    $ y=295
    for i in range(3, 6):
        imagebutton auto "gui/charger/fileslot_%s.png" xpos 755 ypos y focus_mask True action [FileAction(i), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"
        use load_save_slot(number=i, x=755, y=y)
        $ y+=188
            
init -2 python:
    x=0
    y=0
    
    soundOn = True
    
    style.text.font = "gui/century.ttf"
        
screen load_save_slot:
    $ file_text = "{size=30}{color=#000}% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    
    $ x1=x+295
    $ y1=y+22
    add FileScreenshot(number) xpos x1 ypos y1 at filescreenshot
    $ x2=x+30
    $ y2=y+30
    text file_text xpos x2 ypos y2 size 20
    
transform filescreenshot:
    zoom 1.25
        
screen nav_buttons:
    imagebutton auto "gui/charger/retour_%s.png" xpos 250 ypos 880 action [Return(), Hide("sauvegarder"), Hide("charger"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/main_menu_%s.png" xpos 820 ypos 880 action [MainMenu(), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/log_%s.png" xpos 1395 ypos 755 action [ShowMenu('text_history'), Hide("sauvegarder"), Hide("charger"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/charger/credits_%s.png" xpos 1395 ypos 880 action [ShowMenu("credits"), Hide("charger"), Hide("sauvegarder"), Hide("charger"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    
screen sound_Off: 
    imagebutton auto "gui/charger/sound_off_%s.png" xpos 1475 ypos 275 focus_mask True action [ToggleVariable("soundOn"), SetMute("music",False), SetMute("sfx",False), SetMute("menu",False), Hide("sound_Off"), Show("sound_On"), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"
    
screen sound_On: 
    imagebutton auto "gui/charger/sound_on_%s.png" xpos 1475 ypos 275 focus_mask True action [ToggleVariable("soundOn"), SetMute("music",True), SetMute("sfx",True), SetMute("menu",True), Hide("sound_On"), Show("sound_Off"), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"
    
screen fullscreen_Off:
    imagebutton auto "gui/charger/fullscreen_%s.png" xpos 1480 ypos 510 focus_mask True action [Preference('display', 'fullscreen'), Hide("fullscreen_Off"), Show("fullscreen_On"), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"
    
screen fullscreen_On: 
    imagebutton auto "gui/charger/windowed_%s.png" xpos 1480 ypos 510 focus_mask True action [Preference('display', 'window'), Hide("fullscreen_On"), Show("fullscreen_Off"), Play("gui", "music/BoutonSelection.mp3")] mouse "hover"

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show"
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.
    
    if message == layout.OVERWRITE_SAVE:
        add "gui/yesno/ecraser.png"
    elif message == layout.LOADING:
        add "gui/yesno/charger.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno/main_menu.png"

    imagebutton auto "gui/yesno/yes_%s.png" xpos 500 ypos 700 action [yes_action, Hide("sauvegarder"), Hide("charger"), Hide("sound_On"), Hide("sound_Off"), Hide("fullscreen_Off"), Hide("fullscreen_On"), Play("gui", "music/BoutonNavigation.mp3")] mouse "hover"
    imagebutton auto "gui/yesno/no_%s.png" xpos 1050 ypos 700 action [no_action, Play("gui", "music/BoutonNavigation.mp3")]  mouse "hover"
    
    
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
    ## style.say_dialogue.drop_shadow = (2, 2)
    style.say_dialogue.color = "#fff"
    
    style.say_dialogue.font = "gui/century.ttf"
    style.say_dialogue.size = 40
    
    style.say_label.color = "#00000000"
    
    #style.say_dialogue.color = "#231906"

## ■██▓▒░ QUICK MENU ░▒▓████████████████████████████████████■
## Screens for the quick menus above the textbox. We use several different quick menus for presentation purposes.

## screen menu_button:
##     imagebutton auto "gui/ingame/menu_%s.png" action [ShowMenu('save'), Play("gui", "music/BoutonNavigation.mp3")]  xpos 0.75 ypos 0 focus_mask True mouse "hover"

screen credits:
    tag menu
    imagebutton idle "gui/credits.png" action Return()
    
screen end_credits:
    tag menu
    imagebutton idle "gui/credits.png" action ShowMenu("thanks")
screen thanks:
    tag menu
    imagebutton idle "gui/merci.png" action MainMenu(confirm=False)