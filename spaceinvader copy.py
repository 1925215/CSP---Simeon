import turtle as trtl
import time

# Set up the screen
screen = trtl.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)

# Set up the screen
screen = trtl.Screen()
screen.title("Space Invaders")
screen.setup(width=800, height=600)
# background picture
screen.bgpic("space.gif")

background_turtle = trtl.Turtle()
background_turtle.hideturtle()
background_turtle.speed(0)

# Score and Timer variables
score = 0
start_time = time.time()
game_duration = 60  # Game lasts for 60 seconds

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
timer = 0
index = 0
i=0
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
    global timer,i,score
    bruh=0
    if timer == 0:
      timer = 1
      temp_turtle = trtl.Turtle()
      temp_turtle.ht()
      temp_turtle.pencolor("red")
      temp_turtle.shape("arrow")
      temp_turtle.fillcolor("red")
      temp_turtle.pu()
      temp_turtle.pensize(4)
      temp_turtle.speed(0)
      bullets.append(temp_turtle)
      
      bullets[i].goto(spaceship.xcor(),spaceship.ycor())
      bullets[i].setheading(90)
      bullets[i].st()
      bullets[i].speed(0)
      coordinates = []
      for t in aliens:
        coordinates.append(t.pos())
      while bruh < 200:
        index = 0
        bullet_coord = bullets[i].pos()
        bullets[i].forward(5)
        bruh = bruh+1
        for every in aliens:
          first = coordinates[index]
          m = first[0]
          n = first[1]
          if (abs(bullet_coord[0]- m) < 25) and (abs(bullet_coord[1] - n) < 25):
            aliens[index].ht()
            score=score+1
            timer=0
            bullets[i].ht()
            return
            
          index = index +1

      i = i+1
      timer = 0

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", align="left", font=("Courier", 24, "normal"))
    remaining_time = max(0, game_duration - (time.time() - start_time))
    timer_display.clear()
    timer_display.write(f"Time: {int(remaining_time)}", align="right", font=("Courier", 24, "normal"))

for step in range(4):
  while number_of_aliens <= 20:
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
coordinates = []
for t in aliens:
  coordinates.append(t.pos())
scoreboard = trtl.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-350, 480)


timer_display = trtl.Turtle()
timer_display.color("white")
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(200, 480)



start_game = True

while start_game:
    # Update the scoreboard
    update_scoreboard()
    # Update score for demo purposes (replace with your game logic)
    spaceship.setheading(90)
    wn.onkeypress(up,"Up")
    wn.onkeypress(down,"Down")
    wn.onkeypress(left,"Left")
    wn.onkeypress(right,"Right")
    wn.onkeypress(shoot," ")
    wn.listen()
    index = 0
    for every in aliens:
       first = coordinates[index]
       t = first[0]
       u = first[1]
       t = t + 5
       u = u - 5
       aliens[index].goto(t,u)
       index = index + 1
    index = 0
    for every in aliens:
       first = coordinates[index]
       t = first[0]
       u = first[1]
       t = t - 5
       u = u - 5
       aliens[index].goto(t,u)
       index = index + 1

    if time.time() - start_time < game_duration:
        print("nice") # Increase score every frame (for testing)
    else:
        start_game = False  # End game after time runs out
    screen.update()
    time.sleep(0.1)  # Control frame rate


scoreboard.goto(0, 0)
scoreboard.color("red")
scoreboard.write("Game Over!", align="center", font=("Courier", 36, "normal"))
scoreboard.goto(0, -40)
scoreboard.write(f"Final Score: {score}", align="center", font=("Courier", 24, "normal"))

screen.mainloop()

wn.mainloop()
