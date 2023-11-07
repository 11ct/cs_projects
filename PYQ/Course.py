class Courses:

    def __init__(self,CourseTitle, MaxStudent):
        self.__CourseTitle = CourseTitle
        self.__MaxStudent = MaxStudent
        self.__NumberOfLessons = 0
        self.__CourseLesson = {}
        self.__CourseAssessment = None
    
    def GetCoursesTitle(self):
        return self.__CourseTitle
    
    def GetMaxStudent(self):
        return self.__MaxStudent
    
    def GetNumberOfLessons(self):
        return self.__NumberOfLessons
    
    def GetCourseLesson(self):
        return self.__CourseLesson

    def GetCourseAssessment(self):
        return self.__CourseAssessment

    def AddLesson(self, Lesson):
        if self.__NumberOfLessons < 50:
            self.__NumberOfLessons += 1
            self.__CourseLesson[self.__NumberOfLessons] = Lesson
        else:
            print("Cannot add more than 50 lessons")

    def AddAssessment(self, Assessment):
        self.CourseAssessment = Assessment

    def OutputCourseDetails(self):
        print(f"\nCourse Title: {self.__CourseTitle}")
        print(f"Max Student: {self.__MaxStudent}")
        print(f"Number of Lessons: {self.__NumberOfLessons}")

        for Lesson_num, Lesson in self.__CourseLesson.items():
            print(f"Lesson: {Lesson_num}")
            Lesson.OutputLessonDetails()

        if self.__CourseAssessment is not None:
            print("Assessment")
            self.CourseAssessment.OutputAssessmentDetails()

    #Define getters and setters


class Lesson:

    def __init__(self, LessonTitle, DurationMinutes, RequiresLab):
        self.__LessonTitle = LessonTitle
        self.__DurationMinutes = DurationMinutes
        self.__RequiresLab = RequiresLab
    def GetLessonTitle(self):
        return self.__LessonTitle
    
    def GetDurationMinutes(self):
        return self.__DurationMinutes
    
    def GetRequiresLab(self):
        return self.__RequiresLab


    def OutputLessonDetails(self):
        print("\nLesson Title: " + self.__LessonTitle)
        print("Duration: " + str(self.__DurationMinutes))
        print("Requires Lab: " + str(self.__RequiresLab))





class Assessment:

    def __init__(self, AssessmentTitle="", MaxMarks=0):
        self.__AssessmentTitle = AssessmentTitle
        self.__MaxMarks = MaxMarks

    def GetAssessmentTitle(self):
        return self.__AssessmentTitle
    
    def GetMaxMarks(self):
        return self.__MaxMarks

    def OutputAssessmentDetails(self):
        print("Assessment Title: " + self.__AssessmentTitle)
        print("Max Marks: " + self.__MaxMarks)
