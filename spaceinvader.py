import turtle as trtl

space_image = "spaceship.gif"

alien_image = "spaceinvaderalien.gif"

wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.addshape(alien_image)
alien = trtl.Turtle()
alien.ht()

x = -600
y = 400

aliens = []
number_of_aliens = 0

wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.addshape(space_image)
spaceship = trtl.Turtle()
spaceship.pu()
spaceship.goto(0,-400)
speed = 10
time = 0

bullets = []

def draw_alien(alien):
  alien.shape(alien_image)
  wn.update()

def draw_ship(spaceship):
  spaceship.shape(space_image)
  wn.update()

def up():
  spaceship.setheading(90)
  spaceship.forward(speed)

def down():
  spaceship.setheading(90)
  spaceship.backward(speed)

def left():
  spaceship.setheading(180)
  spaceship.forward(speed)

def right():
  spaceship.setheading(0)
  spaceship.forward(speed)

def shoot():
    global time
    if time == 0:
      time = 1
      temp_turtle = trtl.Turtle()
      temp_turtle.ht()
      temp_turtle.pencolor("red")
      temp_turtle.shape("arrow")
      temp_turtle.fillcolor("red")
      temp_turtle.pu()
      temp_turtle.pensize(4)
      temp_turtle.speed(0)
      bullets.append(temp_turtle)
      
      temp_turtle.goto(spaceship.xcor(),spaceship.ycor())
      temp_turtle.setheading(90)
      temp_turtle.st()
      temp_turtle.speed(3)
      temp_turtle.forward(1300)
      time = 0

for step in range(4):
  while number_of_aliens < 20:
    temp_alien = trtl.Turtle()
    temp_alien.speed(0)
    temp_alien.pu()
    draw_alien(temp_alien)
    temp_alien.ht()
    temp_alien.goto(x,y)
    temp_alien.st()
    aliens.append(temp_alien)
    x = x + 60
    number_of_aliens = number_of_aliens + 1
  number_of_aliens = 0
  y = y - 60
  x = -600



draw_ship(spaceship)

spaceship.setheading(90)
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(shoot," ")
wn.listen()

wn.mainloop()