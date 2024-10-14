import turtle as trtl

alien_image = "spaceinvaderalien.gif"

wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.addshape(alien_image)
alien = trtl.Turtle()

def draw_alien(alien):
  alien.shape(alien_image)
  wn.update()
draw_alien(alien)
wn.mainloop()