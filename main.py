import math
from turtle import *
def f(t, v, h=0):
	return -16 * math.pow(t, 2) + v * t + h
def X(t):
	global vox
	return vox * t

def Y(t, h, voy):
	result = 5 + voy * t - 4.9 * t
	return result
t = Turtle()
x = 0 
y = 0
t.speed(100)
t.goto(x, y)
t.down()
t.goto(0, 200)
t.goto(0, 0)
t.goto(200, 0)
t.goto(0, 0)
x = 10
for i in range(20):
	t.goto(x, 0)
	t.goto(x, 5)
	t.goto(x, -5)
	t.goto(x, 0)
	x += 10
t.up()
t.goto(0, 0)
t.down()
y = 10
for i in range(20):
	t.goto(0, y)
	t.goto(5, y)
	t.goto(-5, y)
	t.goto(0, y)
	y += 10
x = 0
y = 0
t.up()
t.goto(0, 0)
t.down()
lh = [-10, -10]
t.pencolor("green")
time = 0
ly = 0
voy = int(input("What will be the starting velocity (V0) of the rocket? "))
h = int(input("What will be the starting height of the rocket? "))
s = 1
t.speed(10)
t.shape("classic")
t.goto(0, h)
X = x
Y = y
while y+h > -1:
	print("Altitude: " + str(y))
	x +=.1
	y = f(x, voy, h)
	if y < lh[0] or y < lh[-1]:
		high = y
		t.pencolor("red")
	t.goto(x*10, y+h)
	ly = y

	lh[0] = lh[-1]
	lh[-1] = y
	
print("Inital settings: Velocity: {}; Height: {}".format(voy, h))
print("Rocket was flying for: {:.2f} seconds".format(x))
print("Rocket's apex: {}".format(high))