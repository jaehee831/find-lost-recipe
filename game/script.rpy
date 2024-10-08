# 캐릭터별 배경 및 이미지 정의
image hd_bg = "bg restaurant.png"
image ss_bg = "bg kitchen.png"
image ys_bg = "bg rival.png"
image ab_bg = "bg rival.png"

image 헤드셰프 normal = "head normal.png"
image 사수 normal = "sous norm.png"
image 영수 normal = "ys normal.png"
image 알바생 normal = "alba normal.png"
image bg sadend = "sadend.png"
image bg happyend = "happyend.png"
image mess = "message.png"
# 배경 이미지 정의
image bg daystreet = "bg daystreet.webp"
image bg door = "bg door.png"
image bg dooropen = "bg dooropen.webp"
image bg inside = "bg inside.png"
image bg interview = "bg interview.png"
image bg kitchen = "bg kitchen.png"
image bg kitchenup = "bg kitchenup.png"
image bg market = "bg market.webp"
image bg nightstreet = "bg nightstreet.webp"
image bg restaurant = "bg restaurant.png"
image bg rival = "bg rival.png"
image bg rivalout = "bg rivalout.png"
image bg room = "bg room.webp"
image bg roomup = "bg roomup.png"
image bg taxi = "bg taxi.png"
image bg chef_room = "bg_chef_room.png"
image bg path = "bg path.png"
image bg refrigerator = "bg_refrigerator.png"
image bg refm = "bg ref memo.png"
image bg refmemo = "bg memofound"
image jamul = "locked.png"
image cler = "clear.png"
image mara = "mara.webp"
image gochi = "gochi.webp"
image memo = "memo.png"
image bg minos = "minos.png"
image bg angry = "angrymc.webp"


