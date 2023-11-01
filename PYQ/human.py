class Humans():
    def __init__(self, DOB="", Nationality="", Height="",Weight=""):
        self.DOB = DOB
        self.Nationality = Nationality
        self.Height = Height
        self.Weight = Weight

Human = Humans()

class Students(Human):
    def __init__(self, DOB, Nationality, Stream="",PreviousSchool=""):
        super().__init__(DOB, Nationality)
        self.Stream = Stream
        self.PreviousSchool = PreviousSchool
        
YoMama = Humans("11/11/1111", "American")
YoMama.Height = 1111
YoMama.Weight = 111

print(YoMama.DOB)

Grace = Students("11/11/1234", "Cambodian", "13E", "Hogwarts")


data = ""



file = open("studentdb.csv", "w")
file.write(data)
file.close()




