import turtle as trtl


wn = trtl.Screen()
wn.title("Happy Birthday!")
wn.bgcolor("white")


card_minion = "minion/click here minion (2).gif"
card = "minion/Happy Birthday Card.gif"


wn.addshape(card_minion)
wn.addshape(card)


minion = trtl.Turtle()
minion.shape(card_minion)
minion.penup()  
minion.goto(0, 0)


card_turtle = trtl.Turtle()
card_turtle.ht()
card_turtle.shape(card)
card_turtle.penup()  
card_turtle.goto(0, -50)  


def click_the_card():
    card_turtle.st()


minion.onclick(lambda x,y: click_the_card())
wn.listen()
wn.mainloop()