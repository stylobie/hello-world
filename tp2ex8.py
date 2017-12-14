TELEPHONES = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
NAMES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numero = input("Quel est le numéro?")
findIt = False
for i in range(0, 9):
    if TELEPHONES[i] == numero:
        print(NAMES[i])
        findIt = True

if not findIt:
    print("non attribué")
