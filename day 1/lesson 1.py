from turtle import *


#we want to build a house

#step 1: draw a square
width(7)
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(95) #height
right(90)
forward(60)
right(90)
forward(95)
end_fill()
#end of door

#drawing the roof
penup()
goto(200, 200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#start of first window

penup()
goto(70, 175)
pendown()

right(60)
color("pink")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)
penup()
goto(70, 145)
pendown()
right(90)
forward(60)
#end of first window

#start of second window

penup()
goto(130, 175)
pendown()

left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)

penup()
goto(160, 175)
pendown()

right(90)
forward(60)

exitonclick()