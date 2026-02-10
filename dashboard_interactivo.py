import pandas as pd
import plotly.express as px
import os

def generar_dashboard_html():
    print("Generando Dashboard Interactivo Completo...")
    
    # Rutas
    ruta_parquet = "datos/processed/qog_magreb.parquet"
    ruta_csv = "datos/qog/qog_std_ts_jan24.csv"
    
    df_magreb = None

    # Intentar leer Parquet
    if os.path.exists(ruta_parquet):
        try:
            df_magreb = pd.read_parquet(ruta_parquet)
        except Exception as e:
            print(f"Error leyendo Parquet: {e}")
    
    # Intentar leer CSV si falla Parquet
    if df_magreb is None and os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
        paises_magreb = ["DZA", "MAR", "TUN", "LBY", "MRT"]
        df_magreb = df[df['ccodealp'].isin(paises_magreb)].copy()
        df_magreb = df_magreb[(df_magreb['year'] >= 2000) & (df_magreb['year'] <= 2022)]
        df_magreb['periodo_historico'] = df_magreb['year'].apply(lambda x: 'Pre-Primavera' if x < 2011 else 'Post-Primavera')

    if df_magreb is None:
        print("ERROR CRÍTICO: No se encontraron datos.")
        return

    # --- GENERACIÓN DE GRÁFICOS ---

    # G1: Evolución Democracia
    fig1 = px.line(df_magreb, x="year", y="vdem_libdem", color="cname", markers=True,
                   title="1. Evolución de la Democracia",
                   labels={"vdem_libdem": "Índice Democracia", "year": "Año", "cname": "País"})
    fig1.add_vline(x=2011, line_dash="dash", line_color="red", annotation_text="Primavera Árabe")

    # G2: PIB vs Democracia
    fig2 = px.scatter(df_magreb, x="gle_cgdpc", y="vdem_libdem", color="cname", size="year", 
                      hover_data=["year"], title="2. Riqueza vs Democracia",
                      labels={"gle_cgdpc": "PIB per cápita", "vdem_libdem": "Índice Democracia"})

    # G3: Matriz de Correlación (Heatmap)
    cols_corr = ["vdem_libdem", "gle_cgdpc", "ti_cpi", "wdi_lifexp"]
    # Filtrar solo columnas que existan
    cols_existentes = [c for c in cols_corr if c in df_magreb.columns]
    if len(cols_existentes) > 1:
        corr_matrix = df_magreb[cols_existentes].corr()
        fig3 = px.imshow(corr_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r',
                         title="3. Matriz de Correlación")
    else:
        fig3 = None

    # G4: Impacto Primavera Árabe
    col_periodo = 'periodo_historico' if 'periodo_historico' in df_magreb.columns else 'Periodo'
    df_impacto = df_magreb.groupby(['cname', col_periodo])['vdem_libdem'].mean().reset_index()
    fig4 = px.bar(df_impacto, x="cname", y="vdem_libdem", color=col_periodo, barmode="group",
                  title="4. Impacto Pre/Post Primavera Árabe",
                  labels={"vdem_libdem": "Democracia Promedio"})

    # G5: Clustering (Simulado con Scatter si no tenemos la columna de cluster, o real si la tenemos)
    # Como el clustering se hizo en Spark y no guardamos la columna 'prediction' en el parquet original,
    # haremos un scatter simple que sirva de base.
    fig5 = px.scatter(df_magreb, x="vdem_libdem", y="gle_cgdpc", color="cname", 
                      title="5. Distribución de Países (Base para Clustering)",
                      labels={"vdem_libdem": "Democracia", "gle_cgdpc": "PIB"})

    # --- GUARDAR HTML ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    entrega_folder = os.path.join(base_dir, "entregas", "trabajo_final", "fernandez_aurora")
    if not os.path.exists(entrega_folder):
        os.makedirs(entrega_folder)
        
    output_file = os.path.join(entrega_folder, "dashboard_interactivo.html")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<html><head><title>Dashboard Interactivo Magreb</title></head><body style='font-family:Arial'>")
        f.write("<h1 style='text-align:center'>Dashboard Interactivo: Magreb</h1>")
        f.write("<p style='text-align:center'>Análisis completo con 5 gráficos interactivos.</p>")
        f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write("<hr>")
        f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write("<hr>")
        if fig3: f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write("<hr>")
        f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write("<hr>")
        f.write(fig5.to_html(full_html=False, include_plotlyjs='cdn'))
        f.write("</body></html>")

    print(f"¡Dashboard Completo guardado en: {output_file}")

if __name__ == "__main__":
    generar_dashboard_html()