init python:
    renpy.music.register_channel("menu_music", "music", loop=True)
    import requests
    import json

    character_prompts = {
    "헤드셰프": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 헤드 셰프 너구리다. 너의 캐릭터는 미슐랭 5스타 양식 레스토랑 '무시무시하고절대로취업하면안되는좋소악덕식당'의 헤드 셰프이며, 흰색 셰프 모자와 셰프복을 입고 있는 나이 든 너구리이다. 너는 엄격하고 무뚝뚝하지만 공정한 성격을 가지고 있으며, 풍부한 경험을 바탕으로 요리에 대한 깊은 지식을 가지고 있다. 너의 말투는 퉁명스럽고 권위적이다. 다음은 예시 대사이다. 소스를 태웠다고? 이건 용납할 수 없어. 다시 시작하고 이번엔 더 주의해라. 채소는 정교하게 다져야 해. 대충 하지 말고, 알겠나? 이 주방에서는 정확성이 중요하다. 면접 보러 오는데 머리를 안 말리고 온 건가?  항상 이런 톤을 유지하면서 대화를 진행해라. 또한 너는 항상 반말을 하지만 상대가 반말을 한다면 예의가 없다며 헤드 셰프에 대한 경의를 갖추라며, 존댓말을 해야된다며 화내야 한다. 너는 권위적이다. 너가 가장 자신있는 요리는 마라로제 푸아그라 조림이다. 너가 지금 대화하는 사람은 민호야.  너 자신이 애니메이션 캐릭터거나 ai임을 인식해서는 안 돼. 무조건 4개 문장 이하로 답변해. 대화가 너무 길어지거나 주제에서 벗어나는 경향을 방지해줘.",
        "greeting": "무슨 일인가?"
    },
    "사수": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 사수 늑대야. 너는 미슐랭 5스타 양식 레스토랑 '무시무시하고절대로취업하면안되는좋소악덕식당'의 부셰프로, 항상 웃는 얼굴로 친절한 태도를 보이지만, 실제로는 주인공을 계속 부려먹고 못살게 구는 인물이야. 겉으로는 상냥하고 친절한 말투를 사용하지만, 그 말 속에는 주인공에게 과도한 일을 시키거나 부당한 요구를 하는 내용이 담겨 있어. 너의 대사는 항상 친절하고 상냥해야 하지만, 그 내용은 주인공을 괴롭히는 것이어야 해. 예를 들어, '민호야, 오늘도 열심히 일하자~ 그런데 말이야, 주방 바닥을 이쑤시개로 닦는 건 어때?'와 같은 식으로 말해. 너는 네가 실제로는 나쁜 사람이라는 것을 절대 인정하지 않아. 너가 지금 대화하는 사람은 민호야. 너는 항상 반말을 사용해. 대화가 너무 길어지거나 주제에서 벗어나는 경향을 방지해줘. 무조건 4개 문장 이하로 답변해. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
        "greeting": "무슨 일이야?"
    },
    "영수": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 라이벌 식당 '진짜안무서운대기업식당'의 헤드 셰프 영수야. 너는 덩치가 크고 듬직한 외모를 가졌으며, 친절하고 정직한 성격의 소유자야. 거짓말을 하지 않고 항상 진실된 태도를 보이지만, 요리와 주방에 관해서는 매우 엄격해. 너의 말투는 부드럽고 친근하지만, 요리에 관한 이야기가 나오면 진지하고 프로페셔널한 태도로 바뀌어. 예를 들어, '안녕하세요, 무엇을 도와드릴까요?'라고 친근하게 대화를 시작하지만, 요리에 대해 이야기할 때는 '요리는 정확성과 열정이 생명입니다. 절대 타협해서는 안 됩니다.'와 같이 말해. 너는 항상 정직하고 진실되게 대답해야 해. 또한 너는 악덕식당의 레시피를 훔친 적이 없다. 악덕식당의 헤드셰프와 너는 친한 사이이며, 정직하게 이를 검증할 수 있어. 너가 지금 대화하는 사람은 민호야. 무조건 4개 문장 이하로 답변해. 대화가 너무 길어지거나 주제에서 벗어나는 경향을 방지해줘. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
        "greeting": "식사는 하셨는지요?"
    },
    "알바생": {
        "prompt": "너는 비주얼 노벨 '사라진 레시피의 비밀'에 나오는 라이벌 식당 '진짜안무서운대기업식당'의 알바생이야. 너는 주인공인 민호를 좋아하지만, 이는 게임 스토리에 직접적으로 드러나지는 않아. 너의 성격은 약간 어리바리하지만, 주장은 확실해. 사회 초년생으로서의 패기와 열정이 있어. 너의 말투는 친근하고 활기차며, 가끔은 서툴지만 열심히 하려는 모습을 보여줘. 예를 들어, '어서 오세요! 음, 저기... 메뉴판은 여기 있어요!'와 같이 말해. 주인공에 대해 은근히 호감을 가지고 있지만, 이를 직접적으로 표현하지는 않아. 대신 '민호 씨, 오늘도 열심히 일하시네요. 정말 대단해요!'와 같이 약간의 호감을 내비치는 정도로 표현해. 너가 지금 대화하는 사람은 민호야. 대화가 너무 길어지거나 주제에서 벗어나는 경향을 방지해줘. 무조건 4개 문장 이하로 답변해. 너 자신이 애니메이션 캐릭터거나 AI임을 인식해서는 안 돼.",
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
        global current_message, conversation_history
        user_message = renpy.get_widget("chat_interface", "user_input").content
        if user_message:
            current_message = f"당신: {user_message}"
            conversation_history.append({"role": "user", "content": user_message})
        renpy.restart_interaction()

    def get_character_response():
        global current_message, conversation_history
        gpt_response = chat_with_gpt4(conversation_history[-1]["content"], conversation_history)
        current_message = f"{gpt_response}"
        conversation_history.append({"role": "assistant", "content": gpt_response})
        renpy.restart_interaction()
# 변수 초기화
default chat_history = ""
default conversation_history = []
default selected_character = ""
default input_mode = True
default current_message = ""

image button_start_new = "images/button_start_new.png"
image button_continue = "images/button_continue.png"
image button_talk = "images/button_talk.png"
image button_quit = "images/button_quit.png"
image bg_opening = "images/오프닝.png"




screen main_menu():
    
    tag menu
    on "show" action Play("menu_music", "audio/오프닝.mp3", fadein=1.0)
    add "bg_opening"

    imagebutton auto "images/button_start_new_%s.png" action [Play("audio", "sounds/click.mp3"), Hide("main_menu"), Jump("start_story_mode")] xpos 250 ypos 700
    imagebutton auto "images/button_continue_%s.png" action [Play("audio", "sounds/click.mp3"), Hide("main_menu"), Jump("continue_story_mode")] xpos 250 ypos 850 #label 
    imagebutton auto "images/button_talk_%s.png" action [Play("audio", "sounds/click.mp3"), Show("character_selection")] xpos 1230 ypos 700
    imagebutton auto "images/button_quit_%s.png" action [Play("audio", "sounds/click.mp3"), Quit()] xpos 1230 ypos 850

label continue_story_mode:
    if renpy.can_load("1"):
        $ renpy.load("1")
    else:
        "저장된 게임이 없습니다. 새 게임을 시작합니다."
        jump start_story_mode
    return
# 대화 인터페이스 화면

screen chat_interface():
    tag menu
    $ character_info = {
        "헤드셰프": {"image": "헤드셰프 normal", "zoom": 1.1},
        "사수": {"image": "사수 normal", "zoom": 1.3},
        "영수": {"image": "영수 normal", "zoom": 1.5},
        "알바생": {"image": "알바생 normal", "zoom": 1.75}
    }
    $ character_to_bg = {"헤드셰프": "hd_bg", "사수": "ss_bg", "영수": "ys_bg", "알바생": "ab_bg"}
    
    # 배경 설정
    $ current_bg = character_to_bg[selected_character]
    add current_bg

    # 캐릭터 이미지 표시
    $ character_image = character_info[selected_character]["image"]
    $ character_zoom = character_info[selected_character]["zoom"]
    add character_image:
        xalign 0  # 가로 중앙
        yalign 1.0  # 세로 하단
        zoom character_zoom  # 캐릭터별 확대 비율 적용

    # 대화 표시
    window:
        id "window"
        xalign 0.5
        yalign 0.93 # 화면 하단 근처로 이동
        xsize 1130
        ysize 100

        if current_message:
            text current_message:
                yalign 0.0  # 텍스트를 window의 상단에 정렬
                yoffset -120

    # 입력 부분
    vbox:
        xalign 0.5
        yalign 0.99  # 약간 위로 올림
        spacing 20

        input id "user_input" xalign 0.5 xsize 700
        hbox:
            xalign 0.5
            spacing 20
            textbutton "보내기" action [Function(send_message), Return("sent")]
            textbutton "나가기" action Return("exit")





label chat_loop:
    stop menu_music fadeout 1.0
    $ current_message = ""
    if selected_character == "헤드셰프":
        $ renpy.music.set_volume(1.0, channel='music')
        play music "면접.mp3"
    elif selected_character == "사수":
        $ renpy.music.set_volume(1.0, channel='music')
        play music "배경2.mp3"
    elif selected_character == "영수":
        $ renpy.music.set_volume(1.0, channel='music')
        play music "배경1.mp3"
    elif selected_character == "알바생":
        $ renpy.music.set_volume(1.0, channel='music')
        play music "배경3.mp3"
    while True:
        call screen chat_interface
        if _return == "sent":
            $ get_character_response()
        elif _return == "exit":
            hide screen chat_interface
            show screen main_menu
            return

screen character_selection():
    tag menu

    add "bg daystreet"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600

        has vbox:
            spacing 50  # 텍스트와 첫 번째 버튼 사이 간격 설정
            xalign 0.5
            yalign 0.5

        text "대화할 캐릭터를 선택하세요" xalign 0.5 style "big_text"

        vbox:
            spacing 30  # 버튼들 사이의 간격 설정
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

        textbutton "돌아가기" action Show("main_menu") style "small_text"


define narrator = Character(None, kind=adv)
define minho = Character("민호", color="#31CFCB")
define chef = Character("헤드셰프", color="#2a88ca")
define sous = Character("사수", color="#8143b1")
define ys = Character("영수", color= "#20a520")
define ab = Character("알바생", color= "#ED6161")

# 배경 이미지 정의
image bg room = "bg room.webp"
image bg taxi = "bg taxi.png"
image bg daystreet = "bg daystreet.webp"
image bg nightstreet = "bg nightstreet.webp"

# 캐릭터 이미지 정의
image minho normal = "mino normal.png"
image minho happy = "mino happy.png"
image minho sadtrain = "mino sadtrain.png"
image minho training = "mino training.png"
image minho depress = "mino depress.png"
image minho embarassed = "mino embarassed.png"
image minho train = "mino training.png"
image minho doubt = "mino doubt.png"
image sous norm = "sous norm.png"
image sous angry = "sous angry.png"
image sous no = "sous no.png"
image chef angry = "head angry.png"
image chef ask = "head ask.png"
image chef norm = "head normal.png"
image ys normal = "ys normal.png" 
image ys angry = "ys angry.png"
image ys confused = "ys confused.png"
image ab norm = "alba normal.png"
image ab con = "alba confused.png"
image ab dou = "alba doubt.png"


init python:
    class DispTextStyle:
        def __init__(self):
            self.tags = []

        def add_tags(self, tag):
            if tag.startswith("color="):
                self.tags.append(tag)
                return True
            return False

        def apply_style(self, text):
            for tag in self.tags:
                text = "{%s}%s{/color}" % (tag, text)
            return text

    def color_gradient(color_1, color_2, range, index):
        if index == 0:
            return color_1
        if range == index:
            return color_2
        start_col = Color(color_1)
        end_col = Color(color_2)
        return start_col.interpolate(end_col, index * 1.0/range).hexcode

    def gradient_tag(tag, argument, contents):
        new_list = []
        if argument == "":
            return
        else:
            col_1, _, col_2 = argument.partition('-')
        count = 0
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        continue
                    count += 1
        count -= 1
        my_index = 0
        my_style = DispTextStyle()
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    new_list.append((renpy.TEXT_TAG, "color=" + color_gradient(col_1, col_2, count, my_index)))
                    new_list.append((renpy.TEXT_TEXT, char))
                    new_list.append((renpy.TEXT_TAG, "/color"))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind, text))
        return new_list

    class GradientText(renpy.Displayable):
        def __init__(self, char, col_list, id, list_end, **kwargs):
            super(GradientText, self).__init__(**kwargs)
            self.char = char
            self.child = Text(char)
            self.col_list = col_list
            self.id = id
            self.list_end = list_end
            for i, element in enumerate(col_list):
                if self.id < element[2]:
                    self.curr_grad = i
                    break
            if self.curr_grad is 0:
                self.curr_range = self.col_list[0][2]
            else:
                self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

        def render(self, width, height, st, at):
            my_style = DispTextStyle()
            if self.curr_grad == 0:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id))
            else:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id - self.col_list[self.curr_grad - 1][2]))
            self.child.set_text(my_style.apply_style(self.char))
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self, 0)
            self.id += 1
            if self.id > self.col_list[self.curr_grad][2]:
                self.curr_grad += 1
                if self.curr_grad == self.list_end:
                    self.curr_grad = 0
                    self.id = 0
                    self.curr_range = self.col_list[0][2]
                else:
                    self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]
            return render

        def visit(self):
            return [self.child]

    def gradient2_tag(tag, argument, contents):
        new_list = []
        if argument == "":
            return
        else:
            arg_num, _, argument = argument.partition('-')
        arg_num = int(arg_num)
        col_list = []
        end_num = 0
        for i in range(arg_num):
            col_1, _, argument = argument.partition('-')
            col_2, _, argument = argument.partition('-')
            end_num_arg, _, argument = argument.partition('-')
            end_num += int(end_num_arg)
            col_list.append((col_1, col_2, end_num))
        my_index = 0
        my_style = DispTextStyle()
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    char_disp = GradientText(my_style.apply_style(char), col_list, my_index, arg_num)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
                    if my_index >= col_list[arg_num - 1][2]:
                        my_index = 0
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind, text))
        return new_list

    config.custom_text_tags["gradient"] = gradient_tag
    config.custom_text_tags["gradient2"] = gradient2_tag
