
pago = ""
monto = 0
monto = int(input("ingrese monto de la compra: "))
pago = input("Al contado?si/no: ")
if (pago == "si"):
    monto = monto - (monto * 10 /100)
    print("El monto a pagar es de $" + str(monto))
else:
    print("El monto a pagar es de $" + str(monto))
