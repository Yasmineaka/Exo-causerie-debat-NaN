
from flask import Flask, render_template, request, redirect, url_for
from moko import students

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello_word():
    if request.method == 'POST':
        name = request.form.get("nom")
        age = request.form.get("age")
        classe = request.form.get("classe")
        user = students()
        user.addStudent(name, classe, age)
        print(f"nom:{name}, age:{age}, classe:{classe}")
        return redirect(url_for(students))

@app.route('/Student')
def index():
    return 'Index Page'

@app.route('/students')
def hello_word():
    user = students()
    return render_template("index.html, student = user.GET all student")

@app.route('/students/<id>')
def salut(id):
    return f"Je suis l'eleve : {id} "