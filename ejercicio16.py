list = [55,68,95,12,88]
aux = list[0]
i = 0
for i in list:
    if (i < aux):
        aux = i
print("de la lista: ", list)
print("el menor número es: ", aux)
