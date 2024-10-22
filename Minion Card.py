import turtle as trtl
wn=trtl.Screen()
card_minion = "minion/click here minion.gif"
card = "minion/Happy Birthday Card.gif"

wn.addshape(card_minion)
wn.addshape(card)

minion  = trtl.Turtle()
minion.shape(card_minion)
wn.update
minion.goto(0,0)


def click_the_card():
    minion.forward(10)


minion.onclick(lambda x,y : click_the_card)
wn.listen()
wn.mainloop()
