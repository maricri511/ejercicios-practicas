numerobcos = 25

alumnos = int(input("ingrese cantidad de alumnos: "))
if (alumnos > numerobcos):
    dif = alumnos - numerobcos
    print("faltan" + str(dif) + "bancos")
else:
    print("los alumnos se pueden inscribir")
