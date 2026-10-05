def calculeouro(lista_notas):
    total = 0
    for nota in lista_notas:
        total += nota
    media = total / len(lista_notas)
    return media

notas = [6, 7, 8]

media = calculeouro(notas)
print(f"A media foi de {media}")