import random
import matplotlib.pyplot as plt

equipos = ['Atlético Nacional', 'Independiente Medellín', 'Deportivo Cali', 'América de Cali', 'Millonarios', 'Santa Fe', 'Junior', 'Atlético Bucaramanga', 'Once Caldas', 'Deportes Tolima', 'Envigado', 'Alianza Petrolera', 'La Equidad', 'Jaguares de Córdoba', 'Patriotas Boyacá', 'Águilas Doradas']

goles_local = [random.randint(0, 5) for _ in range(len(equipos))]
goles_visitante = [random.randint(0, 5) for _ in range(len(equipos))]

print("Equipos locales:", equipos)
print("Goles locales:", goles_local)
print("Goles visitantes:", goles_visitante)

goles_totales_local = sum(goles_local)
print("Goles totales del equipo local:", goles_totales_local)

plt.bar(equipos, goles_local)
plt.title("Goles del equipo local")
plt.xlabel("Equipo")
plt.ylabel("Goles")
plt.show()
