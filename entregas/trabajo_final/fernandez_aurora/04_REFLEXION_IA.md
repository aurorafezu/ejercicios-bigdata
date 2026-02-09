# 04_REFLEXION_IA.md: 3 Momentos Clave del Aprendizaje

## Bloque A: Infraestructura Docker

### 1. Momento de Arranque
Lo primero que le pedí a la IA fue que me generara un `docker-compose.yml` básico con Spark y Postgres. No tenía claro cómo se conectaban los servicios entre sí, qué puertos necesitaba cada uno, ni cómo se compartían los archivos. Necesitaba un punto de partida funcional para empezar a construir.

### 2. Momento de Error
Mi gran error fue la odisea para hacer que el clúster de Spark funcionara. El problema principal era que el `spark-worker` no se conectaba al `spark-master`, lo que provocaba que cualquier trabajo de Spark se quedara "colgado" con el error `Initial job has not accepted any resources`.

El error se manifestó de varias formas:
-   Al principio, los contenedores se apagaban solos con `Exited (0)`.
-   Luego, intentamos cambiar de imagen a `bitnami/spark`, pero no encontrábamos la versión correcta.
-   Finalmente, el error clave estaba en el `docker-compose.yml` con la imagen de `apache/spark`: **le faltaba el `command` explícito** que le dice a un contenedor que actúe como "Master" y al otro como "Worker". Sin esa orden, los contenedores no sabían qué hacer y se apagaban.

La solución fue añadir las líneas `command: /opt/spark/bin/spark-class ...` a cada servicio de Spark, forzándolos a asumir su rol.

### 3. Momento de Aprendizaje
Aprendí que un contenedor de Docker no es una máquina virtual que "sabe" qué es. Es simplemente un proceso aislado. Si no le das un comando de larga duración que lo mantenga ocupado (como iniciar un servicio de Master o Worker), el contenedor ejecuta su punto de entrada, termina y se apaga. **El `command` no es opcional, es la razón de ser del contenedor.**

### Prompt Clave del Bloque A
> "el spark-worker se apaga solo, en `docker ps -a` me sale con estado `Exited (0)`. Ya he intentado reiniciarlo pero no se queda encendido. ¿Cómo puedo saber por qué se para si el log está vacío? ¿Puede ser un problema en el `docker-compose.yml`?"

---

## Bloque B: Pipeline ETL con Spark

### 1. Momento de Arranque
Una vez que la infraestructura funcionó, mi primer paso fue pedirle a la IA el código básico en PySpark para leer el archivo CSV. No conocía la sintaxis para crear una `SparkSession`, leer datos, seleccionar columnas y filtrar por una lista de países.

### 2. Momento de Error
El error más frustrante fue el `ModuleNotFoundError: No module named 'pyspark'`. Yo asumía que si la imagen era de Spark, la librería de Python `pyspark` vendría instalada y lista para usar. La IA me explicó que esto no siempre es así y que necesitaba instalarla **dentro** del contenedor `spark-master` que ya estaba en ejecución. El comando clave fue `docker exec -it spark-master pip install pyspark pandas matplotlib seaborn`.

### 3. Momento de Aprendizaje
Aprendí el concepto de **Lazy Evaluation (Evaluación Perezosa)** de Spark. Me di cuenta de que comandos como `.read.csv()` o `.filter()` no ejecutan nada en el momento. Solo construyen un plan de ejecución (DAG). La "magia" no ocurre hasta que invocas una **acción** como `.show()`, `.count()` o, en mi caso, `.write.parquet()`. Entender esto me hizo ver por qué Spark es tan eficiente: espera a tener el plan completo para optimizarlo antes de mover un solo dato.

### Prompt Clave del Bloque B
> "Estoy ejecutando el script dentro de docker con `docker exec` pero me da el error `ModuleNotFoundError: No module named 'pyspark'`. No se supone que la imagen de `apache/spark` ya debería incluir `pyspark`? ¿Cómo puedo instalarlo correctamente dentro del contenedor que ya está corriendo?"

---

## Bloque C: Análisis y Visualización

### 1. Momento de Arranque
Para empezar el análisis, le pedí a la IA ideas sobre qué gráficos podía crear para responder mi pregunta de investigación. No quería hacer solo los gráficos básicos, sino contar una historia con los datos. La IA me sugirió empezar con una serie temporal para ver la evolución y un gráfico de dispersión para comparar riqueza y democracia.

### 2. Momento de Error
Mi error más tonto fue cuando añadimos los gráficos avanzados. El script se ejecutaba sin errores, pero en la carpeta `resultados` solo aparecían los dos gráficos originales, no los nuevos. El problema era que yo estaba editando el `pipeline.py` que estaba en mi carpeta de entrega (`entregas/trabajo_final/fernandez_aurora/`), pero el `docker-compose.yml` estaba configurado para montar y ejecutar el `pipeline.py` que estaba en la **raíz del proyecto**. No estaban sincronizados. La solución fue copiar el código avanzado al archivo de la raíz.

### 3. Momento de Aprendizaje
Aprendí a interpretar una **matriz de correlación (heatmap)**. Antes, solo veía un cuadro de colores y números. Ahora entiendo que los valores cercanos a 1 o -1 indican una relación fuerte, y que el parámetro `annot=True` en Seaborn es fundamental para imprimir los valores y poder interpretar el gráfico correctamente. También aprendí que una correlación baja (como 0.1 entre PIB y Democracia) es un resultado tan importante como una correlación alta.

### Prompt Clave del Bloque C
> "Ya tengo los dos gráficos básicos que pide el trabajo, pero quiero que el análisis sea más completo para sacar mejor nota. ¿Qué otros gráficos más avanzados puedo hacer con mis variables (democracia, pib, corrupción) para que el trabajo quede más 'pro'? Dame ideas y el código en seaborn para un mapa de calor de correlación y una comparativa."
