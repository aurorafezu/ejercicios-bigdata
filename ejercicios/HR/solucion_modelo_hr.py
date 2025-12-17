#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicio 1.1 - HR en SQLite (creación desde .sql)

Este script toma un archivo SQL (DDL/DML) y construye una base de datos SQLite
a partir de ese script. Luego muestra un resumen de tablas y filas.

Autor: [Tu nombre]
Fecha: 2025-12-17
Entrada:  Modelo_HR.sql
Salida:   hr.db
"""

import sqlite3
from pathlib import Path


# -------------------------------------------------------------------
# CONFIGURACIÓN DE RUTAS
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).parent

RUTA_SQL = BASE_DIR / "Modelo_HR_sqlite.sql"   # <- el archivo que te han pasado
RUTA_DB  = BASE_DIR / "hr.db"          # <- salida SQLite


# -------------------------------------------------------------------
# FUNCIONES
# -------------------------------------------------------------------
def leer_sql(path_sql: Path) -> str:
    if not path_sql.exists():
        raise FileNotFoundError(f"No existe el archivo SQL: {path_sql}")
    return path_sql.read_text(encoding="utf-8", errors="replace")


def crear_db_desde_sql(ruta_db: Path, sql_script: str) -> None:
    # Crear carpeta si no existe
    ruta_db.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(ruta_db)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")

        # Ejecuta TODO el script SQL (DDL + inserts)
        conn.executescript(sql_script)

        conn.commit()
    finally:
        conn.close()


def obtener_tablas(conn: sqlite3.Connection) -> list[str]:
    cur = conn.cursor()
    cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    return [r[0] for r in cur.fetchall()]


def contar_filas(conn: sqlite3.Connection, tabla: str) -> int:
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {tabla};")
    return int(cur.fetchone()[0])


def resumen_db(ruta_db: Path) -> None:
    conn = sqlite3.connect(ruta_db)
    try:
        tablas = obtener_tablas(conn)

        print("\n" + "=" * 70)
        print("📊 RESUMEN - HR SQLITE")
        print("=" * 70)
        print(f"💾 Base de datos: {ruta_db}")
        print(f"📦 Tablas detectadas: {len(tablas)}\n")

        print(f"{'Tabla':<30} {'Filas':>12}")
        print("-" * 44)

        total = 0
        for t in tablas:
            n = contar_filas(conn, t)
            total += n
            print(f"{t:<30} {n:>12,}")

        print("-" * 44)
        print(f"{'TOTAL (suma)':<30} {total:>12,}")

        tam_mb = ruta_db.stat().st_size / 1024 / 1024
        print(f"\n📦 Tamaño: {tam_mb:.2f} MB")
        print("=" * 70 + "\n")

    finally:
        conn.close()


def main():
    print("=" * 70)
    print(" MODELO HR → SQLITE")
    print("=" * 70)
    print(f"📄 SQL de entrada: {RUTA_SQL}")
    print(f"💾 BD de salida:   {RUTA_DB}")
    print("-" * 70)

    sql_script = leer_sql(RUTA_SQL)

    # Opcional: borrar BD anterior para recrear desde cero
    if RUTA_DB.exists():
        print("⚠️  Ya existe hr.db: se eliminará y se recreará desde cero.")
        RUTA_DB.unlink()

    print("⚙️  Creando BD y ejecutando script SQL...")
    crear_db_desde_sql(RUTA_DB, sql_script)

    print("✅ BD creada correctamente.")
    resumen_db(RUTA_DB)

    print("💡 Próximos pasos:")
    print("   1) Abre hr.db con DB Browser for SQLite")
    print("   2) Revisa tablas, FKs y registros")
    print("   3) Haz consultas SELECT / JOIN para practicar")


if __name__ == "__main__":
    main()
