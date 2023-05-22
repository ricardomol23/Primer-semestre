import random
import matplotlib.pyplot as plt
from collections import defaultdict

# Ingresar cantidad de equipos
num_equipos = int(input("Ingrese la cantidad de equipos: "))

# Generar lista de equipos
equipos = ['Equipo ' + str(i) for i in range(1, num_equipos + 1)]

# Definir función para generar partidos de local y visitante
def generar_partidos(equipos):
    partidos = []
    for i in range(len(equipos)):
        for j in range(i+1, len(equipos)):
            partidos.append((equipos[i], equipos[j]))
    return partidos

# Generar lista de partidos
partidos = generar_partidos(equipos)

# Generar resultados aleatorios de los partidos
resultados = defaultdict(lambda: [0, 0])
for partido in partidos:
    goles_local = random.randint(0, 5)
    goles_visitante = random.randint(0, 5)
    resultados[partido[0]][0] += goles_local
    resultados[partido[1]][1] += goles_visitante

# Calcular estadísticas
estadisticas = defaultdict(dict)

for equipo in equipos:
    partidos_jugados = 0
    partidos_ganados = 0
    partidos_perdidos = 0
    partidos_empatados = 0
    goles_a_favor = 0
    goles_en_contra = 0
    diferencia_goles = 0
    for partido in partidos:
        if equipo in partido:
            partidos_jugados += 1
            if resultados[partido[0]][0] > resultados[partido[1]][1]:
                if equipo == partido[0]:
                    partidos_ganados += 1
                else:
                    partidos_perdidos += 1
            elif resultados[partido[0]][0] < resultados[partido[1]][1]:
                if equipo == partido[0]:
                    partidos_perdidos += 1
                else:
                    partidos_ganados += 1
            else:
                partidos_empatados += 1
            if equipo == partido[0]:
                goles_a_favor += resultados[partido[0]][0]
                goles_en_contra += resultados[partido[1]][1]
                diferencia_goles += resultados[partido[0]][0] - resultados[partido[1]][1]
            else:
                goles_a_favor += resultados[partido[1]][1]
                goles_en_contra += resultados[partido[0]][0]
                diferencia_goles += resultados[partido[1]][1] - resultados[partido[0]][0]
    estadisticas[equipo]['partidos_jugados'] = partidos_jugados
    estadisticas[equipo]['partidos_ganados'] = partidos_ganados
    estadisticas[equipo]['partidos_perdidos'] = partidos_perdidos
    estadisticas[equipo]['partidos_empatados'] = partidos_empatados
    estadisticas[equipo]['goles_a_favor'] = goles_a_favor
    estadisticas[equipo]['goles_en_contra'] = goles_en_contra
    estadisticas[equipo]['diferencia_goles'] = diferencia_goles

#Imprimir estadísticas
print("Estadísticas:")
for equipo in equipos:
    print("Equipo:", equipo)
    print("Partidos jugados:", estadisticas[equipo]['partidos_jugados'])
    print("Partidos ganados:", estadisticas[equipo]['partidos_ganados'])
    print("Partidos perdidos:", estadisticas[equipo]['partidos_perdidos'])
    print("Partidos empatados:", estadisticas[equipo]['partidos_empatados'])
    print("Goles a favor:", estadisticas[equipo]['goles_a_favor'])
    print("Goles en contra:", estadisticas[equipo]['goles_en_contra'])
    print("Diferencia de goles:", estadisticas[equipo]['diferencia_goles'])
    print()
#Graficar estadísticas
labels = equipos
partidos_jugados = [estadisticas[equipo]['partidos_jugados'] for equipo in equipos]
partidos_ganados = [estadisticas[equipo]['partidos_ganados'] for equipo in equipos]
partidos_perdidos = [estadisticas[equipo]['partidos_perdidos'] for equipo in equipos]
partidos_empatados = [estadisticas[equipo]['partidos_empatados'] for equipo in equipos]

x = range(len(labels))

plt.bar(x, partidos_empatados, color='gray', label='Partidos empatados', bottom=[partidos_ganados[i]+partidos_perdidos[i] for i in x])
plt.bar(x, partidos_perdidos, color='red', label='Partidos perdidos', bottom=partidos_ganados)
plt.bar(x, partidos_ganados, color='green', label='Partidos ganados')
plt.bar(x, partidos_jugados, color='blue', label='Partidos jugados')

plt.xticks(x, labels)
plt.xlabel("Equipos")
plt.ylabel("Partidos")
plt.legend()

plt.show()