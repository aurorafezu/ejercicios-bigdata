import pandas as pd
import os

# Construir la ruta absoluta al archivo csv basándose en la ubicación de este script
base_dir = os.path.dirname(os.path.abspath(__file__))
# CORREGIDO: El nombre del archivo en tu carpeta es 'qog_data.csv'
file_path = os.path.join(base_dir, "datos", "qog", "qog_data.csv")

try:
    # Cargar datos con Pandas (No requiere Java)
    df = pd.read_csv(file_path, low_memory=False)

    print(f"¡Lectura exitosa!")
    print(f"Total de filas: {df.shape[0]}")
    print(f"Total de columnas: {df.shape[1]}")
    
    # Mostrar las primeras filas para verificar
    print("\nPrimeras 5 filas de ejemplo (País, Año):")
    if "cname" in df.columns and "year" in df.columns:
        print(df[["cname", "year"]].head(5))
    else:
        print(df.head(5))

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en: {file_path}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
