from flask import Flask, jsonify, request
#creation de mini bibliotheque
# from pymongo import MongoClient ////////////
import certifi
from flask_pymongo import PyMongo
from format_id import convert
from mongoengine import connect
# from flask_mongoengine import MongoEngine
from models.user import User
# st = "mongodb+srv://yasmineaka00:TGA8oj4JXPqP4wTf@cluster0.azbbhec.mongodb.net/"
# /compass-connection/

app = Flask(__name__)
# app.config['MONGODB_SETTINGS']=[
#     {
#         "host":"mongodb+srv://yasmineaka00:TGA8oj4JXPqP4wTf@cluster0.azbbhec.mongodb.net/test",
#         "db":"test"
#     }
# ]
# db = MongoEngine(app, tlsCAFile=certifi.where())
connect(host="mongodb+srv://yasmineaka00:TGA8oj4JXPqP4wTf@cluster0.azbbhec.mongodb.net/test")

# mongo = PyMongo(app, tlsCAFile=certifi.where())

# @app.get("/")
# def hello():
#     users = convert(db.users.find())
#     # users=list(map(lambda u: u["nom","prenom"]))
#     print(users)
#     return jsonify(users)

@app.post('/api/user/')
def Create_user():
    try:
        user_info=request.get_json()
        new_user=User(**user_info)
        new_user.save()
        print(new_user)
        # print(request.data)
        # print(request.get_json())
        return "hello"
    except Exception as e:
        print("L'erreur est:", e)
        return "erreur" 
#pip3 install certifi : commende d'activation du certificat
#pip3 freeze> requirements.txt : permet
#pip3 install -r requirements.txt : permet d'installer tout les modules dont on a besoin
#pip3 install flask==2.2.5 : pour installer un module avec la version qui convient


# client = MongoClient(st, tlsCAFile=certifi.where())        ////////////
# test_db = client.test               ////////////

# test_db.users.insert_one({        ////////////
#     "nom":"aka",
#     "prenom":"yasmine"
# }) 
# 
#     ////////////
#insert-one pour ceer un utilisateur
#find pour trouver un tableau de plusieurs utilisateurs
#find-one pour trouver un tableau d'un seul utilisateur
#update prend deux dictionnaires en paramettre
#delete 1 dictionnaire en paramettre : delete-one, delete-many

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "bonjour"




if __name__ == '__main__':
    app.run(debug=True)




