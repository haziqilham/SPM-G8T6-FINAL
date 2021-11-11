import unittest
from app import Options, User, Course, Prerequisites, Class, Chapter, Quiz, Question, Questiontf, Questionmcq, CourseProgression

# --------------------------------------------------------------------------------------------------------------
# Person-in-charge: Jun Hong

class TestUser(unittest.TestCase):
    def test_to_dict(self):
        user1 = User(user_name='marcus', name='marcus', designation='engineer', 
                        department='engineering', role='learner')
        self.assertEqual(user1.to_dict(),{
            'user_id': None,
            'user_name': 'marcus',
            'name': 'marcus',
            'designation':'engineer',
            'department':'engineering',
            'role':'learner'}
        )
# --------------------------------------------------------------------------------------------------------------
# Person-in-charge: Marcus

class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        course1 = Course(course_id = None, course_name='Intro to Engineering', archive_date=None)
        self.assertEqual(course1.to_dict(),{
            'course_id': None,
            'course_name': 'Intro to Engineering',
            'archive_date': None}
        )

class TestPrerequisites(unittest.TestCase):
    def test_to_dict(self):
        prereq1 = Prerequisites(course_id = 1, prereq_course_id = 2)
        self.assertEqual(prereq1.to_dict(),{
            'prereq_id':None,
            'course_id':1,
            'prereq_course_id':2}
        )
# --------------------------------------------------------------------------------------------------------------
# CLASS - Class
# Person-in-charge: Haziq

class TestClass(unittest.TestCase):
    def test_to_dict(self):
        class1 = Class(course_id = 1, trainer_id = 2, class_name='G1', capacity = 20, 
                        start_DateTime = '2021-10-27 12:00:00', end_DateTime = '2021-10-30 14:00:00',
                        start_enrollment = '2021-09-20 00:00:00', end_enrollment = '2021-09-30 00:00:00')
        self.assertEqual(class1.to_dict(),{
            'class_id':None,
            'course_id':1,
            'trainer_id':2,
            'class_name':'G1',
            'capacity':20,
            'start_DateTime':'2021-10-27 12:00:00',
            'end_DateTime':'2021-10-30 14:00:00',
            'start_enrollment':'2021-09-20 00:00:00',
            'end_enrollment':'2021-09-30 00:00:00'}
        )
# --------------------------------------------------------------------------------------------------------------
# CLASS - Chapter
# Person-in-charge: Claudia

class TestChapter(unittest.TestCase):
    def test_to_dict(self):
        chapter1 = Chapter(class_id = 1, chapter_name='Engineering Basics', order = 1, chapter_materials = 'Engineering Gear')
        self.assertEqual(chapter1.to_dict(),{
            'chapter_id':None,
            'class_id':1,
            'chapter_name':'Engineering Basics',
            'order':1,
            'chapter_materials':'Engineering Gear'}
        )
# --------------------------------------------------------------------------------------------------------------
# CLASS - Quiz
# Person-in-charge: Xinyi

class TestQuiz(unittest.TestCase):
    def test_to_dict(self):
        quiz1 = Quiz(chapter_id = 1, duration = 45, graded = True, passing_mark = 50)
        self.assertEqual(quiz1.to_dict(),{
            'quiz_id':None,
            'chapter_id':1,
            'duration':45,
            'graded':True,
            'passing_mark':50}
        )

class TestQuestion(unittest.TestCase):
    def test_to_dict(self):
        question1 = Question(quiz_id = 1, question = "Is it true that you don't have to wear protective gear?", marks = 2)
        self.assertEqual(question1.to_dict(),{
            'question_id':None,
            'quiz_id':1,
            'question':"Is it true that you don't have to wear protective gear?",
            'marks':2}
        )

class TestQuestiontf(unittest.TestCase):
    def test_to_dict(self):
        questiontf1 = Questiontf(question_tf_id = 1, corrected_value = False)
        self.assertEqual(questiontf1.to_dict(),{
            'question_tf_id':1,
            'corrected_value':False}
        )

class TestQuestionmcq(unittest.TestCase):
    def test_to_dict(self):
        questionmcq1 = Questionmcq(question_mcq_id = 2)
        self.assertEqual(questionmcq1.to_dict(),{
            'question_mcq_id':2}
        )

class TestOptions(unittest.TestCase):
    def test_to_dict(self):
        options1 = Options(question_mcq_id = 2, value = 'Goggles', corrected_value = False)
        self.assertEqual(options1.to_dict(),{
            'options_id':None,
            'question_mcq_id':2,
            'value':'Goggles',
            'corrected_value':False}
        )
# --------------------------------------------------------------------------------------------------------------
# CLASS - CourseProgression
# Person-in-charge: Xinyi


class TestCourseProgression(unittest.TestCase):
    def test_to_dict(self):
        progress1 = CourseProgression(user_id = 1, course_id = 1, class_id = 1, chapter_id = 1, 
                                        status = 'enrolled')
        self.assertEqual(progress1.to_dict(),{
            'cc_id':None,
            'user_id':1,
            'course_id':1,
            'class_id':1,
            'chapter_id':1,
            'status':'enrolled',
            'completion_date':None,
            'score':None}
        )
# --------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()
