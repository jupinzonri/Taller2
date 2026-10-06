import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# ==========================================
# 2. Modelo de difusión usando ACs probabilísticos (Enfermedad)
# ==========================================
def simular_difusion_enfermedad(ciclos=20, tamano=50, prob_contagio=0.3, prob_recuperacion=0.1):
    # Inicialización del retículo: 0 = Sano, 1 = Contagiado, 2 = Recuperado
    grid = np.zeros((tamano, tamano))
    
    # Introducir casos iniciales aleatorios (Pacientes cero)
    grid[tamano//2, tamano//2] = 1
    grid[tamano//3, tamano//3] = 1
    
    historial_grid = [grid.copy()]
    
    for _ in range(ciclos):
        nuevo_grid = grid.copy()
        for i in range(tamano):
            for j in range(tamano):
                estado = grid[i, j]
                
                # Evaluar la vecindad de Moore (3x3)
                vecinos = grid[max(0, i-1):min(tamano, i+2), max(0, j-1):min(tamano, j+2)]
                
                if estado == 0:  
                    contagiados_cerca = np.sum(vecinos == 1)
                    if contagiados_cerca > 0 and np.random.rand() < prob_contagio:
                        nuevo_grid[i, j] = 1
                elif estado == 1:  
                    if np.random.rand() < prob_recuperacion:
                        nuevo_grid[i, j] = 2
                        
        grid = nuevo_grid
        historial_grid.append(grid.copy())
        
    return historial_grid

# ==========================================
# 3. Comportamiento de un robot con tres sensores de distancia
# ==========================================
def regla_evasion_robot(sensor_izq, sensor_centro, sensor_der):
    """
    Entradas (distancia): 0 (Crítico), 1 (Medio), 2 (Libre)
    Salidas (Motor Izq, Motor Der): 0 (Apagado), 1 (Adelante), 2 (Atrás)
    """
    if sensor_centro == 0:
        return (2, 0) # Obstáculo inminente al frente: Rotar sobre su eje
    elif sensor_izq == 0:
        return (1, 0) # Obstáculo a la izquierda: Evadir hacia la derecha
    elif sensor_der == 0:
        return (0, 1) # Obstáculo a la derecha: Evadir hacia la izquierda
    else:
        return (1, 1) # Espacio libre: Avanzar en línea recta

# ==========================================
# 4. Análisis con Diagramas de Voronoi en una ciudad
# ==========================================
def generar_voronoi_ciudad():
    # Simular coordenadas (x, y) de servicios en la ciudad
    np.random.seed(15)
    puntos_servicios = np.random.rand(12, 2) * 100 
    
    # Calcular las regiones de Voronoi
    vor = Voronoi(puntos_servicios)
    
    # Generar la visualización
    fig, ax = plt.subplots(figsize=(8, 6))
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='darkred', line_width=2, line_alpha=0.7, point_size=12)
    
    ax.set_title("Diagrama de Voronoi: Áreas de Influencia de Servicios")
    ax.set_xlabel("Coordenada Espacial X")
    ax.set_ylabel("Coordenada Espacial Y")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Para ejecutar la visualización localmente, puedes llamar a la función:
# generar_voronoi_ciudad()