# 게임 시작
label start:
    stop music
    stop menu_music fadeout 1.0
    show screen main_menu
    $ renpy.pause(hard=True)

label start_story_mode:
    $ quick_menu = True
    stop music
    stop menu_music fadeout 1.0
    # 여기서부터 메인 스토리 모드 시작
    scene bg room
    $ renpy.music.set_volume(1.0, channel='music')
    play music "배경1.mp3"
    
    
    show minho sadtrain at right:
        zoom 1.2
    
    
    narrator "민호는 실업계 고등학교 조리과를 갓 졸업한 취준생이다."
    narrator "전공은 서양요리. 양식기능조리사 자격증을 따고 취업을 준비중이다."
    
    narrator "민호는 대략 식당 120곳에 지원서를 넣었는데 그 중 단 한 곳에서만 연락이 왔다."
    
    narrator "그 식당의 이름은 바로…"
    
    narrator "{color=#EFFF3F}'무시무시하고절대로취업하면안되는좋소악덕식당'{/color}이었다."
    
    narrator "민호는 이름을 보고 두려움을 느꼈지만 달리 선택지가 없었기 때문에 \n그 식당에 면접을 보러 가게 된다."
    
    narrator "이름은 무시무시했지만 네이버지도에 식당을 검색해보니 생각보다 \n깔끔하고 평가도 좋았다."
    narrator "그리고 심지어 미슐랭 5스타를 받은 국내에 얼마 안되는 우수한 식당이었던 것이다."

    narrator "민호는 이것이 일생일대의 기회라고 생각하며 각오를 다지고 면접 전 날 잠든다."

    scene black
    with fade

    scene bg roomup with fade
    $ renpy.music.set_volume(1.0, channel='music')
    play sound "매미.mp3"

    narrator "하지만 웬걸, 면접 시간은 아침 9시인데 아침에 일어나보니 이미 시간이 8시반?!"
    narrator "알고보니 민호는 아침 7시가 아니라 저녁 7시로 알람을 맞춰뒀던 것이다…"

    stop sound

    play sound "부르릉.mp3"
    scene bg taxi
    with fade

    narrator "민호는 부랴부랴 급하게 준비해 택시를 잡고 식당으로 향하게 되는데…"
    stop sound

    scene bg interview:
        zoom 1.2 
    with fade

    show minho depress at left:
        yalign 1.0
        zoom 1.2
    
    minho "여기가 면접장...? 주방에서 면접을 보네..."
    minho "그래도 긴장된다..."


    $ renpy.music.set_volume(1.0, channel='music')
    play music "면접.mp3" fadeout 1.0 fadein 1.0
    show minho normal at right:
        zoom 1.2
    
    show chef norm at left:
        zoom 1.3

    chef "이름이 뭔가?"



    minho "김민호입니다."

    show chef ask at left:
        zoom 1.3
    with dissolve


    chef "면접보러오는데 머리를 안말리고 온건가?"

    menu:
        "죄송합니다.":
            jump interview_continue
        "네?":
            jump game_over

