def reemplazar_enlista(l, busco, reemplazo):
    lreemp = []

    for el in l:
        if(el == busco):
            lreemp.append(reemplazo)
        else:
            lreemp.append(el)
    return lreemp

lista_original = ["Cris", "Dario", "Damian", "Valentina", "Cris", "Jesica", "Stella"]
lista_reemplazada = reemplazar_enlista(lista_original, "Cris", "Cristina")

print(lista_reemplazada)
