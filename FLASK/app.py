from flask import Flask, jsonify, request
#creation de mini bibliotheque
# from pymongo import MongoClient ////////////
import certifi
from models.book import Book
from format_id import convert
from mongoengine import connect
# from flask_mongoengine import MongoEngine
from models.user import User
from  format_id import id
from format_id import from_objectId_to_json
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
connect(host="mongodb+srv://yasmineaka00:TGA8oj4JXPqP4wTf@cluster0.azbbhec.mongodb.net/test", tlsCAFile=certifi.where())


@app.post('/api/user/')
def Create_user():
    try:
        user_info=request.get_json()
        del user_info['role']
        print(new_user)
        new_user=User(**user_info)
        new_user.save()
        # exisiting_user= User.objects.get(**"arg")   
        # print(request.data)
        # print(request.get_json())
        return from_objectId_to_json(new_user)
    except Exception as e:
        print("L'erreur est:", e)
        return " il a une erreur" 
    

#nommé optonnel positionnée



@app.get('/api/user/<id>')
def get_user(id):
    try:
        existing_user=User.objects.get(id=id)
        return from_objectId_to_json(existing_user)
    except Exception as e:
        print("erreur", e)
        # if "does not match" in e.__str__():
        #     return "erreur"
        return "erreur interne de serveur"
    
@app.get('/api/users')
def get_all_users():
    try:
        users=User.objects.all()
        return [from_objectId_to_json(user) for user in users]
    

    except Exception as e:
        print(e.with_traceback())
        return jsonify([])

@app.put('/api/user/<id>')
def update_user(id:str):
    try:
        user=User.objects.get(id=id)
        user_info=request.get_json()
        if (user_info['mdp']==from_objectId_to_json(user)["mdp"]):
            print("c'est le bon utilisateur")
            user.update(**user_info)
            user.save()
            return from_objectId_to_json()
        raise PermissionError ("vous n'êtes pas autoriosé")

    except Exception as e:
        print(e)
        return e.__str__()




@app.delete('/api/user/<id>')
def delete_user(id: str):
    try:
        user=User.objects.get(id=id)
        mdp=request.get_json()['mdp']
        if (from_objectId_to_json(user)['mdp'] == mdp or from_objectId_to_json(user)['role'] == 'admin'):
            user.delete()
        return PermissionError('Action non autorisé')
    except:
        return 'une erreur est survenue'
        
#pip3 install certifi : commende d'activation du certificat
#pip3 freeze> requirements.txt : permet de recuperer tout les modules avec lesquels nous avons travailler dans un fichier requirements
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

@app.post('/api/book/')
def create_book():
    try:
        infos = request.get_json()
        user = User.objects.get(id=infos['userId'])
        new_book=Book(**infos)
        to_send=from_objectId_to_json(new_book)
        new_book.save()
        print(to_send)
        user.update(push__bookIds=to_send['_id'])
        return to_send
    except Exception as e:
        error_message=e.__str__()
        print("erreur: ", error_message)
        if ('User matching query' in error_message):
            return "l'utilisateur n'existe pas"
        if ('duplicate key error' in error_message):
            return "ce livre existe deja"
        
        return " une erreur est survenue ... "

@app.get('/api/book/<id>')
def get_book(id):
    try:
        book=Book.objects.get(id=id)
        return from_objectId_to_json(book)
    except:
        return "aucun livre trouvé"



@app.get("/api/books")
def get_all_books():
    try:
        books=Book.objects.all()
        return[from_objectId_to_json(book) for book in books]
    except:
        return "une erreur est survenue"



@app.get('/api/books/<userId')
def get_my_books(userId:str):
    try:
        user=User.get(id=userId)
        books=Book.objects(userId=userId)
       
        return [from_objectId_to_json(book) for book in books]
    except Exception as e:
        print(e)
        return " une erreur est survenue" 
    


@app.delete('/api/books/<id')
def delete_book(id:str):
    try:
        request_info=request.get_json()
        user=User.objects.get(id=request_info ['userId'])
        book=Book.objects.get(id=id)
        book_json=from_objectId_to_json(book)
        if user['mdp']==request_info ['mdp'] and (book_json['mdp']) or user
        return [from_objectId_to_json(book) for book in books]
    except Exception as e:
        print(e)
        return " une erreur est survenue" 


if __name__ == '__main__':
    app.run(debug=True)




