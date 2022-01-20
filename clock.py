from turtle import Turtle, Screen
import time
from digital_clock import Digital_clock
t = time.localtime()
current__time = time.strftime("%H:%M:%S", t)
screen = Screen()
screen.tracer(0)
digital = Digital_clock()
digital.penup()
digital.goto(0, -60)
digital.hideturtle()


screen.title("                                                                                     CLOCK")
for x in range(0, 360, 30):
    t = Turtle()
    t.shape("circle")
    if x % 90 == 0:
        t.shapesize(0.5, 0.5)
    else:
        t.shapesize(0.25, 0.25)
    t.color("blue")
    t.penup()
    t.goto(210, 0)
    t.setheading(90)
    t.circle(210, x)
clock = Turtle()
seconds = Turtle()
minutes = Turtle()
hours = Turtle()
seconds.color("black")
minutes.color("green")
hours.color("red")
seconds.penup()
minutes.penup()
hours.penup()
seconds.shape("square")
minutes.shape("square")
hours.shape("square")
seconds.shapesize(10, 0.01)
minutes.shapesize(7.5, 0.05)
hours.shapesize(5, 0.1)
seconds.goto(0, 100)
minutes.goto(0, 75)
hours.goto(0, 50)
seconds.setheading(180)
minutes.setheading(180)
hours.setheading(180)
clock.width(3)
clock.penup()
clock.goto(220, 0)
clock.setheading(90)
clock.pendown()
clock.hideturtle()
clock.circle(220)
re = Turtle()
re.shape("circle")
re.shapesize(0.5, 0.5)
re.color("black")
screen.update()

def set_time():
    t=int(screen.textinput("time","if you want to set time\n then enter 1 else 0"))
    global ti
    if t==1:
        ti = screen.textinput("TIME", "enter time as hh:mm:ss :")
        ti = ti.split(':')
        for x in range(0, 3):
            ti[x] = int(ti[x])
        digital.set_time(ti)
    else:
        current_time = current__time
        current_time = current_time.split(':')
        for x in range(0, 3):
            current_time[x] = int(current_time[x])
        ti=current_time
        if ti[0]>=13:
            ti[0]=ti[0]-12
        digital.set_time(ti)


    s = ti[2]
    m = ti[1] * 60 + s
    h = ti[0] * 60 * 60 + m
    seconds.circle(100, -6 * s)
    minutes.circle(75, -0.1 * m)
    hours.circle(50, -1 / 120 * (h))
    return s


r = set_time()
while True:
    time.sleep(1)
    r += 1
    seconds.circle(100, -6)
    minutes.circle(75, -0.1)
    hours.circle(50, -1 / 120)
    digital.change_time(r)
    if r == 60:
        r = 0
    screen.update()

screen.exitonclick()
