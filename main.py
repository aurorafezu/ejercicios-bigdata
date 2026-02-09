import pandas as pd
import os

def cargar_datos():
    # Ruta al archivo
    ruta_archivo = 'datos/qog/qog_data.csv'
    
    print(f"Intentando cargar datos desde: {os.path.abspath(ruta_archivo)}")
    
    if not os.path.exists(ruta_archivo):
        print("❌ ERROR: No se encuentra el archivo.")
        print("Por favor, mueve el archivo descargado a la carpeta 'datos/qog' y renómbralo a 'qog_data.csv'")
        return

    try:
        # Cargar el dataset
        # low_memory=False ayuda si el archivo es muy grande y tiene tipos mixtos
        df = pd.read_csv(ruta_archivo, low_memory=False)
        print("✅ Datos cargados correctamente.")
        
        # Filtrar países del Magreb
        # Nombres comunes en inglés en la base de datos QoG: 
        # Morocco, Algeria, Tunisia, Libya, Mauritania
        paises_magreb = ['Morocco', 'Algeria', 'Tunisia', 'Libya', 'Mauritania']
        
        # La columna de nombre de país suele ser 'cname' en QoG
        if 'cname' in df.columns:
            df_magreb = df[df['cname'].isin(paises_magreb)]
            print(f"Se encontraron {len(df_magreb)} registros para el Magreb.")
            print(df_magreb[['cname', 'year']].head())
        else:
            print("⚠️ No se encontró la columna 'cname'. Verifica los nombres de las columnas.")
            print(df.columns[:10]) # Imprimir las primeras 10 columnas para inspeccionar

    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")

if __name__ == '__main__':
    cargar_datos()
