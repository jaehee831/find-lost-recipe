# 이미지 정의
image chef_1 = im.Scale("images/words/chef_1.png", 170, 221)
image chef_2 = im.Scale("images/words/chef_2.png", 170, 221)
image chef_3 = im.Scale("images/words/chef_3.png", 170, 221)
image chef_4 = im.Scale("images/words/chef_4.png", 170, 221)
image chef_5 = im.Scale("images/words/chef_5.png", 170, 221)
image chef_6 = im.Scale("images/words/chef_6.png", 170, 221)
image chef_7 = im.Scale("images/words/chef_7.png", 170, 221)
image chef_8 = im.Scale("images/words/chef_8.png", 170, 221)
image bg_chef_room = "bg_chef_room.png"

# 게임 초기화
init python:
    # 카드 이미지 목록
    cards = ["chef_1", "chef_2", "chef_3", "chef_4", "chef_5", "chef_6", "chef_7", "chef_8"]
    
    # 정답 순서
    correct_order = ["chef_1", "chef_2", "chef_3", "chef_4"]
    
    # 선택된 카드를 저장할 리스트
    selected_cards = []
    
    # 카드 선택 함수
    def select_card(card):

        global selected_cards
        renpy.play("sounds/click.mp3")
        selected_cards.append(card)
        
        if len(selected_cards) == 4:
            if selected_cards == correct_order:
                renpy.show_screen("result", message="정답")
                return "correct"
            else:
                renpy.show_screen("result", message="오답")
                return "incorrect"
        return False

# 게임 시작 레이블
label memorial_game_start:
    $ renpy.music.set_volume(1.0, channel='music')
    play music "sounds/memorial.mp3"
    $ selected_cards = []
    $ renpy.random.shuffle(cards)
    
    scene bg_chef_room
    
    show screen game_screen
    
    # 게임 루프
    while True:
        $ result = ui.interact()
        if result == "correct":
            hide screen result
            hide screen game_screen
            show black
            centered "야호! 셰프의 말을 기억해냈다!" with dissolve
            stop music fadeout 1.0
            pause 2
            return
        elif result == "incorrect":
            hide screen result
            hide screen game_screen
            show black
            centered "앗 내 아이큐..." with dissolve
            pause 2
            hide black
            show screen game_screen
            jump memorial_game_start
    
    return

# 게임 화면
screen game_screen():
    grid 4 2:
        xalign 0.5
        yalign 0.5
        spacing 20
        for card in cards:
            imagebutton:
                idle card
                action Function(select_card, card)

# 결과 화면
screen result(message):
    frame:
        xalign 0.5
        yalign 0.5
        text message
