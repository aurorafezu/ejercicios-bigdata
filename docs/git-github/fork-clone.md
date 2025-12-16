# Fork y Clone

Guia completa para crear tu copia del repositorio y trabajar con ella.

---

## Que es Git? Que es GitHub?

!!! info "Git"
    **Git** = Sistema de control de versiones (como "guardar versiones" de tu codigo)

!!! info "GitHub"
    **GitHub** = Nube donde guardas tu codigo (como Dropbox, pero para codigo)

```
┌─────────────────────────────────────────────────────────────┐
│                  GIT vs GITHUB                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  GIT (Programa en tu PC)                                    │
│  ┌──────────────────────────────────────┐                 │
│  │  Tu computadora                       │                 │
│  │  ┌─────────────────────────────────┐ │                 │
│  │  │  📁 Carpeta con tu codigo       │ │                 │
│  │  │  ├── ejercicio1.py              │ │                 │
│  │  │  ├── ejercicio2.py              │ │                 │
│  │  │  └── .git/  ← Historial local  │ │                 │
│  │  └─────────────────────────────────┘ │                 │
│  └──────────────────────────────────────┘                 │
│                      │                                       │
│                      │ git push (subir)                     │
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

---

## Que es un FORK?

Un **fork** es hacer TU PROPIA COPIA del repositorio del profesor en GitHub.

**Piensalo asi:**

- :books: El profesor tiene un libro (repositorio)
- :page_facing_up: Haces una fotocopia del libro completo (fork)
- :pencil2: Ahora puedes escribir en TU copia sin afectar el original
- :outbox_tray: Cuando termines, le muestras tu trabajo al profesor (Pull Request)

```
┌─────────────────────────────────────────────────────────────┐
│              QUE ES UN FORK? (Explicacion Visual)          │
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
│                        │ (Click en boton "Fork")             │
│                        ↓                                     │
│  TU FORK (Tu Copia Personal en GitHub)                      │
│  ┌────────────────────────────────────────────┐            │
│  │  👤 TU_USUARIO/ejercicios-bigdata           │            │
│  │  ├── ejercicio_01/                          │            │
│  │  ├── ejercicio_02/                          │            │
│  │  └── datos/                                 │            │
│  │                                              │            │
│  │  ✅ Esta copia SI puedes modificarla        │            │
│  └────────────────────────────────────────────┘            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## PASO 1: Hacer Fork del Repositorio

### Instrucciones Paso a Paso

**1. Ir al repositorio del profesor:**

Abre tu navegador y ve a:

```
https://github.com/TodoEconometria/ejercicios-bigdata
```

**2. Hacer Fork (copiar a tu cuenta):**

```
┌─────────────────────────────────────────┐
│  GitHub - Pagina del Repositorio       │
├─────────────────────────────────────────┤
│                                          │
│  [⭐ Star]  [🍴 Fork]  [⬇ Code]        │
│              ↑                           │
│              └── HAZ CLICK AQUI         │
│                                          │
└─────────────────────────────────────────┘
```

- Click en el boton **"Fork"** (arriba a la derecha)
- Selecciona **tu cuenta de GitHub** como destino
- Espera unos segundos mientras GitHub copia todo

**3. Verificar tu fork:**

Ahora deberias estar en TU copia:

```
https://github.com/TU_USUARIO/ejercicios-bigdata
        ↑
        └── Aqui debe aparecer TU nombre de usuario
```

:white_check_mark: **Listo!** Ya tienes tu copia personal del repositorio.

---

## PASO 2: Clonar TU Fork a Tu Computadora

### Que significa "clonar"?

**Clonar** = Descargar todo el codigo de GitHub a tu computadora

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

### Instrucciones Paso a Paso

**1. Abrir la terminal/cmd:**

=== "Windows"

    Presiona `Win + R`, escribe `cmd`, Enter

=== "macOS"

    Busca "Terminal" en Spotlight (`Cmd + Space`)

=== "Linux"

    Presiona `Ctrl + Alt + T`

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

!!! warning "IMPORTANTE"
    Asegurate de poner **TU nombre de usuario**, no "TodoEconometria"

**4. Entrar a la carpeta:**

```bash
cd ejercicios-bigdata
```

**5. Conectar con el repo original del profesor:**

Esto te permite recibir actualizaciones cuando el profesor agregue ejercicios nuevos:

```bash
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git
```

**6. Verificar que todo esta bien:**

```bash
git remote -v
```

Deberias ver algo asi:

