class Courses:

    def __init__(self,CourseTitle, MaxStudent):
        self.CourseTitle = CourseTitle
        self.MaxStudent = MaxStudent
        self.NumberOfLessons = 0
        self.CourseLesson = []
        self.CourseAssessment = None
    
    def GetCoursesTitle(self):
        return self.CourseTitle
    
    def GetMaxStudent(self):
        return self.MaxStudent
    
    def GetNumberOfLessons(self):
        return self.NumberOfLessons
    
    def GetCourseLesson(self):
        return self.CourseLesson

    def GetCourseAssessment(self):
        return self.CourseAssessment

    def AddLesson(self, Lesson):
        if self.NumberOfLessons < 50:
            self.NumberOfLessons += 1
            self.CourseLesson[self.NumberOfLessons] = Lesson
        else:
            print("Cannot add more than 50 lessons")

    def AddAssessment(self, Assessment):
        self.CourseAssessment = Assessment

    def OutputCourseDetails(self):
        print(f"\nCourse Title: {self.CourseTitle}")
        print(f"Max Student: {self.MaxStudent}")
        print(f"Number of Lessons: {self.NumberOfLessons}")

        for Lesson, Lesson_num in self.CourseLesson.items():
            print(f"Lesson {Lesson_num}")

        if self.CourseAssessment is not None:
            print("Assessment")
    #Define getters and setters


class Lesson:

    def __init__(self, LessonTitle="", DurationMinutes=0, RequiresLab=False):
        self.LessonTitle = LessonTitle
        self.DurationMinutes = DurationMinutes
        self.RequiresLab = RequiresLab

    def OutputLessonDetails(self):
        print("Title" + self.LessonTitle)
        print("Duration" + self.DurationMinutes)
        print("Requires Lab" + self.RequiresLab)



class Assessment:

    def __init__(self, AssessmentTitle="", MaxMarks=0):
        self.AssessmentTitle = AssessmentTitle
        self.MaxMarks = MaxMarks

    def OutputAssessmentDetails(self):
        print("Title" + self.AssessmentTitle)
        print("Max Marks" + self.MaxMarks)