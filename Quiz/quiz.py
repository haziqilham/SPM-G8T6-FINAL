from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
# app.config['TESTING'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/is212_example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

class Quiz(db.Model): #to change to Chapter superclass later
    __tablename__ = 'Quiz'

    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(100))
    graded = db.Column(db.Boolean)
    duration = db.Column(db.Integer)
    passing_mark = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'Quiz',
    }

    def toDict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def computeScore(self, computeMarksList):
        totalScore = 0
        for item in computeMarksList:
            totalScore += item['marks']
        return totalScore

#Display all quiz properties in front end
@app.route("/quiz")
def getQuiz():
    quiz = Quiz.query.all()
    if len(quiz):
        return jsonify(
            {
                "code": 200,
                "data": [quiz.to_dict() for prop in quiz]
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no quizzes"
        }
    ), 404

#TODO compute
@app.route("/quiz/computeScore")
def computeScore(userMarksList):
    pass

#TODO creation of quiz in front end
@app.route("/quiz", methods=['POST'])
def createQuiz():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
