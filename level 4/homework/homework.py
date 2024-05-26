from turtle import*

# building a castle

#I couldn't think of a way to draw the king and the queen
width(4)
speed(25)
color("grey")
forward(80)
left(90)
forward(80)
left(90)

color("brown")
forward(80)
left(90)

color("grey")
forward(80)
left(180)

penup()
goto(0, 80)
pendown()

color("brown")
right(45)
forward(58)
right(90)
forward(55)
left(135)

color("grey")
forward(130)

penup()
goto(0, 80)
pendown()

forward(130)

color("brown")
right(90)
forward(80)
left(135)
forward(58)
left(90)
forward(55)
left(135)

penup()
goto(80, 210)
pendown()

color("grey")
left(90)
forward(80)

color("brown")
right(90)
forward(80)
right(90)
color("grey")
forward(290)
right(90)
forward(80)


penup()
goto(80, 290)
pendown()

color("brown")
right(135)
forward(58)
right(90)
forward(55)


color("grey")
left(135)
forward(80)
right(90)
color("brown")
forward(80)
color("grey")
right(90)
forward(372)
right(90)
forward(80)


penup()
goto(160, 372)
pendown()

color("brown")

right(135)
forward(58)
right(90)
forward(55)

penup()
goto(240, 80)
pendown()


left(45)
forward(80)
left(135)
forward(58)
left(90)
forward(55)
color("grey")


penup()
goto(240, 0)
pendown()

right(225)
forward(80)
left(90)
forward(210)
left(90)
color("brown")


forward(80)
right(135)
forward(58)
right(90)
forward(55)


penup()
goto(277, 253)
pendown()

begin_fill()
circle(5)
end_fill()

penup()
goto(280, 253)
pendown()
#flag
left(135)
forward(200)
right(90)
forward(180)
right(90)
forward(95)
right(90)
forward(180)
right(90)

penup()
goto(300, 380)
pendown()

#goa logo
color("grey")
right(90)
forward(30)
left(90)
forward(20)
left(90)
forward(15)
left(90)
forward(10)


penup()
goto(300, 380)
pendown()


left(180)
forward(45)
right(90)
forward(30)

penup()
goto(350, 380)
pendown()

color("green")
forward(35)
left(90)
forward(45)
left(90)
forward(35)
left(90)
forward(45)


penup()
goto(400, 380)
pendown()

color("grey")
left(150)
forward(50)
right(150)
forward(45)


penup()
goto(425, 395)
pendown()

right(90)
forward(13)


penup()
goto(65, 135)
pendown()

forward(50)
right(90)
forward(65)
right(90)
forward(50)
right(90)
forward(65)


penup()
goto(305, 135)
pendown()


right(90)
forward(50)
right(90)
forward(65)
right(90)
forward(50)
right(90)
forward(65)


penup()
goto(105, 0)
pendown()

right(180)
forward(100)
right(90)
forward(110)
right(90)
forward(100)

exitonclick()