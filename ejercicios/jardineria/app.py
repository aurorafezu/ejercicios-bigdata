#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from flask import Flask, render_template, abort, Response, redirect, url_for
import markdown

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# PATHS (ajustados a tu estructura actual)
# ------------------------------------------------------------
BASE_DIR = Path(__file__).parent
RUTA_DB = BASE_DIR / "jardineria.db"
REPORTE_MD = BASE_DIR / "resumen_eda_sqlite_jardineria.md"

CHART_DIR = BASE_DIR / "static" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Import opcional del EDA (para /regen)
# Si tu función se llama distinto, cambia el import.
# ------------------------------------------------------------
try:
    # Ajusta este nombre si tu script EDA se llama distinto:
    # ejemplo: solucion_modelo_jardineria_eda.py
    from solucion_modelo_jardineria_eda import generar_reporte  # type: ignore
except Exception:
    generar_reporte = None


app = Flask(__name__)


# ------------------------------------------------------------
# Helpers Markdown
# ------------------------------------------------------------
def leer_reporte_md() -> str:
    if not REPORTE_MD.exists():
        return ""
    return REPORTE_MD.read_text(encoding="utf-8")


def md_a_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "toc",
            "sane_lists",
        ],
        output_format="html5",
    )


# ------------------------------------------------------------
# Helpers SQL / Charts
# ------------------------------------------------------------
def query_df(db_path: Path, sql: str, params=None) -> pd.DataFrame:
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(sql, conn, params=params or [])


def save_bar(df: pd.DataFrame, x: str, y: str, title: str, filename: str) -> str:
    out = CHART_DIR / filename
    plt.figure()
    plt.bar(df[x].astype(str), df[y])
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    return f"charts/{filename}"  # ruta relativa a /static


def save_line(df: pd.DataFrame, x: str, y: str, title: str, filename: str) -> str:
    out = CHART_DIR / filename
    plt.figure()
    plt.plot(df[x], df[y])
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    return f"charts/{filename}"


def generar_graficos(db_path: Path) -> dict:
    """
    Genera gráficos PNG en static/charts y devuelve un dict:
    { "clave": "charts/archivo.png", ... }
    """
    charts = {}

    if not db_path.exists():
        return charts

    # 1) Filas por tabla
    df_tables = query_df(db_path, """
        SELECT name AS tabla
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
    """)
    counts = []
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        for t in df_tables["tabla"].tolist():
            cur.execute(f"SELECT COUNT(*) FROM {t}")
            counts.append((t, cur.fetchone()[0]))

    df_counts = pd.DataFrame(counts, columns=["tabla", "filas"]).sort_values("filas", ascending=False)
    if len(df_counts) > 0:
        charts["Filas por tabla"] = save_bar(df_counts, "tabla", "filas", "Filas por tabla", "01_filas_por_tabla.png")

    # 2) Pedidos por estado
    try:
        df_estado = query_df(db_path, """
            SELECT estado, COUNT(*) AS n
            FROM pedido
            GROUP BY estado
            ORDER BY n DESC;
        """)
        if len(df_estado) > 0:
            charts["Pedidos por estado"] = save_bar(df_estado, "estado", "n", "Pedidos por estado", "02_pedidos_por_estado.png")
    except Exception:
        pass

    # 3) Pagos por mes (YYYY-MM)
    try:
        df_pagos = query_df(db_path, """
            SELECT substr(fecha_pago, 1, 7) AS mes, SUM(total) AS total
            FROM pago
            GROUP BY substr(fecha_pago, 1, 7)
            ORDER BY mes;
        """)
        if len(df_pagos) > 0:
            charts["Pagos por mes"] = save_line(df_pagos, "mes", "total", "Pagos por mes (SUM total)", "03_pagos_por_mes.png")
    except Exception:
        pass

    # 4) Top productos por unidades (detalle_pedido)
    try:
        df_top = query_df(db_path, """
            SELECT dp.codigo_producto, SUM(dp.cantidad) AS unidades
            FROM detalle_pedido dp
            GROUP BY dp.codigo_producto
            ORDER BY unidades DESC
            LIMIT 10;
        """)
        if len(df_top) > 0:
            charts["Top 10 productos más vendidos"] = save_bar(df_top, "codigo_producto", "unidades",
                                                              "Top 10 productos más vendidos", "04_top_productos.png")
    except Exception:
        pass

    return charts


# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------
@app.get("/")
def home():
    if not RUTA_DB.exists():
        abort(404, description=f"No se encontró la BD: {RUTA_DB.name}")

    md_text = leer_reporte_md()
    if not md_text:
        abort(404, description=f"No se encontró el reporte: {REPORTE_MD.name}")

    reporte_html = md_a_html(md_text)
    charts = generar_graficos(RUTA_DB)

    return render_template(
        "reporte.html",
        titulo="EDA Jardinería (SQLite)",
        reporte_html=reporte_html,
        reporte_path=str(REPORTE_MD),
        db_path=str(RUTA_DB),
        charts=charts,
    )


@app.get("/raw")
def raw():
    md_text = leer_reporte_md()
    if not md_text:
        abort(404, description=f"No se encontró el reporte: {REPORTE_MD.name}")
    return Response(md_text, mimetype="text/plain; charset=utf-8")


@app.get("/regen")
def regen():
    """
    Regenera:
    - Reporte EDA (si está importada la función generar_reporte)
    - Gráficos
    """
    if not RUTA_DB.exists():
        abort(404, description=f"No se encontró la BD: {RUTA_DB.name}")

    # Regenerar reporte si es posible
    if generar_reporte is not None:
        generar_reporte(RUTA_DB, REPORTE_MD)

    # Regenerar charts siempre
    generar_graficos(RUTA_DB)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
