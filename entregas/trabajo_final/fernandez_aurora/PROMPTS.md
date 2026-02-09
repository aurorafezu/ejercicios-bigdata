# PROMPTS.md
# Documentación de Prompts de IA

## Parte 1: Prompts Reales (Copia textual)

### Bloque A: Infraestructura
"el spark-worker se apaga solo, en `docker ps -a` me sale con estado `Exited (0)`. Ya he intentado reiniciarlo pero no se queda encendido. ¿Cómo puedo saber por qué se para si el log está vacío? ¿Puede ser un problema en el `docker-compose.yml`?"

### Bloque B: Pipeline ETL
"Estoy ejecutando el script dentro de docker con `docker exec` pero me da el error `ModuleNotFoundError: No module named 'pyspark'`. No se supone que la imagen de `apache/spark` ya debería incluir `pyspark`? ¿Cómo puedo instalarlo correctamente dentro del contenedor que ya está corriendo?"

### Bloque C: Análisis
"Ya tengo los dos gráficos básicos que pide el trabajo, pero quiero que el análisis sea más completo para sacar mejor nota. ¿Qué otros gráficos más avanzados puedo hacer con mis variables (democracia, pib, corrupción) para que el trabajo quede más 'pro'? Dame ideas y el código en seaborn para un mapa de calor de correlación y una comparativa."

---

## Parte 2: Blueprint (Generado por IA)

### Project Blueprint: Magreb Political-Economic Analysis Pipeline

**1. Project Overview**
Development of a scalable Big Data pipeline to analyze the correlation between democratic stability and economic development in the Magreb region (2000-2022), utilizing the Quality of Government (QoG) dataset.

**2. Infrastructure Architecture (Dockerized)**
*   **Orchestration:** Docker Compose.
*   **Compute Cluster:** Apache Spark 3.5.1 (Standalone Mode).
    *   *Master Node:* Port 7077 (RPC), 8080 (Web UI).
    *   *Worker Node:* 1GB RAM, connected via internal bridge network `qog_network`.
*   **Storage/Database:** PostgreSQL 15 (Alpine) for persistent storage of results.
*   **Environment:** Python 3 environment with `pyspark`, `pandas`, `matplotlib`, and `seaborn` dependencies injected at runtime.

**3. ETL Pipeline Specification (PySpark)**
*   **Source:** `qog_std_ts_jan24.csv` (Raw CSV).
*   **Extraction:** Schema inference enabled, header parsing.
*   **Transformation Logic:**
    *   *Filtering:* Region subset (DZA, MAR, TUN, LBY, MRT) and temporal window (2000-2022).
    *   *Feature Selection:* `vdem_libdem` (Democracy), `gle_cgdpc` (GDP), `ti_cpi` (Corruption), `wdi_lifexp` (Life Expectancy).
    *   *Feature Engineering:*
        *   `nivel_democracia`: Categorical binning (Autoritario/Híbrido/Democracia).
        *   `periodo_historico`: Pre/Post Arab Spring (2011 threshold).
*   **Load:** Optimized storage in Parquet format (`qog_magreb.parquet`).

**4. Advanced Analytics & Machine Learning**
*   **Descriptive Analysis:** Time-series evolution of democratic indices.
*   **Correlation Analysis:** Pearson correlation matrix heatmap to identify variable dependencies.
*   **Impact Assessment:** Pre-post event analysis (2011 Arab Spring) comparing mean democracy scores.
*   **Unsupervised Learning:** K-Means Clustering (`k=3`) applied to standardized features (`vdem_libdem`, `gle_cgdpc`) to identify latent country groupings.

**5. Visualization Output**
*   Generated 5 high-resolution plots using Seaborn/Matplotlib, stored in `resultados/` directory.

---

## Parte 3: Autoevaluación y Declaración

### Verificación de Coherencia
*Responde estas preguntas para verificar que tu blueprint coincide con tu código:*

| Pregunta                                                              | Tu respuesta |
| --------------------------------------------------------------------- | :----------: |
| ¿La versión de Spark en el blueprint coincide con tu docker-compose.yml? |      Sí      |
| ¿Los países del blueprint son los mismos que filtra tu pipeline.py?     |      Sí      |
| ¿Las variables del blueprint están en tu código?                       |      Sí      |
| ¿El tipo de análisis del blueprint coincide con tus gráficos?          |      Sí      |

*Si alguna respuesta es "No", corrige el blueprint o el código.*

### Estadísticas Finales
*Estimación honesta del proceso de trabajo.*

| Métrica                                | Valor      |
| -------------------------------------- | ---------- |
| Total de interacciones con IA (aprox)  | ~55        |
| Prompts que funcionaron a la primera   | 4          |
| Errores resueltos (depuración)         | >10        |
| Horas totales de trabajo (aprox)       | ~12        |

### Declaración

- [x] Confirmo que los prompts de la PARTE 1 son reales y no fueron modificados ni pasados por IA para corregirlos.
- [x] Confirmo que el blueprint de la PARTE 2 fue generado por IA basándose en mi proyecto real.
- [x] Entiendo que inconsistencias entre el blueprint y mi código serán investigadas.

**Nombre:** Aurora Fernandez Zurita
**Fecha:** 10/02/2026
