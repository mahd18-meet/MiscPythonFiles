import turtle
import math
import random
import time
wn = turtle.Screen()
wn.setup(1000,500)
wn.bgcolor("black")
player1 = turtle.Turtle()
player2 = turtle.Turtle()
player1.color("white")
player1.penup()
UP_ARROW = "Up"
DOWN_ARROW = "Down"
startx = -480

x1= player1.xcor()
y1= player1.ycor()
player2.penup()
player2.color("white")
player1.shape("square")
player2.shape("square")
platformlength = 5
player1= []
player2=[]
starty= -50
starty2 = -50

for count in range(platformlength):
    player1.append(turtle.Turtle())
    player1[count].color("white")
    player1[count].penup()
    player1[count].shape("square")
    player1[count].setpos(-480,starty)
    starty +=20
    def up():
        x1 = player1[count].xcor()
        y2 = player1[count].ycor()
        player1[count].goto(x1, y1+25)
        x1 = player1[count].xcor()
        y2 = player1[count].ycor()
    
for count2 in range(platformlength):
    player2.append(turtle.Turtle())
    player2[count2].color("white")
    player2[count2].penup()
    player2[count2].shape("square")
    player2[count2].setpos(480,starty2)
    starty2 +=20
    
def up():
    x1 = player1[count].xcor()
    y2 = player1[count].ycor()
    player1[count].goto(x1, y1+25)
    x1 = player1[count].xcor()
    y2 = player1[count].ycor()
turtle.listen()
turtle.onkeypress(up,UP_ARROW)

def down():
    global x1
    global y1
    player1[count].goto(x1,y1-25)
    x1= player1[count].xcor()
    y1= player1[count].ycor()
    

turtle.onkeypress(down, DOWN_ARROW)



x2= player2.xcor()
y2= player2.ycor()
def up2():
    global x2
    global y2
    player2.goto(x2, y2+25)
    x2= player2.xcor()
    y2= player2.ycor()
    
turtle.listen()
turtle.onkeypress(up2, "w")

def down2():
    global x2
    global y2
    player2.goto(x2,y2-25)
    x2= player2.xcor()
    y2= player2.ycor()
    

turtle.onkeypress(down2, "s")




turtle.mainloop()
turtle.listen()
