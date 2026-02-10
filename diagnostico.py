import os

# Ruta donde deberían estar las imágenes
ruta_imagenes = os.path.join(os.getcwd(), "entregas", "resultados")

print(f"--- DIAGNÓSTICO DE ARCHIVOS ---")
print(f"Buscando en: {ruta_imagenes}")

if os.path.exists(ruta_imagenes):
    archivos = os.listdir(ruta_imagenes)
    print(f"Archivos encontrados ({len(archivos)}):")
    for archivo in archivos:
        print(f" - '{archivo}'") # Las comillas simples nos ayudarán a ver espacios ocultos
else:
    print("¡LA CARPETA NO EXISTE!")
