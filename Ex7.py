a=4
b=7
print("A vous de jouer")
x=int(input("Entrer le numero de ligne\n"))
y=int(input("Entrer le numero de colonne\n"))


if x==a and y==b :
    print ("coulé")
elif  x==(a+1) and y==b :
    print ("en vue")
elif x==(a+1) and y==b-1:
     print ("en vue")
elif x==(a+1) and y==b-1:
    print ("en vue")
elif x==(a) and y==b+1:
    print ("en vue")
elif x==(a) and y==b-1:
    print ("en vue")
elif x==(a-1) and y==b:
    print ("en vue")
elif x==(a-1) and y==b-1:
     print ("en vue")
elif x==(a-1) and y==b-1:
    print ("en vue")
else : 
    print ("à l'eau")