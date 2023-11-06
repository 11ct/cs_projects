class Courses:

    def __init__(self,CourseTitle="", MaxStudent=0, NumberOfLessons=0, CourseLesson=[], CourseAssessment=""):
        self.CourseTitle = CourseTitle
        self.MaxStudent = MaxStudent
        self.NumberOfLessons = NumberOfLessons
        self.CourseLesson = CourseLesson
        self.CourseAssessment = CourseAssessment

    def AddLesson():
        pass

    def AddAssessment():
        pass

    def OutputCourseDetails():
        pass
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