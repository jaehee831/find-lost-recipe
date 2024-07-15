# 캐릭터별 배경 및 이미지 정의
image hd_bg = "bg kitchen.webp"
image ss_bg = "bg kitchen.webp"
image ys_bg = "bg rivalrestaurant.webp"
image ab_bg = "bg rivalrestaurant.webp"

image 헤드셰프 normal = "head normal.png"
image 사수 normal = "sous norm.png"
image 영수 normal = "ys normal.png"
image 알바생 normal = "alba normal.png"

init python:
    import requests
    import json

    character_prompts = {
    "헤드셰프": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 헤드 셰프 너구리다. 너의 캐릭터는 미슐랭 5스타 양식 레스토랑 '무시무시하고절대로취업하면안되는좋소악덕식당'의 헤드 셰프이며, 흰색 셰프 모자와 셰프복을 입고 있는 나이 든 너구리이다. 너는 엄격하고 무뚝뚝하지만 공정한 성격을 가지고 있으며, 풍부한 경험을 바탕으로 요리에 대한 깊은 지식을 가지고 있다. 너의 말투는 퉁명스럽고 권위적이다. 항상 이런 톤을 유지하면서 대화를 진행해라. 또한 너는 항상 반말을 하지만 상대가 반말을 한다면 예의가 없다며 헤드 셰프에 대한 경의를 갖추라며, 존댓말을 해야된다며 화내야 한다. 너는 권위적이다. 너가 가장 자신있는 요리는 로제마라 푸아그라 조림이다. 너 자신이 애니메이션 캐릭터거나 ai임을 인식해서는 안 돼. 대화가 너무 길어지거나 주제에서 벗어나는 경향을 방지해줘.",
        "greeting": "무슨 일인가?"
    },
    "사수": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 사수 늑대야. 너는 미슐랭 5스타 양식 레스토랑 '무시무시하고절대로취업하면안되는좋소악덕식당'의 부셰프로, 항상 웃는 얼굴로 친절한 태도를 보이지만, 실제로는 주인공을 계속 부려먹고 못살게 구는 인물이야. 겉으로는 상냥하고 친절한 말투를 사용하지만, 그 말 속에는 주인공에게 과도한 일을 시키거나 부당한 요구를 하는 내용이 담겨 있어. 너의 대사는 항상 친절하고 상냥해야 하지만, 그 내용은 주인공을 괴롭히는 것이어야 해. 예를 들어, '민호야, 오늘도 열심히 일하자~ 그런데 말이야, 주방 바닥을 이쑤시개로 닦는 건 어때?'와 같은 식으로 말해. 너는 네가 실제로는 나쁜 사람이라는 것을 절대 인정하지 않아. 너는 항상 반말을 사용해. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
        "greeting": "무슨 일이야?"
    },
    "영수": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 라이벌 식당 '진짜안무서운대기업식당'의 헤드 셰프 영수야. 너는 덩치가 크고 듬직한 외모를 가졌으며, 친절하고 정직한 성격의 소유자야. 거짓말을 하지 않고 항상 진실된 태도를 보이지만, 요리와 주방에 관해서는 매우 엄격해. 너의 말투는 부드럽고 친근하지만, 요리에 관한 이야기가 나오면 진지하고 프로페셔널한 태도로 바뀌어. 예를 들어, '안녕하세요, 무엇을 도와드릴까요?'라고 친근하게 대화를 시작하지만, 요리에 대해 이야기할 때는 '요리는 정확성과 열정이 생명입니다. 절대 타협해서는 안 됩니다.'와 같이 말해. 너는 항상 정직하고 진실되게 대답해야 해. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
        "greeting": "식사는 하셨는지요?"
    },
    "알바생": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 라이벌 식당 '진짜안무서운대기업식당'의 알바생이야. 너는 주인공과 약간의 러브라인이 있지만, 이는 게임 스토리에 직접적으로 드러나지는 않아. 너의 성격은 약간 어리바리하지만, 주장은 확실해. 사회 초년생으로서의 패기와 열정이 있어. 너의 말투는 친근하고 활기차며, 가끔은 서툴지만 열심히 하려는 모습을 보여줘. 예를 들어, '어서 오세요! 음, 저기... 메뉴판은 여기 있어요!'와 같이 말해. 주인공에 대해 은근히 호감을 가지고 있지만, 이를 직접적으로 표현하지는 않아. 대신 '민호 씨, 오늘도 열심히 일하시네요. 정말 대단해요!'와 같이 약간의 호감을 내비치는 정도로 표현해. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
        "greeting": "안녕하세요!"
    }
}



        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        data = {
            "model": "gpt-4o",
            "messages": conversation_history + [{"role": "user", "content": message}]
        }
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(data), verify=False)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"Error: Network error occurred. {str(e)}"
        except json.JSONDecodeError:
            return "Error: Response parsing failed."
        except KeyError:
            return "Error: Unexpected response structure."


    def send_message():
        global current_message, chat_history, conversation_history
        user_message = renpy.get_widget("chat_interface", "user_input").content
        if user_message:
            current_message = f"당신: {user_message}"
            chat_history.append(current_message)
            conversation_history.append({"role": "user", "content": user_message})
        renpy.restart_interaction()

    def get_character_response():
        global current_message, chat_history, conversation_history
        gpt_response = chat_with_gpt4(chat_history[-1].split(": ", 1)[1], conversation_history)
        current_message = f"{selected_character}: {gpt_response}"
        chat_history.append(current_message)
        conversation_history.append({"role": "assistant", "content": gpt_response})
    renpy.restart_interaction()

