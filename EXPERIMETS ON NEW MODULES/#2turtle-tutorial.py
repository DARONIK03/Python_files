# python tyrtle tutorial #2 ------ making mathamatical pattern pattern--     -  ----

import turtle as t
t.bgcolor('black')
t.speed(19)
color=['red','green','blue','cyan']
c=0 
for i in range(70):
    t.forward(i*7)
    t.right(200)
    t.color(color[c])
    if c==3:
        c=0
    else:
        c+=1
t.done()
