import turtle , time , random ,winsound
import pygame

pygame.init()

screen=turtle.Screen()
screen.title("Feigned F1")
screen.setup(width=500  , height=700)
screen.bgcolor("black")
screen.tracer(0)
screen.register_shape('racingback.gif')
screen.register_shape('racingcar.gif')

pygame.mixer.init()
pygame.mixer.music.load("MAX.mp3")
pygame.mixer.music.play(-1)

car=turtle.Turtle()
car.speed(0)
car.shape("racingcar.gif")
car.shapesize(2)
car.setheading(90)
car.penup()
car.goto(0,-200)

b=turtle.Turtle()
b.speed(0)
b.pensize(3)
b.penup()
b.hideturtle()
b.goto(0,0)

camera_x=0
camera_y=0

def left():
    x=car.xcor()
    x=x-20
    if x < -170:
        x=-170
    car.setx(x)

def right():
    x=car.xcor()
    x=x+20
    if x > 170:
        x=170
    car.setx(x)

def game_over():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write("GAME OVER" , align="center" , font=("Arial", 36 ,"bold"))
    turtle.exitonclick()


obstacles1=[]
for i in range(10):
    obstacle=turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.shapesize(3 ,6)
    obstacle.color("orange")
    obstacle.setheading(90)
    obstacle.penup()
    obstacle_x= random.randint(-170,170)
    obstacle_y=500
    obstacle.goto(obstacle_x , obstacle_y)   

    obstacles1.append(obstacle)

obstacles2=[]
for i in range(10):
    second_obstacle=turtle.Turtle()
    second_obstacle.speed(0)
    second_obstacle.shape("triangle")
    second_obstacle.shapesize(2,3)
    second_obstacle.color("red")
    second_obstacle.setheading(90)
    second_obstacle.penup()
    second_obstacle_x=random.randint(-170,170)
    second_obstacle_y=500
    second_obstacle.goto(second_obstacle_x , second_obstacle_y)
    
    obstacles2.append(second_obstacle)


coins=[]
for i in range(10):
    coin=turtle.Turtle()
    coin.speed(0)
    coin.shape("circle")
    coin.shapesize(1,2)
    coin.color("yellow")
    coin.setheading(90)
    coin.penup()
    coin_x=random.randint(-170,170)
    coin_y=500
    coin.goto(coin_x , coin_y)
    coins.append(coin)



health =100
health_remaining=turtle.Turtle()
health_remaining.penup()
health_remaining.goto(-180,320)
health_remaining.hideturtle()


screen.listen()
screen.onkeypress(left , "Left")
screen.onkeypress(right , " Right")
start=time.time()


e=-1
a=-1
c=-1

while True:
    camera_x=-2
    camera_y= camera_x +camera_y
    camera_y=camera_y %700

    b.goto(0,camera_y-700)
    b.shape("racingback.gif")
    b.stamp()
    car.shape("racingcar.gif")
    car.stamp()

    b.goto(0,camera_y)
    b.shape("racingback.gif")
    b.stamp()
    car.shape("racingcar.gif")
    car.stamp()

    
    if time.time() - start > random.randint(3, 6):
        start = time.time()
        e = e + 1
        if e == 9:
            e = -1
            for obstacle in obstacles1:
                obstacle_x = random.randint(-300, 300)
                obstacle_y = 500
                obstacle.goto(obstacle_x, obstacle_y)
    y = obstacles1[e].ycor()
    y = y - 2
    obstacles1[e].sety(y)
    
    if obstacles1[e].distance(car) < 50:
        winsound.PlaySound("img_explosion2.wav", winsound.SND_FILENAME)
        obstacles1[e].hideturtle()
        obstacles1[e].goto(3000,3000)
        obstacles1=[obstacle for obstacle in obstacles1 if obstacle.ycor() > -300]
        game_over()
    
    
    if time.time() - start > random.randint(3,6):
        start = time.time()
        a = a + 1
        if a == 9:
            a = -1
            for second_obstacle in obstacles2:
                second_obstacle_x = random.randint(-300, 300)
                second_obstacle_y = 500
                second_obstacle.goto(second_obstacle_x, second_obstacle_y)

    y = obstacles2[a].ycor()
    y = y - 2
    obstacles2[a].sety(y)


    if obstacles2[a].distance(car) < 50:
      winsound.PlaySound("img_explosion.wav", winsound.SND_FILENAME)
      health-=20
      
      obstacles2[a].hideturtle()
      obstacles2[a].goto(3000,3000)
      obstacles2=[second_obstacle for second_obstacle in obstacles2 if second_obstacle.ycor() > -300]
      if health>100:
        health=100

    health_remaining.clear()
    health_remaining.write("Health: {}".format(health), align ="center" , font=("Arial" , 16 ,"bold"))

    if health <=0:
        game_over()
        


    if time.time() - start > random.randint(3,6):
        start = time.time()
        c=c+1
        if c == 9:
            c = -1
            for coin in coins:
                coin_x = random.randint(-200, 200)
                coin_y = 500
                coin.goto(coin_x, coin_y)

    y = coins[c].ycor()
    y = y - 2
    coins[c].sety(y)


    if coins[c].distance(car) < 50:
      winsound.PlaySound("bounce.wav", winsound.SND_FILENAME)
      health+=5
        
      coins[c].hideturtle()
      coins[c].goto(3000,3000)
      coins=[coin for coin in coins if coin.ycor() > -300]
      if health > 100:
        health=100
      health_remaining.clear()
      health_remaining.write("Health: {}".format(health), align ="center" , font=("Arial" , 16 ,"bold")) 
    

    screen.update()

    b.clear()
    car.clear()


turtle.done()
pygame.quit()
