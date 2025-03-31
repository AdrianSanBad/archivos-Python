#se genera un metodo que recibe una matriz de n x m y devuelve la cantidad de celdas dominantes
def numCells(grid):
    #n es el numero de filas
    n = len(grid)
    #m es el numero de columnas
    m = len(grid[0])
    #se crea una lista de tuplas con las direcciones de los vecinos
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    #se inicializa la variable que contara las celdas dominantes
    dominant_count = 0
    #se recorren las filas
    for i in range(n):
        #se recorren las columnas
        for j in range(m):
            
            is_dominant = True
            #se revisa las celdas vecinas mediante nx, ny 
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] >= grid[i][j]:
                    is_dominant = False
                    break
            if is_dominant:
                dominant_count += 1
    
    return dominant_count
