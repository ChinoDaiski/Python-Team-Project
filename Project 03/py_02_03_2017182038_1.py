
import turtle as t

def move_to(x,y):
	t.penup()
	t.goto(x,y)
	t.pendown()
	
def draw_jung_j():
	t.forward(160)
	t.right(135)
	t.forward(200)
	t.backward(100)
	t.left(90)
	t.forward(100)

def draw_jung_u():
	t.setheading(0)
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.backward(200)

def draw_jung_ng():
	t.setheading(0)
	t.circle(50)
	
def draw_seuong_se():
	t.setheading(0)
	t.right(135)
	t.forward(200)
	t.backward(100)
	t.left(90)
	t.forward(100)

def draw_uk_u():
      t.setheading(0)
      t.backward(100)
      t.forward(200)
      t.backward(100)
      t.right(90)
      t.forward(50)

def draw_uk_k():
      t.setheading(0)
      t.forward(160)
      t.right(90)
      t.forward(80)


t.speed(0)

move_to(-300,200)
draw_jung_j()

move_to(-120,120)
draw_jung_u()

move_to(-120,-70)
draw_jung_ng()




move_to(100,200)
draw_seuong_se()

move_to(140,120)
draw_jung_u()

move_to(150,-70)
draw_jung_ng()




move_to(320,150)
draw_jung_ng()

move_to(320,100)
draw_uk_u()

move_to(250,30)
draw_uk_k()


t.exitonclick()
