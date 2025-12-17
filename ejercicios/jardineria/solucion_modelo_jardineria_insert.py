"""
insertar_datos_jardineria.py

Inserta datos de ejemplo en la base de datos SQLite jardineria.db
para poder practicar consultas SQL y JOINs.

Autor: (tu nombre)
Fecha: 2025-12-17
"""

import sqlite3
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------
RUTA_DB = Path(__file__).parent / "jardineria.db"


# -------------------------------------------------------------------
# INSERTS
# -------------------------------------------------------------------
def insertar_oficinas(cur):
    oficinas = [
        ("MAD-ES", "Madrid", "España", "Madrid", "28001", "910000001",
         "Calle Gran Vía 1", None),
        ("BCN-ES", "Barcelona", "España", "Cataluña", "08001", "930000002",
         "Avenida Diagonal 100", None),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO oficina
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, oficinas)


def insertar_empleados(cur):
    empleados = [
        (1, "Juan", "Pérez", None, "101", "juan.perez@jardineria.com",
         "MAD-ES", None, "Director General"),
        (2, "Ana", "López", "García", "102", "ana.lopez@jardineria.com",
         "MAD-ES", 1, "Ventas"),
        (3, "Carlos", "Ruiz", None, "201", "carlos.ruiz@jardineria.com",
         "BCN-ES", 1, "Ventas"),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO empleado
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, empleados)


def insertar_gamas(cur):
    gamas = [
        ("Herramientas", "Herramientas de jardinería", None, None),
        ("Plantas", "Plantas ornamentales", None, None),
        ("Macetas", "Macetas y contenedores", None, None),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO gama_producto
        VALUES (?, ?, ?, ?)
    """, gamas)


def insertar_productos(cur):
    productos = [
        ("P001", "Pala de acero", "Herramientas", "100x20 cm",
         "Gardena", "Pala resistente", 50, 19.99, 12.00),
        ("P002", "Rastrillo", "Herramientas", "80x30 cm",
         "Bosch", "Rastrillo metálico", 40, 14.50, 9.00),
        ("P003", "Rosa roja", "Plantas", None,
         "Viveros SA", "Rosa ornamental", 100, 5.50, 2.50),
        ("P004", "Maceta barro", "Macetas", "30 cm",
         "Cerámicas SL", "Maceta tradicional", 70, 8.00, 4.00),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO producto
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, productos)


def insertar_clientes(cur):
    clientes = [
        (100, "Floristería Ana", "Ana", "Martín", "910123123",
         None, "Calle Flores 10", None, "Madrid", None,
         "España", "28010", 2, 5000),
        (101, "Jardines Ruiz", "Carlos", "Ruiz", "930222333",
         None, "Avenida Verde 5", None, "Barcelona", None,
         "España", "08010", 3, 3000),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO cliente
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, clientes)


def insertar_pedidos(cur):
    pedidos = [
        (1000, "2025-01-10", "2025-01-15", "2025-01-14",
         "Entregado", None, 100),
        (1001, "2025-01-12", "2025-01-18", None,
         "Pendiente", "Entrega urgente", 101),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO pedido
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, pedidos)


def insertar_detalles_pedido(cur):
    detalles = [
        (1000, "P001", 2, 19.99, 1),
        (1000, "P003", 10, 5.50, 2),
        (1001, "P004", 5, 8.00, 1),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO detalle_pedido
        VALUES (?, ?, ?, ?, ?)
    """, detalles)


def insertar_pagos(cur):
    pagos = [
        (100, "Transferencia", "TX1000", "2025-01-14", 94.98),
        (101, "Tarjeta", "TX1001", "2025-01-13", 40.00),
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO pago
        VALUES (?, ?, ?, ?, ?)
    """, pagos)


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------
def main():
    if not RUTA_DB.exists():
        print("❌ No existe jardineria.db. Ejecuta primero crear_jardineria_sqlite.py")
        return

    conn = sqlite3.connect(RUTA_DB)
    conn.execute("PRAGMA foreign_keys = ON;")
    cur = conn.cursor()

    insertar_oficinas(cur)
    insertar_empleados(cur)
    insertar_gamas(cur)
    insertar_productos(cur)
    insertar_clientes(cur)
    insertar_pedidos(cur)
    insertar_detalles_pedido(cur)
    insertar_pagos(cur)

    conn.commit()
    conn.close()

    print("\n" + "=" * 70)
    print("✅ DATOS INSERTADOS CORRECTAMENTE")
    print("=" * 70)
    print("📦 Oficinas, empleados, clientes, productos, pedidos y pagos")
    print("💡 Ya puedes practicar JOINs y subconsultas")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" INSERCIÓN DE DATOS - JARDINERÍA")
    print("=" * 70)

    main()
