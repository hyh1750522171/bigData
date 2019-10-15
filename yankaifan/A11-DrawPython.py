from turtle import *

def drawSnake(rad,angle,len,neckrad):            #rad：半径  angle：弧度值

    for i in range(len):
       circle(rad,angle)                 #turtle.circle()  圆形运行
       circle(-rad,angle)
    circle(rad,angle/2)
    fd(rad)                               #turtle.fd()    直线运行
    circle(neckrad+1,180)
    fd(rad*2/3)

def main():
    setup(1300,800,0,0)
    pythonsize=10
    pensize(pythonsize)
    pencolor("blue")
    seth(-40)
    drawSnake(40,80,5,pythonsize/2)

main()