```
origin    https://github.com/TU_USUARIO/ejercicios-bigdata.git (fetch)
origin    https://github.com/TU_USUARIO/ejercicios-bigdata.git (push)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (fetch)
upstream  https://github.com/TodoEconometria/ejercicios-bigdata.git (push)
```

:white_check_mark: **Listo!** Ya tienes todo el codigo en tu computadora.

---

## Entendiendo origin y upstream

!!! info "origin"
    **origin** = Tu fork en GitHub (donde subes tus cambios)

!!! info "upstream"
    **upstream** = Repositorio original del profesor (de donde descargas actualizaciones)

```
┌─────────────────────────────────────────────────────────────┐
│               ORIGIN vs UPSTREAM                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  UPSTREAM (Profesor)                                        │
│  ┌────────────────────────────────────┐                    │
│  │  TodoEconometria/ejercicios-bigdata │                    │
│  │  - Repo original                    │                    │
│  │  - Solo lectura (para ti)           │                    │
│  │  - Descargas actualizaciones de aqui│                    │
│  └────────────────────────────────────┘                    │
│                        │                                     │
│                        │ Fork                               │
│                        ↓                                     │
│  ORIGIN (Tu Fork)                                           │
│  ┌────────────────────────────────────┐                    │
│  │  TU_USUARIO/ejercicios-bigdata      │                    │
│  │  - Tu copia en GitHub               │                    │
│  │  - Lectura y escritura              │                    │
│  │  - Subes tus cambios aqui           │                    │
│  └────────────────────────────────────┘                    │
│                        │                                     │
│                        │ Clone                              │
│                        ↓                                     │
│  LOCAL (Tu PC)                                              │
│  ┌────────────────────────────────────┐                    │
│  │  ejercicios-bigdata/                │                    │
│  │  - Carpeta en tu computadora        │                    │
│  │  - Trabajas aqui                    │                    │
│  └────────────────────────────────────┘                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Flujo Completo de Trabajo

```mermaid
graph TD
    A[Repo Profesor<br/>upstream] -->|1. Fork| B[Tu Fork<br/>origin]
    B -->|2. Clone| C[Tu PC<br/>local]
    C -->|3. Trabajas| D[Editar codigo]
    D -->|4. Commit| E[Guardar cambios]
    E -->|5. Push| B
    B -->|6. Pull Request| A
    A -->|7. Nuevos ejercicios| C

    style A fill:#e1f5ff,stroke:#0277bd
    style B fill:#fff9c4,stroke:#f57f17
    style C fill:#e8f5e9,stroke:#388e3c
```

---

## Comandos Basicos

### Descargar cambios del profesor

```bash
# Descargar cambios
git fetch upstream

# Aplicar cambios a tu rama main
git checkout main
git merge upstream/main

# Subir a tu fork
git push origin main
```

### Subir tus cambios

```bash
# Ver que cambiaste
git status

# Agregar archivos
git add archivo.py

# Guardar con mensaje
git commit -m "Descripcion del cambio"

# Subir a tu fork
git push origin nombre-de-tu-rama
```

---

## Problemas Comunes

??? question "Error: Permission denied (publickey)"

    **Causa:** No tienes configuradas las SSH keys.

    **Solucion:** Usa HTTPS en lugar de SSH:

    ```bash
    # Usa esta URL (HTTPS):
    git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

    # NO uses esta (SSH):
    git clone git@github.com:TU_USUARIO/ejercicios-bigdata.git
    ```

??? question "Error: fatal: not a git repository"

    **Causa:** No estas en la carpeta del proyecto.

    **Solucion:**

    ```bash
    # Navega a la carpeta correcta
    cd path/to/ejercicios-bigdata

    # Verifica que estas en la carpeta correcta
    ls -la  # Deberas ver una carpeta .git/
    ```

??? question "Clono el repo del profesor en lugar de mi fork"

    **Causa:** Usaste la URL del profesor.

    **Solucion:**

    1. Borra la carpeta clonada
    2. Haz fork primero en GitHub
    3. Clona TU fork, no el del profesor

    ```bash
    # ❌ MAL
    git clone https://github.com/TodoEconometria/ejercicios-bigdata.git

    # ✅ BIEN
    git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
    ```

---

## Proximos Pasos

Ahora que tienes el repositorio clonado:

- [Tu Primer Ejercicio](../guia-inicio/primer-ejercicio.md) - Empezar a trabajar
- [Sincronizar Fork](sincronizar-fork.md) - Mantener tu fork actualizado
- [Crear Pull Requests](pull-requests.md) - Entregar tus ejercicios
