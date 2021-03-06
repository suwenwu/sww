import turtle as t
t.screensize(768,1024)
#t.bgpic(r'bg.png')
t.colormode(255)
t.shape('arrow')
t.speed(0)
#

#起点，头
t.penup()
t.goto(-170,280)
t.setheading(90)
t.pencolor(108,158,253)
#t.fillcolor("white")
t.pensize(7)
t.pendown()
#t.begin_fill()
t.circle(-180,180)
#print(t.pos())
t.setheading(-80)
t.goto(210,140)
t.setheading(-160)
#print(t.pos())
t.circle(-600,39)
#print(t.pos())
t.goto(-170,280)
#t.end_fill()
t.setheading(85)
t.circle(-180,20)
#print(t.pos())
#蓝色条
t.fillcolor(108,158,253)
t.begin_fill()
t.setheading(30)
t.circle(-330,60)
#print(t.pos())
t.setheading(-85)
t.goto(190,280)
t.setheading(150)
t.circle(350,61)
t.goto(-154,340)
t.end_fill()
t.penup()
t.pencolor('white')
t.pensize(15)
t.goto(-70,340)
t.setheading(17)
t.pendown()
t.circle(-300,31)
#脸
t.penup()
t.pensize(3)
t.goto(-88.5,214.7)
t.pencolor(108,158,253)
t.fillcolor(246,233,225)
t.pendown()
t.begin_fill()
t.goto(-108,304.3)
t.setheading(20)
t.circle(-350,40)
t.setheading(-110)
t.goto(105,214.7)
t.circle(-103,139)
t.end_fill()

#五官
t.penup()
t.pensize(3)
t.pencolor(108,158,253)
t.goto(-80, 290)
t.setheading(45)
t.pendown()
t.circle(-50,80)
t.penup()
t.goto(30, 290)
t.setheading(45)
t.pendown()
t.circle(-50,80)
#眼睛
t.penup()
t.goto(-45,270)
t.pendown()
t.dot(35,'white')
t.penup()
t.goto(-43,270)
t.pendown()
t.dot(32,(108,158,253))
t.penup()
t.goto(-43,270)
t.pendown()
t.dot(10,(122,219,251))
t.penup()
t.goto(-36,272)
t.pendown()
t.dot(5,(122,219,251))

t.penup()
t.goto(60,270)
t.pendown()
t.dot(35,'white')
t.penup()
t.goto(63,270)
t.pendown()
t.dot(32,(108,158,253))
t.penup()
t.goto(60,270)
t.pendown()
t.dot(10,(122,219,251))
t.penup()
t.goto(65,272)
t.pendown()
t.dot(5,(122,219,251))
#腮红
t.penup()
t.goto(-65,230)
t.pendown()
t.dot(35,(236,194,180))
t.penup()
t.goto(78,233)
t.pendown()
t.dot(35,(236,194,180))

#蓝色口罩
t.penup()
t.pencolor(108,158,253)
t.fillcolor(122,219,251)
t.begin_fill()
t.goto(-95,140)
t.pensize(7)
t.setheading(85)
t.pendown()
t.fd(75)
t.right(61)
t.fd(100)
t.right(40)
t.fd(93)
t.goto(110,130)
t.setheading(200)
t.circle(-310,40)
t.goto(-95,140)
t.end_fill()

#灰色口罩部分
t.penup()
t.pensize(7)
t.pencolor(108,158,253)
t.fillcolor(230,233,250)
t.begin_fill()
t.goto(190,280)
t.setheading(-110)
t.pendown()
t.fd(90)
t.setheading(-130)
t.circle(-195,95)
t.goto(-160,280)
t.setheading(30)
t.circle(-330,10)
t.setheading(-80)
t.circle(120,160)
t.setheading(-26)
t.circle(350,10)
t.goto(190,280)
t.end_fill()

