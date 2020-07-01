import turtle as t

color_status = ["white", "blue", "red"]
alert_status = ["정상", "주의", "화제"]
tempc  = 50

def check_fire():
    if temp < 80:
        status = 0 
    elif temp < 120:
        status = 1
    else:
        status = 2

t.clear()
t.home()
t.pendown()
t.fillcolor(color_status[status])
t.begin_fill()
t.cricle(20)
t.end_fill()
t.penup()
t.goto(-22,50)
t.write("%s : %d"%(alert_status[status],tempc))

def keyUp():
    global tempc
    if temp < 80:
        temp = temp + 5
    else:
        temp = temp + 10
    check_fire()

def keydown():
    global tempc
    if temp < 80:
        temp = temp - 5
    else:
        temp = temp - 10
    check_fire()

t.setup(300, 300)
s = t.screen()
t.hideturtle()
t.speed(0)
check_fire()
s.onkey(keyup, "Up")
s.onkey(keydown, "Down")
s.onkey(s.bye, "q")
s.listen()
