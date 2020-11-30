import turtle
import random

Jim = turtle.Turtle()
Jim.speed(0)
color_list = ["lime green", "royal blue", "indigo", "plum"] 

def drawSquare(color, size, x,y): 
  Jim.penup()
  Jim.color(color)
  Jim.goto(x,y)
  Jim.pendown()
	
  Jim.forward(size)
  Jim.left(90)
  Jim.forward(size)
  Jim.left(90)
  Jim.forward(size)
  Jim.left(90)
  Jim.forward(size)
  Jim.left(90)


while True:
  random_size = random.randint(20, 200)
  random_x = random.randint(-250, 250)
  random_y = random.randint(-250, 250)
  random_color = random.choice(color_list)
  drawSquare(random_color, random_size, random_x, random_y)
'''
for c in color_list:
  drawSquare(c, 50, -50,100)


red = [255, 0, 0]
yellow = [255, 255, 0]
'''