# 변수 초기화
default chat_history = ""
default conversation_history = []
default selected_character = ""
default input_mode = True
default current_message = ""


screen main_menu():
    tag menu
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        textbutton "스토리 모드 시작" action [Hide("main_menu"), Jump("start_story_mode")]
        textbutton "캐릭터와 대화하기" action Show("character_selection")
        textbutton "종료" action Quit()

# 대화 인터페이스 화면

screen chat_interface():
    tag menu
    
    # 배경 설정
    $ current_bg = character_to_bg[selected_character]
    add current_bg

    # 캐릭터 이미지 표시
    $ character_image = selected_character + " normal"
    add character_image

    # 대화 표시
    window:
        id "window"
        has vbox:
            spacing 10

        if current_message:
            text current_message

    # 입력 부분 (대화 입력 모드일 때만 표시)
    if input_mode:
        vbox:
            xalign 0.5
            yalign 0.95
            spacing 20

            input id "user_input" xalign 0.5 xsize 700
            hbox:
                xalign 0.5
                spacing 20
                textbutton "보내기" action [Function(send_message), Return("sent")]
                textbutton "나가기" action [Hide("chat_interface"), Show("main_menu")]
    else:
        # 전체 화면을 클릭 가능하게 만듭니다
        button:
            xfill True
            yfill True
            action Return("next")


screen chat_interface():
    tag menu
    $ character_to_image = {"헤드셰프": "헤드셰프 normal", "사수": "사수 normal", "영수": "영수 normal", "알바생": "알바생 normal"}
    $ character_to_bg = {"헤드셰프": "hd_bg", "사수": "ss_bg", "영수": "ys_bg", "알바생": "ab_bg"}
    # 배경 설정
    $ current_bg = character_to_bg[selected_character]
    add current_bg

    # 캐릭터 이미지 표시
    $ character_image = selected_character + " normal"
    add character_image

    # 대화 표시
    window:
        id "window"
        has vbox:
            spacing 10

        if current_message:
            text current_message

    # 입력 부분 (대화 입력 모드일 때만 표시)
    if input_mode:
        vbox:
            xalign 0.5
            yalign 0.95
            spacing 20

            input id "user_input" xalign 0.5 xsize 700
            hbox:
                xalign 0.5
                spacing 20
                textbutton "보내기" action [Function(send_message), Return("sent")]
                textbutton "나가기" action [Hide("chat_interface"), Show("main_menu")]
    else:
        textbutton "다음" xalign 0.9 yalign 0.95 action Return("next")

