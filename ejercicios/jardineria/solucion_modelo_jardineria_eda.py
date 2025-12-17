#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EDA sobre SQLite (sin CSV)
Dataset: jardineria.db

Genera un reporte Markdown con:
- Tablas, columnas, tipos, PK
- Número de filas por tabla
- Nulos por columna
- Duplicados de PK (incluye PK compuestas)
- Rangos numéricos básicos (min/max/avg)
- Foreign keys detectadas

Autor: [Tu nombre]
Fecha: 2025-12-17
"""

import sqlite3
from pathlib import Path
from datetime import datetime


# ------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------
RUTA_DB = Path(__file__).parent / "jardineria.db"
SALIDA_MD = Path(__file__).parent / "resumen_eda_sqlite_jardineria.md"


# ------------------------------------------------------------
# SQLITE HELPERS
# ------------------------------------------------------------
def conectar(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def listar_tablas(conn: sqlite3.Connection) -> list[str]:
    cur = conn.cursor()
    cur.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    return [r["name"] for r in cur.fetchall()]


def table_info(conn: sqlite3.Connection, tabla: str) -> list[dict]:
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({tabla});")
    # cid, name, type, notnull, dflt_value, pk
    return [dict(r) for r in cur.fetchall()]


def foreign_keys(conn: sqlite3.Connection, tabla: str) -> list[dict]:
    cur = conn.cursor()
    cur.execute(f"PRAGMA foreign_key_list({tabla});")
    # id, seq, table, from, to, on_update, on_delete, match
    return [dict(r) for r in cur.fetchall()]


def count_rows(conn: sqlite3.Connection, tabla: str) -> int:
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) AS n FROM {tabla};")
    return int(cur.fetchone()["n"])


def nulls_por_columna(conn: sqlite3.Connection, tabla: str, cols: list[str]) -> dict[str, int]:
    """
    Hace un SELECT con SUM(col IS NULL) por cada columna.
    """
    if not cols:
        return {}

    exprs = ", ".join([f"SUM(CASE WHEN {c} IS NULL THEN 1 ELSE 0 END) AS null_{c}" for c in cols])
    sql = f"SELECT {exprs} FROM {tabla};"

    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()

    res = {}
    for c in cols:
        res[c] = int(row[f"null_{c}"])
    return res


def detectar_pk(tabla_info: list[dict]) -> list[str]:
    """
    En SQLite, pk > 0 indica columna parte de PK.
    Para PK compuesta, pk indica orden (1..n).
    """
    pk_cols = [(col["pk"], col["name"]) for col in tabla_info if col["pk"] and col["pk"] > 0]
    pk_cols.sort(key=lambda x: x[0])
    return [name for _, name in pk_cols]


def duplicados_pk(conn: sqlite3.Connection, tabla: str, pk_cols: list[str]) -> int | None:
    """
    Cuenta cuántas filas extra hay por claves PK duplicadas.
    Devuelve None si no hay PK definida.
    """
    if not pk_cols:
        return None

    cols = ", ".join(pk_cols)
    # total extra duplicates = SUM(cnt-1) sobre grupos repetidos
    sql = f"""
        SELECT COALESCE(SUM(cnt - 1), 0) AS dup_extras
        FROM (
            SELECT {cols}, COUNT(*) AS cnt
            FROM {tabla}
            GROUP BY {cols}
            HAVING COUNT(*) > 1
        );
    """
    cur = conn.cursor()
    cur.execute(sql)
    return int(cur.fetchone()["dup_extras"])


def columnas_numericas(tabla_info: list[dict]) -> list[str]:
    """
    Heurística simple: tipos que contengan INT, REAL, NUM, FLOAT, DOUBLE.
    """
    numericas = []
    for col in tabla_info:
        t = (col["type"] or "").upper()
        if any(k in t for k in ["INT", "REAL", "NUM", "FLOAT", "DOUBLE", "DECIMAL"]):
            numericas.append(col["name"])
    return numericas


def rangos_numericos(conn: sqlite3.Connection, tabla: str, cols_num: list[str]) -> dict[str, dict]:
    """
    Para cada columna numérica: min/max/avg (ignorando NULL).
    """
    res = {}
    cur = conn.cursor()
    for c in cols_num:
        sql = f"""
            SELECT
                MIN({c}) AS min_v,
                MAX({c}) AS max_v,
                AVG({c}) AS avg_v
            FROM {tabla}
            WHERE {c} IS NOT NULL;
        """
        cur.execute(sql)
        r = cur.fetchone()
        if r["min_v"] is None and r["max_v"] is None and r["avg_v"] is None:
            continue
        res[c] = {
            "min": r["min_v"],
            "max": r["max_v"],
            "avg": r["avg_v"],
        }
    return res


# ------------------------------------------------------------
# REPORT
# ------------------------------------------------------------
def generar_reporte(db_path: Path, salida_md: Path) -> None:
    if not db_path.exists():
        raise FileNotFoundError(f"No existe la BD: {db_path}")

    conn = conectar(db_path)
    try:
        tablas = listar_tablas(conn)

        # recolectar stats por tabla
        tabla_stats = []
        fk_all = []

        for t in tablas:
            info = table_info(conn, t)
            cols = [c["name"] for c in info]
            pk_cols = detectar_pk(info)
            nrows = count_rows(conn, t)
            nulls = nulls_por_columna(conn, t, cols)
            dup_pk = duplicados_pk(conn, t, pk_cols)
            nums = columnas_numericas(info)
            ranges = rangos_numericos(conn, t, nums)
            fks = foreign_keys(conn, t)

            tabla_stats.append({
                "tabla": t,
                "filas": nrows,
                "columnas": info,
                "pk": pk_cols,
                "nulls": nulls,
                "dup_pk_extras": dup_pk,
                "ranges": ranges,
                "fks": fks,
            })
            for fk in fks:
                fk_all.append({"tabla": t, **fk})

        # escribir markdown
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(salida_md, "w", encoding="utf-8") as f:
            f.write("# Resumen EDA - SQLite (Jardinería)\n\n")
            f.write(f"**Fecha:** {now}\n\n")
            f.write(f"**Base de datos:** `{db_path.name}`\n\n")
            f.write("---\n\n")

            # Resumen ejecutivo
            f.write("## 1. Resumen Ejecutivo\n\n")
            f.write(f"- **Tablas detectadas:** {len(tablas)}\n")
            f.write(f"- **Total filas (suma):** {sum(x['filas'] for x in tabla_stats):,}\n\n")

            f.write("### Tablas y filas\n\n")
            f.write("| Tabla | Filas | Columnas | PK |\n")
            f.write("|------|------:|---------:|----|\n")
            for s in sorted(tabla_stats, key=lambda x: x["filas"], reverse=True):
                pk_txt = ", ".join(s["pk"]) if s["pk"] else "—"
                f.write(f"| `{s['tabla']}` | {s['filas']:,} | {len(s['columnas'])} | {pk_txt} |\n")

            f.write("\n---\n\n")

            # Esquema por tabla
            f.write("## 2. Esquema por Tabla\n\n")
            for s in tabla_stats:
                f.write(f"### `{s['tabla']}`\n\n")
                f.write(f"- Filas: **{s['filas']:,}**\n")
                f.write(f"- PK: **{', '.join(s['pk']) if s['pk'] else 'No definida'}**\n")
                if s["dup_pk_extras"] is not None:
                    f.write(f"- Duplicados PK (filas extra): **{s['dup_pk_extras']:,}**\n")
                f.write("\n| Columna | Tipo | NOT NULL | PK |\n")
                f.write("|--------|------|:--------:|:--:|\n")
                for c in s["columnas"]:
                    notnull = "✅" if c["notnull"] else "❌"
                    pkflag = "✅" if c["pk"] and c["pk"] > 0 else "❌"
                    f.write(f"| `{c['name']}` | `{c['type']}` | {notnull} | {pkflag} |\n")
                f.write("\n---\n\n")

            # Nulos
            f.write("## 3. Nulos por Tabla\n\n")
            for s in tabla_stats:
                total = s["filas"] if s["filas"] else 0
                # listar solo columnas con nulos > 0
                cols_con_nulos = [(c, n) for c, n in s["nulls"].items() if n > 0]
                if not cols_con_nulos:
                    continue
                f.write(f"### `{s['tabla']}`\n\n")
                f.write("| Columna | Nulos | % |\n")
                f.write("|--------|------:|--:|\n")
                for c, n in sorted(cols_con_nulos, key=lambda x: x[1], reverse=True):
                    pct = (n / total * 100) if total else 0.0
                    f.write(f"| `{c}` | {n:,} | {pct:.1f}% |\n")
                f.write("\n")

            f.write("\n---\n\n")

            # Rangos numéricos
            f.write("## 4. Rangos Numéricos\n\n")
            any_ranges = False
            for s in tabla_stats:
                if not s["ranges"]:
                    continue
                any_ranges = True
                f.write(f"### `{s['tabla']}`\n\n")
                f.write("| Columna | Min | Max | Avg |\n")
                f.write("|--------|----:|----:|----:|\n")
                for c, r in s["ranges"].items():
                    f.write(f"| `{c}` | {r['min']} | {r['max']} | {r['avg']} |\n")
                f.write("\n")
            if not any_ranges:
                f.write("No se detectaron columnas numéricas con valores.\n\n")

            f.write("\n---\n\n")

            # Foreign Keys
            f.write("## 5. Foreign Keys Detectadas\n\n")
            if fk_all:
                f.write("| Tabla hija | Columna (from) | Tabla padre | Columna (to) | ON UPDATE | ON DELETE |\n")
                f.write("|-----------|------------------|------------|--------------|----------|----------|\n")
                for fk in fk_all:
                    f.write(
                        f"| `{fk['tabla']}` | `{fk['from']}` | `{fk['table']}` | `{fk['to']}` | "
                        f"`{fk['on_update']}` | `{fk['on_delete']}` |\n"
                    )
            else:
                f.write("No se detectaron FKs (si creaste el esquema sin FKs, esto saldrá vacío).\n")

            f.write("\n---\n\n")
            f.write("## 6. Conclusiones\n\n")
            f.write("- Si hay **duplicados de PK**, revisa la lógica de inserción o define PK correctamente.\n")
            f.write("- Si hay muchas columnas con **nulos**, decide si deben ser opcionales o normalizarse.\n")
            f.write("- Si no aparecen **FKs**, asegúrate de haber creado el esquema con `FOREIGN KEY` y `PRAGMA foreign_keys=ON`.\n")

        print("=" * 80)
        print("[OK] EDA completado")
        print(f"[OK] Reporte guardado en: {salida_md}")
        print("=" * 80)

    finally:
        conn.close()


if __name__ == "__main__":
    generar_reporte(RUTA_DB, SALIDA_MD)
