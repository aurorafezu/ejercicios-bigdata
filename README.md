# Desarrollo Político-Económico en el Magreb: Análisis Big Data

**Autor:** Aurora Fernandez Zurita
**Curso:** Big Data con Python

## 📋 Descripción del Proyecto
Este proyecto implementa un pipeline de Big Data completo utilizando **Docker**, **Apache Spark** y **Python**. El objetivo es analizar la relación entre la estabilidad democrática y el desarrollo económico en la región del Magreb (Argelia, Marruecos, Túnez, Libia y Mauritania) durante el periodo 2000-2022.

El análisis incluye procesamiento ETL, visualización de datos y un modelo de Machine Learning (K-Means Clustering) para identificar patrones de desarrollo.

## 🚀 Instrucciones de Ejecución Rápida

Sigue estos pasos para levantar la infraestructura y ejecutar el análisis:

### 1. Levantar la Infraestructura
Asegúrate de tener Docker Desktop abierto y ejecuta:
```bash
docker compose up -d
```

### 2. Instalar Dependencias (Solo la primera vez)
Instala las librerías necesarias dentro del contenedor Master:
```bash
docker exec -it spark-master pip install pyspark pandas matplotlib seaborn
```

### 3. Ejecutar el Pipeline
Lanza el script de análisis:
```bash
docker exec -it spark-master python3 /opt/spark/work-dir/pipeline.py
```

Los resultados (gráficos) se generarán en la carpeta `resultados/`.

## 📂 Estructura del Repositorio

- **`entregas/trabajo_final/fernandez_aurora/`**: 👈 **AQUÍ ESTÁ LA ENTREGA OFICIAL**. Contiene toda la documentación (`.md`), capturas y archivos finales.
- **`docker-compose.yml`**: Definición de la infraestructura del clúster Spark + Postgres.
- **`pipeline.py`**: Código fuente del ETL y análisis.
- **`datos/`**: Carpeta con el dataset QoG (ignorada por git).
- **`resultados/`**: Carpeta donde se guardan los gráficos generados.

## 🛠️ Tecnologías Usadas
- **Infraestructura:** Docker, Docker Compose.
- **Procesamiento:** Apache Spark 3.5.1 (PySpark).
- **Análisis y ML:** Spark MLlib (K-Means), Pandas.
- **Visualización:** Matplotlib, Seaborn.