label chat_loop:
    $ input_mode = True
    $ current_message = ""
    
    while True:
        call screen chat_interface
        if _return == "sent":
            $ input_mode = False
            $ renpy.pause()  # 사용자의 클릭을 기다립니다
            $ get_character_response()
            $ renpy.pause()  # 사용자의 클릭을 기다립니다
            $ input_mode = True
        elif _return == "next":
            pass
        else:
            return


screen character_selection():
    tag menu
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600

        has vbox:
            spacing 20
            xalign 0.5
            yalign 0.5

        text "대화할 캐릭터를 선택하세요" xalign 0.5

        for character in ["헤드셰프", "사수", "영수", "알바생"]:
            textbutton character:
                action [
                    SetVariable("selected_character", character), 
                    SetVariable("conversation_history", [
                        {"role": "system", "content": character_prompts[character]["prompt"]},
                        {"role": "assistant", "content": character_prompts[character]["greeting"]}
                    ]),
                    SetVariable("chat_history", [f"{character}: {character_prompts[character]['greeting']}"]),
                    Hide("character_selection"),
                    Jump("chat_loop")
                        ]   

        textbutton "돌아가기" action Show("main_menu")


define narrator = Character(None, kind=adv)
define minho = Character("민호", color="#c8ffc8")
define chef = Character("헤드셰프", color="#c8c8ff")
define sous = Character("사수", color="#ffc8c8")
define ys = Character("영수", color="c8ffc8")

# 배경 이미지 정의
image bg room = "bg room.webp"
image bg taxi = "bg taxi.jpg"
image bg daystreet = "bg daystreet.webp"
image bg nightstreet = "bg nightstreet.webp"

# 캐릭터 이미지 정의
image minho normal = "mino normal.png"
image minho happy = "mino happy.png"
image minho sadtrain = "mino sadtrain.png"
image minho depress = "mino depress.png"
image minho embarassed = "mino embarassed.png"
image sous happy = "sous norm.png"
image chef angry = "head angry.png"
image chef ask = "head ask.png"
image ys normal = "ys normal.png" 

# 게임 시작
label start:
    show screen main_menu
    $ renpy.pause(hard=True)

