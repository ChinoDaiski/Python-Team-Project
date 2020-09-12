import turtle as t

t.speed(0)

leng=100

pos=(0,0)
posx=0
posy=0

for i in range(0,6):
      t.penup()
      t.goto(posx,posy)
      t.pendown()
      t.goto(500,posy)
      posy=posy+leng

posy=0

for i in range(0,6):
      t.penup()
      t.goto(posx,posy)
      t.pendown()
      t.goto(posx,500)
      posx=posx+leng

t.exitonclick()
