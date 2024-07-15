# 이미지 선언
image background = "images/bg_냉장고.png"
image card_back = im.Scale("images/card_back.png", 170, 221)
image card_empty = im.Scale("images/card_empty.png", 170, 221)
image card_A = im.Scale("images/card_A.png", 170, 221)
image card_B = im.Scale("images/card_B.png", 170, 221)
image card_C = im.Scale("images/card_C.png", 170, 221)
#define bgm_music = "audio/잔잔.mp3"

init python:

    # DEFAULT GAME SETTINGS:

    # default card type set
    all_cards = ['A', 'B', 'C']
    # width and height of the field
    ww = 3
    hh = 3
    # how many cards can be opened for 1 turn
    max_c = 2
    # text size in the card for text mode
    card_size = 48
    # time allocated for the passage
    max_time = 25
    # pause before the cards disappear
    wait = 0.5
    # mode of cards with images, not with the text
    img_mode = True

    values_list = []
    temp = []
    # we announce picture cards
    # must be in the format "images/card_*.png"
    # required "card_back.png" and "card_empty.png"
    for fn in renpy.list_files():
        if fn.startswith("images/card_") and fn.endswith(".png"):
            name = fn[12:-4]
            renpy.image("card_" + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))
    # if the picture found > 1,
    # then change the set of card types, but the file names
    if len(temp) > 1:
        all_cards = temp
    else:
        # otherwise turn on the text mode,
        # because the pictures are very small
        img_mode = False

    # the function of initializing the playing field
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh:
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list)
        while len(values_list) < ww * hh:
            values_list.append('empty')

# screen game
screen memo_scr:
    # background image
    add "background"

    # timer
    timer 1.0 action If(memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose")) repeat True
    # field
    grid ww hh:
        align(.5, .5) # in the center
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card_empty"
                    else:
                        text "" size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card_" + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card_back"
                        else:
                            text "#" size card_size
                # pressing the button-card
                action If((card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"])])
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

# the game itself
label memoria_game:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range(0, len(values_list)):
            if values_list[i] == 'empty':
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": True})
            else:
                cards_list.append({"c_number": i, "c_value": values_list[i], "c_chosen": False})
    $ memo_timer = max_time
    # show the game screen
    show screen memo_scr
    # main game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append(cards_list[result]["c_number"])
                $ turned_cards_values.append(cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # prevent opening of extra cards
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause(wait, hard=True)
            python:
                for i in range(0, len(turned_cards_numbers)):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump("memo_game_loop")
                renpy.jump("memo_game_win")
        jump memo_game_loop

# loss
label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    scene background
    show screen black_textbox("저런...다음 기회에!")
    $ renpy.pause(1.0, hard=True)
    hide screen black_textbox
    with dissolve
    jump memoria_game
    
# winnings
label memo_game_win:
    hide screen memo_scr
    $ renpy.pause(0.1, hard=True)
    scene background
    show screen black_textbox("성공! 냉장고의 비밀을 풀었다!")
    $ renpy.pause(1.0, hard=True)
    hide screen black_textbox
    with dissolve
    return

label card_match_game_start:
    $ renpy.music.set_volume(1.0, channel='music')
    play music "sounds/card-match.mp3"

    scene black
    $ max_time = 60
    $ ww, hh = 4, 4

    #play music bgm_music
    call memoria_game
    stop music fadeout 1.0
    return

