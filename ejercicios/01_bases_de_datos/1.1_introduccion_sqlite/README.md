# 📝 Ejercicio 1.1: Introducción a SQLite - Cargar Datos desde CSV

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio serás capaz de:

- ✅ Entender qué es SQLite y cuándo usarlo
- ✅ Cargar datos desde archivos CSV a una base de datos
- ✅ Crear tablas con diferentes estructuras (3 modelos)
- ✅ Comprender las diferencias entre modelos normalizados y desnormalizados
- ✅ Realizar consultas SQL básicas para verificar los datos
- ✅ Usar Python con SQLite mediante `sqlite3` y `pandas`

---

## 📚 Pre-requisitos

Antes de empezar, asegúrate de tener:

- ✅ Python 3.11+ instalado
- ✅ Pandas instalado (`pip install pandas`)
- ✅ PyCharm configurado
- ✅ Los archivos CSV en `~/datos/csv_tienda_informatica/`

---

## 🧩 Contexto del Ejercicio

Trabajarás con un dataset real: **catálogo de una tienda de componentes informáticos**.

### Dataset
- **26 archivos CSV** con diferentes tipos de componentes
- **Productos reales** con precios, especificaciones técnicas
- **Estructura variada** (cada CSV tiene columnas diferentes)

### Ejemplos de componentes:
- CPUs (AMD, Intel)
- Placas base (Motherboards)
- Memoria RAM
- Tarjetas gráficas
- Monitores, teclados, ratones
- Y 20 categorías más...

---

## 📋 Enunciado del Ejercicio

Debes crear **3 bases de datos SQLite diferentes**, cada una implementando un modelo de datos distinto:

### **Modelo A: Catálogo Simple** (Desnormalizado)
Carga cada CSV directamente como una tabla independiente. 26 CSV = 26 tablas.

**Archivo resultado:** `tienda_modelo_a.db`

---

### **Modelo B: Normalizado** (3NF)
Diseña un esquema normalizado con:
- Tabla `categorias`
- Tabla `fabricantes`
- Tabla `productos` (con FK a categorias y fabricantes)
- Tabla `colores`
- Tabla `productos_colores` (relación muchos-a-muchos)

**Archivo resultado:** `tienda_modelo_b.db`

---

### **Modelo C: E-Commerce Completo**
Todo lo del Modelo B, más:
- Tabla `clientes`
- Tabla `pedidos`
- Tabla `lineas_pedido`
- Tabla `carritos`
- Tabla `items_carrito`
- Tabla `inventario`

**Archivo resultado:** `tienda_modelo_c.db`

---

## 🔧 Tareas a Realizar

### Parte 1: Modelo A - Catálogo Simple

1. **Crear script Python:** `solucion_modelo_a.py`
2. **Funcionalidad:**
   - Leer todos los CSV de la carpeta
   - Crear una tabla por cada CSV
   - Insertar datos tal cual vienen
3. **Resultado:**
   - Base de datos `tienda_modelo_a.db` con 26 tablas

**Pista:** Usa `pandas.read_csv()` y `DataFrame.to_sql()`

---

### Parte 2: Modelo B - Normalizado

1. **Crear script Python:** `solucion_modelo_b.py`
2. **Funcionalidad:**
   - Crear tablas normalizadas
   - Extraer fabricantes únicos de todos los CSVs
   - Extraer colores únicos
   - Crear categorías basadas en nombres de archivos
   - Insertar productos con Foreign Keys correctas
3. **Resultado:**
   - Base de datos `tienda_modelo_b.db` con ~8 tablas relacionadas

**Pista:** Necesitarás parsear nombres de productos para extraer fabricantes

---

### Parte 3: Modelo C - E-Commerce Completo

1. **Crear script Python:** `solucion_modelo_c.py`
2. **Funcionalidad:**
   - Todo lo del Modelo B
   - Crear tablas adicionales de clientes, pedidos, inventario
   - Generar datos de ejemplo (3-5 clientes ficticios)
   - Generar 2-3 pedidos de ejemplo
   - Inicializar inventario con stock aleatorio (50-200 unidades)
3. **Resultado:**
   - Base de datos `tienda_modelo_c.db` con ~15 tablas

---

### Parte 4: Consultas de Verificación

Crea un archivo `consultas_verificacion.sql` con queries para cada modelo:

#### Para Modelo A:
```sql
-- ¿Cuántas CPUs hay en el catálogo?
-- ¿Cuál es el precio promedio de las placas base?
-- Top 5 tarjetas gráficas más caras
```

#### Para Modelo B:
```sql
-- ¿Cuántos productos hay por categoría?
-- ¿Qué fabricantes tienen más productos?
-- Productos con color "Black" de fabricante "Corsair"
```

#### Para Modelo C:
```sql
-- ¿Cuántos pedidos tiene cada cliente?
-- ¿Cuál es el total de ventas por categoría?
-- Productos con stock bajo (< stock_mínimo)
```

---

### Parte 5: Documento de Reflexión

Crea `REFLEXION.md` respondiendo:

1. **¿Cuál modelo fue más fácil de implementar? ¿Por qué?**
2. **¿Qué ventajas encontraste en el Modelo A?**
3. **¿Qué desventajas encontraste en el Modelo A?**
4. **¿En qué situación usarías el Modelo B sobre el A?**
5. **¿El Modelo C es necesario para todos los casos? Justifica.**
6. **¿Qué pasaría si quisieras agregar una nueva columna "descuento" a todos los productos?**
   - En Modelo A: ¿Cuántas tablas modificarías?
   - En Modelo B: ¿Cuántas tablas modificarías?

