import datetime

class LibraryItems:

    def __init__(self, Title="", AuthorArtist="", ItemID="", OnLoan=False,DueDate=datetime.date.today()):
        self.__Title = Title
        self.__AuthorArtist = AuthorArtist
        self.__ItemID = ItemID
        self.__OnLoan = OnLoan
        self.__DueDate = DueDate

    #Define getters and setters
    def Output(self):
        print("———————————————————————————————————")
        print(f"Title: {self.Title}")
        print(f"Author: {self.Author}") 
        print(f"Reference Number: {self.ReferenceNum}") 
        print(f"Load: {self.Loan}")
        print(f"Date: {self.Date}")



#Child Book of Parent LibraryItem
class Books(LibraryItems):

    def __init__(self, Title, Author, ReferenceNum, Loan):
        super().__init__(Title, Author, ReferenceNum, Loan)
        if Loan:
            self.Requested = True

    def Output(self):
        super().Output()

        print(f"Requested: {self.Requested}")



#Child CD of Parent LibraryItem
class CD(LibraryItems):

    def __init__(self, Title, Author, ReferenceNum, Loan, Genre):
        super().__init__(Title, Author, ReferenceNum, Loan)
        self.Genre = Genre

    def Output(self):
        super().Output()

        print(f"Genre: {self.Genre}")


        


