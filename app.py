from flask import Flask, request, jsonify
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

    user_id = db.Column(db.Integer, primary_key=True)
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

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    archive_date = db.Column(db.DateTime)

    def __init__(self, course_id, course_name, archive_date):   
        self.course_id = course_id
        self.course_name = course_name
        self.archive_date = archive_date

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    

#TO BE DECIDED - replace as app routing? or leave it
    #def archivecourse(self):
        #self.archive_date = dt.date.today()


class Prerequisites(db.Model):
    __tablename__ = 'prerequisites'

    prereq_id = db.Column(db.Integer, primary_key=True)
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

    class_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False) 
    class_name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    start_DateTime = db.Column(db.DateTime, nullable=False)
    end_DateTime = db.Column(db.DateTime, nullable=False)
    start_enrollment = db.Column(db.DateTime, nullable=False)
    end_enrollment = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

#Claudia
class Chapter(db.Model):
    __tablename__ = 'chapter'

    chapter_id = db.Column(db.Integer, primary_key=True)
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

    quiz_id = db.Column(db.Integer, primary_key=True)
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
        
class Question(db.Model):
    __tablename__ = 'question'

    question_id = db.Column(db.Integer, primary_key=True)
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

class Questionmcq(db.Model):
    __tablename__ = 'question_mcq'

    question_mcq_id = db.Column(db.Integer, db.ForeignKey('question.question_id'), primary_key=True, nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

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

    cc_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)    
    class_id = db.Column(db.Integer, db.ForeignKey('class.class_id'), nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.chapter_id'))
    status = db.Column(db.String(50), nullable=False)
    completion_date = db.Column(db.DateTime)
    score = db.Column(db.Integer)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
db.create_all()

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

#display all learners
@app.route("/learners")
def learners():
    getLearner = User.query.filter_by(role='Learners').all()
    if getLearner:
        return jsonify({
            "data": [learner.to_dict() for learner in getLearner]
        }), 200
    else:
        return jsonify({
            "message": "Learners not found."
        }), 404

#COURSE
#display all courses that are not archived
@app.route("/courses")
def displaycourses():
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

#display courses user is enrolled in
@app.route("/courses/users/<int:user_id>")
def course_by_user(user_id):
    userclass = CourseProgression.query.filter(user_id=user_id).filter(status = 'ongoing' | 'enrolled').all()

    if userclass:
        return jsonify({
            "data": [uclass.to_dict() for uclass in userclass]
        }), 200
    else:
        return jsonify({
            "message": "There are no courses found."
        }), 404

    #if userclass:
    #    coursedict = []
    #    for uclass in userclass:
    #        courseinfo = Course.query.filter_by(course_id=uclass.course_id)
    #        coursedict.append(courseinfo)
    
    #    return jsonify({
    #        "data": [course.to_dict() for course in coursedict]
    #    }), 200

    #else:
    #    return jsonify({
    #       "message": "You are not enrolled in any course at the moment."
    #    }), 404


#CLASS
#display all classes
@app.route("/<int:course_id>/classes")
def classes_by_course(course_id):
    #to implement order by start date
    classes = Class.query.filter_by(course_id=course_id).all()

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


#CHAPTER
#TRAINER - display all chapters for creation of quiz
@app.route("/<int:class_id>/chapters")
def chapters_by_class(class_id):
    #order by order
    chapters = Chapter.query.filter_by(class_id=class_id).order_by(Chapter.order.asc()).all()
    if chapters:
        return jsonify({
            "data": [chapter.to_dict() for chapter in chapters]
        }), 200
    else:
        return jsonify({
            "message": "This class has no chapters yet."
        }), 404

#update chapter progress for user when user clicks 'complete chapter' button
@app.route("/<int:class_id>/<int:chapter_id>/<int:user_id>")
def updateprogress(class_id, chapter_id, user_id):
    currentprogress = CourseProgression.query.filter_by(user_id=user_id, class_id=class_id).first()
    currentprogress.chapter_id = chapter_id
    try:
        db.session.commit()
    except Exception:
        return jsonify({
            "message": "Trouble registering completion, please try again later or contact an administrator."
        }), 500

#ATTENDING THE CLASS FUNCTION:
#display all classes that user is currently enrolled in
@app.route("/classes/<int:user_id>")
def class_by_user(user_id):
    userclass = CourseProgression.query.filter_by(user_id=user_id, status="enrolled" or "ongoing").all()
    if userclass:
        return jsonify({
            "data": [uclass.to_dict() for uclass in userclass]
        }), 200
    else:
        return jsonify({
            "message": "You are not enrolled in any class at the moment."
        }), 404

#display chapters of classes that user has access to
@app.route("/<int:class_id>/<int:user_id>/chapters")
def user_chapter(class_id, user_id):
    userprogress = CourseProgression.query.filter_by(user_id=user_id, class_id=class_id, status='ongoing').first()
    userchapter = userprogress.chapter_id
    #retrieve user's latest completed chapter / if user has not started, order = 0
    if userchapter !=  None:
        chapterinfo = Chapter.query.filter_by(chapter_id=userchapter).first()
        chapterorder = chapterinfo.order
    else:
        chapterorder = 0
    
    chapter_data = []
    for i in range(1,chapterorder+2):
        chapter = Chapter.query.filter_by(class_id=class_id, order=i).first()
        if chapter:
            chapter_data.append({
                'chapter_id': chapter.chapter_id,
                'class_id': chapter.class_id,
                'chapter_name': chapter.chapter_name,
                'order': chapter.order,
                'chapter_materials':chapter.chapter_materials
            })

    return jsonify({
        "data": [cdata for cdata in chapter_data]
        }), 200

#QUIZ
#display quiz
@app.route("/<int:chapter_id>/quiz")
def getquiz(chapter_id):
    quizinfo = Quiz.query.filter_by(chapter_id=chapter_id).first()
    if quizinfo:
        return jsonify({
            "data": quizinfo.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "There is no quiz at the moment."
        }), 404

#create quiz
@app.route("/createquiz", methods=['POST'])
def create_quiz():
    data = request.get_json()
    if not all(key in data.keys() for
                key in ('chapter_id', 'duration', 'graded')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    #validate chapter
    chapter = Chapter.query.filter_by(chapter_id=data['chapter_id']).first()
    if not chapter:
        return jsonify({
            "message": "Chapter does not exist."
        })
    #create quiz record
    quiz = Quiz(
        chapter_id=data['chapter_id'], 
        duration=data['duration'],
        graded=data['graded']
    )
    #commit to db
    try:
        db.session.add(quiz)
        db.session.commit()
        return jsonify(quiz.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to create quiz, please try again later or contact an administrator."
        }), 500


#QUESTION
#retrieving questions for quiz
@app.route("/<int:chapter_id>/quiz/questions")
def getquestions(chapter_id):
    quizinfo = Quiz.query.filter_by(chapter_id=chapter_id).first()
    quiz_id = quizinfo.quiz_id
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    finaldict = {}
    qdict = {}
    options = []
    for question in questions:
        #find out if the question is tf or mcq
        question_tf = Questiontf.query.filter_by(question_tf_id=question.question_id).first()
        if question_tf:
            qdict[question.question]=[True, False]                
            finaldict[question.question_id]= qdict
            options = []
            qdict = {}
        else:
            question_mcq = Options.query.filter_by(question_mcq_id=question.question_id).all()
            for option in question_mcq:
                options.append(option.value)
                qdict[question.question]= options
                finaldict[question.question_id]= qdict
                options = []
                qdict = {}
    if finaldict:
        return jsonify({
            "data": finaldict.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "There was an error retrieving quiz questions, please contact an administrator."
        }), 404


#create quiz questions
@app.route("/quiz/createquestions", methods=['POST'])
def create_questions():
    data = request.get_json()
    if not all(key in data.keys() for
                key in ('quiz_id', 'question', 'marks')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    #validate quiz
    quiz = Quiz.query.filter_by(quiz_id=data['quiz_id']).first()
    if not quiz:
        return jsonify({
            "message": "Invalid quiz details"
        })
    #create question record
    question = Question(
        quiz_id=data['quiz_id'], 
        question=data['question'],
        marks=data['marks']
    )
    #commit to db
    try:
        db.session.add(question)
        db.session.commit()
        return jsonify(question.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to create question, please try again later or contact an administrator."
        }), 500


#create quiz options
@app.route("/quiz/question/createoptions", methods=['POST'])
def create_options():
    data = request.get_json()
    #options is a list value containing all options
    if not all(key in data.keys() for
                key in ('question_id', 'correct_value', 'options')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    #validate question
    question = Question.query.filter_by(question_id=data['question_id']).first()
    if not question:
        return jsonify({
            "message": "Invalid question details."
        })
    #create question record
    if data['options'].count() < 3:
        question = Questiontf(
            question_tf_id=data['question_id'],
            corrected_value=data['correct_value']
        )
    else:
        question = Questionmcq(
            question_mcq_id=data['question_mcq_id'], 
        )
        for option in data['options']:
            options = Options(
                question_mcq_id=data['question_mcq_id'],
                value=option,
                corrected_value=data['correct_value']
            )
    #commit to db
    try:
        db.session.add(question)
        if options:
            db.session.add(options)
        db.session.commit()
        return jsonify(question.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to create question options, please try again later or contact an administrator."
        }), 500

    
#GRADE QUIZ
#frontend vue for loop marks each question individually
#retrieves the answer of each question
@app.route("/quiz/<int:question_id>")
def retrieveanswer(question_id):
    #find out if the question is tf or mcq
    question_tf = Questiontf.query.filter_by(question_tf_id=question_id).first()
    if question_tf:
        question_tf = Questiontf.query.filter_by(question_tf_id=question_id).first()
        answer = question_tf.corrected_value
    else:
        question_mcq = Options.query.filter_by(question_mcq_id=question_id, correct_value = True).first()
        answer = question_mcq.value

    return jsonify({
        "data": answer
    }), 200

#check if user passed quiz and record completion
@app.route("/<int:user_id>/<int:quiz_id>/<int:totalmarks>")
def passCourse(user_id, quiz_id, totalmarks):
    #query to retrieve passing_mark of quiz
    quizinfo = Quiz.query.filter_by(quiz_id=quiz_id).first()
    passing_mark = quizinfo.passing_mark
    #query to retrieve class_id
    chapterinfo = Chapter.query.filter_by(chapter_id=quizinfo.chapter_id).first()
    class_id = chapterinfo.class_id
    #record completion
    usercourse = CourseProgression.query.filter_by(user_id = user_id, class_id = class_id).first()
    usercourse.completion_date = dt.datetime.today()
    usercourse.score = totalmarks
    message = ""
    #record pass or fail
    if totalmarks >= passing_mark:
        usercourse.status = 'completed'
        message = "You have successfully completed the course, please inform your supervisor."
    else:
        usercourse.status = 'failed'
        message = "You have failed the course, please inform your supervisor."
    try:
        db.session.commit()
        return jsonify({
            "message": message
        }), 200
    except Exception:
        return jsonify({
            "message": "There was a problem registering your quiz result, please inform an administrator."
        }), 500


#ENROLL FUNCTION:
#base checkers:
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
    #else:
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
    #else:
    return True

#check if class is open for enrollment
def openclass(class_id):
    classinfo = Class.query.filter_by(class_id=class_id).first()
    if dt.datetime.today() >= classinfo.start_enrollment and dt.datetime.today() <= classinfo.end_enrollment:
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
    #else:
    return True


#USER SELF ENROLL - enroll user into class 
@app.route("/learner/<int:course_id>/<int:class_id>/<int:user_id>")
def self_enroll(course_id, class_id, user_id):
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


#HR ENROLL ENGINEER - enroll user into class
@app.route("/admin/<int:course_id>/<int:class_id>/<int:user_id>")
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
