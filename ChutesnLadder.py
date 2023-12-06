import math
import turtle
import random
import winsound
import os
from time import sleep

#screen
wn = turtle.Screen()
wn.bgcolor("cyan")
wn.title("!!CHUTESnLADDER!!")

SQUARE_SIZE = 100
SquareNum = 0
offset = SQUARE_SIZE*13
turtle.setworldcoordinates(-100,-100, 1600, 1600)
gridTurtle = turtle.Turtle(visible=False)
gridTurtle.speed(200)
gridTurtle.penup()
gridTurtle.goto(0,0)
gridTurtle.pendown()

# Turtle that will write numbers on the grid
numTurtle = turtle.Turtle(visible=False)
numTurtle.penup()
numTurtle.speed(200)

# Arrow that spins around on the spinner table
posTurtle = turtle.Turtle(shape="arrow", visible=False)
posTurtle.speed(10)
posTurtle.color("red")

# The Title!
titleMsg = turtle.Turtle(visible=False)
titleMsg.fillcolor("blue")
titleMsg.penup()
titleMsg.goto(offset-offset/2,offset+200)
titleMsg.write("!CHUTES AND LADDER!", align = "center", font=("Arial", 18,"bold"))

# Write messages to the players
msgTurtle = turtle.Turtle(visible=False)
msgTurtle.penup()

# Button that serves to activate the game!
spinButton = turtle.Turtle(shape="circle", visible=False)
spinButton.fillcolor("white")
spinButton.penup()
spinButton.goto(offset,offset)


# Button that serves to randomize the players turns
RandomizeButton = turtle.Turtle(shape="circle", visible=False)
RandomizeButton.fillcolor("purple")
RandomizeButton.penup()
RandomizeButton.goto(offset-offset/2-50,offset)


#Player list
ColorsAvailable = ["red", "blue", "green", "yellow"]
PlayerList = []
playerNum = 0

redTurtle = turtle.Turtle(shape = "turtle", visible = False)
redTurtle.penup()
redTurtle.goto(offset-1200,offset-1350)
redTurtle.speed(5)
redTurtle.color("red")
redTurtle.showturtle()

blueTurtle = turtle.Turtle(shape = "turtle", visible = False)
blueTurtle.penup()
blueTurtle.goto(offset-1100,offset-1350)
blueTurtle.speed(10)
blueTurtle.color("blue")
blueTurtle.showturtle()

yellowTurtle = turtle.Turtle(shape = "turtle", visible = False)
yellowTurtle.penup()
yellowTurtle.goto(offset-1000,offset-1350)
yellowTurtle.speed(10)
yellowTurtle.color("yellow")
yellowTurtle.showturtle()

greenTurtle = turtle.Turtle(shape = "turtle", visible = False)
greenTurtle.penup()
greenTurtle.goto(offset-900,offset-1350)
greenTurtle.speed(10)
greenTurtle.color("green")
greenTurtle.showturtle()
#ChutesDict is for values going down
chutesDict = {5:1,17:2,29:3,48:26,49:11,56:53,62:19,64:60,87:24,93:73,95:75}
#LaddersDict values going up
laddersDict = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:100}
winscore = 100
chuteTurtle = turtle.Turtle(visible=False)
chuteTurtle.shape('triangle')
chuteTurtle.setheading(270)
chuteTurtle.color("red")
chuteTurtle.penup()


ladderTurtle = turtle.Turtle(visible=False)
ladderTurtle.shape('triangle')
ladderTurtle.setheading(90)
ladderTurtle.color("green")
ladderTurtle.penup()


positionDict = {}

playerPos = {'red': 0, 'blue': 0, 'yellow': 0, "green" : 0}

# Ask number of players in a dialog box


screen = turtle.Screen()
NumPlayers = screen.textinput("Welcome to Chutes N Ladders", "How many players (1 - 4)?")
if NumPlayers is None or int(NumPlayers) < 1 or int(NumPlayers) > 4:
    print("Goodbye! but try again!")
    screen.clear()
    screen.bye()
    exit
else:
    for j in range(int(NumPlayers)):
        PlayerList.append(ColorsAvailable[j])
    print(PlayerList)
    msgTurtle.goto(offset-offset/2,offset+100)
    MessageForPlayers_1 = "Players! choose your colored piece,\n and press the RANDOMIZE button"
    msgTurtle.write(MessageForPlayers_1, align = "center", font=("Arial", 12,"bold"))
    msgTurtle.goto(offset-offset/2,offset+50)
    MessageForPlayers_2 = "Color choices are: " + str(PlayerList)
    msgTurtle.write(MessageForPlayers_2, align = "center", font=("Arial", 12,"bold"))
    msgTurtle.goto(offset-offset/2+60,offset-100)
    msgTurtle.write("RANDOMIZE!", align = "right", font=("Arial", 18, "bold"))
    RandomizeButton.showturtle()

