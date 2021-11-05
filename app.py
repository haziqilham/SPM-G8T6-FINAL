from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:ilovespm88@spm-database.c3izrtomcbks.us-east-2.rds.amazonaws.com:3306/spm_database'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}
db = SQLAlchemy(app)
CORS(app)

#JunHong
class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    user_name = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

#Marcus
class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    course_name = db.Column(db.String(50), nullable=False)
    archive_date = db.Column(db.Date)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result    

    def archivecourse(self):
        self.archive_date = dt.date.today()
        #course = Course.query.filter_by(course_id = self.course_id).first()
        #course.archive_date = dt.date.today()


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

#Haziq
class Class(db.Model):
    __tablename__ = 'class'

    class_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False) 
    class_name = db.Column(db.String(50), nullable=False)
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

#Claudia
class Chapter(db.Model):
    __tablename__ = 'chapter'

    chapter_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), nullable=False)
    chapter_name = db.Column(db.String(50), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    chapter_materials = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

#Xinyi
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
    question = db.Column(db.String(250), nullable=False)
    marks = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
    def computeMarks(self, answer):
        if answer == True or answer == False:
            correctans = Questiontf.correctanswer(self.question_id)
        else:
            correctans = Questionmcq.correctanswer(self.question_id)
        
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
    value = db.Column(db.String(50), nullable=False)
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
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.chapter_id'))
    status = db.Column(db.String(50), nullable=False)
    completion_date = db.Column(db.Date)
    score = db.Column(db.Integer)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    

#base render home page
@app.route("/")
def index():
    return render_template('index.html')

#USER
#display all users
@app.route("/users")
def allUsers():
    users = User.query.all()
    if users:
        return jsonify({
            "data": [user.to_dict() for user in users]
        }), 200
    else:
        return jsonify({
            "message": "There are no users found."
        }), 404

#display user by user_id
@app.route("/users/<int:user_id>")
def user_by_id(user_id):
    getuser = User.query.filter_by(user_id=user_id).first()
    if getuser:
        return jsonify({
            "data": getuser.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "User not found."
        }), 404

#COURSE
#display all courses that are not archived
@app.route("/courses")
def allCourses():
    courses = Course.query.filter_by(archive_date=None).all()
    if courses:
        return jsonify({
            "data": [course.to_dict() for course in courses]
        }), 200
    else:
        return jsonify({
            "message": "There are no courses found."
        }), 404

#display course by course_id 
@app.route("/courses/<int:course_id>")
def course_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        return jsonify({
            "data": course.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404

#CLASS
#display all classes from the course
@app.route("/classes")
def classes_by_course(course_id):
    classes = Class.query.filter_by(course_id=course_id).order_by()
    if classes:
        return jsonify({
            "data": [oneclass.to_dict() for oneclass in classes]
        }), 200
    else:
        return jsonify({
            "message": "This course has no classes yet."
        }), 404

#display class info by class id
@app.route("/classes/<int:class_id>")
def class_by_id(class_id):
    getclass = Class.query.filter_by(class_id=class_id).first()
    if getclass:
        return jsonify({
            "data": getclass.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Class not found."
        }), 404

#enroll into class base functions:

#check if user is already enrolled into course
def enrollhistory(user_id, course_id):
    #check user's existing course progress
    progress = CourseProgression.query.filter_by(user_id=user_id, course_id=course_id).all()
        #check that user is not currently in progress or enrolled into the course
    if progress.count() > 0:
        for i in progress:
            if i.course_id == course_id:
                if i.status == "ongoing" or i.status == "enrolled":
                    return False
    else:
        return True

#check if user has already completed the course
def completionhistory(user_id, course_id):
    #check user's existing course progress
    progress = CourseProgression.query.filter_by(user_id=user_id, course_id=course_id).all()
    #check that user has not already completed the course
    if progress.count() > 0:
        for i in progress:
            if i.course_id == course_id:
                if i.status == "completed":
                    return False
    else:
        return True

#check if class is open for enrollment
def openclass(class_id):
    classinfo = Class.query.filter_by(class_id=class_id).first()
    if dt.date.today() >= classinfo.start_enrollment or dt.date.today() <= classinfo.end_enrollment:
        return True
    else:
        return False

#check if class is full
def checkcapacity(class_id):
    classinfo = Class.query.filter_by(class_id=class_id).first()
    capacity = classinfo.capacity
    enrolled = CourseProgression.query.filter_by(class_id=class_id, status="enrolled").all()
    if enrolled.count() >= capacity:
        return False
    else:
        return True


#draw list of course prereqs
def courseprereqs(course_id):
    prereqs = Prerequisites.query.filter_by(course_id=course_id).all()
    prereqlist = []
    if prereqs.count() > 0:
        for i in prereqs:
            prereqlist.append(i.prereq_course_id)
    return prereqlist

#draw list of completed courses of user
def completedcourses(user_id):
    completed = CourseProgression.query.filter_by(user_id=user_id, status="completed").all()
    completedlist = []
    if completed.count() > 0:
        for i in completed:
            completedlist.append(i.course_id)
    return completedlist

#check if user meets prereq
def prereqmet(course_id, user_id):
    prereqlist = courseprereqs(course_id)
    completedlist = completedcourses(user_id)
    if len(prereqlist) != 0:
        if len(prereqlist) > len(completedlist):
            return False
        else:
            for prereq in prereqlist:
                if prereq not in completedlist:
                    return False
    else:
        return True


#enroll user into class - USER SELF ENROLL
@app.route("learner/<int:course_id>/<int:class_id>/<int:user_id>")
def enroll(course_id, class_id, user_id):
    if enrollhistory(user_id, course_id):
        if completionhistory(user_id, course_id):
            if openclass(class_id):
                if checkcapacity(class_id):
                    if prereqmet(course_id, user_id):
                        #create enrollment details
                        enrollment = CourseProgression(
                            user_id = user_id,
                            course_id = course_id,
                            class_id = class_id
                        )
                        #commit to DB
                        try:
                            db.session.add(enrollment)
                            db.session.commit()
                            return jsonify({
                                "message": "You have been enrolled into the class."
                            }), 200
                        except Exception:
                            return jsonify({
                                "message": "Unable to enroll, please try again later."
                            }), 500
                    else:
                        return jsonify({
                            "message": "You have not cleared the course's prerequisites."
                        }), 200
                else:
                    return jsonify({
                        "message": "Class is full."
                    }), 200
            else:
                return jsonify({
                    "message": "This class is not open for enrollment."
                }), 200
        else:
            return jsonify({
                "message": "You have already completed this course."
            }), 200
    else:
        return jsonify({
            "message": "You are already enrolled into the course."
        }), 200


#enroll user into class - HR ENROLL ENGINEER
@app.route("admin/<int:course_id>/<int:class_id>/<int:user_id>")
def enroll(course_id, class_id, user_id):
    if enrollhistory(user_id, course_id):
        if completionhistory(user_id, course_id):
            if openclass(class_id):
                if checkcapacity(class_id):
                    if prereqmet(course_id, user_id):
                        #create enrollment details
                        enrollment = CourseProgression(
                            user_id = user_id,
                            course_id = course_id,
                            class_id = class_id
                        )
                        #commit to DB
                        try:
                            db.session.add(enrollment)
                            db.session.commit()
                            return jsonify({
                                "message": "Learner has been enrolled into the class."
                            }), 200
                        except Exception:
                            return jsonify({
                                "message": "Unable to enroll, please try again later."
                            }), 500
                    else:
                        return jsonify({
                            "message": "Learner has not cleared the course's prerequisites."
                        }), 200
                else:
                    return jsonify({
                        "message": "Class is full."
                    }), 200
            else:
                return jsonify({
                    "message": "This class is not open for enrollment."
                }), 200
        else:
            return jsonify({
                "message": "Learner has already completed this course."
            }), 200
    else:
        return jsonify({
            "message": "Learner has already enrolled into the course."
        }), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
