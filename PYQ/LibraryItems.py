import datetime

class LibraryItems:

    def __init__(self, Title="", AuthorArtist="", ItemID="", OnLoan=False,DueDate=datetime.date.today()):
        self.__Title = Title
        self.__AuthorArtist = AuthorArtist
        self.__ItemID = ItemID
        self.__OnLoan = OnLoan
        self.__DueDate = DueDate

    #Define getters and setters
    def GetTitle(self):
        return self.__Title
    
    def GetAuthorArtist(self):
        return self.__AuthorArtist
    
    def GetItemID(self):
        return self.__ItemID
    
    def GetOnLoan(self):
        return self.__OnLoan
    
    def GetDate(self):
        return self.__DueDate
    
    def Borrowing(self):
        self.__OnLoan = True
        self.__Date = self.__Date + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def PrintDetail(self):
        print("Title" + self.__Title)
        print("AuthorArtist" + self.__AuthorArtist)
        print("Item ID" + self.__ItemID)
        print("On Loan" + self.__OnLoan)
        print("Due Date" + self.__DueDate)


class Books(LibraryItems):

    def __init__(self, Title="", AuthorArtist="", ItemID=""):
        LibraryItems.__init__(self, Title, AuthorArtist, ItemID)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return self.__IsRequested
    
    def GetRequestedBy(self):
        return self.__RequestedBy
    
    def Requesting(self, UserID):
        self.__IsRequested = True
        self.__RequestedBy = UserID
    
    def PrintDetail(self):
        LibraryItems.PrintDetail(self)
        print("Is Requested" + str(self.__IsRequested))
        print("Requested By" + str(self.__RequestedBy)) 


class CD(LibraryItems):

    def __init__(self, Title="",Genre="", AuthorArtist="", ReferenceNum="", Loan=""):
        super.__init__(self, Title, Genre, AuthorArtist, ReferenceNum, Loan)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return self.__IsRequested
    
    def GetRequestedBy(self):
        return self.__RequestedBy
    
    def Requesting(self, UserID):
        self.__IsRequested = True
        self.__RequestedBy = UserID
    
    def PrintDetail(self):
        LibraryItems.PrintDetail(self)
        print("Is Requested" + str(self.__IsRequested))
        print("Requested By" + str(self.__RequestedBy))
        


favourite_book = Books("The Iron Trial", "Cassandra Clare&Holly Black", "12345")


favourite_book.PrintDetail()
favourite_book.Borrowing()
print("\n")
favourite_book.Requesting("1100")
favourite_book.PrintDetail()
favourite_book.Returning()
print("\n")
favourite_book.PrintDetail()

