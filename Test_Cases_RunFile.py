# Harshil Parikh

# Can nearly interpret any function and can draw it
# Note: Holes and Vertical Asymptotes Dont function correctly

from Equation_Formatter import *
from Grapher import *

#COOL FUCNTIONS

#200cos(x/10) * (1/100*x)
#2000cos(x/0.01) * 1/x
#abs(x)
#((23x+56) * (x-500) / 3.14) * log(abs(x))
#((23x+56) * (x-500) / 3.14) * log(abs(x)) * 1/x
#(x-500)(x+1000)(x-123)(x^2-9)*1/x


# Get User Input For Formula
formula = input("What is the function you want analysed? f(x) = ")

# Get Values
lowX = int(-1*width/2)
highX = int(width/2)
coords, formulaL = coordinates(formula, lowX, highX)
scaling(coords)

# Draw Graph
drawGraph(coords, lowX, highX, formulaL)


