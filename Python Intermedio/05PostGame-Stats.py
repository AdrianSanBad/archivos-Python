# Creamos una lista de diccionarios donde cada diccionario representa un jugador
jugadores = [
    {'nombre': 'jugador 1', 'posicion': 'QB', 'numero': 12, 'yardas': 150, 'touchdowns': 2},
    {'nombre': 'jugador 2', 'posicion': 'RB', 'numero': 24, 'yardas': 75, 'touchdowns': 1},
    {'nombre': 'jugador 3', 'posicion': 'WR', 'numero': 88, 'yardas': 200, 'touchdowns': 3}
]

# Imprimir una lista de todas las posiciones de los jugadores en el conjunto de datos
positions = [jugador['posicion'] for jugador in jugadores]
print("Lista de posiciones de los jugadores:")
print(positions)

# Elegir un jugador y actualizar sus estadísticas de juego en el conjunto de datos
jugadorActualizar = 'jugador 1'
for player in jugadores:
    if player['nombre'] == jugadorActualizar:
        player['yardas'] = 200
        player['touchdowns'] = 3

# Calcular las estadísticas promedio (por ejemplo, yardas ganadas, touchdowns) para todos los jugadores e imprimir los resultados
totalYardas = 0
totalTouchdowns = 0

for player in jugadores:
    totalYardas += player['yardas']
    totalTouchdowns += player['touchdowns']

promedioYardas = totalYardas / len(jugadores)
promedioTouchdowns = totalTouchdowns / len(jugadores)

print("Estadísticas promedio:")
print("Yardas promedio ganadas por jugador:", promedioYardas)
print("Touchdowns promedio por jugador:", promedioTouchdowns)
