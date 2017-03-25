print("COTIZACIONES")
importe = 1
moneda = ""
while(importe != 0):
    importe = int(input("ingrese importe a cotizar (0 para salir)"))
    if (importe !=0):
        moneda = input("Ingrese moneda e para Euro y d para Dolar: ")
        if(moneda == "d"):
            importe = importe*15.60
            print("El importe en pesos de los Dólares ingresados es de: " + str(importe))
        elif(moneda == "e"):
            importe = importe*17.90
            print("El importe en pesos de los Euros ingresados es de: " + str(importe))
        else:
            print("solamente ingresare para e Euros y d para Dolar!!")
    
