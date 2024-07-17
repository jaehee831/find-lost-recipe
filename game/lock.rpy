image lock = "lock.png"

define e = Character(None, kind=nvl)
# lock.rpy 파일

# 숫자 입력 화면 정의
screen number_input:
    # 배경 이미지
    add "lock.png"

    # 사용자 입력 필드와 확인 버튼
    frame:
        align (0.5, 0.5)
        has vbox

        text "비밀번호를 입력하세요"

        input value VariableInputValue("input_value") default "" length 1:
            size 40

        textbutton "Submit" action Return(input_value)

# 숫자 입력 변수 초기화
default input_value = ""
default correct_answer = 7

label lock_start:
    # 반복 입력 처리
    while True:
        # 배경 이미지 설정 및 이전 메시지 삭제
        scene lock
        $ renpy.hide_screen("number_input")
        $ renpy.hide_screen("say")
        $ renpy.restart_interaction()

        # 사용자에게 숫자를 입력하도록 요청
        $ input_value = renpy.call_screen("number_input")

        # 입력된 값이 숫자인지 확인
        $ input_number = int(input_value) if input_value.isdigit() else None

        if input_number == correct_answer:
            e "정답"
            $ renpy.pause(1.0, hard=True)
            return  # 여기서 함수를 종료하고 호출한 곳으로 돌아갑니다.
        else:
            e "오답. 다시 시도하세요."
            $ renpy.pause(1.0, hard=True)
