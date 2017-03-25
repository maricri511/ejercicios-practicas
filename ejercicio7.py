primernum = 0
segnum = 0
op = 1
band = True
resultado = 0
print("calculadora")
print("0.- salir")
print("1.- suma")
print("2.- resta")
print("3.- división")
print("4.- multiplicación")
while(op != 0):
    primernum = int(input("ingrese primer numero"))
    op = int(input("ingrese opcion: "))
    if (op != 0):
        if(op == 1):
            segnum = int(input("ingrese segundo numero"))
            resultado = primernum + segnum
        elif(op == 2):
            segnum = int(input("ingrese segundo numero"))
            resultado = primernum - segnum
        elif(op == 3):
            segnum = int(input("ingrese segundo numero"))
            if (segnum == 0):
                band = False
            else:
                resultado = primernum / segnum
        elif(op == 4):
            segnum = int(input("ingrese segundo numero"))
            resultado = primernum * segnum
        else:
            print("solo se deben ingresar una opcion del 1 al 4 o cero para salir!")
    else:
        break
    if (band):
        print ("Resultado: " + str(resultado))
    else:
        print("no existe la división por cero! por lo tanto no hay Resultado")
    band = True
