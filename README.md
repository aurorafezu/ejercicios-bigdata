# 🚀 Big Data con Python - De Cero a Producción

> **Aprende a procesar millones de registros sin que tu computadora explote**
> Repositorio educativo completo para dominar Big Data con Python, desde conceptos básicos hasta producción.

[![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue)](https://www.linkedin.com/in/juangutierrezconsultor/)
[![Web](https://img.shields.io/badge/Web-TodoEconometria-orange)](https://www.todoeconometria.com)

---

## 🎯 ¿Qué es Esto y Por Qué Existe?

### El Problema

Imagina esto: Tienes un archivo Excel con **5 años de ventas** (500,000 filas). Excel se congela. Python con Pandas se queda sin memoria. Tu jefe necesita el análisis **mañana**.

**¿Te suena familiar?**

Este es el problema que enfrentan miles de analistas, científicos de datos y empresas diariamente. Los datos crecen exponencialmente, pero las herramientas tradicionales no escalan.

### La Solución

Este repositorio te enseña a:

```python
# ❌ Antes: Excel y Pandas básico
df = pd.read_csv("ventas_5_años.csv")  # 💥 MemoryError
df.groupby("región").sum()              # 🐌 20 minutos

# ✅ Después: Big Data con Python
df = dd.read_csv("ventas_5_años.csv")  # ⚡ Carga lazy
df.groupby("región").sum().compute()    # 🚀 2 segundos
```

**Resultado:** Procesas 100GB de datos en tu laptop como si fueran 10MB.

### Por Qué Este Repositorio

Este material surge de **230 horas de curso presencial** donde enseño Big Data a profesionales. He destilado:

- ✅ **10+ años de experiencia** en análisis de datos
- ✅ **Errores comunes** que cometen los principiantes (y cómo evitarlos)
- ✅ **Mejores prácticas** de la industria
- ✅ **Proyectos reales** adaptados para aprender

**No es solo teoría.** Cada ejercicio está diseñado para enfrentarte a problemas del mundo real.

---

## 👥 ¿Para Quién es Este Repositorio?

<details>
<summary><b>🎓 Alumnos del Curso Presencial (230 horas)</b></summary>

Si estás inscrito en mi curso presencial:

- ✅ Este repo es tu **material de apoyo** completo
- ✅ Aquí encontrarás **todos los ejercicios** del curso
- ✅ Puedes practicar **antes, durante y después** de las clases
- ✅ Tienes **soporte directo** en las sesiones presenciales

**Ventaja:** Mientras otros solo tienen diapositivas, tú tienes un repositorio completo con código ejecutable.

</details>

<details>
<summary><b>🌐 Autodidactas y Curiosos (Gratis)</b></summary>

Si encontraste este repositorio por tu cuenta:

- ✅ **Todo el contenido es gratuito** y de código abierto
- ✅ Puedes aprender **a tu ritmo** sin presión
- ✅ Practica con **ejercicios reales** de Big Data
- ⚠️ **No incluye soporte** (solo para alumnos presenciales)

**Ventaja:** Material profesional de calidad sin costo, perfecto para tu portafolio.

</details>

<details>
<summary><b>💼 Empresas y Profesionales</b></summary>

Si buscas soluciones para tu empresa:

- ✅ **Portfolio real** de capacidades en Big Data
- ✅ Muestra cómo **entreno equipos** profesionales
- ✅ **Consultoría y capacitación** in-company disponible
- ✅ Proyectos de **análisis de datos a medida**

**Ventaja:** Ve exactamente qué nivel de calidad ofrezco antes de contratarme.

</details>

---

## 🎓 ¿Qué Aprenderás?

### Roadmap de Aprendizaje

```
┌─────────────────────────────────────────────────────────────┐
│                    TU VIAJE EN BIG DATA                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  NIVEL 1: Fundamentos                                       │
│  ├─ SQLite: Bases de datos relacionales                    │
│  ├─ Pandas: Análisis de datos en memoria                   │
│  └─ Git/GitHub: Control de versiones                       │
│                                                              │
│           ↓ Aprenderás en 2-3 semanas                      │
│                                                              │
│  NIVEL 2: Escalando                                         │
│  ├─ Dask: Procesamiento paralelo (datos > RAM)            │
│  ├─ Parquet: Almacenamiento columnar eficiente            │
│  └─ Optimización: Técnicas de performance                  │
│                                                              │
│           ↓ Aprenderás en 3-4 semanas                      │
│                                                              │
│  NIVEL 3: Big Data Real                                     │
│  ├─ PySpark: Procesamiento distribuido                     │
│  ├─ SQL avanzado: Queries complejas                        │
│  └─ Pipelines: ETL/ELT en producción                       │
│                                                              │
│           ↓ Aprenderás en 4-5 semanas                      │
│                                                              │
│  NIVEL 4: Visualización y Deploy                            │
│  ├─ Dashboards: Flask + Chart.js                           │
│  ├─ APIs: Servir datos procesados                          │
│  └─ Deploy: Poner en producción                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘

⏱️ Tiempo total estimado: 10-12 semanas (a tu ritmo)
```

### Tecnologías que Dominarás

| Tecnología | Qué Hace | Cuándo Usarla |
|------------|----------|---------------|
| **Python** | Lenguaje base | Siempre |
| **Pandas** | Datos en memoria (< 5GB) | Análisis exploratorio |
| **Dask** | Datos > RAM (5-100GB) | Datasets grandes en 1 máquina |
| **PySpark** | Datos masivos (> 100GB) | Clusters, producción |
| **SQLite** | Base de datos embebida | Prototipos, proyectos pequeños |
| **Parquet** | Formato columnar | Almacenar datos procesados |
| **Git/GitHub** | Control de versiones | Todo proyecto profesional |
| **Flask** | Web framework | Dashboards, APIs |

### Ejemplos de Qué Podrás Hacer

**Ejemplo 1: Analizar 10 Millones de Viajes de Taxi**

```python
# Dataset: NYC Taxi (121 MB CSV, 10M+ registros)
# Pregunta: ¿Cuál es el ingreso promedio por hora del día?

import dask.dataframe as dd

# Cargar 121 MB como si fueran 10 MB ⚡
df = dd.read_csv("yellow_tripdata_2021-01.csv")

# Análisis que en Pandas tomaría 5 minutos, aquí: 10 segundos
resultado = (df.groupby(df['tpep_pickup_datetime'].dt.hour)
              ['total_amount']
              .mean()
              .compute())

print(resultado)
# Resultado: Hora 23 es la más rentable ($18.50 promedio)
```

**Ejemplo 2: Dashboard en Tiempo Real**

Crear un dashboard interactivo que muestra:
- 📊 Distribución de viajes por hora
- 🗺️ Mapa de calor de zonas más rentables
- 💰 Ingresos totales por día/semana/mes
- 📈 Tendencias temporales

**Ejemplo 3: Pipeline ETL de Producción**

```
CSV (100GB) → Limpiar → Transformar → Parquet → Dashboard
              (Dask)    (PySpark)    (10GB)     (Flask)
```

---

## 🚀 Cómo Empezar (Todos los Niveles)

### NIVEL 0: Primera Vez con Git y Python

<details>
<summary><b>Click aquí si es tu primera vez</b></summary>

#### Paso 1: Instalar Herramientas Básicas

**Windows:**
```bash
# Instalar Git
winget install Git.Git

# Instalar Python
winget install Python.Python.3.11

# Verificar instalación
git --version
python --version
```

**Mac:**
```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Git y Python
brew install git python@3.11

# Verificar
git --version
python3 --version
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install git python3.11 python3-pip
```

#### Paso 2: Configurar Git

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

#### Paso 3: Crear Cuenta en GitHub

1. Ir a https://github.com/
2. Click "Sign Up"
3. Verificar email

¡Listo! Ahora ve a **NIVEL 1** ↓

</details>

---

### NIVEL 1: Tengo Git y GitHub, ¿Ahora Qué?

<details>
<summary><b>Click aquí para el flujo completo</b></summary>

## 📋 ENTENDIENDO GIT Y GITHUB (Para Principiantes)

### ¿Qué es Git? ¿Qué es GitHub?

**Git** = Sistema de control de versiones (como "guardar versiones" de tu código)
**GitHub** = Nube donde guardas tu código (como Dropbox, pero para código)

```
┌─────────────────────────────────────────────────────────────┐
│                  GIT vs GITHUB                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  GIT (Programa en tu PC)                                    │
│  ┌──────────────────────────────────────┐                 │
│  │  Tu computadora                       │                 │
│  │  ┌─────────────────────────────────┐ │                 │
│  │  │  📁 Carpeta con tu código       │ │                 │
│  │  │  ├── ejercicio1.py              │ │                 │
│  │  │  ├── ejercicio2.py              │ │                 │
│  │  │  └── .git/  ← Historial local  │ │                 │
│  │  └─────────────────────────────────┘ │                 │
│  └──────────────────────────────────────┘                 │
│                      │                                       │
│                      │ git push                             │
│                      │ (subir)                              │
│                      ↓                                       │
│  GITHUB (En Internet)                                       │
│  ┌──────────────────────────────────────┐                 │
│  │  🌐 github.com                        │                 │
│  │  ┌─────────────────────────────────┐ │                 │
│  │  │  📦 Tu repositorio online       │ │                 │
│  │  │  (Visible en el navegador)      │ │                 │
│  │  └─────────────────────────────────┘ │                 │
│  └──────────────────────────────────────┘                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### ¿Qué es un FORK?

Un **fork** es hacer TU PROPIA COPIA del repositorio del profesor en GitHub.

**Piénsalo así:**
- 📚 El profesor tiene un libro (repositorio)
- 📄 Haces una fotocopia del libro completo (fork)
- ✏️ Ahora puedes escribir en TU copia sin afectar el original
- 📤 Cuando termines, le muestras tu trabajo al profesor (Pull Request)

```
┌─────────────────────────────────────────────────────────────┐
│              ¿QUÉ ES UN FORK? (Explicación Visual)          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  REPOSITORIO ORIGINAL (Del Profesor)                        │
│  ┌────────────────────────────────────────────┐            │
│  │  👨‍🏫 TodoEconometria/ejercicios-bigdata     │            │
│  │  ├── ejercicio_01/                          │            │
│  │  ├── ejercicio_02/                          │            │
│  │  └── datos/                                 │            │
│  │                                              │            │
│  │  🔒 NO puedes modificar esto directamente   │            │
│  └────────────────────────────────────────────┘            │
│                        │                                     │
│                        │ 🍴 HACER FORK                       │
│                        │ (Click en botón "Fork")             │
│                        ↓                                     │
│  TU FORK (Tu Copia Personal en GitHub)                      │
│  ┌────────────────────────────────────────────┐            │
│  │  👤 TU_USUARIO/ejercicios-bigdata           │            │
│  │  ├── ejercicio_01/                          │            │
│  │  ├── ejercicio_02/                          │            │
│  │  └── datos/                                 │            │
│  │                                              │            │
│  │  ✅ Esta copia SÍ puedes modificarla        │            │
│  └────────────────────────────────────────────┘            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 FLUJO COMPLETO DE TRABAJO (Paso a Paso)

### Visión General: Los 5 Pasos

```
┌─────────────────────────────────────────────────────────────┐
│             TU VIAJE DESDE FORK HASTA ENTREGA               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PASO 1: FORK (En GitHub)                                   │
│         Hacer tu copia del repo del profesor                │
│         ┌──────────────────────────────┐                   │
│         │ Repo Profesor (Original)     │                   │
│         └──────────────────────────────┘                   │
│                      │ Fork                                  │
│                      ↓                                       │
│         ┌──────────────────────────────┐                   │
│         │ Tu Fork (Tu Copia en GitHub) │                   │
│         └──────────────────────────────┘                   │
│                                                              │
│  PASO 2: CLONE (Descargar a tu PC)                         │
│         Traer tu fork a tu computadora                      │
│         ┌──────────────────────────────┐                   │
│         │ Tu Fork (GitHub)              │                   │
│         └──────────────────────────────┘                   │
│                      │ git clone                            │
│                      ↓                                       │
│         ┌──────────────────────────────┐                   │
│         │ Carpeta en tu PC              │                   │
│         └──────────────────────────────┘                   │
│                                                              │
│  PASO 3: TRABAJAR (Editar código)                          │
│         Resolver ejercicios en tu PC                        │
│         📝 Editas código                                    │
│         ✅ Haces commits (guardar versiones)                │
│         🧪 Pruebas que funciona                             │
│                                                              │
│  PASO 4: PUSH (Subir a GitHub)                             │
│         Subir tus cambios a tu fork                         │
│         ┌──────────────────────────────┐                   │
│         │ Carpeta en tu PC              │                   │
│         └──────────────────────────────┘                   │
│                      │ git push                             │
│                      ↓                                       │
│         ┌──────────────────────────────┐                   │
│         │ Tu Fork (GitHub actualizado)  │                   │
│         └──────────────────────────────┘                   │
│                                                              │
│  PASO 5: PULL REQUEST (Entregar al profesor)               │
│         Pedir al profesor que revise tu trabajo             │
│         ┌──────────────────────────────┐                   │
│         │ Tu Fork                       │                   │
│         └──────────────────────────────┘                   │
│                      │ Pull Request                         │
│                      ↓                                       │
│         ┌──────────────────────────────┐                   │
│         │ Repo Profesor (para revisar)  │                   │
│         └──────────────────────────────┘                   │
│                      │                                       │
│                      ↓                                       │
│         📝 Profesor da feedback                             │
│         ✅ Corriges si es necesario                         │
│         🎉 Ejercicio aprobado                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Diagrama de Secuencia Detallado

```
ACTORES:
👤 Tú (Alumno)    |    💻 Tu PC    |    🌐 GitHub    |    👨‍🏫 Profesor

═══════════════════════════════════════════════════════════════

PASO 1: HACER FORK
─────────────────
👤 ─────────────────────────────────────> 🌐
   "Quiero copiar el repo del profesor"

                                          🌐 (GitHub)
                                          ├─ Repo Profesor
                                          │  TodoEconometria/ejercicios-bigdata
                                          │
                                          └─ Tu Fork (copia)
                                             TU_USUARIO/ejercicios-bigdata

                                          🌐 ───────────────> 👤
                                             "Listo! Tu fork está creado"

═══════════════════════════════════════════════════════════════

PASO 2: CLONAR A TU PC
──────────────────────
👤 ─────> 💻 "git clone https://github.com/TU_USUARIO/ejercicios-bigdata"

💻 ─────────────────────────────────────> 🌐 Tu Fork
   "Descárgame todo el código"

                                          🌐 ───────────────> 💻
                                             "Aquí están todos los archivos"

💻 (Ahora tienes):
   📁 ejercicios-bigdata/
   ├── ejercicio_01/
   ├── ejercicio_02/
   └── datos/

💻 ───────────────> 👤 "Descarga completa!"

═══════════════════════════════════════════════════════════════

PASO 3: TRABAJAR LOCALMENTE
────────────────────────────
👤 ───> 💻 "Abrir ejercicio_01.py y editarlo"

💻 (Tu editor de código)
   📝 Escribes código
   🧪 Pruebas: python ejercicio_01.py
   ✅ Funciona!

👤 ───> 💻 "git add ejercicio_01.py"
👤 ───> 💻 "git commit -m 'Ejercicio 01 completado'"

💻 (Ahora Git tiene tu cambio guardado localmente)
   ⚠️ Pero SOLO en tu PC, NO en GitHub todavía!

═══════════════════════════════════════════════════════════════

PASO 4: SUBIR A GITHUB (PUSH)
──────────────────────────────
👤 ───> 💻 "git push origin main"

💻 ─────────────────────────────────────> 🌐 Tu Fork
   "Aquí está mi nuevo código"

                                          🌐 ───────────────> 💻
                                             "Actualización guardada!"

Ahora tu código está en:
  💻 Tu PC ✅
  🌐 Tu Fork en GitHub ✅
  👨‍🏫 Repo del Profesor ❌ (todavía no)

═══════════════════════════════════════════════════════════════

PASO 5: CREAR PULL REQUEST
───────────────────────────
👤 ───> 🌐 "Crear Pull Request desde mi fork al repo del profesor"

                                          🌐 Crea una "solicitud":
                                          ┌────────────────────────┐
                                          │ Pull Request #42       │
                                          │ De: TU_USUARIO         │
                                          │ Para: TodoEconometria  │
                                          │ Cambios: ejercicio_01  │
                                          └────────────────────────┘

                                          🌐 ───────────────> 👨‍🏫
                                             "El alumno X entregó ejercicio"

═══════════════════════════════════════════════════════════════

PASO 6: REVISIÓN Y FEEDBACK
────────────────────────────
👨‍🏫 ───> 🌐 "Revisar Pull Request #42"

                                          🌐 Muestra el código
                                          👨‍🏫 lee línea por línea

👨‍🏫 ───> 🌐 "Agregar comentario: Línea 15, usa mejor método X"

                                          🌐 ───────────────> 👤
                                             "Tienes feedback del profesor"

👤 ───> 💻 "Hacer correcciones en ejercicio_01.py"
👤 ───> 💻 "git commit -m 'Correcciones según feedback'"
👤 ───> 💻 "git push"

💻 ─────────────────────────────────────> 🌐 Tu Fork

                                          🌐 (El PR se actualiza automáticamente!)

                                          🌐 ───────────────> 👨‍🏫
                                             "El alumno hizo correcciones"

👨‍🏫 ───> 🌐 "Aprobar y cerrar PR"

                                          🌐 ───────────────> 👤
                                             "✅ Ejercicio aprobado!"

═══════════════════════════════════════════════════════════════

RESULTADO FINAL:
  ✅ Tu código está en tu fork
  ✅ El profesor vio tu trabajo
  ✅ Recibiste feedback
  ✅ Ejercicio completado y aprobado
  🎓 ¡Aprendiste Git + Big Data!
```

---

### PASO 1: Hacer Fork del Repositorio

#### Instrucciones Paso a Paso

**1. Ir al repositorio del profesor:**

Abre tu navegador y ve a:
```
https://github.com/TodoEconometria/ejercicios-bigdata
```

**2. Hacer Fork (copiar a tu cuenta):**

```
┌─────────────────────────────────────────┐
│  GitHub - Página del Repositorio       │
├─────────────────────────────────────────┤
│                                          │
│  [⭐ Star]  [🍴 Fork]  [⬇ Code]        │
│              ↑                           │
│              └── HAZ CLICK AQUÍ         │
│                                          │
└─────────────────────────────────────────┘
```

- Click en el botón **"Fork"** (arriba a la derecha)
- Selecciona **tu cuenta de GitHub** como destino
- Espera unos segundos mientras GitHub copia todo

**3. Verificar tu fork:**

Ahora deberías estar en TU copia:
```
https://github.com/TU_USUARIO/ejercicios-bigdata
        ↑
        └── Aquí debe aparecer TU nombre de usuario
```

✅ **Listo!** Ya tienes tu copia personal del repositorio.

---

### PASO 2: Clonar TU Fork a Tu Computadora

#### ¿Qué significa "clonar"?

**Clonar** = Descargar todo el código de GitHub a tu computadora

```
┌─────────────────────────────────────────┐
│  🌐 GitHub (Tu Fork)                    │
│  https://github.com/TU_USUARIO/...     │
└─────────────────────────────────────────┘
                  │
                  │ git clone (descargar)
                  ↓
┌─────────────────────────────────────────┐
│  💻 Tu PC                                │
│  📁 Carpeta: ejercicios-bigdata/        │
│     ├── ejercicio_01/                   │
│     ├── ejercicio_02/                   │
│     └── datos/                          │
└─────────────────────────────────────────┘
```

#### Instrucciones Paso a Paso

**1. Abrir la terminal/cmd:**

- **Windows:** Presiona `Win + R`, escribe `cmd`, Enter
- **Mac:** Busca "Terminal" en Spotlight
- **Linux:** `Ctrl + Alt + T`

**2. Ir a la carpeta donde quieres guardar el proyecto:**

```bash
# Ejemplo: Ir a Documentos
cd Documents

# O crear una carpeta nueva para tus proyectos
mkdir mis-proyectos
cd mis-proyectos
```

**3. Clonar TU fork (reemplaza TU_USUARIO):**

```bash
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
```

⚠️ **IMPORTANTE:** Asegúrate de poner **TU nombre de usuario**, no "TodoEconometria"

**4. Entrar a la carpeta:**

```bash
cd ejercicios-bigdata
```

**5. Conectar con el repo original del profesor:**

Esto te permite recibir actualizaciones cuando el profesor agregue ejercicios nuevos:

```bash
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git
```

**6. Verificar que todo está bien:**

```bash
git remote -v
```

Deberías ver algo así:
```
origin    https://github.com/TU_USUARIO/ejercicios-bigdata.git (tu fork)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (profesor)
```

✅ **Listo!** Ya tienes todo el código en tu computadora.

---

### PASO 3: Trabajar en un Ejercicio

#### Instrucciones Super Simples

**1. Abrir el proyecto en tu IDE:**

```bash
# Opción A: PyCharm (Recomendado para el curso)
# - Abre PyCharm
# - File → Open...
# - Selecciona la carpeta: ejercicios-bigdata/

# Opción B: Visual Studio Code
# - Abre la terminal en la carpeta ejercicios-bigdata/
# - Escribe: code .

# Opción C: Otro editor
# - Abre tu editor favorito
# - Busca y abre la carpeta: ejercicios-bigdata/
```

**2. Ir a la carpeta del ejercicio:**

```
ejercicios-bigdata/
  └── ejercicios/
      └── 01_cargar_sqlite/    ← Abre esta carpeta
          ├── README.md        ← Lee primero el enunciado
          └── ejercicio.py     ← Trabaja aquí
```

**3. Leer el enunciado COMPLETO:**

No empieces a codear sin leer. Lee TODO el README.md del ejercicio.

**4. Editar el código:**

Abre `ejercicio.py` y empieza a trabajar. Guarda frecuentemente (`Ctrl + S`).

**5. Probar tu código:**

```bash
# Ejecutar el ejercicio
python ejercicios/01_cargar_sqlite/ejercicio.py
```

🐛 **¿Tienes errores?** Es normal. Lee el error, corrígelo, vuelve a probar.

**6. Cuando funcione, guardar con Git:**

```bash
# Ver qué archivos cambiaste
git status

# Agregar tus cambios
git add ejercicios/01_cargar_sqlite/ejercicio.py

# Guardar con un mensaje
git commit -m "Ejercicio 01 completado: carga de datos SQLite"
```

**7. Subir a GitHub:**

```bash
git push origin main
```

✅ **Listo!** Tus cambios están en tu fork de GitHub.

---

### PASO 4: Actualizar Cuando el Profesor Agregue Ejercicios Nuevos

El profesor va a agregar nuevos ejercicios. Para obtenerlos:

```bash
# 1. Descargar cambios del profesor
git fetch upstream

# 2. Integrar cambios a tu código
git checkout main
git merge upstream/main

# 3. Subir actualizaciones a tu fork
git push origin main
```

⚠️ **Haz esto CADA SEMANA** para tener los ejercicios nuevos.

---

### PASO 5: Hacer Pull Request (Entregar al Profesor)

#### ¿Qué es un Pull Request?

```
┌─────────────────────────────────────────────────────────────┐
│            ¿QUÉ ES UN PULL REQUEST?                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Un Pull Request (PR) es como decir:                        │
│  "Profe, terminé mi ejercicio. ¿Puedes revisarlo?"          │
│                                                              │
│  ┌──────────────────────────────┐                          │
│  │  Tu Fork                      │                          │
│  │  (Ya tiene tu código listo)   │                          │
│  └──────────────────────────────┘                          │
│                  │                                           │
│                  │ Pull Request                             │
│                  │ (Solicitud de revisión)                  │
│                  ↓                                           │
│  ┌──────────────────────────────┐                          │
│  │  Repo del Profesor            │                          │
│  │  (Espera para revisar)        │                          │
│  └──────────────────────────────┘                          │
│                  │                                           │
│                  ↓                                           │
│  👨‍🏫 Profesor revisa:                                        │
│     - Ve tu código línea por línea                          │
│     - Deja comentarios si hay que mejorar algo             │
│     - Aprueba cuando está bien                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Instrucciones Paso a Paso

**1. Verifica que tu código funciona:**

```bash
# Ejecuta tu ejercicio una última vez
python ejercicios/01_cargar_sqlite/ejercicio.py

# ¿Funciona sin errores? ✅ Continúa
# ¿Tiene errores? 🐛 Corrígelos primero
```

**2. Asegúrate de haber hecho commit:**

```bash
# Ver si hay cambios sin guardar
git status

# Si hay cambios, guárdalos:
git add .
git commit -m "Ejercicio 01 completado"
```

**3. Subir a tu fork en GitHub:**

```bash
git push origin main
```

**4. Ir a GitHub en tu navegador:**

Abre: `https://github.com/TU_USUARIO/ejercicios-bigdata`

**5. Crear el Pull Request:**

GitHub te mostrará un banner amarillo:

```
┌───────────────────────────────────────────────────┐
│  ⚠️ main had recent pushes                        │
│  [Compare & pull request]  ← CLICK AQUÍ          │
└───────────────────────────────────────────────────┘
```

Si no ves el banner:
- Click en **"Pull requests"**
- Click en **"New pull request"**
- Selecciona:
  - Base: `TodoEconometria/ejercicios-bigdata` (main)
  - Compare: `TU_USUARIO/ejercicios-bigdata` (main)

**6. Completar la información:**

```markdown
Título:
Ejercicio 01 - [Tu Nombre Completo]

Descripción:
## ✅ Qué hice
- Implementé la carga de datos desde CSV a SQLite
- Agregué queries para análisis básico
- Probé con el dataset completo

## 🧪 Pruebas
- ✅ Funciona sin errores
- ✅ Probado con 10,000 registros
- ✅ Los resultados son correctos

## 💭 Preguntas (opcional)
- ¿Hay una forma más eficiente de hacer X?

```

**7. Click "Create pull request"**

✅ **¡Listo!** El profesor recibirá una notificación y revisará tu trabajo.

---

#### ¿Qué Pasa Después?

**Escenario 1: El profesor pide cambios**

```
┌─────────────────────────────────────────┐
│  👨‍🏫 Profesor comenta:                   │
│  "En la línea 15, usa mejor método X"  │
└─────────────────────────────────────────┘
              ↓
    Tú corriges en tu PC
              ↓
    git commit -m "Correcciones"
    git push origin main
              ↓
    El PR se actualiza automáticamente ✨
              ↓
    Profesor revisa de nuevo
```

**Escenario 2: El profesor aprueba**

```
┌─────────────────────────────────────────┐
│  ✅ Ejercicio aprobado                   │
│  🎉 ¡Felicitaciones!                     │
└─────────────────────────────────────────┘
```

---

### 📚 Tips para el Éxito

**🎯 Antes de Empezar un Ejercicio:**

```
□ Lee el enunciado COMPLETO (no solo el título)
□ Entiende QUÉ se pide antes de pensar en el CÓMO
□ Busca si hay archivos AYUDA.md o TIPS.md
```

**💻 Mientras Trabajas:**

```python
# ✅ BIEN - Trabaja en pasos pequeños
# Paso 1: Cargar datos
df = pd.read_csv("datos.csv")
print(df.head())  # Verifica que funcionó

# Paso 2: Limpiar
df = df.dropna()
print(f"Filas: {len(df)}")

# ❌ MAL - Todo en una línea
df = pd.read_csv("datos.csv").dropna().groupby("x").sum()
# Si falla, ¿dónde está el error?
```

**📝 Haz Commits Frecuentes:**

```bash
# Cada vez que algo funcione, guárdalo:
git commit -m "Agregar función de carga"
git commit -m "Implementar limpieza de datos"
git commit -m "Agregar análisis estadístico"
```

---

</details>

---

### NIVEL 2: Soy Desarrollador, Dame lo Esencial

<details>
<summary><b>TL;DR para devs experimentados</b></summary>

```bash
# Setup (1 minuto)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Workflow
git fetch upstream && git merge upstream/main
git checkout -b ejercicio-XX
# ... work ...
git push origin ejercicio-XX
# Create PR on GitHub

# Actualizar
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

**Estructura del repo:**
```
ejercicios-bigdata/
├── ejercicios/          # Ejercicios progresivos
├── datos/               # Datasets (NYC Taxi, etc.)
├── dashboards/          # Ejemplos de viz
└── docs/                # Guías adicionales
```

**Tech stack:**
- Python 3.11+
- Pandas, Dask, PySpark
- SQLite, Parquet
- Flask para dashboards

</details>

---

## 📚 Ejercicios Disponibles

### Roadmap Detallado

| # | Ejercicio | Tecnología | Nivel | Tiempo Estimado |
|---|-----------|------------|-------|-----------------|
| 01 | Carga de Datos con SQLite | SQLite + Pandas | 🟢 Básico | 2-3 horas |
| 02 | Limpieza y Transformación | Pandas | 🟢 Básico | 3-4 horas |
| 03 | Procesamiento con Parquet y Dask | Dask + Parquet | 🟡 Intermedio | 4-5 horas |
| 04 | Queries Complejas con PySpark | PySpark | 🟡 Intermedio | 5-6 horas |
| 05 | Dashboard Interactivo | Flask + Chart.js | 🔴 Avanzado | 8-10 horas |
| 06 | Pipeline ETL Completo | Dask + PySpark | 🔴 Avanzado | 10-12 horas |

### Ejercicio 01: Carga de Datos con SQLite

**¿Qué aprenderás?**
- Cargar datos desde CSV a base de datos
- Queries SQL básicas (SELECT, WHERE, GROUP BY)
- Optimización con índices
- Exportar resultados

**Dataset:** NYC Taxi Trips (121 MB, 10M+ registros)

**Desafío:** Cargar y analizar datos de taxis sin que tu computadora se congele.

<details>
<summary><b>Ver ejemplo de solución</b></summary>

```python
import sqlite3
import pandas as pd

# Cargar CSV en chunks (por partes)
chunksize = 100000
chunks = pd.read_csv("yellow_tripdata_2021-01.csv", chunksize=chunksize)

# Crear base de datos SQLite
conn = sqlite3.connect("taxi.db")

# Cargar por chunks
for i, chunk in enumerate(chunks):
    chunk.to_sql("trips", conn, if_exists="append", index=False)
    print(f"Chunk {i+1} cargado ({len(chunk)} registros)")

# Crear índices para acelerar queries
conn.execute("CREATE INDEX idx_pickup ON trips(tpep_pickup_datetime)")

# Query ejemplo: Promedio de tarifa por hora
query = """
    SELECT
        strftime('%H', tpep_pickup_datetime) as hora,
        AVG(total_amount) as promedio_tarifa,
        COUNT(*) as num_viajes
    FROM trips
    GROUP BY hora
    ORDER BY hora
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()
```

**Output esperado:**
```
hora  promedio_tarifa  num_viajes
00    15.23           234567
01    14.89           198234
02    16.45           165789
...
```

</details>

---

### Ejercicio 02: Limpieza y Transformación

**¿Qué aprenderás?**
- Detectar y manejar valores nulos
- Identificar outliers
- Transformaciones de datos
- Validación de tipos

**Dataset:** Mismo NYC Taxi (pero "sucio")

**Desafío:** Datos del mundo real siempre vienen sucios. Aprender a limpiarlos profesionalmente.

---

### Ejercicio 03: Procesamiento con Parquet y Dask

**¿Qué aprenderás?**
- Por qué Parquet es mejor que CSV
- Procesamiento paralelo con Dask
- Lazy evaluation
- Optimización de memoria

**Dataset:** NYC Taxi (convertido a Parquet)

**Desafío:** Procesar 10GB de datos en una laptop de 8GB RAM.

---

### Ejercicio 04: Queries Complejas con PySpark

**¿Qué aprenderás?**
- Introducción a Spark
- DataFrames distribuidos
- SQL en Spark
- Particionamiento de datos

**Dataset:** NYC Taxi + Weather Data (join de múltiples fuentes)

**Desafío:** Combinar datos de diferentes fuentes y hacer análisis complejos.

---

### Ejercicio 05: Dashboard Interactivo

**¿Qué aprenderás?**
- Flask para backend
- Chart.js para visualizaciones
- Conectar frontend con análisis de datos
- Deploy local

**Proyecto:** Dashboard EDA (Exploratory Data Analysis) de NYC Taxi

**Desafío:** Crear un dashboard profesional que impresione en entrevistas.

---

## 🔧 Setup del Entorno de Desarrollo

### Instalación de Dependencias

```bash
# Clonar el repositorio (tu fork)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import pandas, dask, pyspark; print('Todo OK!')"
```

### Estructura de Carpetas

```
ejercicios-bigdata/
│
├── .github/                    # Templates de issues y PRs
├── datos/                      # Datasets
│   ├── README.md              # Cómo descargar datos
│   └── descargar_datos.py     # Script automático
│
├── ejercicios/                 # Ejercicios del curso
│   ├── 01_cargar_sqlite.py
│   ├── 02_limpieza_datos.py
│   ├── 03_parquet_dask.py
│   ├── 04_pyspark_query.py
│   └── [futuros ejercicios]
│
├── dashboards/                 # Ejemplos de visualización
│   ├── nyc_taxi_eda/          # Dashboard ejemplo
│   └── ejemplos-destacados/   # Galería de proyectos
│
├── docs/                       # Documentación adicional
│   ├── CONFIGURACION_INICIAL.md
│   ├── GUIA_ENTREGA_DASHBOARDS.md
│   └── INSTRUCCIONES_ALUMNOS.md
│
├── .gitignore                  # Archivos ignorados por Git
├── requirements.txt            # Dependencias Python
├── PARA_ALUMNOS.md            # Info específica del curso
└── README.md                   # Este archivo
```

---

## 🌟 Ejemplos Destacados

### Dashboard NYC Taxi EDA

![Dashboard Preview](dashboards/nyc_taxi_eda/preview.png)

**Características:**
- Visualización interactiva de 10M+ registros
- Filtros dinámicos por fecha, hora, zona
- Mapas de calor de rutas más rentables
- Análisis de tendencias temporales

**Tecnologías:**
- Backend: Flask + Pandas
- Frontend: Chart.js + Leaflet.js
- Deploy: Docker

**Ver código:** [`dashboards/nyc_taxi_eda/`](dashboards/nyc_taxi_eda/)

---

## ❓ Preguntas Frecuentes (FAQ)

<details>
<summary><b>¿Necesito experiencia previa en Big Data?</b></summary>

**No.** El curso empieza desde cero. Solo necesitas:
- Conocimientos básicos de Python
- Saber usar la terminal/consola
- Ganas de aprender

Si no tienes experiencia con Python, te recomiendo hacer estos tutoriales primero:
- [Learn Python (Codecademy)](https://www.codecademy.com/learn/learn-python-3)
- [Python for Everybody (Coursera)](https://www.coursera.org/specializations/python)

</details>

<details>
<summary><b>¿Cuánto tiempo toma completar los ejercicios?</b></summary>

**Depende de tu nivel:**

- **Principiantes:** 10-12 semanas (10-15 horas/semana)
- **Intermedios:** 6-8 semanas (8-10 horas/semana)
- **Avanzados:** 4-5 semanas (5-8 horas/semana)

No hay prisa. Aprende a tu ritmo.

</details>

<details>
<summary><b>¿Los datos son reales o sintéticos?</b></summary>

**Reales.** Usamos datasets públicos reales:
- NYC Taxi & Limousine Commission (TLC)
- Weather data de NOAA
- Otros datasets públicos de Kaggle

Esto te da experiencia con datos del mundo real (sucios, incompletos, grandes).

</details>

<details>
<summary><b>¿Puedo usar esto en mi portafolio?</b></summary>

**¡SÍ!** De hecho, te lo recomiendo.

Muchos alumnos han conseguido trabajo mostrando:
- Sus soluciones de los ejercicios
- El dashboard que crearon
- Su fork de GitHub con commits profesionales

Tip: Haz tu fork público y agrega un README personalizado explicando tu aprendizaje.

</details>

<details>
<summary><b>¿Hay certificado al terminar?</b></summary>

**Para alumnos del curso presencial:** Sí, certificado de 230 horas.

**Para autodidactas:** No hay certificado oficial, pero tu GitHub es tu certificado. Los empleadores valoran más ver tu código que un PDF.

</details>

<details>
<summary><b>¿Qué computadora necesito?</b></summary>

**Mínimo:**
- 8GB RAM
- 20GB espacio en disco
- Procesador i5 o equivalente

**Recomendado:**
- 16GB RAM
- 50GB espacio en disco SSD
- Procesador i7 o equivalente

**Nota:** Si tienes menos recursos, puedes usar Google Colab o GitHub Codespaces (gratis).

</details>

<details>
<summary><b>¿Ofrecen soporte si me atoró?</b></summary>

**Para alumnos del curso presencial:** Sí, soporte completo en las sesiones.

**Para autodidactas:** No hay soporte directo, pero puedes:
- Crear un Issue en GitHub con tu pregunta
- Buscar en Issues existentes (probablemente alguien más tuvo tu problema)
- Unirte a la comunidad de Python/Data Science en Discord/Slack

</details>

---

## 💼 Servicios Profesionales

### Consultoría en Big Data

¿Necesitas ayuda con un proyecto de datos en tu empresa?

**Ofrezco:**

- ✅ **Desarrollo de Pipelines ETL/ELT** con Python y Spark
- ✅ **Capacitación Empresarial** (cursos personalizados para tu equipo)
- ✅ **Análisis de Datos** para insights accionables
- ✅ **Automatización de Procesos** de datos
- ✅ **Migración a Big Data** (de Excel/SQL a Dask/Spark)

**Casos de uso:**

```
Empresa A: "Tenemos 5 años de ventas en Excel y toma 2 horas generar reportes"
→ Solución: Pipeline automatizado con Dask + Dashboard en tiempo real
→ Resultado: Reportes en 30 segundos

Empresa B: "Queremos capacitar a 15 analistas en Big Data"
→ Solución: Curso in-company de 40 horas adaptado a su industria
→ Resultado: Equipo autónomo procesando TB de datos

Startup C: "Necesitamos procesar logs de servidores (1TB/día)"
→ Solución: Pipeline PySpark en AWS EMR
→ Resultado: Análisis en tiempo real con costos optimizados
```

### Capacitación Empresarial

Entreno equipos en:

- **Nivel Básico:** Fundamentos de Python para Datos (40 horas)
- **Nivel Intermedio:** Pandas y Análisis Exploratorio (60 horas)
- **Nivel Avanzado:** Big Data con Dask y PySpark (80 horas)
- **Personalizado:** Adaptado a tu industria y tecnologías

**Modalidades:**
- Presencial (CDMX y área metropolitana)
- Online (Zoom/Teams)
- Híbrido

### Contacto

📧 **Email:** [cursos@todoeconometria.com](mailto:cursos@todoeconometria.com)
💼 **LinkedIn:** [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
🌐 **Web:** [www.todoeconometria.com](https://www.todoeconometria.com)

<!-- Sección lista pero oculta hasta que esté la infraestructura web
### 💰 Inversión

**Consultoría:**
- Sesión de 1 hora: [Precio]
- Paquete 5 horas: [Precio] (ahorras X%)
- Proyecto completo: Cotización personalizada

**Capacitación:**
- Curso básico (40h): [Precio]
- Curso intermedio (60h): [Precio]
- Curso avanzado (80h): [Precio]
- Descuento por grupos: 3+ personas, 15% off

📅 **Agendar reunión:** [Calendly link]
-->

---

## 🤝 Contribuciones

Este repositorio está en constante evolución. Si encuentras:
- 🐛 Errores o bugs
- 📝 Mejoras en la documentación
- 💡 Ideas para nuevos ejercicios
- 🎨 Ejemplos de dashboards

**Crea un Issue o Pull Request:**

1. Fork este repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

**En resumen:** Puedes usar este material para aprender, enseñar, o modificar, siempre que des crédito.

---

## 🙏 Agradecimientos

Este repositorio existe gracias a:

- **Mis alumnos** - Cuyas preguntas y feedback mejoran el contenido constantemente
- **NYC Open Data** - Por los datasets públicos
- **Comunidad de Python** - Pandas, Dask, PySpark developers
- **GitHub** - Por la plataforma que facilita el aprendizaje colaborativo

---

## 📊 Estadísticas del Repositorio

![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub forks](https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TodoEconometria/ejercicios-bigdata?style=social)

---

## 🚀 ¿Listo para Empezar?

```bash
# 1. Haz fork de este repositorio (botón arriba a la derecha)

# 2. Clona TU fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# 3. Instala dependencias
cd ejercicios-bigdata
pip install -r requirements.txt

# 4. Empieza con el Ejercicio 01
cd ejercicios
python 01_cargar_sqlite.py

# 5. ¡Aprende, practica, crece! 🎓
```

---

<p align="center">
  <b>Tu carrera en Big Data empieza aquí.</b><br>
  ¿Preguntas? Abre un <a href="../../issues">Issue</a> o contáctame en <a href="https://www.linkedin.com/in/juangutierrezconsultor/">LinkedIn</a>
</p>

<p align="center">
  Hecho con ❤️ por <a href="https://www.todoeconometria.com">TodoEconometria</a>
</p>