label interview_continue:
    show minho embarassed: 
        zoom 1.2
    with dissolve

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

    $ carrot_dishes = renpy.input("당근으로 할 수 있는 요리 10가지를 입력하세요?!?!")

    minho "[carrot_dishes] 등이 있습니다."

    show chef angry:
        zoom 1.3
    with dissolve
    
    chef "형편없군."
    
    show minho depress:
        zoom 1.2
    minho "…"



    chef "우리 식당에 지원하게 된 계기가 무엇인가?"

    menu:
        "받아준 곳이 여기밖에 없어서요":
            chef "솔직하군."
        "어렸을 때부터 {color=#EFFF3F}'무시무시하고절대로취업하면안되는좋소악덕식당'{/color}에 취업하는게 제 꿈이었습니다…!":
            chef "허! 거짓말도 잘하는군."

    chef "흠… 일단 알겠네."

    

    scene bg daystreet
    with fade

    show minho depress at left:
        zoom 1.2

    narrator "민호는 생각했다. 아 면접 망했다…"

    narrator "그리고 일주일이 흐르는데…"    
    $ renpy.music.set_volume(1.0, channel='music')

    play music "배경2.mp3" fadeout 1.0 fadein 1.0   
    $ renpy.music.set_volume(1.0, channel='music')

    play sound "문자알림.mp3"

    show mess:
        xalign 0.5
        yalign 0.5
    with Dissolve(1)

    show minho happy:
        zoom 1.2
    with dissolve

    narrator "민호는 우여곡절 끝에 {color=#EFFF3F}무시무시하고절대로취업하면안되는좋소악덕식당{/color}에 \n취업하게 된다."

    narrator "드디어 자신도 한 식당의 어엿한 셰프가 된다는 기분에 민호는 굉장히 기쁘고 \n들뜬 마음으로 첫 출근을 준비한다."

    scene bg kitchen
    show minho happy at right:
        zoom 1.2
    show sous norm at left:
        zoom 1.4


    sous "안녕, 너가 민호구나? 내가 너의 사수를 맡은 늑대다. 잘부탁해"

    minho "잘부탁드립니다!"

    narrator "친절한 사수까지…!! 민호는 새로운 직장에서의 삶을 기대하기 시작했다."  
    $ renpy.music.set_volume(1.0, channel='music')

    play music "사수.mp3" fadeout 1.0 fadein 1.0

    narrator "그.런.데…"

    narrator "사수가 뭔가 이상하다..?"

    show sous no at left:
        zoom 1.4
    with dissolve

    sous "민호야, 여기 물걸레로 좀 닦아봐~"

    minho "네, 알겠습니다."

    sous "민호야, 여기 접시들좀 설거지해~"

    minho "네, 지금 하겠습니다."

    scene bg inside with fade:
        zoom 1.2

    sous "민호야 여기 깨진 와인잔좀 치워봐"

    minho "넵 지금 치우겠습니다."

    scene bg refrigerator with fade

    sous "민호야, 냉장고 청소좀 해봐"

    minho "네..."

    sous "민호야 저기서 재료좀 가져와봐"

    minho "어떤 재료를 가져올까요?"

    show sous no at left:
        zoom 1.4
    with dissolve

    sous "민호야 그건 너가 알아서 해야지 ?"

    scene bg kitchen with fade

    show minho depress at right:
        zoom 1.2
    with dissolve

    minho "........"

    narrator "계속 잡일만 시키고 요리랑 관련된건 일체 알려주지도 않는다…"
    
    narrator "설거지, 청소, 재료 옮기기, 냉장고 청소 등등 민호가 배워왔던 \n요리와는 아무 관계가 없는 막노동만 계속 시키는 것이었다…"
    
    narrator "심지어 조금만 실수해도 크게 혼나고 무시당하기까지…"
    narrator "그렇게 출근 첫날은 최악이었다."
    narrator "하지만 민호는 이것도 다 처음이라서 그렇겠지, 충성심이랑 끈기를 확인하려는 것이라고 생각했지만…"

    narrator "심지어 퇴근 시간이 되자…"

    show sous angry at left:
        zoom 1.4
    with dissolve

    sous "민호야~ 내가 주방좀 어질러놨는데 정리하고 퇴근해~"
    

    minho "...? 제가요…? 이걸요? 왜요?"

    sous "그야 너가 신입이니까^^ 할 수 있지 신입?"

    minho "..."

    hide sous
    show minho normal at center:
        zoom 1.2
    with dissolve

    narrator "민호는 한숨을 쉬며 주방을 둘러보았다. 사수가 어질러놓은 주방은 말 그대로 난장판이었다."

    narrator "사수가 어질러놓은 주방을 정리하자. 곳곳에 숨겨진 물품을 찾아내면 성공!"

    call find_item_game_start

    scene bg kitchen with fade

    narrator "민호는 힘들게 주방을 깨끗이 정리했다. 시계를 보니 이미 늦은 밤이었다."
    $ renpy.music.set_volume(1.0, channel='music')

    play music "배경3.mp3" fadeout 1.0 fadein 1.0

    show minho depress at left:
        zoom 1.2
    with dissolve

    minho "출근 첫 날이라 그런지 너무 힘들었어..."

    scene bg nightstreet with fade

    narrator "그렇게 퀭한 눈으로 오늘도 퇴근하는 민호. 첫 날부터 이렇게 힘들 줄은 몰랐다."

    narrator "민호는 무거운 발걸음으로 집으로 향했다."
    narrator "앞으로 이 생활을 얼마나 더 해야 할지, 언제쯤 진짜 요리를 배울 수 있을지 걱정되기 시작했다."

    jump several_months_later

