import pygame
import pgzrun




WIDTH = 615
HEIGHT = 600
background = Actor('back')
banana = Actor('bananapeel')
aluminium = Actor('aluminiums')
eggcarton = Actor('eggcarton')
styrofoam = Actor('styrofoam')
plasticbottle = Actor('plasticbottle')

compost = Actor('green')
compost.x = 80
compost.y = 459

blue = Actor('blue')
blue.x = 310
blue.y = 500

black = Actor('maingarbage')
black.x = 531
black.y = 504

def draw():
    screen.clear()
    background.draw()
    compost.draw()
    blue.draw()
    black.draw()
    banana.draw()



    if banana.x == 700:
        aluminium.draw()
        screen.draw.text("Good Job! Banana peels go in compost", (50, 30), color="black")

    if aluminium.x == 800:
        styrofoam.draw()
        screen.draw.text("Perfect! Aluminium foil goes in the blue box", (50, 50), color="black")

    if styrofoam.x == 800:
        eggcarton.draw()
        screen.draw.text("Styrofoam containers go in garbage", (50, 70), color="black")

    if eggcarton.x == 900:

        screen.draw.text("Egg cartons go in the blue box", (50, 90), color="black")



def update():
    if banana.x != 700:


        moving(banana)
    if banana.colliderect(compost):
        banana.x = 700

    if aluminium.x != 800:
        moving(aluminium)

    if aluminium.colliderect(blue):
        aluminium.x = 800

    if styrofoam.x != 800:
       moving(styrofoam)

    if styrofoam.colliderect(black):
        styrofoam.x = 800

    if styrofoam.x == 800:
        moving(eggcarton)

    if eggcarton.colliderect(blue):
        eggcarton.x = 900








def moving(object):
    if keyboard.right:
            object.x = object.x + 2
    elif keyboard.left:
            object.x = object.x - 2
    elif keyboard.down:
            object.y = object.y + 2
    elif keyboard.up:
            object.y = object.y - 2




pgzrun.go()
