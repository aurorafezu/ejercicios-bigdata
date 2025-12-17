#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from flask import Flask, render_template, abort, Response, redirect, url_for
import markdown

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# PATHS
# ------------------------------------------------------------
BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "hr.db"
MD_PATH = BASE_DIR / "eda_hr.md"

CHART_DIR = BASE_DIR / "static" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# (Opcional) si quieres que /regen regenere el md:
# Asegúrate de que tu script se llame eda_hr_sqlite.py y tenga generar_eda(RUTA_DB, SALIDA_MD)
try:
    from eda_hr_sqlite import generar_eda  # type: ignore
except Exception:
    generar_eda = None


app = Flask(__name__)


# ------------------------------------------------------------
# Markdown
# ------------------------------------------------------------
def read_md() -> str:
    if not MD_PATH.exists():
        return ""
    return MD_PATH.read_text(encoding="utf-8", errors="replace")


def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "toc", "sane_lists"],
        output_format="html5",
    )


# ------------------------------------------------------------
# DB helpers
# ------------------------------------------------------------
def query_df(db_path: Path, sql: str, params=None) -> pd.DataFrame:
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(sql, conn, params=params or [])


def table_exists(db_path: Path, table_name: str) -> bool:
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?;",
            (table_name,),
        )
        return cur.fetchone() is not None


# ------------------------------------------------------------
# Chart helpers (NO fijamos colores)
# ------------------------------------------------------------
def save_bar(df: pd.DataFrame, x: str, y: str, title: str, filename: str) -> str:
    out = CHART_DIR / filename
    plt.figure()
    plt.bar(df[x].astype(str), df[y])
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    return f"charts/{filename}"


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


def save_hist(series: pd.Series, title: str, filename: str, bins: int = 12) -> str:
    out = CHART_DIR / filename
    plt.figure()
    plt.hist(series.dropna(), bins=bins)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    plt.close()
    return f"charts/{filename}"


# ------------------------------------------------------------
# Charts for HR
# ------------------------------------------------------------
def generate_charts(db_path: Path) -> dict:
    """
    Devuelve dict {titulo: 'charts/archivo.png'}.
    Genera solo los gráficos que tengan datos disponibles.
    """
    charts = {}
    if not db_path.exists():
        return charts

    # 1) Filas por tabla
    df_tables = query_df(
        db_path,
        """
        SELECT name AS tabla
        FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name;
        """,
    )
    if len(df_tables) > 0:
        counts = []
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            for t in df_tables["tabla"].tolist():
                cur.execute(f"SELECT COUNT(*) FROM {t}")
                counts.append((t, cur.fetchone()[0]))
        df_counts = pd.DataFrame(counts, columns=["tabla", "filas"]).sort_values("filas", ascending=False)
        charts["Filas por tabla"] = save_bar(df_counts, "tabla", "filas", "Filas por tabla", "01_filas_por_tabla.png")

    # 2) Empleados por departamento (si existe employees/departments)
    if table_exists(db_path, "employees") and table_exists(db_path, "departments"):
        df_emp_dept = query_df(
            db_path,
            """
            SELECT
              d.department_name AS departamento,
              COUNT(e.employee_id) AS empleados
            FROM departments d
            LEFT JOIN employees e ON e.department_id = d.department_id
            GROUP BY d.department_id, d.department_name
            ORDER BY empleados DESC, departamento ASC;
            """,
        )
        if len(df_emp_dept) > 0:
            charts["Empleados por departamento"] = save_bar(
                df_emp_dept, "departamento", "empleados",
                "Empleados por departamento",
                "02_empleados_por_departamento.png"
            )

    # 3) Empleados por job_title (si existe jobs)
    if table_exists(db_path, "employees") and table_exists(db_path, "jobs"):
        df_emp_job = query_df(
            db_path,
            """
            SELECT
              j.job_title AS puesto,
              COUNT(*) AS empleados
            FROM employees e
            JOIN jobs j ON j.job_id = e.job_id
            GROUP BY j.job_title
            ORDER BY empleados DESC, puesto ASC;
            """,
        )
        if len(df_emp_job) > 0:
            # si hay demasiados puestos, limitamos top 12 para que se lea bien
            df_top = df_emp_job.head(12)
            charts["Empleados por puesto (Top 12)"] = save_bar(
                df_top, "puesto", "empleados",
                "Empleados por puesto (Top 12)",
                "03_empleados_por_puesto.png"
            )

    # 4) Histograma de salarios (si existe salary)
    if table_exists(db_path, "employees"):
        df_sal = query_df(db_path, "SELECT salary FROM employees WHERE salary IS NOT NULL;")
        if len(df_sal) > 0:
            charts["Distribución de salarios"] = save_hist(
                df_sal["salary"], "Distribución de salarios", "04_hist_salarios.png", bins=12
            )

    # 5) Contrataciones por año (hire_date) si hay formato YYYY-MM-DD
    if table_exists(db_path, "employees"):
        df_hires = query_df(
            db_path,
            """
            SELECT substr(hire_date, 1, 4) AS anio, COUNT(*) AS contrataciones
            FROM employees
            WHERE hire_date IS NOT NULL AND length(hire_date) >= 4
            GROUP BY substr(hire_date, 1, 4)
            ORDER BY anio;
            """,
        )
        if len(df_hires) > 0:
            charts["Contrataciones por año"] = save_line(
                df_hires, "anio", "contrataciones",
                "Contrataciones por año",
                "05_contrataciones_por_anio.png"
            )

    return charts


# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------
@app.get("/")
def home():
    if not DB_PATH.exists():
        abort(404, description=f"No se encontró la BD: {DB_PATH.name}")
    if not MD_PATH.exists():
        abort(404, description=f"No se encontró el reporte MD: {MD_PATH.name}")

    html = md_to_html(read_md())
    charts = generate_charts(DB_PATH)

    return render_template(
        "reporte.html",
        titulo="Reporte HR (SQLite) – EDA + Gráficos",
        reporte_html=html,
        db_path=str(DB_PATH),
        md_path=str(MD_PATH),
        charts=charts,
    )


@app.get("/raw")
def raw():
    md_text = read_md()
    if not md_text:
        abort(404, description=f"No se encontró el reporte MD: {MD_PATH.name}")
    return Response(md_text, mimetype="text/plain; charset=utf-8")


@app.get("/regen")
def regen():
    if not DB_PATH.exists():
        abort(404, description=f"No se encontró la BD: {DB_PATH.name}")

    # Regenerar md si existe función
    if generar_eda is not None:
        generar_eda(DB_PATH, MD_PATH)

    # Regenerar gráficos siempre
    generate_charts(DB_PATH)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
