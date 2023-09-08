import random as rd
import turtle
import time

drawing_area = turtle.Screen()
drawing_area.setup(width=750, height=500)
drawing_area.bgcolor("black")
drawing_area.tracer(0)
turtle.colormode(255)
turtle.hideturtle()

while True:
    turtle.width(rd.randrange(0, 3))
    turtle.setx(rd.randrange(-360, 360))
    turtle.sety(rd.randrange(-240, 240))
    turtle.pendown()

    steps = int(rd.random() * 100)
    turtle.color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
    turtle.fd(steps)
    turtle.left(90)
    turtle.fd(0.1)
    turtle.left(90)
    turtle.fd(steps)
    turtle.left(90)
    turtle.fd(0.1)
    turtle.left(90)
    turtle.penup()
    drawing_area.update()
    time.sleep(rd.uniform(0.01, 0.3))

drawing_area.mainloop()
