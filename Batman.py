import turtle
t = turtle.Turtle()
t.pensize(4)

turtle.bgcolor("black")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
t.pencolor("yellow")
t.fillcolor("yellow")

go(211.85,-94.91)
t.begin_fill()
t.seth(32.92)
t.circle(106.58,113.09)
t.seth(146.01)
t.circle(385.89,66.66)
t.seth(214.34)
t.circle(108.67,114.4)
t.seth(327.08)
t.circle(386,65.85)
t.end_fill()

t.pencolor("black")
t.fillcolor("black")

go(15,-106)
t.begin_fill()
t.seth(65.31)
t.forward(17.62)
t.seth(65.31)
t.circle(-335.72,6.8)
t.seth(58.51)
t.circle(-37.46,130.52)
t.seth(49.71)
t.circle(-82.46,37.74)
t.seth(-11.97)
t.circle(-25.55,107.98)
t.seth(264)
t.circle(-79.52,26.66)
t.seth(25.15)
t.circle(372.94,7.79)
t.seth(32.92)
t.circle(92.67,114.51)
t.seth(147.32)
t.circle(369.89,17.41)
t.seth(322.52)
t.circle(-46.55,47.05)
t.seth(276.98)
t.circle(-46.37,187.01)
t.seth(90)
t.forward(44.72)
t.seth(238.67)
t.forward(29.85)
t.seth(160.73)
t.circle(34.15,18.11)
t.seth(181.16)
t.circle(34.15,18.11)
t.seth(121.33)
t.forward(29.85)
t.seth(270)
t.forward(44.72)
t.seth(270)
t.circle(-46.37,187.01)
t.seth(83.02)
t.circle(-46.55,47.05)
t.seth(195.27)
t.circle(369.89,17.41)
t.seth(212.68)
t.circle(92.67,114.51)
t.seth(327.08)
t.circle(372.94,7.79)
t.seth(122.66)
t.circle(-79.52,26.66)
t.seth(96)
t.circle(-25.55,107.98)
t.seth(348.03)
t.circle(-82.46,37.74)
t.seth(72.01)
t.circle(-37.46,130.52)
t.seth(301.49)
t.circle(-335.72,6.8)
t.seth(294.69)
t.forward(28)
t.seth(65.31)
t.forward(25)
t.end_fill()

t.hideturtle()