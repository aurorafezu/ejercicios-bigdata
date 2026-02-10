from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os
from datetime import datetime

# --- Función para convertir Markdown simple a Paragraphs de ReportLab ---
# Ahora acepta un argumento opcional 'image_folder' para insertar imágenes inline
def markdown_to_paragraphs(md_text, styles, image_folder=None):
    paragraphs = []
    lines = md_text.split('\n')
    in_code_block = False
    code_block_text = ""

    for line in lines:
        # DETECCIÓN DE IMÁGENES EN EL MARKDOWN
        if line.strip().startswith("![") and image_folder:
            # Extraer el nombre del archivo de la sintaxis ![alt](ruta/archivo.png)
            try:
                start = line.find("(") + 1
                end = line.find(")")
                image_path_md = line[start:end] # Ej: resultados/1_evolucion.png
                image_filename = os.path.basename(image_path_md) # Ej: 1_evolucion.png
                
                real_image_path = os.path.join(image_folder, image_filename)
                
                if os.path.exists(real_image_path):
                    img = Image(real_image_path)
                    # Ajustar tamaño
                    aspect_ratio = img.imageHeight / float(img.imageWidth)
                    target_width = 6 * inch 
                    img.drawWidth = target_width
                    img.drawHeight = target_width * aspect_ratio
                    paragraphs.append(Spacer(1, 0.1 * inch))
                    paragraphs.append(img)
                    paragraphs.append(Spacer(1, 0.1 * inch))
                else:
                    # Si no encuentra la imagen, no ponemos nada (o un mensaje de error discreto)
                    pass
            except:
                pass # Si falla el parseo, ignoramos la línea
            continue

        if line.startswith("```"):
            if in_code_block:
                paragraphs.append(Paragraph(f"<pre>{code_block_text}</pre>", styles['Code']))
                code_block_text = ""
            in_code_block = not in_code_block
            continue
        
        if in_code_block:
            code_block_text += line + '\n'
            continue

        if line.startswith("###"):
            paragraphs.append(Paragraph(line.replace("###", "").strip(), styles['H3']))
        elif line.startswith("##"):
            paragraphs.append(Paragraph(line.replace("##", "").strip(), styles['H2']))
        elif line.startswith("#"):
            paragraphs.append(Paragraph(line.replace("#", "").strip(), styles['H1']))
        elif line.strip().startswith("- "):
            paragraphs.append(Paragraph(f"• {line.strip()[2:]}", styles['Body']))
        elif line.strip() == "---":
            paragraphs.append(Spacer(1, 0.2 * inch))
            paragraphs.append(PageBreak()) # Salto de página en los separadores
        elif line.strip():
            line_html = line.replace("**", "<b>", 1).replace("**", "</b>", 1)
            paragraphs.append(Paragraph(line_html, styles['Body']))
        else:
            paragraphs.append(Spacer(1, 0.1 * inch))
            
    return paragraphs