def RandomizeTurns(x,y):
    msgTurtle.clear()
    msgTurtle.goto(offset-offset/2,offset)
    print(str(PlayerList))
    random.shuffle(PlayerList)
    Message_Order_of_Players = "You will go in this order\n" + str(PlayerList)
    msgTurtle.write(Message_Order_of_Players, align = "center", font=("Arial", 12,"bold"))
    spinButton.fillcolor(PlayerList[0])
    msgTurtle.goto(offset,offset-270)
    start_message = "Player " + PlayerList[0] + "\nPress the center button to start!"
    msgTurtle.write(start_message, align = "center",  font=("Verdana", 12, "bold"))
    RandomizeButton.hideturtle()

def song1():
    winsound.PlaySound("sound1", winsound.SND_FILENAME)

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
    positionDict[SquareNum] = tpos[0] + SQUARE_SIZE/2, tpos[1] + SQUARE_SIZE/3

def makeLeftSquare():
    global SquareNum
    gridTurtle.setheading(180)
    for i in range(4):
        gridTurtle.forward(SQUARE_SIZE)
        gridTurtle.right(90)
    SquareNum+=1
    tpos = gridTurtle.position()
    writeNuminBox(SquareNum,tpos[0] - SQUARE_SIZE/2, tpos[1] + SQUARE_SIZE/3)
    positionDict[SquareNum] = tpos[0] - SQUARE_SIZE/2, tpos[1] + SQUARE_SIZE/3

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
    spinButton.showturtle()
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
        spinBoard.write(i+1, font=("Verdana", 10, "bold"))
    
def SpinIt(x,y):
    global playerNum
    msgTurtle.clear()
    randomSpin = random.randint(1,12)
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
    song1()
    # Move player playerNum by b+1 units
    Move(playerNum, b+1)
    checkifGameOver()
    playerNum += 1
    if playerNum == len(PlayerList):
        playerNum = 0

    spinButton.fillcolor(PlayerList[playerNum])
    spinnerMsg = "Awesome! " + PlayerList[playerNum] + " goes next!"
    msgTurtle.write(spinnerMsg, align = "center",  font=("Verdana", 12, "bold"))


def placeChutes():
    #stamp every circle at a chutes point
    for chute in chutesDict.keys():
        chuteTurtle.goto(positionDict[chute])
        chuteTurtle.stamp()
        chuteTurtle.pendown()
        chuteTurtle.goto(positionDict[chutesDict[chute]])
        chuteTurtle.penup()
    
def placeLadders():
    for ladder in laddersDict.keys():
            ladderTurtle.goto(positionDict[ladder])
            ladderTurtle.stamp()
            ladderTurtle.pendown()
            ladderTurtle.goto(positionDict[laddersDict[ladder]])
            ladderTurtle.penup()


def Move(playerNum, rollednumber):
    if PlayerList[playerNum] == 'red':
        if playerPos['red'] + rollednumber <= winscore:
            playerPos['red'] = playerPos['red'] + rollednumber
            redTurtle.goto(positionDict[playerPos['red']])
            #put chutes and ladder dict method
            playerPos['red'] = checkForChutesandLadders('red')
            redTurtle.goto(positionDict[playerPos['red']])
    elif PlayerList[playerNum] == 'blue':
        if playerPos['blue'] + rollednumber <= winscore:
            playerPos['blue'] = playerPos['blue'] + rollednumber
            blueTurtle.goto(positionDict[playerPos['blue']])
            playerPos['blue'] = checkForChutesandLadders('blue')
            blueTurtle.goto(positionDict[playerPos['blue']])
    elif PlayerList[playerNum] == 'yellow':
        if playerPos['yellow'] + rollednumber <= winscore:
            playerPos['yellow'] = playerPos['yellow'] + rollednumber
            yellowTurtle.goto(positionDict[playerPos['yellow']])
            playerPos['yellow'] = checkForChutesandLadders('yellow')
            yellowTurtle.goto(positionDict[playerPos['yellow']])
    elif PlayerList[playerNum] == 'green':
        if playerPos['green'] + rollednumber <= winscore:
            playerPos['green'] = playerPos['green'] + rollednumber
            greenTurtle.goto(positionDict[playerPos['green']])
            playerPos['green'] = checkForChutesandLadders('green')
            greenTurtle.goto(positionDict[playerPos['green']])
       


def checkForChutesandLadders(playercolor):
    currentplayerPosition = playerPos[playercolor]
    for chute in chutesDict:
        if chute == currentplayerPosition:
            currentplayerPosition = chutesDict[chute]
    for ladder in laddersDict:
        if ladder == currentplayerPosition:
            currentplayerPosition = laddersDict[ladder]
    return currentplayerPosition




def checkifGameOver():
    for player in playerPos:
        if playerPos[player] == winscore:
            winningMessage = player.upper() + ": You Won the game"
            msgTurtle.write(winningMessage, align = "right", font=("Arial", 18, "bold"))
            sleep(4)
            exit()
            #print("You won", player, playerPos[player])
        




        





createGrid()
placeChutes()
placeLadders()
CreateSpinner()
RandomizeTurns(0,0)
""" spinButton.onclick(SpinIt) 
RandomizeButton.onclick(RandomizeTurns)  """

while True:
    SpinIt(100,100)
    print(playerPos)

print(playerPos)

turtle.done()

    