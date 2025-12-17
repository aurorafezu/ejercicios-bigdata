# -*- coding: utf-8 -*-
"""
================================================================================
|| MI SOLUCIÓN - Modelo B: Normalizado (3NF)                                ||
================================================================================
Este es mi script para crear la base de datos del Modelo B, aplicando lo
aprendido en el EDA.
"""

import sqlite3
import pandas as pd
import glob
from pathlib import Path

# --- 1. CONFIGURACIÓN DE RUTAS ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent 
RUTA_CSVs = BASE_DIR / "datos" / "csv_tienda"
RUTA_DB = BASE_DIR / "mi_tienda_modelo_b.db"

def crear_esquema(conexion):
    """
    Crea las 5 tablas del modelo normalizado si no existen.
    """
    cursor = conexion.cursor()
    
    print("🏗️  Creando esquema de la base de datos...")

    # Tabla para las categorías (CPU, GPU, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    # Tabla para los fabricantes (Intel, AMD, etc.)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fabricantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    # Tabla para los colores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    # Tabla principal de productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL,
            categoria_id INTEGER,
            fabricante_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id)
        )
    """)

    # Tabla de relación Muchos-a-Muchos entre productos y colores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos_colores (
            producto_id INTEGER,
            color_id INTEGER,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (color_id) REFERENCES colores(id)
        )
    """)
    
    conexion.commit()
    print("✅ Esquema creado con 5 tablas.")

# --- SCRIPT PRINCIPAL ---
def main():
    print("🚀 INICIANDO CONSTRUCCIÓN DEL MODELO B...")
    
    # Nos aseguramos de que el archivo de la BD esté limpio cada vez que ejecutamos
    if RUTA_DB.exists():
        RUTA_DB.unlink()
        print(f"🗑️ Base de datos anterior '{RUTA_DB.name}' eliminada.")

    # Creamos la conexión (y el archivo de la BD)
    with sqlite3.connect(RUTA_DB) as conexion:
        print(f"💾 Conexión establecida con {RUTA_DB.name}")
        
        # 1. Crear el esqueleto de la base de datos
        crear_esquema(conexion)

        # Aquí irán los siguientes pasos...

    print("\n🏁 ¡CONSTRUCCIÓN DEL MODELO B COMPLETADA (por ahora)!")

if __name__ == "__main__":
    main()
