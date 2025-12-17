#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inserta datos en la base de datos HR usando un archivo SQL de INSERTs.

Entrada:
  - hr.db
  - Modelo_HR_sqlite_inserts.sql

Autor: [Tu nombre]
Fecha: 2025-12-17
"""

import sqlite3
from pathlib import Path


# ------------------------------------------------------------
# CONFIGURACIÓN DE RUTAS
# ------------------------------------------------------------
BASE_DIR = Path(__file__).parent

RUTA_DB = BASE_DIR / "hr.db"
RUTA_SQL_INSERTS = BASE_DIR / "Modelo_HR_sqlite_inserts.sql"


# ------------------------------------------------------------
# FUNCIONES
# ------------------------------------------------------------
def leer_sql(path_sql: Path) -> str:
    if not path_sql.exists():
        raise FileNotFoundError(f"No existe el archivo SQL: {path_sql}")
    return path_sql.read_text(encoding="utf-8", errors="replace")


def ejecutar_sqlite(db_path: Path, sql_script: str) -> None:
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.executescript(sql_script)
        conn.commit()
    finally:
        conn.close()


def resumen_db(db_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """)
        tablas = [t[0] for t in cur.fetchall()]

        print("\n" + "=" * 70)
        print("📊 RESUMEN DE INSERCIÓN HR")
        print("=" * 70)

        for tabla in tablas:
            cur.execute(f"SELECT COUNT(*) FROM {tabla}")
            n = cur.fetchone()[0]
            print(f"{tabla:<25} {n:>10,}")

        print("=" * 70 + "\n")
    finally:
        conn.close()


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    print("=" * 70)
    print(" INSERCIÓN DE DATOS HR DESDE SQL")
    print("=" * 70)

    if not RUTA_DB.exists():
        print(f"❌ No existe la base de datos: {RUTA_DB}")
        print("Ejecuta primero el script de creación del esquema.")
        return

    if not RUTA_SQL_INSERTS.exists():
        print(f"❌ No existe el archivo de INSERTs: {RUTA_SQL_INSERTS}")
        return

    print(f"💾 Base de datos: {RUTA_DB}")
    print(f"📄 SQL de INSERTs: {RUTA_SQL_INSERTS}")
    print("-" * 70)

    try:
        sql_script = leer_sql(RUTA_SQL_INSERTS)
        ejecutar_sqlite(RUTA_DB, sql_script)

        print("✅ INSERTs ejecutados correctamente")
        resumen_db(RUTA_DB)

    except sqlite3.IntegrityError as e:
        print("❌ Error de integridad (FK / PK):", e)

    except sqlite3.OperationalError as e:
        print("❌ Error SQL:", e)

    except Exception as e:
        print("❌ Error inesperado:", e)


if __name__ == "__main__":
    main()
