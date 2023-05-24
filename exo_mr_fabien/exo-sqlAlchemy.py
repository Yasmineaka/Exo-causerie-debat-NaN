from flask_sqlalchemy import SQLAlchemy
from flask import Flask






app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///projet_sqlite.db'
db = SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True) 
    fullname=db.Column(db.String, nulleble=False)
    email=db.column(db.String, nulleble=False , unique= True)

    @app.route('/users')
    def get_users():
       return f"nom : {id}"

    @app.route('/users/delete/<int:id>')
    def delete(id):
        return f"supprimer {id}"

    @app.route('/users/update/<int:id>/<fullname>/<email>')
    def update(id,fullname,email):
        return f"mettre a jour {fullname},{email}"

    @app.route('/users/<fullname>/<email>')
    def creat(fullname,email):
        return f"{fullname}, {email}"

