# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

label start:
    scene bg_path

    # 인트로 텍스트
    centered "Welcome to the Mini Game Collection!"
    centered "First, let's play the find-item game."
    
    # find-item-game.rpy 호출
    call find_item_game_start

    call click_game_start


    centered "Great job! Now, let's move on to the card match game."

    # card-match-game.rpy 호출
    call card_match_game_start

    centered "Well done! You've completed both mini games."
    centered "Thank you for playing!"
    return
