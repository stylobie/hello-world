caractereASupprimer = "e"
print("tapez votre suite de caractères")
phrase = input()
nouvellePhrase = ""

for c in phrase:
    if c != caractereASupprimer:
        nouvellePhrase = nouvellePhrase + c
print(nouvellePhrase)
