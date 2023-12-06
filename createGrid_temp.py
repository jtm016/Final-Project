import math
import turtle
import random

SQUARE_SIZE = 100
SquareNum = 0
offset = SQUARE_SIZE*13
turtle.setworldcoordinates(-100,-100, 1600, 1600)
gridTurtle = turtle.Turtle(visible=False)
gridTurtle.speed(100)
gridTurtle.penup()
gridTurtle.goto(0,0)
gridTurtle.pendown()
# Turtle that will write numbers
numTurtle = turtle.Turtle(visible=False)
numTurtle.penup()
numTurtle.speed(100)

posTurtle = turtle.Turtle(shape="arrow", visible=False)
posTurtle.speed(10)
posTurtle.color("red")

spinButton = turtle.Turtle(shape="circle", visible=False)
spinButton.fillcolor("blue")
spinButton.penup()
spinButton.goto(offset,offset-250)
spinButton.write("Click the Center Button!", align = "center",  font=("Verdana", 12, "bold"))
spinButton.goto(offset,offset)
spinButton.showturtle()


def writeNuminBox(number,x,y):
        numTurtle.goto(x,y)
        font_size = 10
        numTurtle.write(number, font=("Arial", font_size, "bold"))

def makeRightSquare():
    global SquareNum
    for i in range(4):
        gridTurtle.forward(SQUARE_SIZE)
        gridTurtle.left(90)
    SquareNum = SquareNum + 1
    tpos = gridTurtle.position()
    writeNuminBox(SquareNum,tpos[0] + SQUARE_SIZE/2, tpos[1] + SQUARE_SIZE/3)
    
    
def makeLeftSquare():
    global SquareNum
    gridTurtle.setheading(180)
    for i in range(4):
        gridTurtle.forward(SQUARE_SIZE)
        gridTurtle.right(90)
    SquareNum+=1
    tpos = gridTurtle.position()
    writeNuminBox(SquareNum,tpos[0] - SQUARE_SIZE/2, tpos[1] + SQUARE_SIZE/3)

def createRightRow():
    gridTurtle.setheading(0)
    for k in range(10):
        makeRightSquare()
        gridTurtle.forward(SQUARE_SIZE)

    
def createLeftRow():
    for k in range(10):
        makeLeftSquare()
        gridTurtle.forward(SQUARE_SIZE)

def createGrid():
    for i in range(10):
        if i % 2 == 0:
            createRightRow()
            gridTurtle.left(90)
            gridTurtle.forward(SQUARE_SIZE)
        else:
            createLeftRow()
            gridTurtle.right(90)
            gridTurtle.forward(SQUARE_SIZE)

def CreateSpinner():
    spinBoard = turtle.Turtle()
    spinBoard.shape("turtle")
    spinBoard.speed(10)
    spinBoard.penup()
    spinBoard.hideturtle()

    for i in range(6):

        x = 200*math.cos(i*60*math.pi/180)
        y = 200*math.sin(i*60*math.pi/180)
        spinBoard.goto(offset+x/2,offset+y/2)
        spinBoard.pendown()
        spinBoard.goto(offset+3*x/4,offset+3*y/4)
        spinBoard.penup()
        spinBoard.goto(offset+x,offset+y)
        spinBoard.hideturtle()
        spinBoard.write(i+1, align = "center", font=("Verdana", 15, "bold"))
    
def SpinIt(x,y):
    randomSpin = random.randint(20,50)
    DEG_TO_RAD = math.pi/180
    posList = []
    b=0
    for k in range(6):
        posList.append([math.cos(k*60*DEG_TO_RAD), math.sin(k*60*DEG_TO_RAD)])
    for a in range(randomSpin):
        b = a % 6
        posTurtle.penup()
        posTurtle.goto(offset+150*posList[b][0], offset+150*posList[b][1])
        posTurtle.showturtle()
        posTurtle.setheading(b*60)
    spinButton.color("green")
    return (b+1)
    
    
createGrid()
CreateSpinner()
spinButton.onclick(SpinIt)

#SpinIt(random.randint(20,40))


turtle.done()

    