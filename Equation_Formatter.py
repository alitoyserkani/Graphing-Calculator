#GC Formula Formatter

# Harshil Parikh

# Gets equation and creates an array with x and y values


# Imports
from math import *
import sys


#CREDITS GOES TO SOME KIND STRANGER ON THE NET FOR INSPIRATION ON
#FUNCTIONS f(x, formulaL), f_prime(x, formulaL) and newt(x, n, formulaL)
def f(x, formulaL):
    eqn1 = ""
    for eqnC in formulaL:
        if eqnC == "x":
           eqnC = "(" + str(x) + ")"
        eqn1 += eqnC

    try:
        x1 = eval(eqn1)
    except:
        return "ERROR"
        pass
    return x1

def f_prime(x, formulaL):
    h = 0.00000000000000000001
    xh = x + h
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
        return 0
        pass

    num = x1 - x2
    m = (num / h) * -1
    return m

def newt(x,n, formulaL):
    for i in range(n):
        if f_prime(x, formulaL) == 0:
            return x
        if f(x, formulaL) == "ERROR":
            continue
        x -= f(x, formulaL)/f_prime(x, formulaL)
    return x

def findXInts(coord, formulaL):
    xInts = []
    for xY in range(len(coord)):
        xY = coord[xY][0]
        x = newt(xY,1000, formulaL)
        if f(x, formulaL) != "ERROR":
            if f(x, formulaL) == 0:
                if int(x) not in xInts:
                    xInts.append(int(x))
    return xInts

def analyzationOfFunction(formula, coord, lowX, highX, yInt, xInt):
    name = formula
    domain = "Domain = {x| "
    yV = []
    for undefined in range(len(coord)):
        if coord[undefined][1] == "Error":
            domain += " x =\= " + str(coord[undefined][0]) + ", "
        else:
            yV.append(coord[undefined][1])
    domain += "xER}"
    rangeY = "Range = {y| "
    rangeY += str(min(yV)) + " <= y <= " + str(max(yV)) + ", yER}"
    file = open("function.txt", "a")
    file.write("ANALYZING THE FUNCTION: f(x) = " + name + "\n")
    file.write("NOTE: This is only an analyzing of the graph that is in the X-Range \n")
    file.write(domain + "\n")
    file.write(rangeY + "\n")
    if yInt == "Error":
        file.write("Their is no y-int \n")
    else:
        file.write("The y-int is: " + str(yInt) + "\n")

    for xInts in range(len(xInt)):
        file.write("Approximate x-int in graph range is: " + str(xInt[xInts]) + "\n")
    if len(xInt) == 0:
        file.write("Their is no x-int \n")
    file.write("\n")
    file.write("These are coordintes in range " + str(lowX) + " to " + str(highX) + ": \n")
    file.write(str(coord))
    
    file.close()


def coordinates(formula, lowX, highX):
    chars = ["^"]
    charsR = ["**"]

    originalFormula = formula

    #formula = input("Please input the equation you would like graphed: ")
    formula = formula.replace(" ", "")
        
    xRange = [lowX, highX]
    
    for char in chars:
        formula = formula.replace(char, charsR[chars.index(char)])

    for num in range(0, 10):
        formula = formula.replace(str(num) + "x", str(num) + "*x")
        formula = formula.replace(str(num) + "(", str(num) + "*(")
        formula = formula.replace(str(num) + "s", str(num) + "*s")
        formula = formula.replace(str(num) + "c", str(num) + "*c")
        formula = formula.replace(str(num) + "t", str(num) + "*t")
        formula = formula.replace(str(num) + "a", str(num) + "*a")

    formula = formula.replace("x" + "(", "x*(")
    formula = formula.replace(")" + "x", ")*x")
    formula = formula.replace(")" + "(", ")*(")
    formula = formula.replace(")s", ")*s")
    formula = formula.replace(")c", ")*c")
    formula = formula.replace(")t", ")*t")
    formula = formula.replace(")a", ")*a")

    formulaL = list(formula)
    eqn = ""
    coord = []
    yInt = 0
        
    for coords in range(xRange[1] - xRange[0] + 1):
        coord.append([xRange[0] + coords])

    for coordY in range(len(coord)):
        for eqnC in formulaL:
            if eqnC == "x":
               eqnC = "(" + str(coord[coordY][0]) + ")"
            
            eqn += eqnC

        try:
            eqn = eval(eqn)
        except ZeroDivisionError:
            eqn = "Error"
        except ValueError:
            eqn = "Error"
            
        coord[coordY].append(eqn)
        if coord[coordY][0] == 0:
            yInt = eqn
        eqn = ""

    analyzationOfFunction(originalFormula, coord, lowX, highX, yInt, findXInts(coord, formulaL))

    return coord, formulaL