#手臂右
t.penup()
t.pensize(7)
t.setheading(-20)
t.goto(110,135)
t.pendown()
t.circle(-380,22)
t.circle(-70,110)
t.circle(-100,48)
t.setheading(92)
t.circle(-78,60)
t.right(70)
t.circle(25,100)
t.right(70)
t.circle(-50,60)
#右手
t.penup()
t.pensize(3)
t.setheading(130)
t.fillcolor(253,232,203)
t.begin_fill()
t.goto(175.8,9.68)
t.pendown()
t.circle(-350,5)
t.left(70)
t.circle(-350,3)
t.left(-80)
t.circle(-60,35)
t.left(-25)
t.circle(-40,90)
t.left(-30)
t.goto(213.21,17.6)
t.setheading(-120)
t.circle(-25,100)
t.end_fill()

t.penup()
t.pensize(3)
t.setheading(85)
t.fillcolor(253,232,203)
t.begin_fill()
t.goto(175,80)
t.pendown()
t.fd(10)
t.circle(10,180)
t.left(10)
t.fd(10)
t.goto(175,80)
t.end_fill()


#手臂左
t.penup()
t.pensize(7)
t.setheading(200)
t.goto(-95,135)
t.pendown()
t.circle(350,22)
t.circle(70,110)
t.circle(100,48)
t.setheading(85)
t.circle(78,52)
t.setheading(220)
t.circle(-25,100)
t.right(-70)
t.circle(50,60)
#左手
t.penup()
t.pensize(3)
t.setheading(130)
t.fillcolor(253,232,203)
t.begin_fill()
t.goto(-140.33,15)
t.pendown()
t.setheading(60)
t.circle(-350,5)
t.left(-70)
t.circle(350,3)
t.left(80)
t.circle(60,35)
t.left(25)
t.circle(40,90)
t.left(-30)
t.goto(-176.6,15)
t.setheading(-70)
t.circle(18,135)
t.end_fill()

t.penup()
t.pensize(3)
t.setheading(85)
t.fillcolor(253,232,203)
t.begin_fill()
t.goto(-147,85)
t.pendown()

t.fd(10)
t.circle(-10,180)
t.left(-10)
t.fd(10)
t.goto(-147,85)
t.end_fill()

#腿
t.penup()
t.pensize(7)
t.goto(175,-62)
t.setheading(-85)
t.pendown()
t.circle(-800,20)
t.circle(-40,43)
t.setheading(-40)
t.circle(-80,60)
t.setheading(-140)
t.circle(-45,50)
t.setheading(160)
t.circle(-180,32)
t.setheading(95)
t.goto(41.07,-362.35)
t.setheading(105)
t.circle(-800,13)
t.setheading(-93)
t.circle(-800,13)
t.setheading(-85)
t.fd(35)
t.setheading(-132)
t.circle(-180,30)
t.setheading(175)
t.circle(-48,60)
t.setheading(85)
t.circle(-80,55)
t.setheading(160)
t.circle(-40,43)
t.setheading(106)
t.circle(-800,20)

#细节
t.penup()
t.pencolor(122,219,251)
t.goto(0,450)
t.pendown()
t.pensize(20)
t.setheading(-90)
t.fd(55)


t.penup()
t.goto(0,90)
t.setheading(-97)
t.pendown()
t.circle(800,19)

t.penup()
t.goto(-141,-70)
t.setheading(-20)
t.pendown()
t.circle(180,40)

t.penup()
t.setheading(-30)
t.pendown()
t.circle(180,57)

t.penup()
t.goto(-90.31,-361.86)
t.setheading(-30)
t.pendown()
t.circle(60,61)

t.penup()
t.goto(48,-362.86)
t.setheading(-31)
t.pendown()
t.circle(68,68)

#爱心
t.penup()
t.goto(110, 75)
t.pencolor("brown")
t.pensize(1)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.setheading(35)
t.circle(-8, 180)
t.circle(-60, 24)
t.setheading(110)
t.circle(-60, 24)
t.circle(-8, 180)
t.end_fill()
t.hideturtle()

t.penup()
t.pencolor((252,204,198))
t.goto(53, 5)
t.pendown()
t.write('XDF', font=('Arial', 30, 'bold'))
t.done()



