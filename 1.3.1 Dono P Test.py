import turtle as trtl
import random as rand
import math

wn = trtl.Screen()
wn.bgpic("minion/space background.gif")

ship_image = "minion/gruship.gif"
explosion = "minion/explosion.gif"
smoke = "minion/smoke.gif"
minion1 = "minion/minion1.gif"
minion2 = "minion/minion2.gif"
minion3 = "minion/minion3.gif"
minion4 = "minion/minion4.gif"
minion5 = "minion/minion5.gif"
minion6 = "minion/minion6.gif"
minion7 = "minion/minion7.gif"
minion8 = "minion/minion1.gif"
minion9 = "minion/minion2.gif"
minion10 = "minion/minion3.gif"
minion11= "minion/minion4.gif"
minion12= "minion/minion5.gif"
minion13= "minion/minion6.gif"
minion14= "minion/minion7.gif"
i=0
j=0
minions = []
shapes = []
go = False

gruship = trtl.Turtle()
wn = trtl.Screen()

#ship_image = PhotoImage(file=r"minion/Gru Ship.gif").subsample(2,2)
#wn.addshape("ship_image", Shape("image", ship_image))
wn.addshape(ship_image)
wn.addshape(explosion)
wn.addshape(minion1)
wn.addshape(minion2)
wn.addshape(minion3)
wn.addshape(minion4)
wn.addshape(minion5)
wn.addshape(minion6)
wn.addshape(minion7)
wn.addshape(minion8)
wn.addshape(minion9)
wn.addshape(minion10)
wn.addshape(minion11)
wn.addshape(minion12)
wn.addshape(minion13)
wn.addshape(minion14)
wn.addshape(smoke)
shapes.append(minion1)
shapes.append(minion2)
shapes.append(minion3)
shapes.append(minion4)
shapes.append(minion5)
shapes.append(minion6)
shapes.append(minion7)
shapes.append(minion8)
shapes.append(minion9)
shapes.append(minion10)
shapes.append(minion11)
shapes.append(minion12)
shapes.append(minion13)
shapes.append(minion14)

def exploding(thing):
  global go
  #unicorn_move(unicorn, -100, -45)
  if go == False:
    go = True
    thing.pu()
    thing.shape(explosion)
    wn.update
    i=0
    for step in minions:
        minions[i].shape(shapes[i])
        x = rand.randint(-300,300)
        y = rand.randint(-100,200)
        temp = minions[i]
        temp.goto(x,y)
        temp.st()
        i=i+1
    thing.ht()
    fall()

def draw_ship(thing):
  thing.pu()
  thing.ht()
  thing.shape(ship_image)
  wn.update()

def fall():
    wn.tracer(0)
    for step in range(650):
      i=0
      for each in minions:
        minions[i].speed(0)
        minions[i].backward(2)
        if i % 2 == 0:
          minions[i].setx(minions[i].xcor() + 1) 
        else:
          minions[i].setx(minions[i].xcor() - 1)
        i=i+1
      wn.update()
      trtl.time.sleep(0.05)
    wn.tracer(1)


while i<14:
  minioni = trtl.Turtle()
  minioni.pu()
  minioni.ht()
  minioni.setheading(90)
  minions.append(minioni)
  i = i+1

draw_ship(gruship)

gruship.goto(-500,0)
gruship.st()
x=-500
while x<0:
  x += 1
  y =math.sin(0.5*x)*2.5
  gruship.goto(x,y)

#box.onclick(lambda x,y: bananafling(banana1))

#wn.onclick(lambda x,y: unicorn_move(unicorn, -100, -45))

wn.onclick(lambda x,y: exploding(gruship))


wn.listen()
wn.mainloop()