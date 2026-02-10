from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os

def generar_dashboard_pdf(output_path, image_folder):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Título del Dashboard
    story.append(Paragraph("<b>Dashboard: Desarrollo Político-Económico en el Magreb</b>", styles['h1']))
    story.append(Spacer(1, 0.2 * inch))

    # Subtítulo
    story.append(Paragraph("<i>Análisis de la relación entre democracia y desarrollo económico (2000-2022)</i>", styles['h2']))
    story.append(Spacer(1, 0.2 * inch))

    # Lista de imágenes a incluir (en orden)
    image_files = [
        "1_evolucion_democracia.png",
        "2_pib_vs_democracia.png",
        "3_correlacion_variables.png",
        "4_impacto_primavera_arabe.png",
        "5_clustering_paises.png"
    ]

    # Añadir cada imagen al PDF
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        if os.path.exists(img_path):
            img = Image(img_path)
            # Escalar la imagen para que quepa en la página (ajustar según necesidad)
            img_width = 6 * inch
            img_height = img.drawHeight * img_width / img.drawWidth
            img.drawWidth = img_width
            img.drawHeight = img_height
            story.append(img)
            story.append(Spacer(1, 0.1 * inch)) # Espacio entre imágenes
        else:
            story.append(Paragraph(f"<b>Error: Imagen no encontrada en '{image_folder}': {img_file}</b>", styles['Normal']))
            story.append(Spacer(1, 0.1 * inch))

    doc.build(story)
    print(f"Dashboard PDF generado exitosamente en: {output_path}")

if __name__ == "__main__":
    # Rutas
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Carpeta de imágenes
    image_folder = os.path.join(base_dir, "entregas", "resultados") 
    
    # Carpeta de entrega
    entrega_folder = os.path.join(base_dir, "entregas", "trabajo_final", "fernandez_aurora")
    if not os.path.exists(entrega_folder):
        os.makedirs(entrega_folder)

    # CAMBIO DE NOMBRE PARA EVITAR ERROR DE PERMISOS
    output_pdf_path = os.path.join(entrega_folder, "dashboard_magreb_final.pdf")

    # Generar el PDF
    generar_dashboard_pdf(output_pdf_path, image_folder)
