print("tapez votre chaine de caractères")
phrase = input()
compteur = 0
for i in range(0, len(phrase)):
    if phrase[i] == "e":
        compteur = compteur + 1
print(compteur)
