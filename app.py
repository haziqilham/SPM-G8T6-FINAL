from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://admin:ilovespm88@spm-database.c3izrtomcbks.us-east-2.rds.amazonaws.com:3306/spm_database'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_name = db.Column(db.Varchar(50), nullable=False)
    name = db.Column(db.Varchar(50), nullable=False)
    designation = db.Column(db.Varchar(50), nullable=False)
    department = db.Column(db.Varchar(50), nullable=False)
    role = db.Column(db.Varchar(50), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def enroll(self, classid):
        #get Class info
        classinfo = Class.query.filter_by(class_id = classid).first()

        #get Course id from class info
        courseid = classinfo.Course_id
        #check Capacity
        if Class.checkCapacity(classid):
            #check prereq
            prereqs = Prerequisites.query.filter_by(course_id = courseid).all()
            #append all prereq into list
            if len(prereqs) > 0:
                prereqlist = []
                for i in prereqs:
                    prereqlist.append(i.prereq_course_id)

            #check user's existing course progress
            progress = CourseProgression.query.filter_by(user_id = self.user_id).all()
            #check that user is not currently in progress or enrolled into the course
            if len(progress) > 0:
                for i in progress:
                    if i.course_id == courseid:
                        if i.status == "ongoing" or i.status == "enrolled":
                            raise Exception("User is already enrolled into the course.")

            #append into completed list
            completedlist = []
            if len(progress) > 0:
                for i in progress:
                    if i.status == 'completed':
                        completedlist.append(i.course_id)

            #check that user meets all prereq
            if len(prereqlist) == 0 and len(completedlist) == 0:
                self.to_dict(self)
            else: 
                if len(prereqlist) > 0 and len(completedlist) < 1:
                    raise Exception("User does not meet the course requirements.")               
                else:
                    for i in prereqlist:
                        if i not in completedlist:
                            raise Exception("User does not meet the course requirements.")
                        else:
                            self.to_dict(self)


class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    course_name = db.Column(db.Varchar(50), nullable=False)
    archive_date = db.Column(db.Date)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result    

    def archivecourse(self):
        course = Course.query.filter_by(course_id = self.course_id).first()
        course.archive_date = dt.date.today()


class Prerequisites(db.Model):
    __tablename__ = 'prerequisites'

    prereq_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    prereq_course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Class(db.Model):
    __tablename__ = 'class'

    class_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False) 
    class_name = db.Column(db.Varchar(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    start_Date = db.Column(db.Date, nullable=False)
    end_Date = db.Column(db.Date, nullable=False)
    start_Time = db.Column(db.Time, nullable=False)
    end_Time = db.Column(db.Time, nullable=False)
    start_enrollment = db.Column(db.Date, nullable=False)
    end_enrollment = db.Column(db.Date, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    #check if the class is full
    def checkCapacity(self, classid):
        enrolled = CourseProgression.query.filter_by(class_id = classid, status = "enrolled").all()
        classinfo = Class.query.filter_by(class_id = classid).first()
        if len(enrolled) < classinfo.capacity:
            return True
        else:
            raise Exception("Class is at max capacity.")


class Chapter(db.Model):
    __tablename__ = 'chapter'

    chapter_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), nullable=False)
    chapter_name = db.Column(db.Varchar(50), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    chapter_materials = db.Column(db.Varchar(50), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.chapter_id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    graded = db.Column(db.Boolean, nullable=False)
    passing_mark = db.Column(db.Integer)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def computeScore(self, answerdict):
        marks = 0
        for key, value in answerdict.items():
            questionid = key
            answer = value
            marks += Question.computeMarks(questionid, answer)
        return marks

    def passCourse(self, answerdict, userid):
        marks = self.computeScore(answerdict)
        if marks >= self.passing_mark:
            chapterinfo = Chapter.query.filter_by(chapter_id = self.chapter_id).first()
            classid = chapterinfo.class_id
            usercourse = CourseProgression.query.filter_by(user_id = userid, class_id = classid).first()
            usercourse.status = 'completed'
            usercourse.completion_date = dt.date.today()
            usercourse.score = marks
        else:
            raise Exception("You have failed the course.")
        
class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'), nullable=False)
    question = db.Column(db.Varchar(250), nullable=False)
    marks = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
    def computeMarks(self, questionid, answer):
        if answer == True or answer == False:
            correctans = Questiontf.correctanswer(questionid)
        else:
            correctans = Questionmcq.correctanswer(questionid)
        
        if correctans == answer:
            return self.marks
        else:
            return 0
        

class Questiontf(db.Model):
    __tablename__ = 'question_tf'

    question_tf_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), primary_key=True, nullable=False)
    corrected_value = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def correctanswer(self, questionid):
        correct = Questiontf.query.filter_by(question_tf_id = questionid).first()
        return correct.corrected_value

class Questionmcq(db.Model):
    __tablename__ = 'question_mcq'

    question_mcq_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), primary_key=True, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    #check if answer is correct
    def correctanswer(self, questionid):
        correct = Options.query.filter_by(question_mcq_id = questionid, correct_value = True).first()
        return correct.value    

class Options(db.Model):
    __tablename__ = 'options'

    options_id = db.Column(db.Integer, primary_key=True, nullable=False)
    question_mcq_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), nullable=False)
    value = db.Column(db.Varchar(50), nullable=False)
    corrected_value = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class CourseProgression(db.Model):
    __tablename__ = 'course_progression'

    cc_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)    
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.chapter_id'), nullable=False)
    status = db.Column(db.Varchar(50), nullable=False)
    completion_date = db.Column(db.Date)
    score = db.Column(db.Integer)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    


