"""def nomAge(nom,age) :
    i = nom
    b = age
    i = str(input("Etrez votre nom \t"))
    print(" ")
    b = int(input("Entrez votre age \t"))
    if b>100:
        age = 100 - age
    
    else:print("votre age est", b)
    return ("vous etes mort")

print(nomAge("nom","age"))"""







"""def ageText(a,b):
    if ((a*b)%3==0 and (a*b)%2==0):      
         return a+b
    if ((a*b)%5==0 or (a*b)%7==0):
          return b-a
    else: return a*b
print(ageText(7,7))"""




"""def lessThan(chaine,num):
    if (type(num) is not int or type(chaine) is not str):
        return -1
    elif (len(chaine)<num):
        return "less"
    elif (len(chaine)>num):
        return "most"
    else:
        return "same"
print(lessThan(5,"5"))"""












"""def Factoriel(nombre):
  nombre = int(input("Entrez un nombre"))
for  
print(Factoriel(4!))"""
  




















def recursive(i):

    while i >= 0:
        print (i)
        i = i - 1
        recursive(i)
        return i
recursive(995)


"""def compteur3():
    i = 0
    while i < 3:
        print(i)
        i = i + 1

print("bonjour")
compteur3()
compteur3()"""






