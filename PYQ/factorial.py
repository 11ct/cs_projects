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
MaxAnimalSize = 20
MaxColourSize = 10
Animal = ["" for x in range(0,MaxAnimalSize)]
Colour = ["" for t in range(0, MaxColourSize)]


AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DTP):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DTP
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global AnimalTopPointer, ReturnData
    ReturnData = 0
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData
    
def ReadData():
    RAnimals = AnimalFile.read().splitlines()
    for counter in range(0,len(RAnimals)):
        print(RAnimals[counter])
    print(RAnimals.readlines())
    PushAnimal(ReadData())

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
    RAnimals = AnimalFile.read().splitlines()
    for counter in range(0,len(RAnimals)):
        print(RAnimals[counter])
    print(RAnimals.readlines())
    
    RColours = ColourFile.read().splitlines()
    for counter1 in range(0,len(RColours)):
        print(RColours[counter1])
    print(RColours.readlines())

    PushAnimal(ReadData())
    PushColour(ReadData1())


def OutputItem():
    CurrentColour = PopColour(Colour)
    CurrentAnimal = PopAnimal(Animal)
    if ReturnData == 0:
        print("No animal")
    elif ReturnData1 == 0:
        print("No colour")
    else:
        print(CurrentColour,CurrentAnimal)

def MainProgram():
    ReadData1()
    for x in range(0,3):
        OutputItem()
    

