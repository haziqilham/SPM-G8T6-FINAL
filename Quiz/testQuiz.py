import unittest
from quiz import Quiz
from unittest import mock


class TestQuiz(unittest.TestCase):
    def setUp(self):
        question1 = {
            'question_id': 1,
            'question': 'How many cartridges are there in Xerox Printer?',
            'marks': 2
        }

        question2 = {
            'question_id': 2,
            'question': 'A Xerox Printer can print double-sided',
            'marks': 2
        }
        questions = [question1, question2]

        self.s = Quiz(quiz_id=1, quiz_name='Chapter 1 Quiz', duration=60,
                      graded=True, passing_mark=50)

    def tearDown(self):
        self.s = None

    # Converts to JSON, so its easier for front end later
    def test_ToDict(self):
        #Testing of to_dict
        self.assertEqual(self.s.toDict(), {
            'quiz_id': 1,
            'quiz_name': 'Chapter 1 Quiz',
            'duration': 60,
            'graded': True,
            "passing_mark": 50,
            }
        )

    def test_updateScore(self):
        self.assertEqual(self.s.updateScore(10), 10)

    def test_computeScore(self):
        #Mock 2 Question Class
        Question1 = mock.MagicMock()
        Question1.computeMarks.return_value = {
            'marks': 2
        }

        Question2 = mock.MagicMock()
        Question2.computeMarks.return_value = {
            'marks': 0
        }

        questionMarksList = [Question1.computeMarks(), Question2.computeMarks()]
        
        #Testing of computeScore
        self.assertEqual(self.s.computeScore(questionMarksList), 2)
