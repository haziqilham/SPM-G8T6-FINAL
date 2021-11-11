from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime as dt


#################################################################################################################
# BASE connectors start

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:ilovespm88@spm-database.c3izrtomcbks.us-east-2.rds.amazonaws.com:3306/spm_database'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}
db = SQLAlchemy(app)
CORS(app)

# BASE connectors end
#################################################################################################################


#################################################################################################################
# CLASS initialisation section start
# --------------------------------------------------------------------------------------------------------------

# CLASS - User
# Person-in-charge: Jun Hong

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
# ---------------------------------------------------------------------------------------------------------------
# CLASS - Course
# Person-in-charge: Marcus

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    archive_date = db.Column(db.DateTime)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
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
# ---------------------------------------------------------------------------------------------------------------
# CLASS - Class
# Person-in-charge: Haziq

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
# ---------------------------------------------------------------------------------------------------------------
# CLASS - Chapter
# Person-in-charge: Claudia

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
# ---------------------------------------------------------------------------------------------------------------
# CLASS - Quiz
# Person-in-charge: Xinyi

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
# ---------------------------------------------------------------------------------------------------------------
# CLASS - CourseProgression
# Person-in-charge: Xinyi

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
# ---------------------------------------------------------------------------------------------------------------
db.create_all()
# --------------------------------------------------------------------------------------------------------------
# CLASS initialisation section end
#################################################################################################################



#################################################################################################################
# APPLICATION ROUTINGS section start
# --------------------------------------------------------------------------------------------------------------

# BASE ROUTES section start
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES - User start

# display user by user_id
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

# display all learners
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

# display all trainers
@app.route("/trainers")
def trainers():
    getTrainer = User.query.filter_by(role='Trainers').all()
    if getTrainer:
        return jsonify({
            "data": [trainer.to_dict() for trainer in getTrainer]
        }), 200
    else:
        return jsonify({
            "message": "Trainers not found."
        }), 404

# BASE ROUTES - User end
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES - Course start 

# display course by course_id 
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

# display courses user is enrolled in
@app.route("/courses/users/<int:user_id>")
def course_by_user(user_id):
    userclass = CourseProgression.query.filter_by(user_id=user_id).filter(CourseProgression.status.like('%n%'))
    if userclass:
        coursedict = []
        for uclass in userclass:
            courseinfo = Course.query.filter_by(course_id=uclass.course_id).first()
            coursedict.append(courseinfo)
    
        return jsonify({
            "data": [course.to_dict() for course in coursedict]
        }), 200
    else:
        return jsonify({
           "message": "You are not enrolled in any course at the moment."
        }), 404

# display courses user is not enrolled in
@app.route("/not/courses/users/<int:user_id>")
def not_course_by_user(user_id):
    courses = Course.query.filter_by(archive_date=None).all()
    userclass = CourseProgression.query.filter_by(user_id=user_id).filter(CourseProgression.status.like('%n%')).all()
    if userclass:
        coursedict = []
        for uclass in userclass:
            courseinfo = Course.query.filter_by(course_id=uclass.course_id).first()
            coursedict.append(courseinfo)
        
        finaldict = []
        for c in courses:
            if c not in coursedict:
                finaldict.append(c)

        return jsonify({
            "data": [final.to_dict() for final in finaldict]
        }), 200
    else:
        return jsonify({
            "data": [course.to_dict() for course in courses]
        }), 200

# BASE ROUTES - Course end 
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES - Class start 

# display all classes of the course
@app.route("/<int:course_id>/classes")
def classes_by_course(course_id):
    classes = Class.query.filter_by(course_id=course_id).all()
    if classes:
        return jsonify({
            "data": [oneclass.to_dict() for oneclass in classes]
        }), 200
    else:
        return jsonify({
            "message": "This course has no classes yet."
        }), 404

