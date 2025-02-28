import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.shape("turtle")
t.pensize(5)

t.pencolor("White")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def arco(direc, radio, ang):
    t.seth(direc)
    t.circle(radio, ang)

def linea(direc, longitud):
    t.seth(direc)
    t.forward(longitud)
    
go(-119.44, -109.72) 
arco(163.11, -48.03, 72.9)
linea(180, 62.22)
linea(49.88, 96.56)
arco(51.11, 71.72, 39.14)
arco(90.25, 60.76, 89.75)
linea(180, 24.33)
arco(180, 63.36, 96.52)
linea(0, 50.08)
arco(96.29, -23.4, 125.77)
arco(330.52, -19.81, 100.07)
linea(230.45, 139.48)
linea(270, 40.42)
linea(0, 164.66)

go(0, 58.06)
arco(90, 57.51, 90)
linea(180, 29.62)
arco(180, 59.40, 56.69)
arco(299.43, -74.97, 70.12)
linea(270, 54.69)
arco(270, 59, 90)
linea(0, 28.73)
arco(0, 57.5, 90)
linea(90, 111.17)

go(-48.44, 49.40)
arco(90, 23.34, 180)
linea(270, 92.77)
arco(270, 23.34, 180)
linea(90, 92.77)

go(10, 45.42)
arco(79.15, 65.58, 37.36)
arco(49.72, -85.98, 69.92)
arco(339.8, -60.66, 90.59)
arco(249.21, -119.62, 18.67)
linea(230.54, 82.99)
linea(0, 102.48)
linea(270, 45.40)
linea(180, 170.6)
linea(90, 15.48)
arco(45.82, 59.28, 49.47)
linea(50.54, 101.75)
arco(50.54, 93.58, 8.54)
arco(59.09, 19.06, 127.97)
arco(187.06, 25.13, 85.68)
linea(180, 33.49)

t.pencolor("Red")
go(146.63, 4.28)
linea(243.98, 40.63)
linea(270, 42.84)
linea(0, 94.01)
linea(270, 34.5)
linea(0, 51.17)
linea(90, 34.5)
linea(0, 17.54)
linea(90, 45.42)
linea(180, 17.54)
linea(90, 54.91)
linea(180, 51.17)
linea(270, 57.5)
linea(180, 36.22)
linea(63.98, 164.14)
linea(180, 57.40)
linea(243.82, 123.68)

t.pencolor("Black")
linea(243.98, 40.63)
linea(270, 42.84)
linea(0, 94.01)
linea(270, 34.5)
linea(0, 51.17)
linea(90, 34.5)
linea(0, 17.54)
linea(90, 45.42)
linea(180, 17.54)
linea(90, 54.91)
linea(180, 51.17)
linea(270, 57.5)
linea(180, 36.22)
linea(63.98, 164.14)
linea(180, 57.40)
linea(243.82, 123.68)

t.pencolor("Gold")
linea(270, 19.78)
linea(0, 46.85)
arco(80.84, -22.31, 170.84)
linea(270, 22.90)
arco(270, -23.48, 180)
linea(90, 3.16)
linea(180, 50.63)
arco(270.74, 72.69, 83.02)
arco(353.76, 77.99, 88.66)
arco(82.42, 103.42, 25.77)
arco(108.19, 63.87, 68.77)
arco(176.96, 72.03, 26.34)
linea(90, 29.49)
linea(0, 83.07)
linea(90, 45.99)
linea(180, 133.37)
linea(270, 112.13)

t.hideturtle()
turtle.done()