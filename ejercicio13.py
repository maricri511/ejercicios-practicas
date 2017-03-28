num = 0
acum = 0
prom = 0
list = []
while num < 5:
    num_op = int(input("ingrese numero: "))
    acum = acum + num_op
    list.append(num_op)
    num += 1
prom = acum / num
print(list)
print("el promedio de la lista de numeros es: " + str(prom))
