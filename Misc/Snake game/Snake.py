import turtle, random,time
snake=turtle.clone()
food = turtle.clone()
food.penup()
snakestamp = []
foodstamp = []
my_pos = []
pos_list=[]
foodpos= []
x = 800
y = 500
turtle.setup(x,y)
start_length = 6
xloc = snake.pos() [0]
yloc = snake.pos()[1]
turtle.hideturtle()
sqsize = 20
food.ht()
snake.ht()
snake.penup()
snake.shape("square")
snake.color("blue")
turtle.bgcolor('lightgreen')
UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"
turtle.register_shape("gameover.gif")
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
UP_EDGE =  250
DOWN_EDGE = -250
LEFT_EDGE = -400
RIGHT_EDGE = 400
food.st()
turtle.setup(800,500)
food.speed(0)
for b in range(0,6):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos+=sqsize
    my_pos = (x_pos, y_pos)
    snake.goto(my_pos)
    pos_list.append(my_pos)
    s = snake.stamp()
    snakestamp.append(s)
    print (snakestamp)


    
def makefood():
    min_x = -int(x/2/sqsize) +1
    max_x =int(x/2/sqsize) -1
    min_y = -int(y/2/sqsize) +1
    max_y = int(y/2/sqsize)-1
    food_x = random.randint(min_x, max_x) *sqsize
    food_y = random.randint(min_y, max_y) *sqsize
    food.goto(food_x,food_y)
    food_pos= food.pos()
    foodpos.append(food_pos)
    '''
    food.stamp()
    food_stamp = food.stamp()
    print(food_stamp)
    foodstamp.append(food_stamp)
    turtle.ontimer(makefood,10000)
'''
direction = RIGHT



def  up():
    global direction
    direction = UP
   
    print ("You pressed the up key")

    
def  left():
    global direction
    direction = LEFT
    
    print ("You pressed the left key")

def  down():
    global direction
    direction = DOWN
    
    print ("You pressed the down key")

def right():
    global direction
    direction = RIGHT
    
    print ("You pressed the right key")
    
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos =  my_pos[1]
    if direction ==RIGHT:
        snake.goto(x_pos + sqsize, y_pos)
        
    elif direction == LEFT:
        snake.goto(x_pos -sqsize, y_pos)

        
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - sqsize)

    elif direction  == UP:
        snake.goto(x_pos, y_pos +sqsize)
        
    my_pos= snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    snakestamp.append(new_stamp)
    #SPECIAL PLACE
    if snake.pos() in foodpos:
        food.ht()
        makefood()
        food.st()
        
        food_ind=foodpos.index(snake.pos())
        snake.clearstamp(foodpos.index(snake.pos()))
        foodpos.pop(food_ind)
     
    else:
        old_stamp = snakestamp.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

  

    


    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print ("GAME OVER")
       
        turtle.bgpic("gameover.gif")
        time.sleep(3)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print ("GAME OVER")
        turtle.bgpic("gameover.gif")
        time.sleep(3)
        quit()
    elif new_y_pos >= UP_EDGE:
        print ("GAME OVER")
        turtle.bgpic("gameover.gif")
        time.sleep(3)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print ("GAME OVER")
        turtle.bgpic( "gameover.gif")
        time.sleep(3)
        exit()
    


    turtle.ontimer(move_snake,30)

def pause():
    time.sleep(15)

    

    
move_snake()
food.color('red')
food.shape("square")


    
 

makefood()

turtle.onkeypress(pause,"p")
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()
turtle.mainloop()
turtle.listen()
