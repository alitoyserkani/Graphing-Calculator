#DRAW THE GRAPH

# Harshil Parikh

# Given x and y values this python file draws the function along with updating
# the tangent line based on current x pos of the mouse

from tkinter import *
from time import *
from math import *

root = Tk()
root.title("Grapher")
#root.attributes("-fullscreen", True)

yLines = 50
xLines = 50

widthR = int(root.winfo_screenwidth()/2) % yLines
width  = root.winfo_screenwidth() - 2*widthR

heightR = int(root.winfo_screenheight()/2) % xLines
height = root.winfo_screenheight() - 2*heightR

screen = Canvas(root, width =width ,height = height)
screen.pack()
    
#Calling the exit call
def exitCall(event):
    if event.keysym == "Escape":
        root.destroy()

def drawTangent(x, y):
    global tangent, tanText
    
    formulaL = formulaG
    formula = formulaG
    h = 0.001
    xh = x+h

    eqn1, eqn2 = "", ""
    for eqnC in formulaL:
        eqnD = eqnC
        if eqnC == "x":
           eqnC = "(" + str(x) + ")"
           eqnD = "(" + str(xh) + ")"
        
        eqn1 += eqnC
        eqn2 += eqnD
    try:
        x1 = eval(eqn1)
        x2 = eval(eqn2)
    except:
        try:
            screen.delete(tangent, tanText)
        except:
            pass
        return None
    num = x1 - x2
    m = (num / h) * -1

    
    endingLine = -1*m*x + x1

    mR = round(m, 5)
    endingLineR = round(endingLine, 5)

    lx1 = (-1*m*width/2 + float(endingLine)) /scaler
    lx2 = (m*width/2 + float(endingLine)) / scaler

    tanTX = x
    tanTY = (m*tanTX + float(endingLine)) / scaler

    if x > 0:
        tanTX -= 50
    else:
        tanTX += 50

    if tanTY > 0:
        tanTY -= 50
    else:
        tanTY += 50

    if endingLine >= 0:
        endingLineR = "+ " + str(endingLineR)

    tanTX, tanTY = cartToScreen(tanTX, tanTY)

    tangentF = "y= " + str(mR) + "x " + str(endingLineR)

    #print("LINE IS : y= " + str(m) + "x " + str(endingLine))
    if tangent != None:
        screen.delete(tangent, tanText)
        
    tangent = screen.create_line(0, height/2-lx1, width,  height/2-lx2,fill="green")
    tanText = screen.create_text(tanTX, tanTY, text=tangentF)

def getMousePosition( event ):
    global ball, textL    
    xMouse = int(event.x)

    if xMouse > len(coordsG)-1:
        xMouse = len(coordsG)-1
    elif xMouse < 0:
        xMouse = 0

    ballY = coordsG[xMouse][1]
    if ballY == "Error":
        ballY = 0
    ballYScreen = height/2 - ballY

    if ball != None:
        screen.delete(ball, textL)

    drawTangent(xMouse - width/2, ballY)
    ball = screen.create_oval(xMouse-5, ballYScreen-5, xMouse+5, ballYScreen+5, fill="yellow")
    textL = screen.create_text(xMouse, ballYScreen+10, text="(" + str(coordsG[xMouse][0]) + ", " + str(int(scaler*ballY)) + ")")
    screen.update()

def cartToScreen(cartX, cartY):
    return cartX + width/2, height/2 - cartY

def scaling(coords):
    global scaler
    
    yArray = []
    for yValues in range(len(coords)):
        if coords[yValues][1] != "Error":
            yArray.append(abs(coords[yValues][1]))

    y = max(yArray)
    yAvg = sum(yArray)/len(yArray)
    if yAvg >= yArray[0] or yAvg <= yArray[0]:
        yScale = height/4
    else:
        yScale  = height/2
    scaler = 1

    if y > yScale:
        scaler = y / yScale

    elif y < 50:
        scaler = y / (yScale/7)

    for scaling in range(len(coords)):
        if coords[scaling][1] != "Error" and coords[scaling][1] != 0:
            coords[scaling][1] = coords[scaling][1] / scaler

    for y in range(0, height+1, yLines):
        screen.create_line(0, y, width, y, width=1, fill="gray")
        screen.create_text(width/2+10, y, text=round((scaler*(height/2-y)), 2))

    for x in range(0, width+1, xLines):
        screen.create_line(x, 0, x, height, width=1, fill="gray")
        screen.create_text(x, height/2+15, text=round((x - width/2), 2))

    screen.create_line(width/2,0, width/2,height,width=3)
    screen.create_line(0,height/2, width,height/2,width=3)

def drawGraph(coords, lowX, highX, formulaL):
    global coordsG, ball, formulaG, tangent

    formulaG = formulaL
    coordsG = coords
    ball = None
    tangent = None
    asymptoteLineLength = 20
    
    for coordA in range(len(coords)-1):
        cartX = coords[coordA][0]
        cartY = coords[coordA][1]
        cartX2 = coords[coordA+1][0]
        cartY2 = coords[coordA+1][1]
        if cartY2 != "Error" and cartY != "Error":
            sX, sY = cartToScreen(cartX, cartY)
            sX2, sY2 = cartToScreen(cartX2, cartY2)
            #screen.create_oval(sX-1, sY-1,sX+1, sY+1,
            #                   fill="black")
            screen.create_line(sX, sY, sX2, sY2, smooth=True,width=2, fill = "blue")
        elif cartY == "Error":
            for asyY in range(0, height, int(height/yLines)):
                if (asyY / (height/yLines)) % 2 == 0:
                    screen.create_line(cartX+width/2,asyY, cartX+width/2,asyY+asymptoteLineLength,fill="yellow", width=2)
            screen.create_text(cartX+width/2, height-25, text="x = " + str(cartX))

    root.bind("<Key>", exitCall)
    screen.bind("<Motion>", getMousePosition )
    screen.update()
