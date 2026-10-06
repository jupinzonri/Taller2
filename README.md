# Taller 2: Autómatas Celulares
**Nombre:** Juan Felipe Pinzón Rincón

## 2.10 Ejercicios y Problemas

### 1. Reglas básicas de comportamiento en distintos escenarios
Las personas actuamos como autómatas celulares mediante una serie de reglas implícitas que definen nuestro comportamiento. Mis reglas se definirían de la siguiente manera:
* **En casa:** Si es de noche y terminé mis asignaciones, procedo a realizar mi rutina personal y descansar; si es de día y hay trabajo pendiente, enciendo la laptop para programar modelos en Python.
* **En la Universidad:** Si es hora de clase, me dirijo al aula correspondiente; si tengo un bloque libre, voy a la biblioteca a estudiar o avanzar en proyectos.
* **En el medio de transporte (conduciendo):** Si el semáforo está en rojo o el vehículo de adelante frena, piso el freno para detenerme; si la vía está libre y el semáforo en verde, acelero manteniendo la velocidad permitida.

### 2. Modelo de difusión usando ACs probabilísticos (Enfermedad)
Los autómatas celulares probabilísticos utilizan reglas para emular contagios espaciales. 
* **Estados:** Sano (0), Contagiado (1), Recuperado (2).
* **Regla de contagio:** Si una célula sana tiene al menos un vecino contagiado, se contagia con cierta probabilidad.
* **Regla de recuperación:** Tras un tiempo determinado, la célula pasa a estado recuperado.
*(El código de simulación se encuentra en el archivo Python adjunto en este repositorio)*

### 3. Comportamiento de un robot con tres sensores de distancia
El robot opera mediante autómatas celulares no uniformes.
* **Sensores pasivos:** Centro (C), Derecho (D), Izquierdo (I) detectan obstáculos en distintos rangos.
* **Actuadores activos:** Motor Izquierdo (Mi) y Motor Derecho (Md).
* **Lógica de evasión:** Cuando el sensor central detecta un objeto en distancia crítica, la regla de transición invierte un motor y apaga el otro para evitar la colisión frontal, permitiendo la rotación sobre su propio eje.
*(La lógica algorítmica programada se encuentra en el archivo Python adjunto)*

### 4. Análisis con Diagramas de Voronoi en una ciudad
Los diagramas de Voronoi permiten dividir espacios físicos en zonas de influencia basadas en la proximidad.
* **Análisis de cobertura:** Si un polígono de Voronoi (por ejemplo, para un colegio o centro de salud) es inusualmente grande, indica un déficit de cobertura y obliga a los ciudadanos a realizar grandes desplazamientos.
* **Relación entre diagramas:** Al cruzar los diagramas de distintas infraestructuras, las áreas con polígonos densos y pequeños coincidirán con los focos de mayor desarrollo urbano.
*(El script de generación gráfica se encuentra en el archivo Python adjunto)*
