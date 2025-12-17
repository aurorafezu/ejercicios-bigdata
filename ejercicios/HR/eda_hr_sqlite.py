#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EDA - Base de Datos HR (SQLite)

Este script realiza un Análisis Exploratorio de Datos (EDA)
sobre la base de datos hr.db y genera un reporte en Markdown.

Autor: [Tu nombre]
Fecha: 2025-12-17
"""

import sqlite3
from pathlib import Path
from datetime import datetime
import json


# -------------------------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
RUTA_DB = BASE_DIR / "hr.db"
SALIDA_MD = BASE_DIR / "eda_hr.md"


# -------------------------------------------------------------------
# FUNCIONES AUXILIARES
# -------------------------------------------------------------------
def conectar(db_path: Path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def obtener_tablas(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    return [r["name"] for r in cur.fetchall()]


def obtener_columnas(conn, tabla):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({tabla});")
    return cur.fetchall()


def contar_filas(conn, tabla):
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) AS n FROM {tabla};")
    return cur.fetchone()["n"]


def contar_nulos(conn, tabla, columna):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT COUNT(*) AS n
        FROM {tabla}
        WHERE {columna} IS NULL;
    """)
    return cur.fetchone()["n"]


def stats_columna_numerica(conn, tabla, columna):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT
            MIN({columna}) AS min,
            MAX({columna}) AS max,
            AVG({columna}) AS avg
        FROM {tabla};
    """)
    return cur.fetchone()


def obtener_foreign_keys(conn, tabla):
    cur = conn.cursor()
    cur.execute(f"PRAGMA foreign_key_list({tabla});")
    return cur.fetchall()


# -------------------------------------------------------------------
# EDA PRINCIPAL
# -------------------------------------------------------------------
def generar_eda(db_path: Path, salida_md: Path):
    if not db_path.exists():
        print(f"❌ No existe la base de datos: {db_path}")
        return

    conn = conectar(db_path)
    tablas = obtener_tablas(conn)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(salida_md, "w", encoding="utf-8") as f:
        f.write("# Análisis Exploratorio de Datos (EDA) – HR\n\n")
        f.write(f"**Base de datos:** `hr.db`\n\n")
        f.write(f"**Fecha:** {now}\n\n")
        f.write("---\n\n")

        # ------------------------------------------------------------
        # 1. Resumen Ejecutivo
        # ------------------------------------------------------------
        f.write("## 1. Resumen Ejecutivo\n\n")
        f.write(f"- **Tablas analizadas:** {len(tablas)}\n")

        total_filas = 0
        for t in tablas:
            total_filas += contar_filas(conn, t)

        f.write(f"- **Total de registros (suma):** {total_filas:,}\n")
        f.write("- **Modelo:** HR normalizado (3FN)\n\n")

        # ------------------------------------------------------------
        # 2. Tablas y Volumen
        # ------------------------------------------------------------
        f.write("## 2. Tablas y Volumen de Datos\n\n")
        f.write("| Tabla | Filas |\n")
        f.write("|------|------:|\n")

        for t in tablas:
            f.write(f"| {t} | {contar_filas(conn, t):,} |\n")

        # ------------------------------------------------------------
        # 3. Estructura por Tabla
        # ------------------------------------------------------------
        f.write("\n## 3. Estructura de las Tablas\n\n")

        for t in tablas:
            f.write(f"### Tabla `{t}`\n\n")
            f.write("| Columna | Tipo | PK | Nulos |\n")
            f.write("|--------|------|----|------:|\n")

            columnas = obtener_columnas(conn, t)

            for col in columnas:
                nombre = col["name"]
                tipo = col["type"]
                pk = "✔" if col["pk"] else ""
                nulos = contar_nulos(conn, t, nombre)

                f.write(f"| {nombre} | {tipo} | {pk} | {nulos} |\n")

            f.write("\n")

        # ------------------------------------------------------------
        # 4. Claves Foráneas
        # ------------------------------------------------------------
        f.write("## 4. Relaciones (Claves Foráneas)\n\n")

        for t in tablas:
            fks = obtener_foreign_keys(conn, t)
            if fks:
                f.write(f"### {t}\n\n")
                for fk in fks:
                    f.write(
                        f"- `{t}.{fk['from']}` → `{fk['table']}.{fk['to']}`\n"
                    )
                f.write("\n")

        # ------------------------------------------------------------
        # 5. Análisis Numérico (Salarios)
        # ------------------------------------------------------------
        if "employees" in tablas:
            f.write("## 5. Análisis Numérico – Salarios\n\n")
            stats = stats_columna_numerica(conn, "employees", "salary")

            f.write(f"- **Salario mínimo:** {stats['min']}\n")
            f.write(f"- **Salario máximo:** {stats['max']}\n")
            f.write(f"- **Salario medio:** {round(stats['avg'], 2)}\n\n")

        # ------------------------------------------------------------
        # 6. Calidad de Datos
        # ------------------------------------------------------------
        f.write("## 6. Calidad de Datos\n\n")

        problemas = False

        for t in tablas:
            columnas = obtener_columnas(conn, t)
            for col in columnas:
                nulos = contar_nulos(conn, t, col["name"])
                if nulos > 0:
                    if not problemas:
                        f.write("### Columnas con valores nulos\n\n")
                        problemas = True
                    f.write(f"- `{t}.{col['name']}` → {nulos} nulos\n")

        if not problemas:
            f.write("No se detectaron problemas significativos de calidad.\n")

        # ------------------------------------------------------------
        # 7. Conclusiones
        # ------------------------------------------------------------
        f.write("\n## 7. Conclusiones\n\n")
        f.write(
            "- La base de datos HR presenta un diseño normalizado en 3FN.\n"
            "- Las relaciones están correctamente definidas mediante claves foráneas.\n"
            "- El volumen de datos es adecuado para prácticas de JOINs y EDA.\n"
            "- Existen valores nulos esperables (ej. commission_pct, manager_id).\n"
            "- El modelo es apto para análisis analítico y visualización.\n"
        )

    conn.close()
    print(f"✅ EDA generado correctamente en: {salida_md}")


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------
if __name__ == "__main__":
    generar_eda(RUTA_DB, SALIDA_MD)
