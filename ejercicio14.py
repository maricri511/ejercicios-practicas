cont = 0
frase = ""
frase = input("ingrese frase para contar sus vocales: ")
for l in frase:
    if (l == "a" or l== "e" or l == "i" or l == "o" or l == "u"):
        cont += 1
print("la frase tiene: ", cont, "vocales")
