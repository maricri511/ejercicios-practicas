usuario = cristina
contrasena = 511
while (true):
    usuario_op = input("ingrese nombre de ususario")
    if (usuario_op == usuario):
        contrasena_op = int(input("ingrese contraseña"))
        if (contrasena_op == contrasena):
            print("puede ingresar al sistema")
        break
        else:
            print("la contraseña no es válida")
    else:
        print("no existe el usuario")
