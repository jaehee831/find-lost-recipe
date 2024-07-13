# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image bg_room = "images/bg_room.png"
image figure1 = im.Scale("images/figure1.png", 100, 100)
image figure2 = im.Scale("images/figure2.png", 100, 100)
image figure3 = im.Scale("images/figure3.png", 100, 100)
image figure4 = im.Scale("images/figure4.png", 100, 100)

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:

    # 배경 이미지 표시
    show bg_room

    e "Welcome to the game."
    e "Let's start the item finding mini-game."

    # 아이템 찾기 게임 초기화 및 실행
    $ InitGame("bg_room", 5.0, (735, 300), "figure1", (640, 226), "figure2", (288, 38), "figure3", (115, 260), "figure4")
    $ result = StartGame()
    
    # 결과에 따른 메시지 표시
    if result:
        e "You found all items within the time limit!"
    else:
        e "You did not find all items in time."

    return