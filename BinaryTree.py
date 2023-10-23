NullP = -1


class Tree:
    def __init__(self, Data=None, LeftP=None, RightP=None):
        self.Data = Data
        self.LeftP = LeftP
        self.RightP = RightP

global RootP, FreeP, RightP, LeftP

RootP = NullP

Tree = [Tree() for j in range(7)]

Found = False
SearchAnimal = input("")
Current = RootP


"""while Found == False:
    if SearchAnimal == Tree[Current].Data:
        print("Found")
        Found = True
    elif SearchAnimal > Tree[Current].Data:
        Current = RightP[Current]
    elif SearchAnimal < Tree[Current].Data:
        Current = LeftP[Current]"""


def InitialiseTree():
    RootP = NullP
    FreeP = 0
    for i in range(6):
        Tree[i].LeftP = i+1
    Tree[6].LeftP = NullP

InitialiseTree()

for item in Tree:
    print(item.LeftP)
    