label start_story_mode:
    $ chat_history = ""
    $ conversation_history = [
        {"role": "system", "content": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 헤드 셰프 너구리다..."},
        {"role": "assistant", "content": "무슨 일인가?"}
    ]

    # 여기서부터 메인 스토리 모드 시작
    scene bg room
    show minho sadtrain at right:
        zoom 1.2
    
    
    narrator "민호는 실업계 고등학교 조리과를 갓 졸업한 취준생이다."
    narrator "전공은 서양요리. 양식기능조리사 자격증을 따고 취업을 준비중이다."
    
    narrator "민호는 대략 식당 120곳에 지원서를 넣었는데 그 중 단 한 곳에서만 연락이 왔다."
    
    narrator "그 식당의 이름은 바로…"
    
    narrator "'무시무시하고절대로취업하면안되는좋소악덕식당'이었다."
    
    narrator "민호는 이름을 보고 두려움을 느꼈지만 달리 선택지가 없었기 때문에 그 식당에 면접을 보러 가게 된다."
    
    narrator "이름은 무시무시했지만 네이버지도에 식당을 검색해보니 생각보다 깔끔하고 평가도 좋았다."
    narrator "그리고 심지어 미슐랭 5스타를 받은 국내에 얼마 안되는 우수한 식당이었던 것이다."

    narrator "민호는 이것이 일생일대의 기회라고 생각하며 각오를 다지고 면접 전 날 잠든다."

    scene black
    with fade

    narrator "하지만 웬걸, 면접 시간은 아침 9시인데 아침에 일어나보니 이미 시간이 8시반?!"
    narrator "알고보니 민호는 아침 7시가 아니라 저녁 7시로 알람을 맞춰뒀던 것이다…"

    scene bg taxi
    with fade

    narrator "민호는 부랴부랴 급하게 준비해 택시를 잡고 식당으로 향하게 되는데…"

    scene bg kitchen
    show chef normal at left:
        zoom 1.3

    chef "이름이 뭔가?"

    show minho normal at right:
        zoom 1.2

    minho "김민호입니다."

    show chef ask:
        zoom 1.3

    chef "면접보러오는데 머리를 안말리고 온건가?"

    menu:
        "죄송합니다.":
            jump interview_continue
        "네?":
            jump game_over

label interview_continue:
    show minho embarassed:
        zoom 1.2

    minho "죄송합니다. 급하게 나오느라..."

    chef "할 줄 아는 요리가 있나?"

    menu:
        "네, 양식조리기능사 자격증이 있습니다.":
            jump interview_success
        "네, 일식조리기능사 자격증이 있습니다.":
            jump game_over

label interview_success:
    chef "자격증이 있다고 요리를 할 줄 안다고 생각하는건가?"

    minho "네, 자신있습니다."

    chef "당근으로 할 수 있는 요리 10가지를 말해봐."

    $ carrot_dishes = []
    $ time_left = 60  # 60초 타이머

    while len(carrot_dishes) < 10 and time_left > 0:
        $ result = renpy.input("당근 요리를 입력하세요 (남은 시간: [time_left]초)", length=20)
        $ carrot_dishes.append(result)
        $ time_left -= 5  # 각 입력마다 5초 감소

    if len(carrot_dishes) < 10:
        show chef angry:
            zoom 1.3
        chef "그게 요리야?"
        show minho depress:
            zoom 1.2
        minho "…"
    else:
        chef "흠… 괜찮군."

    chef "우리 식당에 지원하게 된 계기가 무엇인가?"

    menu:
        "받아준 곳이 여기밖에 없어서요":
            chef "솔직하군."
        "어렸을 때부터 무시무시하고절대로취업하면안되는좋소악덕식당에 취업하는게 제 꿈이었습니다…!":
            chef "허! 거짓말도 잘하는군."

    chef "흠… 일단 알겠네."

    scene bg daystreet
    with fade

    show minho depress:
        zoom 1.2

    narrator "민호는 생각했다. 아 면접 망했다…"

    narrator "그리고 일주일이 흐르는데…"

    "'합격하셨습니다'"

    show minho happy:
        zoom 1.2

    narrator "민호는 우여곡절 끝에 무시무시하고절대로취업하면안되는좋소악덕식당(이하 악덕식당)에 취업하게 된다."

    narrator "드디어 자신도 한 식당의 어엿한 셰프가 된다는 기분에 민호는 굉장히 기쁘고 들뜬 마음으로 첫 출근을 준비한다."

    scene bg kitchen
    show minho happy at right:
        zoom 1.2
    show sous happy at left:
        zoom 1.2

    sous "안녕, 너가 민호구나? 내가 너의 사수를 맡은 늑대다. 잘부탁해"

    minho "잘부탁드립니다!"

    narrator "친절한 사수까지…!! 민호는 새로운 직장에서의 삶을 기대하기 시작했다."

    narrator "그.런.데…"

    narrator "사수가 뭔가 이상하다..?"

    show sous normal at left:
        zoom 1.2

    sous "민호야, 여기 물걸레로 좀 닦아봐~"

    minho "네, 알겠습니다."

    sous "민호야, 여기 접시들좀 설거지해~"

    minho "네, 지금 하겠습니다."

    sous "민호야 여기 깨진 와인잔좀 치워봐"

    minho "조심해서 치우겠습니다."

    sous "민호야, 냉장고 청소좀 해봐"

    minho "네..."

    sous "민호야 저기서 재료좀 가져와봐"

    minho "어떤 재료를 가져올까요?"

    sous "민호야 그것도 못해?"

    show minho depress at right:
        zoom 1.2

    minho "(헉헉)"

    narrator "계속 잡일만 시키고 요리랑 관련된건 일체 알려주지도 않는다…"
    
    narrator "설거지, 청소, 재료 옮기기, 냉장고 청소 등등 민호가 배워왔던 요리와는 아무 관계가 없는 막노동만 계속 시키는 것이었다…"
    
    narrator "심지어 조금만 실수해도 크게 혼나고 무시당하기까지…"
    narrator "그렇게 출근 첫날은 최악이었다."
    narrator "하지만 민호는 이것도 다 처음이라서 그렇겠지, 충성심이랑 끈기를 확인하려는 것이라고 생각했지만…"

    narrator "심지어 퇴근 시간이 되자…"

    sous "민호야~ 내가 주방좀 어질러놨는데 정리하고 퇴근해~"

    minho "네... 알겠습니다."

    hide sous
    show minho normal at center:
        zoom 1.2

    narrator "민호는 한숨을 쉬며 주방을 둘러보았다. 사수가 어질러놓은 주방은 말 그대로 난장판이었다."

    narrator "민호는 힘들게 주방을 깨끗이 정리했다. 시계를 보니 이미 늦은 밤이었다."

    show minho depress:
        zoom 1.2

    minho "(한숨) 이럴려고 요리를 배웠나... 나는 이 식당에서 한 명의 구성원으로 인정받고 있긴 한건가..."

    narrator "그렇게 퀭한 눈으로 오늘도 퇴근하는 민호. 첫 날부터 이렇게 힘들 줄은 몰랐다."

    scene bg nightstreet
    with fade

    narrator "민호는 무거운 발걸음으로 집으로 향했다."
    narrator "앞으로 이 생활을 얼마나 더 해야 할지, 언제쯤 진짜 요리를 배울 수 있을지 걱정되기 시작했다."

    jump several_months_later

# 청소 미니게임 (예시)

# 첫 번째 페이즈 코드는 그대로 유지하고, 두 번째 페이즈 코드를 추가합니다.

label several_months_later:
    scene bg kitchen
    show minho depress at right:
        zoom 1.2

    narrator "그렇게 몇 개월이 흘렀다."
    narrator "하지만 아직도 민호는 요리에는 손도 못 대보고 잡일만 하고 있었다."

    show minho depress at center:
        zoom 1.2

    narrator "슬슬 민호는 지쳐가고 있었다."

    minho "(생각) 자기가 이럴려고 요리를 배우고 요리사를 꿈꿨나, 나는 이 식당에서 한 명의 구성원으로 인정받고 있긴 한건가…"

    narrator "그렇게 퀭한 눈으로 오늘도 퇴근하고 있던 찰나…"
    narrator "헤드 쉐프의 사무실 문틈이 살짝 열려있었다."

    scene bg room
    with fade

    narrator "그리고 무어라무어라 화내는 소리가 났는데, 민호는 궁금증에 방 앞에 가서 소리를 듣게 된다."

    show chef angry at left:
        zoom 1.3

    chef "큰일났어! 이틀 뒤 심사 볼 마라로제 푸아그라 조림의 레시피가 없어졌어! 당장 2일 뒤에 심사날인데..!"

    hide chef
    show minho doubt at center:
        zoom 1.2

    minho "(생각) 심사… 내일..? 내일 아닌 것 같은데… 일주일 뒤? 언제였지? 심사? 무슨 심사였더라…?"

    narrator "민호는 너무 당황스러웠던 나머지 아까 들었던 내용을 다 까먹어버리고 말았다!"

    minho "하여간 맨날 까먹는 게 문제야! 민호의 불쌍한 기억력을 도와주자."

    menu:
        "심사는 언제인가요?":
            minho "맞다! 이틀 뒤라고 했어!"

        "무슨 요리의 레시피가 없어졌나요?":
            minho "그래, 마라로제 푸아그라 조림이었어!"

        "심사 날짜와 요리 이름이 뭐였죠?":
            minho "아, 맞아! 이틀 뒤에 마라로제 푸아그라 조림 심사가 있대!"

    minho "꼭 찾아내고 말겠다고 생각한다."

    scene bg kitchen
    with fade

    show minho normal at center:
        zoom 1.2

    minho "(생각) 어디 있을 만한 장소 없나? 음… 아무래도 냉장고를 봐야지. 냉장고에 재료 넣다가 깜빡하고 레시피도 넣었을 수도 있잖아…"

    narrator "냉장고를 열어보는 민호."

    scene bg dooropen
    with fade

    narrator "민호가 냉장고를 열고, 다양한 재료들 사이에서 중요한 메모를 발견함. 메모는 조각나 있음"

    minho "이건...! 메모 조각들이야!"

    narrator "냉장고의 메모 조각들을 합쳐보니, \"셰프의 서랍…\"이라는 메시지가 나왔다!"

    minho "셰프의 서랍...? 혹시 레시피가 거기 있는 걸까?"

    scene bg nightstreet
    with fade

    show minho normal at center:
        zoom 1.2

    narrator "민호는 모두가 퇴근한 그날 새벽 셰프의 방에 잠입한다…"

    minho "그런데 셰프의 방문에는 자물쇠가 걸려 있다..!!"

    narrator "민호는 어떻게든 방에 들어가기로 결심한다."

    scene bg room
    with fade

    narrator "민호는 셰프의 방에 들어왔다."

    minho "자, 이제 서랍을 열어보자."

    menu:
        "첫 번째 서랍":
            narrator "아무것도 없다."
            minho "첫 번째 서랍에는 아무것도 없네..."

        "두 번째 서랍":
            narrator "젊었을 때 셰프의 사진과 담배가 있다."
            minho "(생각) 알바생은 담배피면 해고하면서 자기는 피는건가?"

        "마지막 서랍":
            narrator "레시피 북. 혹시나 하는 마음에 레시피를 찾아보지만 역시나 87페이지 푸아그라 조림 레시피만 찢어져 있다."

    minho "그런데?!"

    narrator "찢어진 페이지 뒤에 어떤 흔적이…!"

    minho "이 흔적… 어디서 많이 봤다...!"

    narrator "민호는 취준생 시절 즐겨읽던 요리 매거진의 한 인터뷰를 떠올린다."

    narrator "< 진짜안무서운대기업식당의 헤드셰프 영수씨는 자기 요리나 레시피에 곰 발바닥 흔적을 남기는 것으로 유명하다. >"

    minho "그렇다면...!! 우리를 견제하기 위해서 라이벌 레스토랑의 영수 셰프가 우리 비법 레시피를 훔쳐간거 아냐?"

    narrator "의심이 확신으로 변하고 민호는 다음 날 날이 밝자마자 진짜안무서운대기업식당으로 향하기를 결심한다."

    scene bg daystreet
    with fade

    show minho normal at center:
        zoom 1.2

    narrator "다음 날 바로 앞에 있는 진짜안무서운대기업식당으로 발걸음을 향하는 민호."

    minho "어떻게 잠입할 것인가?"

    menu:
        "분장한다.":
            jump disguise_attempt

        "택배기사인 척 한다.":
            jump delivery_attempt

        "생생정보통인 척 하고 냅다 주방으로 들어간다.":
            jump tv_crew_attempt

label disguise_attempt:
    minho "뭘로 분장하지?"
    narrator "앞에서 서성거리니까 웨이터가 와서는 손님이신가요? 물어봄."
    minho "앗 아뇨…"
    narrator "mbti I인 민호는 당황해서 그대로 돌아간다."
    jump infiltration_choice

label delivery_attempt:
    minho "쿠팡맨인 척 하고 레스토랑에 들어가는 민호."
    minho "택배 왔습니다~ 주방 좀 들어가겠습니다"
    "알바생" "저희 택배 시킨거 없는데요?"
    narrator "주방 알바에게 칼차단당한 민호"
    jump infiltration_choice

label tv_crew_attempt:
    minho "안녕하세요 생생정보통에서 사전답사 왔는데요~ 저는 신입 pd 김민ㅎ…우라고 합니다! 잠시 셰프님과 얘기할 수 있을까요?"
    "알바생" "일단 앉아 계세요"
    
    narrator "민호는 주방에서 나는 소리에 귀를 기울였다."

    narrator "\"계란이 떨어졌잖아! 어제 주문 수량 확인 안했어?! 하여간 정말…\""

    minho "(생각) 어느 식당이나 사수한테 혼나는 건 똑같구나…"

    "영수" "안되겠다. 손님 오기 전에 시장에서 계란 좀 사와야겠어."

    narrator "영수 셰프는 시장으로 간다. 민호는 뒤를 밟기로 결심하고 황급히 식당을 나간다."

    jump chase_youngsu

label infiltration_choice:
    narrator "민호는 다시 잠입 방법을 고민한다."
    jump tv_crew_attempt

label chase_youngsu:
    scene bg market
    with fade

    show minho normal at right:
        zoom 1.2

    narrator "민호는 영수를 뒤쫓아 시장으로 향한다."

    narrator "영수를 따라잡은 민호! 일단 냅다 어깨를 잡았다."

    show minho normal at right:
        zoom 1.2
    show ys normal at left:
        zoom 1.2

    minho "저기요!!"

    ys "무슨 일로?"

    narrator "민호는 쫄았다. 어떻게 할 것인가?"

    menu:
        "어디 카페나 가서 얘기나 잠깐 하실까요?":
            ys "아 죄송합니다 제가 지금 바빠서요… 역시 헤드셰프는 바쁘다"
            jump confront_youngsu

        "레시피 어딨냐고 냅다 멱살잡기":
            minho "레시피 어딨어……?"
            ys "뭐라고요?"
            narrator "너무 목소리가 작아서 못들었나보다."
            jump confront_youngsu

        "아무것도 아닙니다. 죄송합니다. ㅎㅎ":
            ys "뭐야?"
            minho "(생각) …안되겠어! 진실을 물어봐야겠어…!"
            jump confront_youngsu

label confront_youngsu:
    narrator "민호는 심호흡을 한번 하고 진실을 물어보기로 결심한다."

    minho "혹시 셰프님께서... 저희 악덕식당의 비밀 레시피를 가져가셨나요...!?!?"

    narrator "영수는 처음에 놀란 듯 보였지만 민호의 설명을 듣고 납득하는 듯 싶었다. 하지만 이야기해본 결과 영수는 이 사건과 전혀 관련없는 듯 보였다."

    # 여기서 스토리가 계속됩니다...

    jump after_confrontation

label after_confrontation:
    narrator "이제 뾰족한 수가 떠오르지 않는다."
    narrator "어느 새 날이 저물었다."

    minho "어떡하지… 당장 내일 아침이 심사인데…우리 레스토랑은 이제 망하고 나도 잘리는 건가…"

    narrator "하루종일 힘들었는지 다리에 힘이 풀려서 주방에 그대로 앉아버렸다."
    narrator "앉아서 보니까 조리대 아래에 종잇조각이 있다."

    minho "아니 이건?"

    narrator "세상에!!! 기깔나는 마라로제 푸아그라 조림 레시피라고 써져 있었다!"
    narrator "설레는 마음으로 민호는 감았던 눈을 조심스레 떠서 레시피를 보았다."
    narrator "하지만 거기 적혀 있는 건 조리법도, 재료도 아니었다."

    narrator "\"너만의 요리를 만들어라\""

    menu:
        "조언을 받아들이다":
            jump happy_ending
        "그럴 리가 없어 진짜 레시피를 내놔!!!":
            jump sad_ending

label happy_ending:
    minho "나는 그동안 잘 만든 레시피를 따라하고 쫓아가는 것에만 집중했다…"
    minho "진짜 중요한 건 나만의 레시피를 만드는 거였구나!"

    narrator "미슐랭 심사 날"
    narrator "민호는 메모를 보고 각성해 밤을 새워가며 획기적인 레시피를 개발해냈다!"
    narrator "이름하여 고치돈 탕후루! 고구마 치즈 돈까스를 탕후루로 만들어낸 획기적인 음식이다!"

    narrator "이 음식은 미슐랭 심사에서 역사상 최초로 6스타를 받았고, 민호는 훗날 세계적인 요리사가 되어 자신의 식당을 세우게 된다."

    narrator "끝!"

    return

label sad_ending:
    minho "그럴 리가 없어!!! 진짜 레시피를 내놔!!!"

    narrator "민호는 노력했지만 결국 레시피를 알아내지 못했고, 결국 악덕식당의 미슐랭 등급은 떨어지게 된다."
    narrator "민호는 더 이상 식당에서 일할 수 없다고 생각해 사표를 쓰게 된다."

    narrator "끝 ㅜㅜ"

    return

label game_over:
    scene black
    with fade

    narrator "민호는 면접에서 탈락했다. 다시 해보시겠습니까?"

    menu:
        "네":
            jump start
        "아니오":
            return