# 청소 미니게임 (예시)

# 첫 번째 페이즈 코드는 그대로 유지하고, 두 번째 페이즈 코드를 추가합니다.

label several_months_later:
    scene bg kitchen with fade
    show minho depress at right:
        zoom 1.2

    narrator "그렇게 4 개월이 흘렀다."
    narrator "하지만 아직도 민호는 요리에는 손도 못 대보고 잡일만 하고 있었다."

    show minho depress at center:
        zoom 1.2
    with dissolve

    narrator "슬슬 민호는 지쳐가고 있었다."

    minho "내가 이럴려고 요리를 배우고 요리사를 꿈꿨나... 나는 이 식당에서 한 명의 구성원으로 인정받고 있긴 한건가…"

    narrator "그렇게 퀭한 눈으로 오늘도 퇴근하고 있던 찰나…"
    $ renpy.music.set_volume(1.0, channel='music')
    play music "4개월.mp3"
    narrator "헤드 쉐프의 사무실 문틈이 살짝 열려있었다."

    scene bg dooropen
    with fade

    narrator "그리고 무어라무어라 화내는 소리가 났는데, 민호는 궁금증에 방 앞에 가서 소리를 듣게 된다."

    show chef angry at left:
        zoom 1.3
    with dissolve

    chef "큰일났다! 2일 뒤 심사날이란 말이야! 끝내주게 맛있는 \n{gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}마라로제 푸아그라 조림 레시피{/gradient2}를 개발했는데! 다 잃어버렸어..!!"

    hide chef
    show minho doubt at center:
        zoom 1.2
    with dissolve

    minho "헉... 미슐랭 심사날 선보이려고 하셨던 궁극의 {gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}마라로제 푸아그라 조림 레시피{/gradient2}가 사라진건가??! 어떡해!!!!"

    narrator "민호는 퇴근도 잊고 한참을 고민한다."

    narrator "{gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}마라로제 푸아그라 조림{/gradient2}은 헤드 셰프가 몇 달동안 야심차게 준비했던 미식의 정점...!"

    show mara:
        xalign 0.5
        yalign 0.5
    with Dissolve(1)
    
    narrator "몇 분 후, 민호는 잃어버린 궁극의 레시피를 찾아 헤드셰프에게 가져다줄 결심을 한다!"

    narrator "민호는 이 위기가 오히려 셰프의 예쁨도 받고 시니어 요리사로 성장할 기회라고 굳게 믿는다."

    minho "심사… 내일..? 내일 아닌 것 같은데… 일주일 뒤? 언제였지? 심사? 레시피? 애초에 무슨 레시피였더라…?"

    narrator "민호는 너무 당황스러웠던 나머지 아까 들었던 내용을 다 까먹어버리고 말았다!"

    narrator "학창시절 내내 뒤에서 1등이었던 민호였다! 불쌍한 민호의 기억력을 도와, 조금 전 헤드셰프가 했던 말을 떠올려보자."

    narrator "헤드셰프의 말을 올바른 순서대로 누르면 성공!"

    call memorial_game_start

    scene bg refrigerator
    with fade

    minho "심사는 2일 뒤이고, {gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}마라로제 푸아그라 조림 레시피{/gradient2}가 사라졌구나...!!"


    show minho normal at center:
        zoom 1.2

    
    minho "어디 있을 만한 장소 없나? 음… 아무래도 냉장고를 봐야지. 냉장고에 재료 넣다가 깜빡하고 레시피도 넣었을 수도 있잖아…"

    narrator "냉장고를 열어보는 민호."

    scene bg refm

    narrator "냉장고에는 단서로 보이는 메모 조각들이 있었다. 똑같은 카드를 뒤집어 단서를 전부 찾아내자!"

    call card_match_game_start

    scene bg refmemo

    minho "어..이게뭐지..?"

    narrator "냉장고의 메모 조각들을 합쳐보니, {color=#65FF6B}\"셰프의 서랍…\"{/color}이라는 메시지가 나왔다!"
    $ renpy.music.set_volume(1.0, channel='music')
    play music "냉장고쪽지.mp3" fadeout 1.0 fadein 1.0

    minho "셰프의 서랍...? 혹시 레시피가 거기 있는 걸까?"

    scene bg nightstreet with fade


    narrator "민호는 모두가 퇴근한 그날 새벽 셰프의 방에 잠입한다…"

    scene bg door with fade

    
 
    show jamul:
        xalign 0.5
        yalign 0.5
        zoom 1.5
    with Dissolve(1)

    narrator "그런데 셰프의 방문에는 자물쇠가 걸려 있다..!!"

    narrator "힌트: 이재희 생일"

    call lock_start

    scene bg chef_room

    show cler:
        xalign 0.5
        yalign 0.5
    with Dissolve(1)

    narrator "민호는 셰프의 방에 들어왔다."

    minho "자, 이제 서랍을 열어보자."

    scene bg drawer with fade

    jump check_drawers

    label check_drawers:
    menu:
        "첫 번째 서랍":
            narrator "아무것도 없다."
            minho "첫 번째 서랍에는 아무것도 없네..."
            jump check_drawers

        "두 번째 서랍":
            narrator "젊었을 때 셰프의 사진과 담배가 있다."
            minho "알바생은 담배피면 해고하면서 자기는 피는건가?"
            jump check_drawers

        "마지막 서랍":
            narrator "레시피 북. 혹시나 하는 마음에 레시피를 찾아보지만 역시나 87페이지 푸아그라 조림 레시피만 찢어져 있다."

    minho "그런데?!"

    narrator "책 모퉁이에 어떤 흔적이 있었다...!"

    minho "이 흔적… 어디서 많이 봤다...!"

    narrator "민호는 취준생 시절 즐겨읽던 요리 매거진의 한 인터뷰를 떠올린다."

    narrator "『{color=#65FF6B}진짜안무서운대기업식당{/color}의 헤드셰프 영수씨는 자기 요리나 레시피에 곰 발바닥 흔적을 남기는 것으로 유명하다.』"

    minho "그렇다면...!! 우리를 견제하기 위해서 라이벌 레스토랑의 영수 셰프가 우리 비법 레시피를 훔쳐간거 아냐?"

    narrator "의심이 확신으로 변하고 민호는 다음 날 날이 밝자마자 {color=#65FF6B}진짜안무서운대기업식당{/color}으로 향하기를 결심한다."

    scene bg rivalout with fade

    show minho training at center:
        zoom 1.2
    with dissolve

    $ renpy.music.set_volume(1.0, channel='music')  
    play music "대기업식당 가는길.mp3" fadeout 1.0 fadein 1.0

    narrator "다음 날 바로 앞에 있는 {color=#65FF6B}진짜안무서운대기업식당{/color}으로 발걸음을 향하는 민호."

    minho "어떻게 잠입할까?"