# trainer - view classes trainer is teaching
@app.route("/trainer/classes/<int:trainer_id>")
def classes_by_trainer(trainer_id):
    classes = Class.query.filter_by(trainer_id=trainer_id).all()
    filter_classes = []
    for oneclass in classes:
        if dt.datetime.today() >= oneclass.start_enrollment and dt.datetime.today() <= oneclass.end_enrollment:
            courseinfo = Course.query.filter_by(course_id=oneclass.course_id).first()
            filter_classes.append({
                'course_name': courseinfo.course_name,
                'class_id': oneclass.class_id,
                'class_name': oneclass.class_name,
                'start_DateTime': oneclass.start_DateTime,
                'end_DateTime': oneclass.end_DateTime
            })
    if filter_classes:
        return jsonify({
            "data": filter_classes
        }), 200
    else:
        return jsonify({
             "message": "There are no classes assigned to you yet."
        }), 404

# display the class of the course that the user is enrolled in
@app.route("/user/<int:user_id>/<int:course_id>/class")
def classenrolled(user_id, course_id):
    userclass = CourseProgression.query.filter_by(user_id=user_id, course_id=course_id).filter(CourseProgression.status.like('%n%')).first()
    class_id = userclass.class_id
    classinfo = Class.query.filter_by(class_id=class_id).first()
    if classinfo:
        return jsonify({
            "data": classinfo.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "You are not enrolled in any class for this course."
        }), 404

# BASE ROUTES - Class end 
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES - Chapter start 

# trainer - display all chapters for creation of quiz
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

# display chapters of classes that user has access to
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
    if chapter_data:
        return jsonify({
            "data": [cdata for cdata in chapter_data]
            }), 200
    else:
        return jsonify({
            "message": "The class has not started yet."
        }), 404

# update chapter progress for user when user clicks 'complete chapter' button
@app.route("/complete/<int:class_id>/<int:chapter_id>/<int:user_id>")
def updateprogress(class_id, chapter_id, user_id):
    currentprogress = CourseProgression.query.filter_by(user_id=user_id, class_id=class_id).first()
    currentprogress.chapter_id = chapter_id
    try:
        db.session.commit()
        return jsonify({
            "message": "Ok"
        }), 500
    except Exception:
        return jsonify({
            "message": "Trouble registering completion, please try again later or contact an administrator."
        }), 500

# BASE ROUTES - Chapter end       
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES - Quiz start  

# display quiz of the chapter
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

# trainer - get quizzes that trainer can create quiz for
@app.route("/trainer/<int:chapter_id>/quiz")
def getquizfortrainer(chapter_id):
    quizinfo = Quiz.query.filter_by(chapter_id=chapter_id).all()
    if quizinfo:
        return jsonify({
            "data": [qinfo.to_dict() for qinfo in quizinfo]
        }), 200
    else:
        return jsonify({
            "message": "There is no quiz at the moment."
        }), 404

# BASE ROUTES - Quiz end 
# --------------------------------------------------------------------------------------------------------------
# BASE ROUTES section end
# --------------------------------------------------------------------------------------------------------------

# CORE FEATURE - Enrollment start

# learner - self-enroll into class
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
                            class_id = class_id,
                            chapter_id = None,
                            status = "enrolled",
                            completion_date = None,
                            score = None
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


# hr - enroll learner into class
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
                            class_id = class_id,
                            chapter_id = None,
                            status = "enrolled",
                            completion_date = None,
                            score = None
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

# ------------------------------------------------------------
# Enroll - base checkers start

# check if user is already enrolled into course
def enrollhistory(user_id, course_id):
    #check user's existing course progress
    progress = CourseProgression.query.filter_by(user_id=user_id, course_id=course_id).all()
    
    #check that user is not currently in progress or enrolled into the course
    if len(progress) > 0:
        for i in progress:
            if i.course_id == course_id:
                if i.status == "ongoing" or i.status == "enrolled":
                    return False
    return True

# check if user has already completed the course
def completionhistory(user_id, course_id):
    #check user's existing course progress
    progress = CourseProgression.query.filter_by(user_id=user_id, course_id=course_id).all()
    #check that user has not already completed the course
    if len(progress) > 0:
        for i in progress:
            if i.course_id == course_id:
                if i.status == "completed":
                    return False
    return True

