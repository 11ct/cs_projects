import Course


course1 = Course.Courses("Object Oriented Programming", 30)
lesson1 = Course.Lesson("Introduction to OOP", 60, False)
lesson2 = Course.Lesson("Inheritance and Polymorphism", 90, True)
finalassessment = Course.Assessment("Final Exam", 100)


course1.AddLesson(lesson1)
course1.AddLesson(lesson2)
course1.AddAssessment(finalassessment)

course1.OutputCourseDetails()

"""
print(f"\nCourse Title: {course1.GetCoursesTitle()}")
print(f"Max Student: {course1.GetMaxStudent()}")
print(f"Number of Lessons: {course1.GetNumberOfLessons()}")


for Lesson_num, Lesson in course1.GetCourseLesson().items():
    print(f"Lesson: {Lesson_num}")
    Lesson.OutputLessonDetails()
if course1.GetCourseAssessment() is not None:
    print(f"\nAssessment Title: {course1.GetCourseAssessment().GetAssessmentTitle()}")
    print(f"Max Marks: {course1.GetCourseAssessment().GetMaxMarks()}")
"""

course2 = Course.Courses("Social Works and Social Administration", 100)
lesson3 = Course.Lesson("Administrative Law", 180, False)
finalexam = Course.Assessment("Final Exam", 100)

course2.AddLesson(lesson1)
course2.AddLesson(lesson3)
course2.AddAssessment(finalexam)

