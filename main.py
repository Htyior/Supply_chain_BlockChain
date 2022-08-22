from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200))
    email = db.Column(db.String(200))
    contact = db.Column(db.Integer)
    course = db.Column(db.String(200))



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('Supply_Chain.html')

@app.route('/chain')
def createChain():
    students = Student.query.all()
    print(students)
    return render_template('index.html', students = students)

@app.route('/add', methods = ['GET', 'POST'])
def add():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            contact = request.form['contact']
            course = request.form['course']
            print(name, email, contact, course)

            new_student = Student(name = name, email = email, contact = contact, course = course)
            db.session.add(new_student)
            db.session.commit()
            return redirect('/chain')


        else:
            return render_template('add.html')



if __name__ == "__main__":
    app.run(port=5555, debug=True)
