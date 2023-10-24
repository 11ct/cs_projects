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

NullPtr = -1

#Insert a New Node into Binary Tree
def InsertNode(NewItem):
    if FreePtr != NullPtr:
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr].LeftPtr
        Tree[NewNodePtr].data = NewItem
        Tree[NewNodePtr].LeftPtr = NullPtr
        Tree[NewNodePtr].RightPtr = NullPtr
        if RootPtr == NullPtr:
            RootPtr = NullPtr
        else:
            ThisNodePtr = RootPtr
            while ThisNodePtr != NullPtr:
                PreviousNodePtr = ThisNodePtr
                if NewItem < Tree[ThisNodePtr].data:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPtr
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr].RightPtr
            if TurnedLeft:
                Tree[PreviousNodePtr].LeftPtr = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPtr = NewNodePtr
                
#Find a node in a binary tree
RootPointer = 0

def FindNode(SearchItem):
    ThisNodePointer = RootPointer
    while ThisNodePointer != NullPtr and Tree[ThisNodePointer].data > SearchItem:
        if SearchItem < Tree[ThisNodePointer].LeftPtr:
            ThisNodePointer = Tree[ThisNodePointer]
        else:
            ThisNodePointer = Tree[ThisNodePointer].RightPtr
    return ThisNodePointer





