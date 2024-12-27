#Début du programme 

operateur = input("Veuillez choisir un opérateur entre +, -, *, /, % \n")

premierNombre = int(input("Veuillez entrer un premier nombre ="))
secondNombre = int(input("Veuillez entrer un deuxième nombre = "))

if operateur == "+":
    resultat = premierNombre + secondNombre
if operateur == "-":
    resultat = premierNombre - secondNombre
if operateur == "*":
    resultat = premierNombre * secondNombre
if operateur == "/":
    resultat = premierNombre / secondNombre
if operateur == "%":
    resultat = premierNombre % secondNombre

#Fin du programme
print(f"{premierNombre} {operateur} {secondNombre} = {resultat}")