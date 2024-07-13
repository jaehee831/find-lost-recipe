init python:
    # 셰프의 말을 저장
    correct_sequence = ["큰일났다", "2일 뒤 심사날이란 말이야!", "다 잃어버렸어", "끝내주게 맛있는 파스타 레시피를 개발했는데!"]
    # 모든 카드들의 인덱스와 그에 대응하는 텍스트
    all_cards = [
        ("2일 뒤 심사날이란 말이야!", "1.png"),
        ("일주일 뒤 심사하러 온단 말이야!", "2.png"),
        ("비법 레시피를 잃어버렸다...", "3.png"),
        ("끝내주게 맛있는 파스타 레시피를 개발했는데!", "4.png"),
        ("다 잃어버렸어", "5.png"),
        ("진짜 맛있는 피자 레시피를 개발했단 말야!", "6.png"),
        ("망했다 ㅠㅠ", "7.png"),
        ("큰일났다", "8.png")
    ]
    # 셰프의 말 순서 체크를 위한 변수 초기화
    clicked_sequence = []
    current_index = 0

    # 게임 초기화 함수
    def initialize_game():
        global clicked_sequence, current_index, button_data
        clicked_sequence = []
        current_index = 0
        button_data = all_cards.copy()
        import random
        random.shuffle(button_data)

    # 카드 버튼 클릭 시 호출되는 함수
    def card_click(card_text):
        global clicked_sequence, current_index
        renpy.play("sounds/click.mp3")  # 클릭 시 효과음 재생
        clicked_sequence.append(card_text)
        if len(clicked_sequence) == len(correct_sequence):
            for i in range(len(correct_sequence)):
                if clicked_sequence[i] != correct_sequence[i]:
                    return "fail"
            return "success"
        return None

# 이미지 선언
image kitchen_w_minho = "images/kitchen_w_minho.png"
image card_1 = "images/cards/1.png"
image card_2 = "images/cards/2.png"
image card_3 = "images/cards/3.png"
image card_4 = "images/cards/4.png"
image card_5 = "images/cards/5.png"
image card_6 = "images/cards/6.png"
image card_7 = "images/cards/7.png"
image card_8 = "images/cards/8.png"

# 카드 클릭 화면
screen card_click_screen:
    tag menu
    default button_data = []
    python:
        import random
        if not button_data:
            button_data = all_cards.copy()
            random.shuffle(button_data)

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            # 2행 4열의 그리드로 카드 배치
            for i in range(0, 8, 4):
                hbox:
                    for j in range(4):
                        $ index = i + j
                        $ card_text, card_image = button_data[index]
                        button:
                            add "images/cards/" + card_image
                            at transform:
                                size(170.0, 220.0)
                            action Function(card_click, card_text)

label check_result:
    $ result = "continue"
    if len(clicked_sequence) == len(correct_sequence):
        $ result = card_click(clicked_sequence[-1])
    if result == "success":
        show text "성공! 민호는 셰프의 말을 기억해냈다"
        $ renpy.pause(2)
        return
    elif result == "fail":
        show text "실패! 아쉽지만 다음 기회에"
        $ renpy.pause(2)
        return
    else:
        call screen card_click_screen
        return

label memory_game_start:
    scene kitchen_w_minho
    with dissolve
    $ initialize_game()
    call screen card_click_screen
    return
