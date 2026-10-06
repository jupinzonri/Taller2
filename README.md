"""
# Taller 2: Autómatas Celulares
**Nombre:** Juan Felipe Pinzón Rincón

## 2.10 Ejercicios y Problemas

### 1. Reglas básicas de comportamiento en distintos escenarios
El documento menciona que las personas también actuamos como autómatas celulares mediante una serie de reglas implícitas que definen nuestro comportamiento[span_0](start_span)[span_0](end_span). Mis reglas se definirían de la siguiente manera:
- **En casa:** Si es de noche y terminé mis asignaciones, procedo a realizar mi rutina de skincare y dormir; si es de día y hay trabajo pendiente, enciendo mi laptop Lenovo para correr modelos de optimización en Python.
- **En la Universidad Nacional:** Si es hora de clase, me dirijo al aula correspondiente; si tengo un bloque libre, voy a la biblioteca a estudiar.
- **En el medio de transporte (conduciendo):** Si el semáforo está en rojo o el vehículo de adelante frena, piso el freno para detenerme; si la vía está libre y el semáforo en verde, acelero manteniendo la velocidad permitida.

### 2. Modelo de difusión usando ACs probabilísticos (Enfermedad)
Los autómatas celulares probabilísticos utilizan reglas que permiten el cambio de estado basándose en probabilidades para emular movimientos y contagios, como en la difusión de un virus[span_1](start_span)[span_1](end_span). 
- **Estados del retículo:** Sano (S), Contagiado (C), y Recuperado (R).
- **Regla de contagio:** Si una célula S tiene al menos un vecino C, pasa al estado C con una probabilidad de 0.3 en el siguiente ciclo temporal[span_2](start_span)[span_2](end_span).
- **Regla de recuperación:** Una célula en estado C, después de 14 ciclos, tiene una probabilidad de 0.9 de pasar al estado R y 0.1 de desaparecer del retículo simulando el deceso[span_3](start_span)[span_3](end_span).
- **Movimiento espacial:** En cada ciclo ejecutado en paralelo, las células pueden desplazarse hacia celdas vecinas vacías (Norte, Sur, Este u Oeste) con una probabilidad de 0.25[span_4](start_span)[span_4](end_span).

### 3. Comportamiento de un robot con tres sensores de distancia
El robot móvil se modela operando mediante autómatas celulares no uniformes que cambian de estado dependiendo de la información de proximidad que proveen los sensores[span_5](start_span)[span_5](end_span).
- **Sensores:** Las células pasivas Centro (C), Derecho (D) e Izquierdo (I) perciben el entorno, asumiendo estados (0, 1, 2) que representan diferentes intervalos de distancia en centímetros respecto a los 4 objetos aleatorios[span_6](start_span)[span_6](end_span).
- **Actuadores:** Los motores actúan como células activas (Mi y Md) con estados propios (0, 1, 2) que dictan si están apagados, encendidos hacia adelante o encendidos hacia atrás[span_7](start_span)[span_7](end_span).
- **Regla de evasión:** Cuando el sensor C detecta un objeto en el intervalo de proximidad crítico (estado 0), una regla de transición activa el motor izquierdo para girar hacia atrás (estado 2) y apaga el derecho (estado 0), logrando una rotación que evita la colisión frontal[span_8](start_span)[span_8](end_span).

### 4. Análisis con Diagramas de Voronoi en una ciudad
Los diagramas de Voronoi son útiles para teselaciones irregulares, dividiendo un espacio físico en zonas de influencia según la proximidad a un conjunto de puntos[span_9](start_span)[span_9](end_span).
- **Zonificación de servicios:** Al tomar el plano de la ciudad, cada droguería, centro de salud o colegio actúa como un punto central, y los polígonos resultantes delimitan el área donde ese establecimiento es la opción más cercana[span_10](start_span)[span_10](end_span).
- **Análisis de cobertura:** Sí, el diagrama permite identificar falencias; si un polígono de Voronoi es inusualmente grande, indica que los residentes de los extremos deben recorrer grandes distancias, evidenciando la necesidad de ubicar un nuevo centro de salud o colegio en esa zona.
- **Relación entre diagramas:** Se espera una correlación directa entre los distintos mapas de Voronoi, ya que las zonas con polígonos pequeños (alta densidad de servicios de salud) coincidirán generalmente con polígonos pequeños en educación, reflejando las áreas de mayor desarrollo urbano.
"""
