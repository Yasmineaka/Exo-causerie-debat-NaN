from mongoengine import Document,StringField, EmailField, ReferenceField, ListField


class User(Document):
    nom=StringField(requiered=True)
    prenom=StringField(requiered=True)
    email=EmailField(requiered=True)
    mdp=StringField(requiered=True)
    role= StringField(requiered=False, default='user')
    username=StringField(requiered=True, unique=True)
    book_id=ListField(ReferenceField('Book'))


