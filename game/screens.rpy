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
        outlines [(1, "#000099", 0, 0)]
        hover_outlines [(1, "#000000", 0, 0)]
        selected_outlines [(1, "#000000", 0, 0)]
        selected_hover_outlines [(1, "#000000", 0, 0)]
    
    # la boite de texte
    style menu_choice_button is button:
        xminimum 700
        xmaximum 700
        yminimum 90
        ymaximum 90
        ypadding 10
        xpadding 10
        background "#000000dd"
        hover_background "#000033dd"
        

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
## Screen that's used to display the main menu, when Ren'Py first starts
## http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    # begin-end comments like the one in the next line are used to display code examples in the game
#begin add_image
    add "gui/main_menu_ground.jpg" # Add a background image for the main menu.
#end add_image
    $ y=250 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 1490 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav")] at main_eff1
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=142 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 1490 ypos y focus_mask True  action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav")] at main_eff2
    $ y+=142
    imagebutton auto "gui/main_quit_%s.png" xpos 1490 ypos y focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav")] at main_eff3
    
screen example: #this screen isn't used. It's just used as an example in the script.
#begin at_atl
    imagebutton auto "gui/main_start_%s.png" xpos 1490 ypos 114 focus_mask True action Start() at main_eff1
#end at_atl

# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 1
        easein 0.4 zoom 2
    transform main_eff2:
        zoom 1
        easein 0.8 zoom 2
    transform main_eff3:
        zoom 1
        easein 1.2 zoom 2
#end main_eff

            
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
        
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    
    $ x1=x+220
    $ y1=y+10
    add FileScreenshot(number) xpos x1 ypos y1
    $ x2=x+10
    $ y2=y+10
    text file_text xpos x2 ypos y2 size 20
    

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
    
screen save:
    tag menu
    
    image "gui/save_tab_on.png" xpos 0.22 ypos 0.1
    imagebutton auto "gui/load_tab_off_%s.png" xpos 0.1 ypos 0.1 focus_mask True action [Hide("save"), Show("load")] hovered [ Play ("test_one", "sfx/click.wav")]
    use save_load_slots
    
    use sound_On
    use fullscreen_Off
    
    imagebutton auto "gui/retour_%s.png" xpos 0.1 ypos 0.8 action Return() hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/menu_%s.png" xpos 0.22 ypos 0.8 action MainMenu() hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/log_%s.png" xpos 0.7 ypos 0.8 action ShowMenu('text_history') hovered [ Play ("test_one", "sfx/click.wav")]
    
screen load:
    tag menu
    
    image "gui/load_tab_on.png" xpos 0.1 ypos 0.1
    imagebutton auto "gui/save_tab_off_%s.png" xpos 0.22 ypos 0.1 focus_mask True action [Hide("load"), Show("save")] hovered [ Play ("test_one", "sfx/click.wav")]
    use save_load_slots
    
    use sound_On
    use fullscreen_Off
    
    imagebutton auto "gui/retour_%s.png" xpos 0.1 ypos 0.8 action Return() hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/menu_%s.png" xpos 0.22 ypos 0.8 action MainMenu() hovered [ Play ("test_one", "sfx/click.wav")]
    imagebutton auto "gui/log_%s.png" xpos 0.7 ypos 0.8 action ShowMenu('text_history') hovered [ Play ("test_one", "sfx/click.wav")]
    
screen save_load_slots:
    $ y=210
    for i in range(0, 3):
        imagebutton auto "gui/fileslot_%s.png" xpos 195 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=195, y=y)
        $ y+=124
    
    $ y=210
    for i in range(3, 6):
        imagebutton auto "gui/fileslot_%s.png" xpos 620 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=620, y=y)
        $ y+=124
    
