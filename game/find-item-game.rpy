image bg_room = "images/bg_room.png"
image bg_path = "images/bg_path.png"
image item1 = im.Scale("images/pot.png", 80, 80)
image item2 = im.Scale("images/fan.png", 110, 110)
image item3 = im.Scale("images/knife.png", 70, 70)
image item4 = im.Scale("images/board.png", 100, 100)
image item5 = im.Scale("images/plate.png", 80, 80)
image item_list_bg = "images/item-list.png"  # item-list 이미지 추가

init python:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    oXY = []
    oN = []
    oLen = 0
    maxLen = 0
    oBg = ""
    oLast = -1
    oTime = 0.0
    oMaxTime = 5.0
    needTimer = False
    oActive = False


    def InitGame(bg, time, *args):
        global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, item_list
        oXY = []
        oN = []
        oLen = 0
        oBg = bg
        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True 
        if oTime > 0.0:
            needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            oXY.append(xy)
            oN.append(obj_name)
            maxLen += 1
            item_list.append(obj_name) 

    def StartGame():
        global oActive, needTimer
        oActive = True
        while (oLen < maxLen) and ((oTime > 0.0) or not needTimer):
            renpy.call_screen("game", _layer="master")
            renpy.pause(0.01)
        if oLen >= maxLen:
            return True
        else:
            return False

    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("game", _layer="master")

    def oClick():
        global oLen, oActive
        if oLast >= 0:
            if oN[oLast]:
                oN[oLast] = ""
                oLen += 1
                renpy.play("sounds/click.mp3", channel="sound")
                item_list[oLast] = "" 
                if oLen >= maxLen:
                    oActive = False
                    return True
        return False

screen game:
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime - .01), If(oTime <= 0.0, true=[Hide("game"), Function(lambda: renpy.return_statement(False))])]
    add oBg
    for i in range(len(oN)):
        if oN[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle oN[i]
                hover oN[i]
                if oActive:
                    action [SetVariable("oLast", i), Function(oClick), If(oLen >= maxLen, [Function(lambda: renpy.return_statement(True))])]
                else:
                    action []

    if oActive and needTimer:
        bar value StaticValue(oTime, oMaxTime):
            align (.5, .001)
            xmaximum 400
            ymaximum 20
            thumb None
            thumb_shadow None

label find_item_game_start:
    window hide
    $ renpy.music.set_volume(1.0, channel='music')
    play music "sounds/find-item.mp3"

    # 아이템 찾기 게임 초기화 및 실행
    show bg_room
    show screen black_textbox("사수가 어질러놓은 주방 물건을 찾아야 해!")
    with dissolve
    pause
    hide screen black_textbox
    $ InitGame("bg_room", 5.0, (400, 267), "item1", (790, 517), "item2", (610, 573), "item3", (1130, 560), "item4", (1640, 560), "item5")
    $ result = StartGame()

    # 결과에 따른 메시지 표시
    if result:
        show screen black_textbox("성공! 사수가 어질러놓은 물건을 모두 찾는데 성공했다.ㅎㅎ")
        $ renpy.pause(1.0, hard=True)
        hide screen black_textbox
        with dissolve
        stop music fadeout 1.0
        return 
    else:
        show screen black_textbox("실패! 다시 도전해보자...")
        $ renpy.pause(1.0, hard=True)
        hide screen black_textbox
        with dissolve
        jump find_item_game_start
