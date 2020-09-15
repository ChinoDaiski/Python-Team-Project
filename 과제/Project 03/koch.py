
import turtle as t

t.penup()
t.goto(-500,0)
t.pendown()

def koch(length,n):
	if (n == 0) :
		t.forward(length)
	else:
		koch(length/3, n-1)
		t.left(60)
		koch(length/3, n-1)
		t.right(120)
		koch(length/3, n-1)
		t.left(60)
		koch(length/3, n-1)


t.speed(0)
koch(900,5)

