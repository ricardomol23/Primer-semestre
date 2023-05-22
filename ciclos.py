# Suma y promedio de los primeros 20 números pares e impares
suma_pares = 0
suma_impares = 0

# Suma de los primeros 20 números pares
for i in range(2, 42, 2):
    suma_pares += i

# Suma de los primeros 20 números impares
for i in range(1, 41, 2):
    suma_impares += i

# Cálculo de los promedios
promedio_pares = suma_pares / 20
promedio_impares = suma_impares / 20

# Imprimir los resultados
print("La suma de los primeros 20 números pares es:", suma_pares)
print("El promedio de los primeros 20 números pares es:", promedio_pares)

print("La suma de los primeros 20 números impares es:", suma_impares)
print("El promedio de los primeros 20 números impares es:", promedio_impares)