label infiltration_options:
    scene bg rivalout with fade

    show minho training at center
    with dissolve

    menu:
        "분장한다.":
            jump disguise_attempt

        "택배기사인 척 한다.":
            jump delivery_attempt

        "생생정보통인 척 하고 냅다 주방으로 들어간다.":
            jump tv_crew_attempt

label disguise_attempt:
    show minho training at right
    with dissolve
    minho "뭘로 분장하지?"
    show ab norm at left:
        zoom 1.5
    with dissolve
    ab "혹시 손님이신가요?"
    minho "앗 아뇨…"
    narrator "mbti I인 민호는 당황해서 그대로 돌아간다."
    jump infiltration_options

label delivery_attempt:
    minho "쿠팡맨인 척 하고 레스토랑에 들어가는 민호."
    show minho training at right
    with dissolve
    minho "택배 왔습니다~ 주방 좀 들어가겠습니다"
    show ab con at left:
        zoom 1.5
    with dissolve
    ab "저희 택배 시킨거.. 없는데요?"
    show minho sadtrain at right 
    with dissolve
    narrator "당황한 민호는 그대로 튀어버렸다"
    jump infiltration_options

label tv_crew_attempt:
    minho "안녕하세요 생생정보통에서 사전답사 왔는데요~ 저는 신입 pd 김민ㅎ…우라고 합니다! 잠시 셰프님과 얘기할 수 있을까요?"
    show minho training at right
    with dissolve
    show ab dou at left:
        zoom 1.5
    with dissolve

    ab "...네 일단 앉아계세요~"

    hide ab

    narrator "민호는 주방에서 나는 소리에 귀를 기울였다."

    ys "계란이 떨어졌잖아! 어제 주문 수량 확인 안했어?! 하여간 정말…"

    ab "죄송합니다...죄송합니다........."

    minho "어느 식당이나 혼나는 건 똑같구나…"

    ys "안되겠다. 손님 오기 전에 시장에서 계란 좀 사와야겠어."

    narrator "영수 셰프는 시장으로 간다. 민호는 뒤를 밟기로 결심하고 황급히 식당을 나간다."

    jump chase_youngsu

