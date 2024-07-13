init python:
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    flash = Fade(.25, 0, .5, color="#fff")
    flash2 = Fade(.25, 0, .5, color="#222")

    max_points = 100
    img_name = "n"
    minN = 0  # 애니메이션의 시작 프레임을 0으로 설정
    maxN = 14  # 애니메이션 프레임 수를 14개로 유지
    points_plus = 2.5

    points_minus = 1.0
    ani_time = .1
    number = 0
    plus = 1
    points = 0
    clicked = True

    def NextFrameF():
        global points, number, plus, clicked
        if clicked:
            number += plus
            if number > maxN:
                number = maxN - 1
                plus = -plus
            if number < minN:
                number = minN + 1
                plus = -plus
        points -= points_minus
        if points < 0:
            points = 0
        clicked = False
        renpy.restart_interaction()

    NextFrame = renpy.curry(NextFrameF)

# 이미지 선언 부분
init:
    image n0 = "images/scene/n0.png"
    image n1 = "images/scene/n1.png"
    image n2 = "images/scene/n2.png"
    image n3 = "images/scene/n3.png"
    image n4 = "images/scene/n4.png"
    image n5 = "images/scene/n5.png"
    image n6 = "images/scene/n6.png"
    image n7 = "images/scene/n7.png"
    image n8 = "images/scene/n8.png"
    image n9 = "images/scene/n9.png"
    image n10 = "images/scene/n10.png"
    image n11 = "images/scene/n11.png"
    image n12 = "images/scene/n12.png"
    image n13 = "images/scene/n13.png"
    image n14 = "images/scene/n14.png"
    image heart = "images/heart.png"
    image heartempty = "images/heartempty.png"

screen clicker:
    modal True
    on "show" action [SetVariable("number", 0), SetVariable("plus", 1), SetVariable("clicked", True)]
    timer ani_time repeat True action [NextFrame(), If(points <= 0, Return(False), NullAction())]
    add img_name + str(number)
    button:
        text _("")
        xfill True
        yfill True
        background "#00000001"
        action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, Return(True), NullAction())]
    key "K_SPACE" action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, Return(True), NullAction())]
    vbar value StaticValue(points, max_points):
        align (0, 0)
        maximum (150, 150)
        left_bar "heartempty"
        right_bar "heart"
        thumb None
        thumb_shadow None

label click_game_start:
    scene expression (img_name + "0")
    pause .5
    show expression Text("Prepared!") at truecenter as txt
    with dissolve
    pause
    hide txt
    $ points = 10
    call screen clicker
    if _return:
        while number < maxN:
            $ number += 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + str(maxN))
        with flash
        show expression Text("Victory!") at truecenter as txt
    else:
        while number > 0:
            $ number -= 1
            scene expression (img_name + str(number))
            $ renpy.pause(ani_time, hard=True)
        scene expression (img_name + "0")
        with flash2
        show expression Text("Loss.") at truecenter as txt
    $ renpy.pause(1.0, hard=True)
    hide txt
    with dissolve
    return
