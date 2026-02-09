# 05_RESPUESTAS.md: Preguntas de Comprensión

### 1. Infraestructura: Si tu worker tiene 2 GB de RAM y el CSV pesa 3 GB, ¿qué pasa? ¿Cómo lo solucionarías?

Si un worker de Spark con 2 GB de RAM intenta cargar directamente en memoria un archivo CSV de 3 GB, el proceso fallará. Ocurrirá un error de tipo `OutOfMemoryError` (OOM) y el contenedor del worker probablemente se reiniciará o morirá. Esto se debe a que Spark, aunque está diseñado para trabajar con datos más grandes que la memoria, necesita poder cargar los datos en **particiones**. Si una sola partición es más grande que la memoria disponible para el executor de Spark en ese worker, el trabajo no podrá procesarse.

**Soluciones:**

1.  **Aumentar los Recursos del Worker (Solución Obvia):** La solución más directa es aumentar la memoria RAM asignada al worker. En el `docker-compose.yml`, se podría cambiar `SPARK_WORKER_MEMORY` de `1G` a `4G` (o más, dependiendo de la máquina anfitriona). Esto permitiría que particiones más grandes quepan en memoria.

2.  **Incrementar el Número de Particiones (Solución Inteligente de Spark):** La forma correcta de trabajar en Spark no es cargar todo el archivo de golpe. Al leer el CSV, podemos forzar a Spark a dividirlo en más trozos (particiones) más pequeños.
    ```python
    # Forzar a Spark a usar 200 particiones al leer el CSV
    df = spark.read.csv("ruta/al/csv.csv", header=True, inferSchema=True).repartition(200)
    ```
    De esta manera, cada partición será mucho más pequeña (ej: 3 GB / 200 = 15 MB por partición), y cabrán fácilmente en los 2 GB de RAM del worker. Spark procesará las particiones una por una o en paralelo, sin agotar nunca la memoria.

3.  **Añadir más Workers:** Si una sola máquina no es suficiente, la solución de Big Data es escalar horizontalmente: añadir más `spark-worker` al clúster. Si tenemos dos workers de 2 GB, el clúster tendría 4 GB de RAM total para procesamiento, distribuyendo las particiones entre ambos.

---

### 2. ETL: ¿Por qué `spark.read.csv()` no ejecuta nada hasta que llamas a `.count()` o `.show()`?

Esto se debe a un concepto fundamental de Spark llamado **Lazy Evaluation** (Evaluación Perezosa).

Cuando ejecutas una **transformación** como `spark.read.csv()`, `.filter()`, `.select()` o `.withColumn()`, Spark no ejecuta la operación inmediatamente. En lugar de eso, construye un "plan de ejecución" lógico, conocido como **DAG (Directed Acyclic Graph)**. Es como si Spark tomara nota de todas las operaciones que quieres hacer en una libreta, pero sin mover un solo dato.

La ejecución real solo se dispara cuando se invoca una **acción**. Las acciones son operaciones que requieren que Spark produzca un resultado concreto, como:
-   `.show()`: Para mostrar filas en la consola.
-   `.count()`: Para contar el número total de filas.
-   `.collect()`: Para traer los datos a la memoria del driver (¡cuidado con esto!).
-   `.write.parquet()`: Para guardar los datos en un archivo.

La **ventaja** de la Lazy Evaluation es la **optimización**. Al tener el plan completo antes de ejecutar, el optimizador de Spark (llamado Catalyst) puede reorganizar, combinar o simplificar las operaciones para encontrar la forma más eficiente de llegar al resultado final, minimizando la cantidad de datos que se leen y se mueven por la red.

---

### 3. Análisis: Interpreta tu gráfico principal: ¿qué patrón ves y por qué crees que ocurre?

Mi gráfico principal es la **Evolución de la Democracia en el Magreb (2000-2022)**. El patrón más evidente y dramático es la **divergencia radical** de los países a partir de 2011.

-   **Patrón Observado:** Antes de 2011, todos los países se movían en un rango bajo y estable de democracia (índices entre 0.1 y 0.3). A partir de 2011, la línea de **Túnez** se dispara hacia arriba, superando el umbral de "Régimen Híbrido" y entrando en "Democracia/Transición". En cambio, la línea de **Libia** se desploma a casi cero. Mientras tanto, **Argelia, Marruecos y Mauritania** apenas muestran cambios, continuando en sus trayectorias de autoritarismo o régimen híbrido.

-   **Causa Probable:** Este patrón es un reflejo directo del impacto de la **Primavera Árabe**, que comenzó precisamente en Túnez a finales de 2010 y se extendió por la región en 2011.
    -   En **Túnez**, las protestas llevaron al derrocamiento del dictador Ben Ali y al inicio de una transición democrática exitosa (la única de la Primavera Árabe), lo que explica el espectacular aumento en su índice de democracia.
    -   En **Libia**, el mismo evento llevó a una intervención militar de la OTAN y a una guerra civil que desintegró el estado, explicando el colapso total de sus instituciones.
    -   En los otros países, los regímenes lograron contener las protestas mediante reformas cosméticas (Marruecos), represión o gasto social (Argelia), por lo que su estructura política no cambió fundamentalmente.

---

### 4. Escalabilidad: Si tuvieras que repetir este ejercicio con un dataset de 50 GB, ¿qué cambiarías en tu infraestructura?

Un dataset de 50 GB ya no es manejable por un mini-clúster en un solo portátil. Para escalar la infraestructura, realizaría los siguientes cambios:

1.  **No usar `localhost`:** Movería la infraestructura de mi portátil a un proveedor de **Cloud Computing** (como Amazon Web Services, Google Cloud o Microsoft Azure). Esto me daría acceso a recursos virtualmente ilimitados.

2.  **Aumentar el Tamaño y Número de los Workers:** En lugar de un solo worker con 1 GB de RAM, configuraría un clúster con múltiples nodos (ej: 5 workers), cada uno con mucha más memoria y CPU (ej: 16 GB de RAM y 4 cores cada uno). Esto se conoce como **escalado horizontal**.

3.  **Usar un Sistema de Almacenamiento Distribuido:** El CSV de 50 GB no estaría en el disco local de un contenedor. Lo almacenaría en un servicio de almacenamiento optimizado para Big Data, como **Amazon S3**, **Google Cloud Storage** o **Azure Blob Storage**. Spark está diseñado para leer datos directamente desde estos sistemas de forma paralela y muy eficiente.

4.  **Optimizar el Código de Spark:**
    -   **Schema Definition:** En lugar de `inferSchema=True` (que obliga a Spark a leer el archivo una vez solo para adivinar los tipos de datos), definiría el `schema` manualmente. Esto ahorra mucho tiempo en un dataset grande.
    -   **Formato de Archivo:** Si el dataset ya estuviera procesado, me aseguraría de que estuviera en formato **Parquet** u **ORC**, que son formatos columnares mucho más eficientes para las consultas de Spark que un CSV.
    -   **Gestor de Clúster Profesional:** En un entorno de producción, en lugar de usar el modo Standalone de Spark, utilizaría un gestor de recursos más robusto como **Kubernetes** o **YARN**, que gestionan de forma más inteligente la asignación de recursos y la tolerancia a fallos.