# check if class is open for enrollment
def openclass(class_id):
    classinfo = Class.query.filter_by(class_id=class_id).first()
    if dt.datetime.today() >= classinfo.start_enrollment and dt.datetime.today() <= classinfo.end_enrollment:
        return True
    else:
        return False

# check if class is full
def checkcapacity(class_id):
    classinfo = Class.query.filter_by(class_id=class_id).first()
    capacity = classinfo.capacity
    enrolled = CourseProgression.query.filter_by(class_id=class_id, status="enrolled").all()
    if len(enrolled) >= capacity:
        return False
    else:
        return True

# draw list of course prereqs
def courseprereqs(course_id):
    prereqs = Prerequisites.query.filter_by(course_id=course_id).all()
    prereqlist = []
    if len(prereqs) > 0:
        for i in prereqs:
            prereqlist.append(i.prereq_course_id)
    return prereqlist

# draw list of completed courses of user
def completedcourses(user_id):
    completed = CourseProgression.query.filter_by(user_id=user_id, status="completed").all()
    completedlist = []
    if len(completed) > 0:
        for i in completed:
            completedlist.append(i.course_id)
    return completedlist

# check if user meets prereq
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
    return True

# Enroll - base checkers end
# ------------------------------------------------------------
# CORE FEATURE - Enrollment end
# --------------------------------------------------------------------------------------------------------------

# CORE FEATURE - Create Quiz start

# trainer - create quiz
@app.route("/createquiz", methods=['POST'])
def create_quiz():
    data = request.get_json()
    if not all(key in data.keys() for
                key in ('chapter_id', 'duration', 'quizType', 'passing', 'qnsTF', 'qnsMCQ')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    #validate chapter
    chapter = Chapter.query.filter_by(chapter_id=data['chapter_id']).first()
    if not chapter:
        return jsonify({
            "message": "Chapter does not exist."
        }), 500
    #create quiz record
    quiz = Quiz(
        chapter_id=data['chapter_id'], 
        duration=data['duration'],
        graded=data['quizType'],
        passing_mark=data['passing']
    )
    #commit to db
    try:
        db.session.add(quiz)
        db.session.commit()
        if (createQnTF(quiz.to_dict()["quiz_id"], data['qnsTF']) and createQnMCQ(quiz.to_dict()["quiz_id"], data['qnsMCQ'])):
            return jsonify(quiz.to_dict()), 201

    except Exception:
        return jsonify({
            "message": "Unable to create quiz, please try again later or contact an administrator."
        }), 500

# ------------------------------------------------------------
# Create Quiz - base functions start

#create MCQ Qn
def createQnMCQ(quiz_id, mcq):
    print(len(mcq))
    for m in mcq:
        question = Question(
            quiz_id=quiz_id, 
            question=m['questions'],
            marks=m['marks']
        )
        print(question)
        try:
            db.session.add(question)
            db.session.commit()
            createMCQ(question.to_dict()["question_id"])
            createOptions(question.to_dict()["question_id"], m['options'])
        except Exception:
            return jsonify({
                "message": "Unable to create question, please try again later or contact an administrator."
            }), 500
    return True

#put mcq sub class
def createMCQ(qnTf_id):
    print(qnTf_id)
    q = Questionmcq(
        question_mcq_id=qnTf_id
    )
    try:
        db.session.add(q)
        db.session.commit()
        return True
    except Exception:
        return jsonify({
            "message": "Unable to create question, please try again later or contact an administrator."
        }), 500


#create options
def createOptions(quiz_id, options):
    for o in options:
        print(o)
        a=1
        if o['corrected'] == '':
            a=0

        opt = Options(
            question_mcq_id=quiz_id,
            value=o['value'],
            corrected_value=a
        )
        print(opt)
        try:
            db.session.add(opt)
            db.session.commit()
        except Exception:
            return jsonify({
                "message": "Unable to create question, please try again later or contact an administrator."
            }), 500
    return True

#create TF Qn
def createQnTF(quiz_id, tf):
    for t in tf:
        question = Question(
            quiz_id=quiz_id, 
            question=t['questions'],
            marks=t['marks']
        )
        print(question)
        try:
            db.session.add(question)
            db.session.commit()
            createTF(question.to_dict()["question_id"], t['value'])
            #return jsonify(question.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to create question, please try again later or contact an administrator."
            }), 500
    return True

