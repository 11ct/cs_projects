NullP = -1

global StartP
global FreeP

class ListNode:
    def __init__(self, Data=None, Pointer=None):
        self.Data = Data
        self.Pointer = Pointer


global List


List = [ListNode() for j in range(7)]


def fun():
    for x in range(7):
        print(f"{x}: {List[x].Pointer}")


def InitialiseList():
    StartP = NullP
    FreeLP = 0
    for i in range(0, 6):
        List[i].Pointer = i+1
    List[6].Pointer = NullP


InitialiseList()

counter = 0
for item in List:
    print(f"{counter} --> {item.Pointer}")
    counter += 1






















def InsertNode(NewItem):
    global FreeLP, NullP
    if FreeLP != NullP:
        NewNodeP = FreeLP
        FreeLP = List[FreeLP].Pointer
        ThisNodePointer = StartP
        PreviousNodePointer = NullP
        while ThisNodePointer != NullP and List[ThisNodePointer].Data < NewItem:
            PreviousNodePointer = ThisNodePointer
            ThisNodePointer = List[ThisNodePointer].Pointer
        if PreviousNodePointer == StartP:
            List[NewNodeP].Pointer = StartP
            StartP = NewNodeP
        else:
            List[NewNodeP].Pointer = List[PreviousNodePointer].Pointer
            List[PreviousNodePointer].Pointer = NewNodeP



