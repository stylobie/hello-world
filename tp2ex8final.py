#On attribue les numéros de téléphone étant de 01 à 10 dans la liste TELEPHONES 
TELEPHONES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
#On attribue les noms de A à J dans la liste NAMES
NAMES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#On demande le numéro de la personne
numero = input("Quel est le numéro?")
#Ce booléen est mis sur False, quand on trouvera le numéro et le
#on met le booléen sur true pour sortir de la boucle
findIt = False
#La boucle va chercher le numéro et attribuer le nom de la personne
for i in range(0, 9):
    if TELEPHONES[i] == numero:
        print(NAMES[i])
        findIt = True
#Si le nombre est attribué, le booléen est sur True. Dans le test prochain, on
#vérifie si ce booléen est False. Si il est false le numéro à pas été attribué
#et donc le numéro est pas attribué.
if not findIt:  
    print("non attribué")