screen sound_Off: 
    imagebutton auto "gui/sound_off_%s.png" xpos 0.58 ypos 0.22 focus_mask True action [SetMute("music",False), SetMute("sfx",False), SetMute("voice",False), Hide("sound_Off"), Show("sound_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen sound_On: 
    imagebutton auto "gui/sound_on_%s.png" xpos 0.58 ypos 0.22 focus_mask True action [SetMute("music",True), SetMute("sfx",True), SetMute("voice",True), Hide("sound_On"), Show("sound_Off")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen fullscreen_Off:
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 0.58 ypos 0.1 focus_mask True action [Preference('display', 'fullscreen'), Hide("fullscreen_Off"), Show("fullscreen_On")] hovered [ Play ("test_one", "sfx/click.wav")]
    
screen fullscreen_On: 
    imagebutton auto "gui/config_display_window_%s.png" xpos 0.58 ypos 0.1 focus_mask True action [Preference('display', 'window'), Hide("fullscreen_On"), Show("fullscreen_Off")] hovered [ Play ("test_one", "sfx/click.wav")]

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 0.35 ypos 0.8 action yes_action hover_sound "sfx/click.wav"
    imagebutton auto "gui/yesno_no_%s.png" xpos 0.65 ypos 0.8 action no_action hover_sound "sfx/click.wav"
    
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

## ■██▓▒░ CUSTOM MOUSE POINTER ░▒▓██████████████████████████■
##This block is responsible for the custom mouse pointer
# init python:
    # config.mouse = { }
    # config.mouse["default"] = [
         # ("gui/mouse_pointer.png", 8.8, 0.0),
    # ]
# Configuration variables: http://www.renpy.org/doc/html/config.html
# Custom mouse pointer is commented out, to disable it for the time being, because of an issue in all recent versions of Ren'Py.
# PyTom: "There's also an issue where display latency introduced by newer Nvidia drivers makes config.mouse noticeably slow, when Maximum Pre-Rendered Frames is set (which is the default for the driver). As far as I know, this isn't fixable in the short term. For now, I strongly recommend disabling custom mouse cursors (config.mouse)." (Mar 29, 2013) http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=19703&start=45#p259263

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

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
init:
    $ style.say_dialogue.drop_shadow = (2, 2)
    $ style.say_dialogue.drop_shadow_color = "#000000"

## ■██▓▒░ QUICK MENU ░▒▓████████████████████████████████████■
## Screens for the quick menus above the textbox. We use several different quick menus for presentation purposes.

screen menu_button:
    imagebutton auto "gui/ingame_menu_%s.png" action ShowMenu('save') xpos 0.85 ypos 0 focus_mask True

screen ingame_menu:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') focus_mask True at option
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() focus_mask True at home
    imagebutton auto "gui/ingame_menu_%s.png" action [Show('menu_button'), Hide('ingame_menu')] xpos 0.85 ypos 0 focus_mask True
    
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
            
# readback.rpy
# drop in readback module for Ren'Py by delta
# this file is licensed under the terms of the WTFPL
# see http://sam.zoy.org/wtfpl/COPYING for details

# voice_replay function added by backansi from Lemma soft forum.
# required renpy 6.12 or higher.

init -3 python:
    # config.game_menu.insert(1,( "text_history", u"Text History", ui.jumps("text_history_screen"), 'not main_menu'))

    # styles
    style.readback_window.xmaximum = 1400
    style.readback_window.ymaximum = 700
    style.readback_window.align = (.5, .5)
    style.readback_window.background = None

    style.readback_frame.background = "#000000aa"
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5
    
    style.readback_text.color = "#fff"

    style.create("readback_button", "readback_text")
    style.readback_button.background = None
    
    style.create("readback_button_text", "readback_text")
    style.readback_button_text.selected_color = "#f12"
    style.readback_button_text.hover_color = "#f12"
    
    style.readback_label_text.bold = True
    
    # starts adding new config variables
    config.locked = False 
    
    # Configuration Variable for Text History 
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    
    # ends adding new config variables
    config.locked = True
    
init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return
            
    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    
    config.nvl_show_display_say = say_wrapper
    
    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    
    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        if not config.has_voice:
            return
        
        _voice.play = file
        
        store.current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input): 
        
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
                
        rv = renpy.display_menu(newitems, **add_input)
        
        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """

        widget_properties = { }
        dialogue = [ ]
        
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue

            who, what, kwargs = entry

            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
                
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            dialogue.append((who, what, who_id, what_id, window_id))
        
        return widget_properties, dialogue
        
    # Overwriting nvl menu function
    def nvl_menu(items):

        renpy.mode('nvl_menu')
        
        if nvl_list is None:
            store.nvl_list = [ ]

        screen = None
        
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
            
        if screen is not None:

            widget_properties, dialogue = nvl_screen_dialogue()        

            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
                
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
            
        # Traditional version.
        ui.layer("transient")
        ui.clear()
        ui.close()

        ui.window(style=__s(style.nvl_window))
        ui.vbox(style=__s(style.nvl_vbox))

        for i in nvl_list:
            if not i:
                continue

            who, what, kw = i            
            rv = renpy.show_display_say(who, what, **kw)

        renpy.display_menu(items, interact=False,
                           window_style=__s(style.nvl_menu_window),
                           choice_style=__s(style.nvl_menu_choice),
                           choice_chosen_style=__s(style.nvl_menu_choice_chosen),
                           choice_button_style=__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=__s(style.nvl_menu_choice_chosen_button),
                           )

        ui.close()

        roll_forward = renpy.roll_forward_info()

        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)

        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None
    
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)

    # remove text tags from dialogue lines 
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    # keymap overriding to show text_history.
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=(SetVariable("yvalue", 1.0), ShowMenu("text_history"))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher)    
    
init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):

            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)
                
    def store_yvalue(y):
        global yvalue
        yvalue = int(y)

screen text_history:

    #use navigation
    tag menu 
    
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
        
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
        
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
        
    else:
        $ lines_to_show = readback_buffer
    
    
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    
    window:
        style_group "readback"
    
        side "c r":
            
            frame:
                
                has viewport:
                    mousewheel True
                    draggable True
                    yinitial yvalue
                    yadjustment adj

                vbox:
                    null height 10
                    
                    for line in lines_to_show:
                        
                        if line[0] and line[0] != " ":
                            label line[0] # name

                        # if there's no voice just log a dialogue
                        if not line[2]:
                            text line[1]
                            
                        # else, dialogue will be saved as a button of which plays voice when clicked
                        else: 
                            textbutton line[1] action Play("voice", line[2] )
                        
                        null height 10
                
            bar adjustment adj style 'vscrollbar'
        imagebutton auto "gui/retour_%s.png" xpos 0.0 ypos 1.1 focus_mask True action Return() hovered [ Play ("test_one", "sfx/click.wav")]