import random
import matplotlib.pyplot as plt

# Lista de equipos de la liga Colombiana
equipos = ['Nacional', 'Junior', 'Millonarios', 'Cali', 'Santa Fe', 'Once Caldas', 'Tolima', 'América', 'Medellín', 'Pasto']

# Generar listas paralelas para cada partido
equipos_local = []
equipos_visitante = []
goles_local = []
goles_visitante = []
for equipo in equipos:
    # Generar partidos de local
    for i in range(5):
        equipos_local.append(equipo)
        equipos_visitante.append(random.choice(equipos))
        goles_local.append(random.randint(0, 5))
        goles_visitante.append(random.randint(0, 5))
    # Generar partidos de visitante
    for i in range(5):
        equipos_local.append(random.choice(equipos))
        equipos_visitante.append(equipo)
        goles_local.append(random.randint(0, 5))
        goles_visitante.append(random.randint(0, 5))

# 1. Calcular la cantidad de partidos por equipo
partidos_jugados = {equipo: 0 for equipo in equipos}
for equipo in equipos_local:
    partidos_jugados[equipo] += 1
for equipo in equipos_visitante:
    partidos_jugados[equipo] += 1
print("Cantidad de partidos jugados por equipo:")
print(partidos_jugados)

# 2. Calcular la cantidad de partidos ganados por equipo
partidos_ganados = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    if goles_local[i] > goles_visitante[i]:
        partidos_ganados[equipos_local[i]] += 1
    elif goles_local[i] < goles_visitante[i]:
        partidos_ganados[equipos_visitante[i]] += 1
print("Cantidad de partidos ganados por equipo:")
print(partidos_ganados)

# 3. Calcular la cantidad de partidos perdidos por equipo
partidos_perdidos = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    if goles_local[i] < goles_visitante[i]:
        partidos_perdidos[equipos_local[i]] += 1
    elif goles_local[i] > goles_visitante[i]:
        partidos_perdidos[equipos_visitante[i]] += 1
print("Cantidad de partidos perdidos por equipo:")
print(partidos_perdidos)

# 4. Calcular la cantidad de partidos empatados por equipo
partidos_empatados = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    if goles_local[i] == goles_visitante[i]:
        partidos_empatados[equipos_local[i]] += 1
        partidos_empatados[equipos_visitante[i]] += 1
print("Cantidad de partidos empatados por equipo:")
print(partidos_empatados)
# 5. Calcular cantidad de goles de los equipos locales PLUS graficar
goles_por_equipo_local = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    goles_por_equipo_local[equipos_local[i]] += goles_local[i]

print("Cantidad de goles de los equipos locales:")
print(goles_por_equipo_local)

# Graficar cantidad de goles de los equipos locales
plt.bar(goles_por_equipo_local.keys(), goles_por_equipo_local.values())
plt.title("Goles de equipos locales")
plt.xlabel("Equipo")
plt.ylabel("Cantidad de goles")
plt.show()

# 6. Calcular cantidad de goles de los equipos visitantes PLUS graficar
goles_por_equipo_visitante = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_visitante)):
    goles_por_equipo_visitante[equipos_visitante[i]] += goles_visitante[i]

print("Cantidad de goles de los equipos visitantes:")
print(goles_por_equipo_visitante)

# Graficar cantidad de goles de los equipos visitantes
plt.bar(goles_por_equipo_visitante.keys(), goles_por_equipo_visitante.values())
plt.title("Goles de equipos visitantes")
plt.xlabel("Equipo")
plt.ylabel("Cantidad de goles")
plt.show()

# 7. Calcular la cantidad total de goles de todos los partidos
goles_totales = sum(goles_local) + sum(goles_visitante)
print("Cantidad total de goles en la liga Colombiana:")
print(goles_totales)

# 8. Calcular la cantidad de partidos por equipo
partidos_jugados = {equipo: 0 for equipo in equipos}
for equipo in equipos_local:
    partidos_jugados[equipo] += 1
for equipo in equipos_visitante:
    partidos_jugados[equipo] += 1
print("Cantidad de partidos jugados por equipo:")
print(partidos_jugados)

# 9. Listado de los equipos con sus goles de local y de visitante
goles_por_equipo = {equipo: [0, 0] for equipo in equipos}
for i in range(len(equipos_local)):
    goles_por_equipo[equipos_local[i]][0] += goles_local[i]
    goles_por_equipo[equipos_visitante[i]][1] += goles_visitante[i]
print("Goles por equipo:")
for equipo in equipos:
    print(equipo + ": local - " + str(goles_por_equipo[equipo][0]) + ", visitante - " + str(goles_por_equipo[equipo][1]))
# 10. Equipo que más goles realizó
equipo_mas_goles = max(goles_por_equipo, key=lambda x: sum(goles_por_equipo[x]))
print("Equipo que más goles realizó:")
print(equipo_mas_goles)

# 11. Equipo que menos goles recibió
goles_recibidos_por_equipo = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    goles_recibidos_por_equipo[equipos_local[i]] += goles_visitante[i]
    goles_recibidos_por_equipo[equipos_visitante[i]] += goles_local[i]
