"""
#Pseudocode

FUNCTION Factorial(n: INTEGER) RETURNS INTEGER
    IF n = 0
        THEN
            Result <- 1
    ELSE
        Result <- n * Factorial(n-1)
    ENDIF
    RETURN Result
ENDFUNCTION
"""
"""
def Factorial(n):
    global Result
    if n == 0:
        Result = 1
    else:
        Result = n*Factorial(n-1)
    return Result

print(Factorial(10))
"""


"""
PROCEDURE Iterative(n: INTEGER) 
    FOR count <- n TO 1 STEP -1
        OUTPUT count
    NEXT count
ENDPROCEDURE

PROCEDURE Recursive(n: INTEGER)
    IF n > 0
        THEN
            OUTPUT n
            CALL Recursive(n-1)
    ENDIF
ENDPROCEDURE
"""

"""
def Recursive(n):
    if n > 0:
        print(n)
        Recursive(n-1)

print(Recursive(10))


def Iterative(n):
    for count in range(n,0,-1):
        print(count)

print(Iterative(10))
"""



AnimalFile = open("AnimalData.txt", "r")
ColourFile = open("ColourData.txt", "r")



"""split lines:
for line in AnimalFile:
    line = line.strip()
    Animals.append(line)
"""


global Animal, Colour
Animal = [] #To contain 20 elements
Colour = [] #To contain 10 elements


AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DTP):
    global AnimalTopPointer, ColourTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DTP)
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global AnimalTopPointer, ReturnData
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData
    
def ReadData():
    global AnimalTopPointer, ColourTopPointer
    RAnimals = open("AnimalData.txt", "r")
    for thisline in RAnimals:
        PushAnimal(thisline)
    RAnimals.close()

def PushColour(CTP):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = CTP
        ColourTopPointer += 1
        return True
    
def PopColour():
    global ColourTopPointer, ReturnData1
    ReturnData1 = 0
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData1 = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData1


def ReadData1():
    try:
        RAnimals = open("AnimalData.txt", "r")
        for line in AnimalFile:
            PushAnimal(line)
        RAnimals.close()
    except IOError:
        print("Please check if the file exists")

    try:  
        RColours = open("ColourData.txt", "r")
        for line1 in RColours:
            PushColour(line1)
        RColours.close()
    except IOError:
        print("Please check if the file exists")

def OutputItem():
    global ReturnData
    CurrentColour = PopColour(Colour)
    CurrentAnimal = PopAnimal(Animal)
    if ReturnData == 0:
        print("No animal")
    elif ReturnData1 == 0:
        print("No colour")
    else:
        print(CurrentColour,CurrentAnimal)

def MainProgram():
    global AnimalTopPointer, ColourTopPointer
    ReadData1()
    for x in range(4):
        OutputItem()
    

