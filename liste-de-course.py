import sys

file = open('courses.json','a').close()
read = file.read()
courses = json.load('r')
   

# declaration liste vide
liste_de_course = ["coco", "caca","viande"]

# choisi une option
user_entrer = int(input("""
    Choisissez parmis les 5 options suivant:
    1 - Ajoutez un élément à la liste 
    2 - Retirer un élément de la liste
    3 - Afficher les éléments de la liste  
    ? Votre choix : """
))

# si l'entrer est incorrect
if not 1 <= user_entrer <= 5:
    print("Veuillez choisir une option valide")

# execution en fonction de l'entrer
if user_entrer == 1:
    elem_ajouter = input("Entrer votre elelment ")
    liste_de_course.append(elem_ajouter)
    print(f"L'élément {elem_ajouter} à bien été ajouté")
    print(liste_de_course)
elif user_entrer == 2:
    elem_sup = input("Entrer votre élément à retirer ")
    if elem_sup in liste_de_course:
        liste_de_course.remove(elem_sup)
        print(f"L'élément {elem_sup} à bien supprimer de la liste")
        print(liste_de_course)
    else:
        print(f"L'élément {elem_sup} n'est pas dans la liste")
elif user_entrer == 3:
    if liste_de_course:
        for i,item in enumerate(liste_de_course,1):
            print(f"{i}.{item}")
    else:
        print("La liste est vide ")
else:
    print("Code")