equipo_menos_goles_recibidos = min(goles_recibidos_por_equipo, key=goles_recibidos_por_equipo.get)
print("Equipo que menos goles recibió:")
print(equipo_menos_goles_recibidos)

# 12. Leer por teclado el nombre del equipo y listar los partidos en los que ha participado y sus marcadores
equipo_busqueda = input("Ingrese el nombre de un equipo para buscar sus partidos: ")
print("Partidos de " + equipo_busqueda + ":")
for i in range(len(equipos_local)):
    if equipos_local[i] == equipo_busqueda or equipos_visitante[i] == equipo_busqueda:
        print(equipos_local[i] + " " + str(goles_local[i]) + " - " + str(goles_visitante[i]) + " " + equipos_visitante[i])

# 13. Armar la tabla de posiciones y crear una nueva lista con los puntos por equipo
puntos_por_equipo = {equipo: 0 for equipo in equipos}
for i in range(len(equipos_local)):
    if goles_local[i] > goles_visitante[i]:
        puntos_por_equipo[equipos_local[i]] += 3
    elif goles_local[i] < goles_visitante[i]:
        puntos_por_equipo[equipos_visitante[i]] += 3
    else:
        puntos_por_equipo[equipos_local[i]] += 1
        puntos_por_equipo[equipos_visitante[i]] += 1
tabla_posiciones = sorted(puntos_por_equipo.items(), key=lambda x: x[1], reverse=True)

# 14. Imprimir la tabla de posiciones de mayor a mejor por puntaje
print("Tabla de posiciones:")
print("Equipo | Puntos")
for equipo, puntos in tabla_posiciones:
    print(equipo + " | " + str(puntos))   

# 15. Articular todo en un menú
while True:
    print("Menú")
    print("1. Ver cantidad de partidos por equipo")
    print("2. Ver cantidad de partidos ganados por equipo")
    print("3. Ver cantidad de partidos perdidos por equipo")
    print("4. Ver cantidad de partidos empatados por equipo")
    print("5. Ver cantidad de goles de los equipos locales")
    print("6. Ver cantidad de goles de los equipos visitantes")
    print("7. Ver cantidad total de goles de todos los partidos")
    print("8. Ver lista de los equipos con sus goles de local y de visitante")
    print("9. Ver equipo que más goles realizó")
    print("10. Ver equipo que menos goles recibió")
    print("11. Buscar los partidos de un equipo")
    print("12. Ver tabla de posiciones")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        for equipo in equipos:
            print(equipo + " jugó " + str(partidos_por_equipo[equipo]) + " partidos")
    elif opcion == "2":
        for equipo in equipos:
            print(equipo + " ganó " + str(partidos_ganados_por_equipo[equipo]) + " partidos")
    elif opcion == "3":
        for equipo in equipos:
            print(equipo + " perdió " + str(partidos_perdidos_por_equipo[equipo]) + " partidos")
    elif opcion == "4":
        for equipo in equipos:
            print(equipo + " empató " + str(partidos_empatados_por_equipo[equipo]) + " partidos")
    elif opcion == "5":
        plt.bar(equipos, goles_por_equipo_local)
        plt.title("Cantidad de goles de los equipos locales")
        plt.xlabel("Equipo")
        plt.ylabel("Goles")
        plt.show()
    elif opcion == "6":
        plt.bar(equipos, goles_por_equipo_visitante)
        plt.title("Cantidad de goles de los equipos visitantes")
        plt.xlabel("Equipo")
        plt.ylabel("Goles")
        plt.show()
    elif opcion == "7":
        print("Se marcaron " + str(sum(goles_local) + sum(goles_visitante)) + " goles en total")
    elif opcion == "8":
        print("Goles de los equipos locales:")
        for i in range(len(equipos)):
            print(equipos[i] + " - " + str(goles_por_equipo_local[i]))
        print("Goles de los equipos visitantes:")
        for i in range(len(equipos)):
            print(equipos[i] + " - " + str(goles_por_equipo_visitante[i]))
    elif opcion == "9":
        print("Equipo que más goles realizó:")
        print(equipo_mas_goles)
    elif opcion == "10":
        print("Equipo que menos goles recibió:")
        print(equipo_menos_goles_recibidos)
    elif opcion == "11":
        equipo_busqueda = input("Ingrese el nombre de un equipo para buscar sus partidos: ")
        print("Partidos de " + equipo_busqueda + ":")
        for i in range(len(equipos_local)):
            if equipos_local[i] == equipo_busqueda or equipos_visitante[i] == equipo_busqueda:
                print(equipos_local[i] + " " + str(goles_local[i]) + " - " + str(goles_visitante[i]) + " " + equipos_visitante[i])
    elif opcion == "12":
        tabla_posiciones = []
        for equipo in equipos:
            puntos = partidos_ganados_por_equipo[equipo] * 3 + partidos_empatados_por_equipo[equipo]
            tabla_posiciones.append((equipo, puntos))
        tabla_posiciones.sort(key=lambda x: x[1], reverse=True)
        print("Tabla de posiciones:")
        print("Equipo".ljust(20) + "Puntos")
        for posicion, equipo in enumerate(tabla_posiciones, 1):
            print(str(posicion).ljust(4) + equipo[0].ljust(20) + str(equipo[1]))
    else:
        print("Opción inválida")