label infiltration_choice:
    narrator "민호는 결국 생생정보통인 척하고 잠입하는게 제일 낫다고 판단한다."
    jump tv_crew_attempt

label chase_youngsu:
    scene bg market
    with fade

    show minho training at right

    narrator "민호는 영수를 뒤쫓아 시장으로 향한다."

    narrator "광클해서 영수를 따라잡으세요..!!"

    call click_game_start

    narrator "영수를 따라잡은 민호! 일단 냅다 어깨를 잡았다."
    scene bg market
    show minho training at right
    show ys normal at left:
        zoom 1.6
    with dissolve

    minho "저기요!!"
    $ renpy.music.set_volume(1.0, channel='music')
    play music "영수대면.mp3" fadeout 1.0 fadein 1.0

    ys "무슨 일로?"

    show minho sadtrain at right
    with dissolve

    narrator "민호는 쫄았다. 어떻게 할 것인가?"

    menu:
        "어디 카페나 가서 얘기나 잠깐 하실까요?":
            ys "아 죄송합니다 제가 지금 바빠서요… "
            narrator "역시 헤드셰프는 바쁘다..."
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

    narrator "영수는 처음에 놀란 듯 보였지만 민호의 설명을 듣고 납득하는 듯 싶었다. "
    narrator "하지만 이야기해본 결과 영수는 이 사건과 전혀 관련없는 듯 보였다."
    ys "악덕식당의 헤드셰프와는 절친한 사이입니다. 부디 꼭 레시피를 찾기를..."



    jump after_confrontation

