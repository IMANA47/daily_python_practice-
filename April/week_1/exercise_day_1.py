"""
Nom du fichier : exercise_day_1.py
Auteur : Francois Nsengimana
Date : 18/04/2026
Version : 1.0

Description :
Ce programme permet la mise en pratique des notion de Variable et types.

Dépendances :
- Python 3.14.0
"""


"""
=======================
Consigne pratique
=======================

Exercice : Variables et types

"""
#1. Créer une variable nom et lui assigner votre prénom.
nom = "Nsengimana"

#2. Créer une variable age et lui assigner votre âge.
age = 26

# 3. Afficher le type de la variable age.
print(type(age))

# 4. Créer une variable taille et lui assigner votre taille en mètres.
taille = 1.80

# 5. Afficher la variable nom et age dans une seule phrase.
print(f"Votre nom est {nom}  et age {age} ")

# 6. Convertir l'âge en chaîne de caractères et l'afficher. 
age_str = str(age)
print("L'age ", age_str)

# 7. Créer une variable est_etudiant de type booléen.
est_etudiant = True

# 8. Vérifier si age est supérieur à 18. 
if age > 18:
    print("Superieur")

# 9. Créer une variable somme et lui assigner la somme de 10 et 20. 
somme = 10 + 20
print(somme)

# 10. Créer une variable produit et lui assigner le produit de 5 et 7.
produit = 5, 7
