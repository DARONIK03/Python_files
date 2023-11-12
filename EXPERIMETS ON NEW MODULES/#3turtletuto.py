# Rangoli / graphical  circle of rgb flower

import turtle as t
import colorsys as cs
t.setup(800,800)
t.speed(11)
t.tracer(10)
t.width(2)
t.bgcolor("Black")
for i in range(24):
    for j in range(14):
        t.color(cs.hsv_to_rgb(i/14,j/24,1))
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(100)
        t.circle(50,24)
t.hideturtle()

