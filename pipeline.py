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
    print("--- INICIANDO PIPELINE 'SOBRESALIENTE' (Apache) ---")
    
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
        output_dir = "/opt/spark/work-dir/resultados"
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        sns.set_theme(style="whitegrid")
        
        # --- ANÁLISIS DE CLUSTERING (K-MEANS) ---
        print("\n--- INICIANDO ANÁLISIS DE CLUSTERING K-MEANS ---")
        
        # CORRECCIÓN: Usamos solo las 2 variables principales para el clustering para evitar problemas con nulos.
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
            plt.xlabel("Índice de Democracia Liberal")
            plt.ylabel("PIB per cápita (USD)")
            plt.legend(title="País / Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, "5_clustering_paises.png"))
            plt.close()

            print(f"¡Gráfico de Clustering generado exitosamente en {output_dir}!")
        else:
            print("No hay suficientes datos para el análisis de clustering después de eliminar nulos.")
        
    else:
        print("\nSaltando visualización: Librerías no instaladas.")

    spark.stop()
    print("--- PIPELINE FINALIZADO ---")

if __name__ == "__main__":
    main()