def generar_informe_final(output_path, image_folder, doc_folder):
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    
    def add_style_if_not_exists(name, **kwargs):
        if name not in styles:
            styles.add(ParagraphStyle(name, **kwargs))

    add_style_if_not_exists('PortadaTitulo', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=26, leading=32, textColor=colors.navy, alignment=TA_CENTER, spaceAfter=20)
    add_style_if_not_exists('PortadaSub', parent=styles['Normal'], fontName='Helvetica', fontSize=16, textColor=colors.dimgrey, alignment=TA_CENTER, spaceAfter=10)
    add_style_if_not_exists('Autor', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.black, alignment=TA_CENTER, spaceBefore=50)
    add_style_if_not_exists('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, textColor=colors.navy, spaceBefore=20, spaceAfter=10)
    add_style_if_not_exists('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, textColor=colors.royalblue, spaceBefore=15, spaceAfter=10)
    add_style_if_not_exists('H3', parent=styles['Heading3'], fontName='Helvetica-Bold', fontSize=12, textColor=colors.darkslategray, spaceBefore=10, spaceAfter=5)
    add_style_if_not_exists('Body', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=14, alignment=TA_JUSTIFY, spaceAfter=10)
    add_style_if_not_exists('Code', parent=styles['Normal'], fontName='Courier', fontSize=10, textColor=colors.darkslategray, backColor=colors.whitesmoke, borderPadding=5, leading=12)

    story = []

    # --- PORTADA ---
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("TRABAJO FINAL: BIG DATA CON PYTHON", styles['PortadaSub']))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("Desarrollo Político-Económico en el Magreb", styles['PortadaTitulo']))
    story.append(Paragraph("Análisis de Infraestructura Docker y Pipeline ETL con Spark", styles['PortadaSub']))
    story.append(Spacer(1, 2 * inch))
    story.append(Paragraph("Presentado por:", styles['PortadaSub']))
    story.append(Paragraph("Aurora Fernandez Zurita", styles['Autor']))
    story.append(Spacer(1, 0.5 * inch))
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    story.append(Paragraph(f"Fecha: {fecha_actual}", styles['PortadaSub']))
    story.append(PageBreak())

    # --- INTRODUCCIÓN ---
    story.append(Paragraph("1. Introducción y Objetivos", styles['H1']))
    story.extend(markdown_to_paragraphs(open(os.path.join(doc_folder, '01_README.md'), encoding='utf-8').read(), styles))
    story.append(PageBreak())

    # --- INFRAESTRUCTURA ---
    story.append(Paragraph("2. Infraestructura Docker", styles['H1']))
    infra_md = open(os.path.join(doc_folder, '02_INFRAESTRUCTURA.md'), encoding='utf-8').read()
    # Aquí pasamos la carpeta de capturas para que inserte la imagen inline
    capturas_folder = os.path.join(doc_folder, "capturas")
    story.extend(markdown_to_paragraphs(infra_md, styles, image_folder=capturas_folder))
    story.append(PageBreak())

    # --- RESULTADOS (Aquí ocurre la magia de insertar gráficos inline) ---
    story.append(Paragraph("3. Análisis de Resultados", styles['H1']))
    resultados_md = open(os.path.join(doc_folder, '03_RESULTADOS.md'), encoding='utf-8').read()
    # Pasamos la carpeta de resultados para que inserte los gráficos donde correspondan
    story.extend(markdown_to_paragraphs(resultados_md, styles, image_folder=image_folder))
    story.append(PageBreak())

    # --- REFLEXIÓN IA ---
    story.append(Paragraph("4. Reflexión sobre el Proceso y Uso de IA", styles['H1']))
    story.extend(markdown_to_paragraphs(open(os.path.join(doc_folder, '04_REFLEXION_IA.md'), encoding='utf-8').read(), styles))
    story.append(PageBreak())

    # --- PREGUNTAS DE COMPRENSIÓN ---
    story.append(Paragraph("5. Preguntas de Comprensión", styles['H1']))
    story.extend(markdown_to_paragraphs(open(os.path.join(doc_folder, '05_RESPUESTAS.md'), encoding='utf-8').read(), styles))
    story.append(PageBreak())

    # --- CONCLUSIONES ---
    story.append(Paragraph("6. Conclusiones Generales", styles['H1']))
    texto_conclusiones = """
    El análisis realizado permite concluir que la región del Magreb no es un bloque homogéneo. 
    La Primavera Árabe actuó como un catalizador que bifurcó las trayectorias de los países: 
    Túnez hacia la democratización y Libia hacia la inestabilidad, mientras que el resto mantuvo el status quo.
    <br/><br/>
    Técnicamente, la infraestructura Docker y Spark ha demostrado ser capaz de procesar y analizar 
    estos datos de manera eficiente, permitiendo la integración de técnicas estadísticas y de Machine Learning.
    """
    story.append(Paragraph(texto_conclusiones, styles['Body']))

    doc.build(story)
    print(f"Informe Final Definitivo generado exitosamente en: {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(base_dir, "resultados") 
    entrega_folder = os.path.join(base_dir, "entregas", "trabajo_final", "fernandez_aurora")
    if not os.path.exists(entrega_folder):
        os.makedirs(entrega_folder)

    # CAMBIO DE NOMBRE PARA EVITAR BLOQUEO
    output_pdf_path = os.path.join(entrega_folder, "Informe_Final_Definitivo_v2.pdf")

    generar_informe_final(output_pdf_path, image_folder, entrega_folder)
