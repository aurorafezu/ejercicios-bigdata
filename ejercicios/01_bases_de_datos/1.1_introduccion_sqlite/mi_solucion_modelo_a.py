# -*- coding: utf-8 -*-
"""
================================================================================
|| MI SOLUCIÓN - Modelo A: Catálogo Simple (Desnormalizado)                 ||
================================================================================
Este es mi script para crear la base de datos del Modelo A.
"""

import sqlite3
import pandas as pd
import glob
from pathlib import Path

# --- 1. CONFIGURACIÓN DE RUTAS ---
# Apuntamos a la raíz del proyecto para que las rutas siempre funcionen
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent 
RUTA_CSVs = BASE_DIR / "datos" / "csv_tienda"
# Guardaremos nuestra base de datos en la raíz del proyecto
RUTA_DB = BASE_DIR / "mi_tienda_modelo_a.db"

def extraer_nombre_tabla(ruta_csv):
    """
    Crea un nombre de tabla válido a partir del nombre del archivo CSV.
    Ej: 'case-fan.csv' -> 'case_fan'
    """
    nombre_base = Path(ruta_csv).stem
    return nombre_base.replace('-', '_')

# --- 2. SCRIPT PRINCIPAL ---
def main():
    print("🚀 INICIANDO CONSTRUCCIÓN DEL MODELO A...")
    print(f"Buscando CSVs en: {RUTA_CSVs}")
    print(f"La base de datos se guardará en: {RUTA_DB}")

    # Buscamos todos los archivos .csv en la carpeta de datos
    archivos_csv = glob.glob(str(RUTA_CSVs / "*.csv"))

    if not archivos_csv:
        print("❌ ¡Error! No se encontraron archivos CSV. Asegúrate de que la carpeta 'datos/csv_tienda' existe y contiene los archivos.")
        return

    print(f"✅ Se encontraron {len(archivos_csv)} archivos CSV.")

    # Creamos la conexión a la base de datos (se crea si no existe)
    with sqlite3.connect(RUTA_DB) as conexion:
        print(f"💾 Conexión establecida con {RUTA_DB.name}")
        
        total_filas = 0
        # --- 3. BUCLE PARA PROCESAR CADA CSV ---
        for ruta_csv in archivos_csv:
            nombre_tabla = extraer_nombre_tabla(ruta_csv)
            print(f"   -> Procesando '{Path(ruta_csv).name}' para la tabla '{nombre_tabla}'...")
            
            # Leemos el archivo CSV con pandas
            df = pd.read_csv(ruta_csv)
            
            # Usamos to_sql() para volcar el DataFrame a una tabla SQLite
            # if_exists='replace': si la tabla ya existe, la borra y la vuelve a crear
            # index=False: para no guardar el índice de pandas como una columna
            df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)
            
            print(f"      ✅ Tabla '{nombre_tabla}' creada con {len(df)} filas.")
            total_filas += len(df)

    print("\n" + "="*70)
    print("🏁 ¡CONSTRUCCIÓN DEL MODELO A COMPLETADA!")
    print(f"Se crearon {len(archivos_csv)} tablas.")
    print(f"Se cargaron un total de {total_filas:,} filas.")
    print(f"Puedes abrir el archivo '{RUTA_DB.name}' con DB Browser for SQLite para explorarlo.")
    print("="*70)


if __name__ == "__main__":
    main()
