import random
import os
import json

choix_fichier= input("Choissisez le fichier que vous souhaitez ouvrir : ")
ouvre_fichier = open(choix_fichier,"r", encoding='utf8')
#nom_equipe = open("equipe.txt","r", encoding='utf8')
#lire_nom_equipe = nom_equipe.readlines()

#equipe = shuffle.nom_equipe()

lire_fichier = ouvre_fichier.readlines()
groupe_final = []
nombre_max_pers_groupe = int(input("Combien de nombre de personnes max souhaitez-vous par groupe :"))

for prenom in lire_fichier:
    strip_prenom = prenom.strip()
    groupe_final.append(strip_prenom)

pers_fichier = len(groupe_final)
print("Vous êtes : ", pers_fichier, "personnes")

pers_par_groupe = []


if  pers_fichier % nombre_max_pers_groupe == 0 : 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)
else: 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)+1
print("Il y'aura donc ", nb_groupes, "groupes :")



x=1
while x <= nb_groupes:
    pers_par_groupe.append([])
    x +=1


i=0
while i <= nombre_max_pers_groupe:
    for groupe in pers_par_groupe :  
        if pers_fichier > 0 :
            choix_random = random.choice(groupe_final)
            groupe.append(choix_random)
            groupe_final.remove(choix_random)
            pers_fichier=len(groupe_final)
        
    i+=1


for personne in pers_par_groupe :

    log_final = f"{personne}"
    with open("log.json", 'a') as f:
        json.dump(log_final, f)
    e = open ("log.txt",'a')
    e.writelines(log_final)
    e.close()
    print(log_final)









