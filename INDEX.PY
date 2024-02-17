
# # print("Deepak")
# # # import math
# # # from turtle import * 
# # # def hearta(k):
# # #     return 15*math.sin(k)**3
# # # def heartb(k):
# # #     return 12*math.cos(k)-5*\
# # #     math.cos(2*k)-2*\
# # #     math.cos(3*k)-\
# # #     math.cos(4*k)
# # # speed(10000)
# # # bgcolor("blue")
# # # for i in range (6000):
# # #     goto(hearta(i)*20,heartb(i)*20)
# # #     for j in range(5):
# # #         color("#f73487")
# # #         goto(0,0)
# # #         done()




# # # from matplotlib import pyplot as plt
 
# # # x = []
# # # y = []
 
# # # for i in range(100):
# # #     x.append(i)
# # #     y.append(i)
 
# # #     # Mention x and y limits to define their range
# # #     plt.xlim(0, 100)
# # #     plt.ylim(0, 100)
     
# # #     # Plotting graph
# # #     plt.plot(x, y, color = 'green')
# # #     plt.pause(0.01)
 
# # # plt.show()














# # # required modules
# # from turtle import * from random import randint
  
     
# # # classic shape turtle
# # speed(0)
# # penup()
# # goto(-140, 140)
  
# # # racing track
 
# # for step in range(15):
# #     write(step, align ='center')
# #     right(90)
     
# #     for num in range(8):
# #         penup()
# #         forward(10)
# #         pendown()
# #         forward(10)
         
# #     penup()
# #     backward(160)
# #     left(90)
# #     forward(20)
 
# # # first player details
# # player_1 = Turtle()
# # player_1.color('red')
# # player_1.shape('turtle')
  
# # # first player proceeds to racing track
# # player_1.penup()
# # player_1.goto(-160, 100)
# # player_1.pendown()
  
# # # 360 degree turn
# # for turn in range(10):
# #     player_1.right(36)
 
# # # second player details
# # player_2 = Turtle()
# # player_2.color('blue')
# # player_2.shape('turtle')
  
# # # second player enters in the racing track
# # player_2.penup()
# # player_2.goto(-160, 70)
# # player_2.pendown()
  
# # # 360 degree turn
# # for turn in range(72):
# #     player_2.left(5)
 
# # # third player details
# # player_3 = Turtle()
# # player_3.shape('turtle')
# # player_3.color('green')
  
# # # third player enters in the racing track
# # player_3.penup()
# # player_3.goto(-160, 40)
# # player_3.pendown()
  
# # # 360 degree turn
# # for turn in range(60):
# #     player_3.right(6)
 
# # # fourth player details
# # player_4 = Turtle()
# # player_4.shape('turtle')
# # player_4.color('orange')
  
# # # fourth player enters in the racing track
# # player_4.penup()
# # player_4.goto(-160, 10)
# # player_4.pendown()
  
# # # 360 degree turn
# # for turn in range(30):
# #     player_4.left(12)
 
# # # turtles run at random speeds
# # for turn in range(100):
# #     player_1.forward(randint(1, 5))
# #     player_2.forward(randint(1, 5))
# #     player_3.forward(randint(1, 5))
# # #     player_4.forward(randint(1, 5))













# # import turtle

# # window = turtle.Screen()
# # window.bgcolor("black")

# # # Whole pumpkin
# # pumpkin = turtle.Turtle()
# # pumpkin.hideturtle()
# # pumpkin.color("orange")
# # pumpkin.dot(200)

# # # The turtle to "carve" the pumpkin
# # carver = turtle.Turtle()

# # # "Flatten" the lower part of the pumpkin
# # carver.penup()
# # carver.setposition(-200, -100)
# # carver.pensize(60)
# # carver.pendown()
# # carver.forward(600)
# # carver.pensize(2)

# # turtle.done()





# import turtle

# window = turtle.Screen()
# window.bgcolor("black")

# # Whole pumpkin
# pumpkin = turtle.Turtle()
# pumpkin.hideturtle()
# pumpkin.color("orange")
# pumpkin.dot(200)

# # The turtle to "carve" the pumpkin
# carver = turtle.Turtle()

# # "Flatten" the lower part of the pumpkin
# carver.penup()
# carver.setposition(-200, -100)
# carver.pensize(60)
# carver.pendown()
# carver.forward(600)
# carver.pensize(2)

# def carve_pumpkin(colour):
#     carver.color(colour)

#     # Make eyes
#     def make_eye(start, orientation):
#         carver.setheading(0)
#         carver.penup()
#         carver.setposition(*start)
#         carver.pendown()
#         carver.begin_fill()
#         carver.forward(orientation * 40)
#         carver.setheading(orientation * 135)
#         carver.forward(orientation * 70)
#         carver.end_fill()

#     make_eye((-50, 20), 1)
#     make_eye((50, 20), -1)

# carve_pumpkin("black")

# turtle.done()



from  turtle import *
import colorsys
bgcolor('black')
tracer (500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt (98)
        circle(i, 12)
        fd (290)
        fd(i)
        lt (29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2)
            end_fill()
draw()
done()