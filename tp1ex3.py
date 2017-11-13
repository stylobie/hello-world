print("entrez votre prénom et votre nom séparés d'un espace")
fullName = input()

sep = " "
nom = ""
prenom = ""
inPrenom = True
for i in range(0, len(fullName)):
    if fullName[i] == sep:
        inPrenom = False
    elif inPrenom:
        prenom = prenom + fullName[i]
    else:
        nom = nom + fullName[i]
print(prenom[0].upper() + ". " + nom[0].upper())
