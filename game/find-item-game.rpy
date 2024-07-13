image bg_room = "images/bg_room.png"
image figure1 = im.Scale("images/figure1.png", 100, 100)
image figure2 = im.Scale("images/figure2.png", 100, 100)
image figure3 = im.Scale("images/figure3.png", 100, 100)
image figure4 = im.Scale("images/figure4.png", 100, 100)

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
        global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer
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
                if oLen >= maxLen:
                    oActive = False
                    #renpy.hide_screen("game")
                    return True
        return False

screen game:
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime - .01), If(oTime <= .0, true=[Hide("game"), Function(lambda: renpy.return_statement(False))])]
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
