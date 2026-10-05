def notas(notas):
    aprovadas = []
    for nota in notas:
        if nota >= 7:
            aprovadas.append(nota)
    return aprovadas


notas_aprovadas = [7, 5, 6, 8, 4, 10, 2, 14, 10, 7]

print("Notas aprovadas:", notas_aprovadas(notas))