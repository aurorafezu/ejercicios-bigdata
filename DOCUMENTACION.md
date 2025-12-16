# Documentacion con MkDocs Material

Este repositorio incluye documentacion completa generada con **MkDocs Material**.

## Vista Rapida

La documentacion incluye:

- **Guia de Inicio:** Instalacion, primer ejercicio, roadmap
- **Git y GitHub:** Fork, clone, sincronizacion, Pull Requests
- **Ejercicios:** Detalles de cada ejercicio con ejemplos
- **Dashboards:** Guia para crear dashboards interactivos
- **FAQ:** Preguntas frecuentes

## Ver Documentacion Localmente

### Paso 1: Instalar Dependencias

```bash
pip install -r requirements-docs.txt
```

### Paso 2: Servir Documentacion

```bash
mkdocs serve
```

Abre tu navegador en: **http://localhost:8000**

La documentacion se recarga automaticamente cuando editas archivos.

## Build para Produccion

```bash
# Generar sitio estatico
mkdocs build

# Los archivos HTML estaticos se generan en: site/
```

## Deploy a GitHub Pages

### Opcion 1: Manual

```bash
mkdocs gh-deploy
```

Esto publicara la documentacion en: `https://TU_USUARIO.github.io/ejercicios-bigdata/`

### Opcion 2: Automatico (GitHub Actions)

El repositorio incluye un workflow de GitHub Actions (`.github/workflows/docs.yml`) que automaticamente:

1. Detecta cambios en `docs/` o `mkdocs.yml`
2. Construye la documentacion
3. La publica en GitHub Pages

**Configuracion necesaria:**

1. Ve a Settings → Pages en tu repositorio de GitHub
2. Source: Selecciona "Deploy from a branch"
3. Branch: Selecciona `gh-pages` y carpeta `/ (root)`
4. Save

Cada push a `main` que modifique archivos de documentacion actualizara automaticamente el sitio.

## Estructura de la Documentacion

```
docs/
├── index.md                      # Home (landing page)
├── guia-inicio/
│   ├── index.md
│   ├── instalacion.md           # Setup de herramientas
│   ├── primer-ejercicio.md      # Quick start
│   └── roadmap.md               # Roadmap del curso
├── git-github/
│   ├── index.md
│   ├── fork-clone.md            # Fork y Clone
│   ├── sincronizar-fork.md      # Mantener fork actualizado (CON DIAGRAMAS)
│   ├── pull-requests.md         # Crear PRs
│   └── comandos-utiles.md       # Cheatsheet Git
├── ejercicios/
│   ├── index.md                 # Lista de ejercicios
│   └── 01-introduccion-sqlite.md # Ejercicio 1.1
├── dashboards/
│   └── index.md                 # Guia de dashboards
├── faq.md                       # Preguntas frecuentes
├── stylesheets/
│   └── extra.css                # Estilos personalizados
└── javascripts/
    └── mathjax.js               # MathJax config
```

## Editar Documentacion

### Agregar Nueva Pagina

1. Crear archivo Markdown en la carpeta apropiada
2. Agregar entrada en `mkdocs.yml` bajo `nav:`

```yaml
nav:
  - Home: index.md
  - Tu Nueva Seccion:
    - tu-seccion/index.md
    - Nueva Pagina: tu-seccion/nueva-pagina.md
```

### Sintaxis Markdown Especial

MkDocs Material soporta extensiones avanzadas:

#### Admonitions

```markdown
!!! note "Titulo Opcional"
    Contenido de la nota

!!! warning "Importante"
    Contenido de advertencia

!!! tip "Consejo"
    Contenido de tip

!!! example "Ejemplo"
    Contenido de ejemplo
```

#### Tabs

```markdown
=== "Python"
    ```python
    print("Hola")
    ```

=== "JavaScript"
    ```javascript
    console.log("Hola");
    ```
```

#### Diagramas Mermaid

```markdown
\`\`\`mermaid
graph LR
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
\`\`\`
```

#### Botones

```markdown
[Texto del Boton](url){ .md-button }
[Boton Primario](url){ .md-button .md-button--primary }
```

## Personalizacion

### Colores

Edita `mkdocs.yml`:

```yaml
theme:
  palette:
    primary: indigo  # Color principal
    accent: deep orange  # Color de acento
```

Opciones: red, pink, purple, deep purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange

### Logo y Favicon

Agrega imagenes en `docs/images/` y configura en `mkdocs.yml`:

```yaml
theme:
  logo: images/logo.png
  favicon: images/favicon.ico
```

### CSS Personalizado

Edita `docs/stylesheets/extra.css` para agregar estilos personalizados.

## Recursos

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Material Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Markdown Guide](https://www.markdownguide.org/)

## Problemas Comunes

### "mkdocs: command not found"

**Solucion:** Asegurate de haber instalado las dependencias:

```bash
pip install -r requirements-docs.txt
```

### Cambios no se reflejan

**Solucion:**

- Verifica que `mkdocs serve` este corriendo
- Refresca el navegador (Ctrl+F5)
- Revisa errores en la consola

### Error al hacer deploy

**Solucion:**

```bash
# Asegurate de tener el remote correcto
git remote -v

# Intenta de nuevo
mkdocs gh-deploy --force
```

## Soporte

Para preguntas sobre la documentacion:

- **Issues:** [Crear Issue](https://github.com/TodoEconometria/ejercicios-bigdata/issues)
- **Email:** cursos@todoeconometria.com
