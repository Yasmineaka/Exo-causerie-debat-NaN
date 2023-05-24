from mongoengine import Document,StringField, EmailField, ReferenceField, ListField


class User(Document):
    nom=StringField(requiered=True)
    prenom=StringField(requiered=True)
    e_mail=EmailField(requiered=True)
    mdp=StringField(requiered=True)
    User_name=StringField(requiered=True)
    Book_id=ListField(ReferenceField('book'))