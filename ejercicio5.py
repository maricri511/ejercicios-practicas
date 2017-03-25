nota = 0
cant = 0
prom = 0
acum = 0
while(cant < 5):
    cant += 1
    nota = int(input("ingrese nota: "))
    if (nota > 0 and nota < 11):
        acum = acum + nota
    else:
        print("ingrese una nota del 1 al 10")
        cant -=1
prom = acum /5
if (prom >7):
    print("el alumno aprobó la materia tiene un promedio de " + str(prom))
else:
    print("el alumno reprobó la materia tiene un promedio de " + str(prom))
