from mongoengine import Document,StringField, EmailField, ReferenceField, DateField
class User(Document):
    categorie=StringField(requiered=True)
    nom=StringField(requiered=True)
    description=EmailField(requiered=True)
    auteur=StringField(requiered=True)
    user_id=ReferenceField('user',requiered=True)
    date_d_ajout=DateField(required=True)
    