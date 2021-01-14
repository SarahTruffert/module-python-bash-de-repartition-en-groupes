
# Demander utilisateur ce qu'il veux OK
print("script pour former des groupes")
# importer liste (Liste.txt) en input et l'enregistrer dans mon programme OK
listeprenoms=input("Nom du fichier :") 
print(listeprenoms)
#input nombre max par groupe OK
nombre_max=input("Nombre maximal de personnes dans un groupe : ")
print(nombre_max)

# Lecture d'un fichier :
#fichier = open(nom,mode"r" ou "w"pour écrire,encoding)
#fichier = fichier.readlines()
#for ligne in fichier print (ligne)
listeprenoms=open(listeprenoms,encoding="utf8") 
#lire les noms ligne par ligne .readlines OK
listeprenoms=listeprenoms.readlines()
for ligne in listeprenoms : 
    print(ligne)


    #Avec Nicolas et Killian:
    import random
import os

choix_fichier= input("Choissisez le fichier que vous souhaitez ouvrir : ")
ouvre_fichier = open(choix_fichier,"r", encoding='utf8')
lire_fichier = ouvre_fichier.readlines()

#print(lire_fichier)

nombre_max_pers_groupe = int(input("Combien de nombre de personnes max souhaitez-vous par groupe :"))

pers_fichier = len(lire_fichier)
print(pers_fichier)

pers_par_groupe = []


if  pers_fichier % nombre_max_pers_groupe == 0 : 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)
else: 
    nb_groupes = (pers_fichier//nombre_max_pers_groupe)+1
print(nb_groupes)

# Si le groupe est pleins, remplir un autre groupe et supprimer de la liste promo :

# for personne in range(pers_fichier) :
#         if personne>0:
#             pers_par_groupe.extend([pers_par_groupe+1])
#             pers_fichier-=1
#             print(personne)


#Renvoyer aléatoirement, s' occuper du hasard = .random
#Renvoyer ce fichier en j.son des groupes repartis "pyhon export j.son file"
#Packager le script en module ? Liens Abdé
#Log