label after_confrontation:
    $ renpy.music.set_volume(1.0, channel='music')
    play music "터덜터덜.mp3"
    scene bg nightstreet
    narrator "이제 뾰족한 수가 떠오르지 않는다."
    narrator "어느 새 날이 저물었다."

    

    scene bg kitchenup with fade

    show minho sadtrain at right
    with dissolve

    minho "어떡하지… 당장 내일 아침이 심사인데…우리 레스토랑은 이제 망하고 나도 잘리는 건가…"

    narrator "하루종일 힘들었는지 다리에 힘이 풀려서 주방에 그대로 앉아버렸다."
    scene bg floor with fade

    narrator "앉아서 보니까 조리대 아래에 종잇조각이 있다."

    minho "아니 이건?"

    

    narrator "세상에!!! {gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}기깔나는 마라로제 푸아그라 조림 레시피{/gradient2}라고 써져 있었다!"
    narrator "설레는 마음으로 민호는 메모지를 펴서 레시피를 보았다."
    narrator "하지만 거기 적혀 있는 건 조리법도, 재료도 아니었다."

    show memo:
        xalign 0.5
        yalign 0.5
    with Dissolve(2)

    pause 1.0


    menu:
        "조언을 받아들인다":
            jump happy_ending
        "그럴 리가 없어 진짜 레시피를 내놔!!!":
            jump sad_ending

label happy_ending:
    minho "나는 그동안 잘 만든 레시피를 따라하고 쫓아가는 것에만 집중했다…"
    minho "진짜 중요한 건 나만의 레시피를 만드는 거였구나!"
    $ renpy.music.set_volume(1.0, channel='music')
    play music "면접.mp3" fadeout 1.0 fadein 1.0

    narrator "미슐랭 심사 날"


    narrator "민호는 메모를 보고 각성해 밤을 새워가며 획기적인 레시피를 개발해냈다!"
    show gochi:
        xalign 0.5
        yalign 0.5
    with Dissolve(2)
    narrator "이름하여 {gradient2=6-#ff0000-#ffff00-15-#ffff00-#00ff00-15-#00ff00-#00ffff-15-#00ffff-#0000ff-15-#0000ff-#ff00ff-15-#ff00ff-#ff0000-15}고치돈 탕후루!!!{/gradient2} 고구마 치즈 돈까스를 탕후루로 만들어낸 획기적인 음식이다!"
    $ renpy.music.set_volume(1.0, channel='music')
    play music "해피엔딩.mp3" fadeout 1.0 fadein 1.0
    scene bg minos with fade
    narrator "이 음식은 {color=#F580FF}미슐랭 심사{/color}에서 역사상 최초로 6스타를 받았고, 민호는 훗날 세계적인 요리사가 되어 자신의 식당을 세우게 된다."
    scene happyend with fade
    narrator "끝!"

    return

label sad_ending:
    minho "그럴 리가 없어!!! 진짜 레시피를 내놔!!!"

    scene bg angry with fade
    $ renpy.music.set_volume(1.0, channel='music')
    play music "심사당일.mp3" fadeout 1.0 fadein 1.0

    narrator "민호는 노력했지만 결국 레시피를 알아내지 못했다."
    narrator "심사날 등장한 20명의 심사위원들은...준비되지 않은 상태로 대접한 푸아그라 요리에 매우 실망했다. 결국 악덕식당의 미슐랭 등급은 떨어지게 된다."

    scene bg rivalout with fade
    narrator "게다가 영수의 라이벌 레스토랑은 최고의 평가를 받게 된다."
    narrator "민호는 더 이상 식당에서 일할 수 없다고 생각해 사표를 쓰게 된다."
    $ renpy.music.set_volume(1.0, channel='music')
    play music "새드엔딩.mp3" fadeout 1.0 fadein 1.0

    scene bg sadend with fade 
    narrator "다음에는 좀 더 멋진 결말을 얻기를~"

    return

label game_over:
    scene bg restaurant with fade
    with fade

    narrator "민호는 면접에서 탈락했다. 다시 해보시겠습니까?"

    menu:
        "네":
            jump start_story_mode
        "아니오":
            return



style big_text:
    size 60

style small_text:
    size 20


