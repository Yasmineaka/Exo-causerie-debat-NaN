"""bureau = open('./exo.py', 'r')

#print(bureau.read())
#print(bureau.readline())
print(bureau.readlines())"""


classe = open('./contact.txt', 'r')
print(classe.read())
for classe in classe:
    item = classe.split(':')
print(classe.read(f'''nom : {[0]}
                  prenom : {[1]}
                  contact : {[2]}'''))