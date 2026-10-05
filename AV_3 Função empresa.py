def dias(horas_trabalhadas):
    total = 0
    for hora in horas_trabalhadas:
        total += hora
    return total

horas = [8,8,8,8,8]

horasTrabalhadas = dias(horas)
print(f"Sua carga horaria essa semana foi de {horasTrabalhadas}")
if horasTrabalhadas >= 40:
    print("Carga horaria completa")
else:
    print("Carga horaria incompleta")