import turtle
import random

color = "black"
size = 2
i = 10

p = turtle.Turtle()
player = turtle.Turtle()

p.speed(0)
p.left(90)
p.pencolor(color)
p.pensize(size)

def barrier(randomizer):
  if randomizer == 1:
    p.right(90)
    p.forward(20)
    p.backward(20)
    p.left(90)
  else: 
    p.left(90)
    p.forward(20)
    p.backward(20)
    p.right(90)

def spiral_maze(i, randomizer):
  bar_size = random.randint(1,10)
  end_bar_size = i - i/bar_size

  p.forward(i/bar_size)
  p.penup()
  p.forward(20)
  p.pendown()
  barrier(randomizer)
  p.forward(end_bar_size)
  p.left(90)

for x in range(49):
   bar_randomizer = random.randint(1,2)
   if x < 41:
     spiral_maze(i,2)
   elif x==49:
     p.forward(i + 10)
   else:
     p.forward(i)
     p.left(90)
   
   i = i + 10

wn = turtle.Screen()
wn.mainloop()