---

## 📦 Estructura de Entrega

Tu carpeta `1.1_introduccion_sqlite/` debe contener:

```
1.1_introduccion_sqlite/
├── solucion_modelo_a.py         # Script Modelo A
├── solucion_modelo_b.py         # Script Modelo B
├── solucion_modelo_c.py         # Script Modelo C
├── consultas_verificacion.sql   # Queries de prueba
├── REFLEXION.md                 # Respuestas a preguntas
├── tienda_modelo_a.db          # BD generada (gitignore)
├── tienda_modelo_b.db          # BD generada (gitignore)
└── tienda_modelo_c.db          # BD generada (gitignore)
```

**Nota:** Los archivos `.db` NO se suben a GitHub (están en `.gitignore`)

---

## 🎓 Criterios de Evaluación

| Criterio | Peso | Qué se evalúa |
|----------|------|---------------|
| **Funcionalidad** | 40% | Los 3 scripts generan las BDs correctamente, datos se cargan sin errores |
| **Diseño del Esquema** | 30% | Modelo B y C tienen estructura correcta, FKs bien definidas, normalización adecuada |
| **Código** | 20% | Limpio, comentado, buenas prácticas, manejo de errores |
| **Reflexión** | 10% | Respuestas demuestran comprensión de trade-offs entre modelos |

---

## 💡 Pistas y Consejos

### Para Modelo A:
```python
import pandas as pd
import sqlite3

# Listar todos los CSV
csv_files = glob.glob("ruta/*.csv")

# Por cada CSV:
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    nombre_tabla = extraer_nombre(csv_file)
    df.to_sql(nombre_tabla, conn, if_exists="replace")
```

### Para Modelo B:
```python
# Extraer fabricantes únicos de todos los productos
all_manufacturers = set()
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    # Parsear 'name' para extraer fabricante
    manufacturers = df['name'].str.split().str[0]
    all_manufacturers.update(manufacturers)

# Insertar en tabla fabricantes
for mfr in all_manufacturers:
    cursor.execute("INSERT INTO fabricantes (nombre) VALUES (?)", (mfr,))
```

### Para Modelo C:
```python
# Generar clientes ficticios
clientes = [
    ("juan@email.com", "Juan", "Pérez"),
    ("maria@email.com", "María", "López"),
]

for email, nombre, apellido in clientes:
    cursor.execute("""
        INSERT INTO clientes (email, nombre, apellido)
        VALUES (?, ?, ?)
    """, (email, nombre, apellido))
```

---

## 📚 Recursos de Apoyo

### Documentación:
- [SQLite Official Docs](https://www.sqlite.org/docs.html)
- [Python sqlite3 module](https://docs.python.org/3/library/sqlite3.html)
- [Pandas to_sql](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)

### Lecturas complementarias:
- Ver `TEORIA.md` en esta carpeta
- Ver `../MODELOS_DE_DATOS.md` para diagramas completos

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar SQLAlchemy en lugar de sqlite3?**
R: Sí, pero para este ejercicio sqlite3 nativo es más didáctico.

**P: ¿Debo limpiar los datos (valores nulos, etc.)?**
R: Para este ejercicio no es necesario, enfócate en la estructura.

**P: ¿Los nombres de columnas deben ser exactamente como en el CSV?**
R: En Modelo A sí. En Modelo B y C puedes normalizarlos.

**P: ¿Cómo extraigo el fabricante del nombre del producto?**
R: Generalmente es la primera palabra: "AMD Ryzen..." → "AMD"

**P: ¿El inventario inicial debe ser real?**
R: No, usa números aleatorios entre 50-200 unidades.

---

## 🚀 Desafíos Extra (Opcional)

Si terminas antes y quieres más práctica:

1. **Agregar validaciones:**
   - Precio > 0
   - Stock >= 0
   - Email válido en clientes

2. **Crear vistas SQL:**
   - Vista con productos + categoría + fabricante (Modelo B)
   - Vista con total de ventas por cliente (Modelo C)

3. **Índices:**
   - Agregar índices a FKs para mejorar performance
   - Índice en precio para búsquedas rápidas

4. **Triggers:**
   - Trigger que actualiza inventario al crear pedido
   - Trigger que valida stock antes de insertar en carrito

---

## ✅ Checklist de Completitud

Antes de dar por terminado el ejercicio, verifica:

- [ ] `solucion_modelo_a.py` funciona y genera `tienda_modelo_a.db`
- [ ] `solucion_modelo_b.py` funciona y genera `tienda_modelo_b.db`
- [ ] `solucion_modelo_c.py` funciona y genera `tienda_modelo_c.db`
- [ ] Las 3 bases de datos se pueden abrir con DB Browser for SQLite
- [ ] `consultas_verificacion.sql` tiene al menos 3 queries por modelo
- [ ] Todas las queries ejecutan sin errores
- [ ] `REFLEXION.md` tiene respuestas completas a las 6 preguntas
- [ ] El código está comentado y es legible
- [ ] No hay archivos `.db` en el repositorio Git

---

**¡Mucha suerte!** 🚀

Recuerda: El objetivo no es solo que funcione, sino que **entiendas** las diferencias entre los modelos.

---

**Creado:** 2025-12-11
**Duración estimada:** 5.5-7 horas
**Nivel:** Básico-Intermedio
