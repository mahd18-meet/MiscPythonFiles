import turtle
import math
import random
import winsound
#Set up Screen
wn = turtle.Screen()
wn.bgcolor("black")
turtle.setup(700,700)
wn.bgpic("game2.gif")
wn.tracer(2)
mypen = turtle.Turtle()
player = turtle.Turtle()
speed = 1
RIGHT_ARROW = "Right"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
UP_ARROW = "Up"
turtle.hideturtle()
player.penup()
player.color("blue")
player.shape("triangle")
player.speed(0)
mypen.penup()
mypen.setpos(-300,-300)
mypen.pensize(3)
mypen.speed(0)
mypen.color("white")

maxEnemy = 1
maxGoals = 6
goals = []
Enemy = []
score = 0




for side in range(4):
    mypen.pendown()
    mypen.fd(600)
    mypen.left(90)
mypen.hideturtle()
for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].shape("circle")
    goals[count].setpos(random.randint(-300,300), random.randint(-300,300))
for count in range(maxEnemy):
     Enemy.append(turtle.Turtle())
     Enemy[count].color("green")
     Enemy[count].penup()
     Enemy[count].speed(0)
     Enemy[count].shape("square")
     Enemy[count].setpos(random.randint(-300,300), random.randint(-300,300))
     


def turnleft():
    player.left(30)
turtle.onkeypress(turnleft, LEFT_ARROW)
turtle.listen()

def turnright():
    player.right(30)
turtle.onkeypress(turnright, RIGHT_ARROW)

def incresespeed():
    global speed
    speed+=1
turtle.onkeypress(incresespeed, UP_ARROW)

def downspeed():
    global speed
    speed = speed -1
turtle.onkeypress(downspeed, DOWN_ARROW)

def  isCollision(t1, t2):
    d = math.sqrt(math.pow(player.xcor()-goals[count].xcor(),2) +math.pow(player.ycor() - goals[count].ycor(),2))
    if d  <20:
        return True
    else:
        return False



while True:
    player.forward(speed)
    #Boundry checking
    if  player.ycor() > 300 or player.ycor() <-300:
        player.right(180)

    if  player.xcor() > 300 or player.xcor() <-300:
        player.right(180)
    

    for count in range(maxGoals):
    
        if isCollision(player, goals[count]):
           goals[count].setpos(random.randint(-300,300), random.randint(-300,300))
           goals[count].right(random.randint(0,360))
           score +=1
           mypen.undo()
           mypen.penup()
           mypen.hideturtle()
           mypen.setpos(-290,310)
           scorestring = "Score: " + str(score)
           mypen.write(scorestring, False, align = "left", font =("Arial" , 14, "normal"))
           #Boundry checking
        if  goals[count].ycor() > 290 or goals[count].ycor() <-290:
            goals[count].right(180)

        if  goals[count].xcor() > 290 or goals[count].xcor() <-290:
            goals[count].right(180)


        goals[count].forward(3)
    for count in range(maxEnemy):
        if isCollision(player,Enemy[count]):
            for c in range(0,100):
                 print ("Game over")
                 quit()

        if  Enemy[count].ycor() > 290 or Enemy[count].ycor() <-290:
            Enemy[count].right(180)

        if  Enemy[count].xcor() > 290 or Enemy[count].xcor() <-290:
            Enemy[count].right(180)
            

        
        Enemy[count].fd(3)

   

turtle.mainloop()
