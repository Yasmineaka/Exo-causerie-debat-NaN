import random
import json





def randomWord():
    liste = ["e_mail", "prenom", "classe"]
    return (random.choice(liste) )


if __name__ == '__main__':
     nom = input('Entrez votre e_mail') 
     progression = {
              'email':nom,
              'chance': 3, 
              'level': {
              'motCache': 'mot caché',
              'motTrouvé': ''
              }
          }
     with open('j_son_de_l_exo.json', 'r') as f:
          r = f.read()
          progressions = json.load(r)
          for player in progressions:
               if player.get('email') == nom:
                    progression = player
     
     
     mot = randomWord()
     chance = 3
     flag = False
     startGame = True
     motCache = ["*"]*len(mot)
     print("".join(motCache))

while startGame:
     nombre = input(" Entrez un caractère de taille 1 \t")
     #for nombre in mot:
         
    
     #if len(nombre) != 1 and nombre is not str:
          #print("TypeError") 
#else:
     #print("*", end="")  

     #for i in mot:
          #print("*", end="")


#if nombre in mot:
     #print(mot) 
#else: 
     #print("*")


     for i in range(len(mot)):
          if mot[i]==nombre:
                motCache[i]= nombre
     else:
          chance -= 1
          print("Vous n'avez pas trouver le caractère")
     if flag:
          flag = False
     else:
          if chance <= 0:
               chance-= 1
               startGame = False
          else:
               print("Il vous reste ", chance)

     
     output = "".join(motCache)
     print(output)
     if output == mot:
          startGame = False

          
#print(randomWord())