import json



"""fichier =  open('fichier.JSON', 'w')
print(fichier)
f=json.dumps({'name': "nan", 'prenom':"6.23"})
fichier.write(f)"""




fichier =  open('fichier.json', 'r')
print(fichier.read())
f = fichier.read()
print(json.load(f))
