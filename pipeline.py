# pipeline.py
# Bloque B: Pipeline ETL con Spark
# Bloque C: Análisis y Visualización Avanzada + Machine Learning

from pyspark.sql import SparkSession, functions as F
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
import os
import sys

# Intentamos importar librerías de visualización.
try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    VISUALIZATION_READY = True
except ImportError as e:
    VISUALIZATION_READY = False
    print(f"Advertencia: Librerías de visualización no encontradas ({e}).")

def main():
    """
    Función principal del pipeline ETL + Análisis + ML.
    """
    print("--- INICIANDO PIPELINE COMPLETO (Apache) ---")
    
    spark = SparkSession.builder \
        .appName("QoG Magreb Analysis") \
        .master("spark://spark-master:7077") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")
    print("SparkSession creada exitosamente.")

    # --- BLOQUE B: ETL ---
    paises_magreb = ["DZA", "MAR", "TUN", "LBY", "MRT"]
    
    variables_interes = [
        "cname", "year", "ccodealp",
        "vdem_libdem", "gle_cgdpc", "ti_cpi", "bti_ci", "wdi_lifexp" 
    ]
    ruta_csv = "/opt/spark/work-dir/datos/qog/qog_data.csv"
    
    try:
        df_raw = spark.read.csv(ruta_csv, header=True, inferSchema=True)
    except Exception as e:
        print(f"Error crítico leyendo el archivo CSV: {e}"); spark.stop(); sys.exit(1)

    variables_existentes = [col for col in variables_interes if col in df_raw.columns]
    df_processed = df_raw.select(variables_existentes) \
        .filter(F.col("ccodealp").isin(paises_magreb)) \
        .filter(F.col("year").between(2000, 2022))

    df_processed = df_processed.withColumn("periodo_historico",
        F.when(F.col("year") < 2011, "Pre-Primavera")
         .otherwise("Post-Primavera")
    )
    
    ruta_salida = "/opt/spark/work-dir/datos/processed/qog_magreb.parquet"
    df_processed.write.mode("overwrite").parquet(ruta_salida)
    print("Datos procesados y guardados en Parquet.")

    # --- BLOQUE C: ANÁLISIS Y VISUALIZACIÓN ---
    if VISUALIZATION_READY:
        print("\n--- INICIANDO ANÁLISIS Y VISUALIZACIÓN ---")
        pdf = df_processed.toPandas()
        output_dir = "/opt/spark/work-dir/resultados"
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        sns.set_theme(style="whitegrid")
        
        # GRÁFICO 1: Evolución de la Democracia
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=pdf, x="year", y="vdem_libdem", hue="cname", marker="o")
        plt.title("Evolución de la Democracia en el Magreb (2000-2022)")
        plt.ylabel("Índice de Democracia Liberal")
        plt.axvline(x=2011, color='r', linestyle='--', alpha=0.5, label="Primavera Árabe")
        plt.savefig(os.path.join(output_dir, "1_evolucion_democracia.png"))
        plt.close()
        print("Gráfico 1 generado.")

        # GRÁFICO 2: PIB vs Democracia
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=pdf, x="gle_cgdpc", y="vdem_libdem", hue="cname", size="year", sizes=(20, 200), alpha=0.7)
        plt.title("Relación Riqueza (PIB) vs Democracia")
        plt.savefig(os.path.join(output_dir, "2_pib_vs_democracia.png"))
        plt.close()
        print("Gráfico 2 generado.")

        # GRÁFICO 3: Matriz de Correlación
        plt.figure(figsize=(8, 6))
        cols_corr = ["vdem_libdem", "gle_cgdpc", "ti_cpi", "wdi_lifexp"]
        cols_corr_existentes = [c for c in cols_corr if c in pdf.columns]
        if len(cols_corr_existentes) > 1:
            sns.heatmap(pdf[cols_corr_existentes].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
            plt.title("Matriz de Correlación")
            plt.savefig(os.path.join(output_dir, "3_correlacion_variables.png"))
            plt.close()
            print("Gráfico 3 generado.")

        # GRÁFICO 4: Impacto Primavera Árabe
        plt.figure(figsize=(10, 6))
        sns.barplot(data=pdf, x="cname", y="vdem_libdem", hue="periodo_historico", errorbar=None, palette="muted")
        plt.title("Democracia: Pre vs Post Primavera Árabe")
        plt.savefig(os.path.join(output_dir, "4_impacto_primavera_arabe.png"))
        plt.close()
        print("Gráfico 4 generado.")

        # --- ANÁLISIS DE CLUSTERING (K-MEANS) ---
        print("\n--- INICIANDO ANÁLISIS DE CLUSTERING K-MEANS ---")
        
        cluster_cols = ["vdem_libdem", "gle_cgdpc"]
        df_ml = df_processed.select(cluster_cols + ["cname", "year"]).dropna()

        if df_ml.count() > 0:
            assembler = VectorAssembler(inputCols=cluster_cols, outputCol="features_raw")
            scaler = StandardScaler(inputCol="features_raw", outputCol="features", withStd=True, withMean=True)
            
            df_assembled = assembler.transform(df_ml)
            scaler_model = scaler.fit(df_assembled)
            df_scaled = scaler_model.transform(df_assembled)

            kmeans = KMeans(featuresCol="features", k=3, seed=1)
            model = kmeans.fit(df_scaled)
            df_clustered = model.transform(df_scaled)
            
            pdf_clustered = df_clustered.toPandas()
            
            plt.figure(figsize=(12, 7))
            sns.scatterplot(data=pdf_clustered, x="vdem_libdem", y="gle_cgdpc", hue="cname", style="prediction", palette="viridis", s=150, alpha=0.8)
            plt.title("Clustering de Países del Magreb (K-Means)")
            plt.savefig(os.path.join(output_dir, "5_clustering_paises.png"))
            plt.close()

            print(f"¡Gráfico 5 (Clustering) generado!")
        else:
            print("No hay suficientes datos para el análisis de clustering.")
        
    else:
        print("\nSaltando visualización: Librerías no instaladas.")

    spark.stop()
    print("--- PIPELINE FINALIZADO ---")

if __name__ == "__main__":
    main()
