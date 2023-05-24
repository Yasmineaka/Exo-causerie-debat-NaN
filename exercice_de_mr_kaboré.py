import json



fichier = open('exo_maison.json', 'w')
coordonnés = {'nom':'aka', 'prenom':'yasmine', 'nom2':'ak', 'prenom2':'amenan'}
f= json.dumps(coordonnés)
fichier.write(f)
fichier.close()
print(f)
rep = open('exo_maison.json', 'r')

for i in f:
    a = input('Bonjour bienvenue Mr/ Mme' + " " + '\n' + 'Entrez votre nom:' + " " )
    b = input('Entrez votre prenom:' + " ")
    if a and b in f:
        print('Vos coordonnés correspondent')
    else:
        print("Vous n'êtes pas encore enregistré veillez vous enregistrer") 
Ajouter = open('exo_maison.json', 'a')
enregistrement = input('Entrez votre nom') and input('entrez votre prenom')
enreg = json.dumps(enregistrement)
fichier.append(enreg)





        
       
        