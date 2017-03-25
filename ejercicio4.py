cont_admin = "123"
cont_operador = "456"
usuario_op =""
contrase_op = 0
while (True):
    usuario_op = input("ingrese nombre de usuario: ")
    if (usuario_op == "admin"):
        print("bienvenido administrador")
        contrase_op = input("ingrese contraseña: ")
        if (contrase_op == cont_admin):
            print("puede ingresar al sistema")
            break
        else:
            print("contraseña incorrecta!!!")
    elif(usuario_op == "operador"):
        print("bienvenido señor operador")
        contrase_op = input("ingrese contraseña: ")
        if(contrase_op == cont_operador):
            print("puede ingresar al sistema")
            break
        else:
            print("contraseña incorrecta")
    else:
        print("ususario incorrecto")