#put TF answer
def createTF(qnTf_id, value):
    print(value)
    q = Questiontf(
        question_tf_id=qnTf_id,
        corrected_value=int(value)
    )
    try:
        db.session.add(q)
        db.session.commit()
        #return jsonify(q.to_dict()), 201
        return True
    except Exception:
        return jsonify({
            "message": "Unable to create question, please try again later or contact an administrator."
        }), 500

# Create Quiz - base functions end        
# ------------------------------------------------------------
# CORE FEATURE - Create Quiz end
# --------------------------------------------------------------------------------------------------------------

# CORE FEATURE - Take Quiz start

# retrieving questions for quiz
@app.route("/quiz/<int:quiz_id>/questions")
def getquestions(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    finaldict = []
    options = []
    for question in questions:
        #find out if the question is tf or mcq
        question_tf = Questiontf.query.filter_by(question_tf_id=question.question_id).first()
        if question_tf:
            options = [True, False]
            finaldict.append({
                'question_id': question.question_id,
                'question': question.question,
                'options': options
            })
            options = []
        else:
            question_mcq = Options.query.filter_by(question_mcq_id=question.question_id).all()
            for option in question_mcq:
                options.append(option.value)
            finaldict.append({
                'question_id': question.question_id,
                'question': question.question,
                'options': options
            })
            options = []

# submit quiz and return total marks
@app.route("/quiz/submit", methods=['POST'])
def submit_quiz():
    data = request.get_json()
    marks = 0
    answerarray = data['answer']
    #get one question id
    question_id = answerarray[0]['qnID']
    #check if quiz is graded
    graded = quiz_graded(question_id)
    #if quiz is graded, then grade quiz
    if graded:
        for answer in answerarray:
            #mark each question
            questionmarks = markquestion(answer['ans'], answer['qnID'])
            marks += questionmarks
            return jsonify({
                "data": marks
            }), 200
    else:
        return jsonify({
            "data": -1
        }), 200

# check if user passed quiz and record completion
@app.route("/complete/<int:user_id>/<int:quiz_id>/<totalmarks>")
def passCourse(user_id, quiz_id, totalmarks):
    totalmarks = int(totalmarks)
    if totalmarks >= 0:
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
    return jsonify({
        "message": "Please click complete chapter to register your chapter completion."
    }), 200

# ------------------------------------------------------------
# Take Quiz - base functions start       

# determine if quiz is graded: return T/F
def quiz_graded(question_id):
    questioninfo = Question.query.filter_by(question_id=question_id).first()
    quiz_id = questioninfo.quiz_id
    quizinfo = Quiz.query.filter_by(quiz_id=quiz_id).first()
    graded = quizinfo.graded
    return graded

# marks each question individually
def markquestion(answer, question_id):
    questioninfo = Question.query.filter_by(question_id=question_id).first()
    questionmarks = questioninfo.marks
    correctvalue = retrieveanswer(question_id)
    if correctvalue == answer:
        return questionmarks
    else:
        return 0

# retrieves the answer of each question
def retrieveanswer(question_id):
    #find out if the question is tf or mcq
    question_tf = Questiontf.query.filter_by(question_tf_id=question_id).first()
    if question_tf:
        question_tf = Questiontf.query.filter_by(question_tf_id=question_id).first()
        answer = question_tf.corrected_value
    else:
        question_mcq = Options.query.filter_by(question_mcq_id=question_id, corrected_value = True).first()
        answer = question_mcq.value
    return answer

# Take Quiz - base functions end 
# ------------------------------------------------------------
# CORE FEATURE - Take Quiz end
# --------------------------------------------------------------------------------------------------------------

# APPLICATION ROUTINGS section end
#################################################################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
