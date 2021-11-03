import unittest
from app import User, Course, Prerequisites, Class, Chapter, Quiz, Question, Questiontf, Questionmcq, CourseProgression

class TestUser(unittest.TestCase):
    def test_to_dict(self):
        user1 = User(user_name='marcus', name='marcus', designation='engineer', department='engineering', role='learner')
        self.assertEqual(user1.to_dict(),{
            'user_id': None,
            'user_name': 'marcus',
            'name': 'marcus',
            'designation':'engineer',
            'department':'engineering',
            'role':'learner'}
        )

    def test_enroll(self):
        user1 = User(user_name='marcus', name='marcus', designation='engineer', department='engineering', role='learner')
        enroll = user1.enroll(2)



#class TestCourse(unittest.TestCase):

if __name__ == "__main__":
    unittest.main()