#Imc : poid(kg)/taille^2(m)
poidStr = input("combien tu pèse?\n")
tailleStr = input("quelle taille fais-tu?\n")

poid = float(poidStr)
taille = float(tailleStr)
imc = poid / (taille**2)
print("ton imc vaut:", imc)
