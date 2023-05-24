#nom =  open('connecter.json', 'w')
#nom.write(input('Salut bienvenue étranger'))

"""import json

t=open(';/code.txt', 'w')

fres=({'nom':'code', 'prenom':'kasm'})
conversion=json.dumps(fres)

t.write(conversion)

print()

t.close()"""
    

import json


fichier = open('exo_groupe.json', 'w')

fich = {'nom':'prenom', 'note':'pourcentage'}
f= json.dumps(fich)
fichier.write(f)
fichier.close()
print(f)
rep = open('exo_groupe.json', 'r')
for i in f:
    a = input('Entrez une donnée:' +" ")
    if a in f:
        print(True)
    else:
        print(False)