from pathlib import Path

p = input("entrez un chemin")
chemin = Path.home() / p
chemin.mkdir(exist_ok = True)
dico = { 'janvier':['exercice', 'training', 'projet', 'presentation'],
         'fevrier':['exercice', 'training', 'projet', 'presentation'],
         'mars':['exercice', 'training', 'projet', 'presentation'],
         'avril':['exercice', 'training', 'projet', 'presentation'],
         'mai':['exercice', 'training', 'projet', 'presentation'],
         'juin':['exercice', 'training', 'projet', 'presentation'],
         'juillet':['exercice', 'training', 'projet', 'presentation'],
         'aout':['exercice', 'training', 'projet', 'presentation'],
         'septembre':['exercice', 'training', 'projet', 'presentation'],
         'octobre':['exercice', 'training', 'projet', 'presentation'],
         'novembre':['exercice', 'training', 'projet', 'presentation'],
         'decembre':['exercice', 'training', 'projet', 'presentation'] }


for k,v in dico.items():
    parents = chemin / k
    parents.mkdir(exist_ok = True)
    for f in v:
        c = parents /f
        c.mkdir(exist_ok = True)





















   
         