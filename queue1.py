EMPTYSTRING = ""
NullPointer = -1
MaxQueueSize = 8
FrontOfQueuePointer = 0
EndOfQueuePointer = 0
NumberInQueue = 0


Queue = ["" for x in range(MaxQueueSize)]

def InitialiseQueue():
    global FrontOfQueuePointer, EndOfQueuePointer, NumberInQueue
    FrontOfQueuePointer = NullPointer
    EndOfQueuePointer = NullPointer
    NumberInQueue = 0


