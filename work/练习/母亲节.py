import time
import turtle as t

t.screensize(960, 720)
t.bgpic('母亲节.png')
t.pensize(3)
t.tracer(0)  # 设置为手动将图片更新到屏幕上
t.colormode(255)  # 设置颜色模式为255
t.hideturtle()

for i in range(800):
    # ========4.清除屏幕=========
    t.clear()
    # =========1.绘制图片============
    t.pencolor(254, 220, 224)
    t.seth(0)
    t.penup()
    t.goto(0, i - 300 + i * 2)
    t.pendown()
    t.fillcolor(254, 220, 224)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.right(90)
    t.fd(150)
    t.pencolor('black')
    t.penup()
    t.goto(-50, i - 220 + i * 2)
    t.pendown()
    #写字
    t.write("妈妈，母亲节快乐", move=False, align='left', font=('Arial', 10, 'normal'))

    # =========2.图片更新到屏幕上=========
    t.update()
    # ========3.等待=========
    time.sleep(1 / 30)

t.done()
