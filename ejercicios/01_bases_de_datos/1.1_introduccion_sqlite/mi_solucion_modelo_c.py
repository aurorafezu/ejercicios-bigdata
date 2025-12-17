# -*- coding: utf-8 -*-
"""
================================================================================
|| MI SOLUCIÓN - Modelo C: E-Commerce Completo                              ||
================================================================================
Este script extiende el Modelo B para crear una base de datos de e-commerce
completa, añadiendo clientes, pedidos, inventario y generando datos de ejemplo.
"""

import sqlite3
import pandas as pd
import glob
from pathlib import Path
import random
from datetime import datetime, timedelta

# --- 1. CONFIGURACIÓN DE RUTAS ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent 
RUTA_CSVs = BASE_DIR / "datos" / "csv_tienda"
RUTA_DB = BASE_DIR / "mi_tienda_modelo_c.db"

# --- 2. FUNCIONES DE CREACIÓN DE ESQUEMA ---

def crear_esquema_base(conexion):
    """Crea las tablas del Modelo B (productos, categorías, etc.)."""
    cursor = conexion.cursor()
    print("🏗️  Creando esquema base (Modelo B)...")
    cursor.execute("CREATE TABLE IF NOT EXISTS categorias (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS fabricantes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS colores (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL UNIQUE)")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, precio REAL,
            categoria_id INTEGER, fabricante_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos_colores (
            producto_id INTEGER, color_id INTEGER,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (color_id) REFERENCES colores(id)
        )
    """)
    conexion.commit()
    print("✅ Esquema base creado.")

def crear_esquema_ecommerce(conexion):
    """Crea las tablas adicionales para el e-commerce."""
    cursor = conexion.cursor()
    print("🏗️  Creando tablas de e-commerce (clientes, pedidos, etc.)...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            producto_id INTEGER PRIMARY KEY,
            stock INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            fecha TEXT NOT NULL,
            total REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lineas_pedido (
            id INTEGER PRIMARY KEY,
            pedido_id INTEGER,
            producto_id INTEGER,
            cantidad INTEGER,
            precio_unitario REAL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """)
    
    conexion.commit()
    print("✅ Tablas de e-commerce creadas.")

# --- SCRIPT PRINCIPAL ---
def main():
    print("🚀 INICIANDO CONSTRUCCIÓN DEL MODELO C...")
    
    if RUTA_DB.exists():
        RUTA_DB.unlink()
        print(f"🗑️ Base de datos anterior '{RUTA_DB.name}' eliminada.")

    with sqlite3.connect(RUTA_DB) as conexion:
        print(f"💾 Conexión establecida con {RUTA_DB.name}")
        
        # 1. Crear todos los esqueletos de tablas
        crear_esquema_base(conexion)
        crear_esquema_ecommerce(conexion)

        # Aquí irán los siguientes pasos...

    print("\n🏁 ¡CONSTRUCCIÓN DEL MODELO C COMPLETADA (por ahora)!")

if __name__ == "__main__":
    main()
