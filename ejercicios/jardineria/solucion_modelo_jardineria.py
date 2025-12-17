"""
crear_jardineria_sqlite.py

Crea la base de datos SQLite 'jardineria.db' con el esquema del ejercicio.

Tablas:
- oficina
- empleado (FK a oficina, FK a empleado como jefe)
- gama_producto
- cliente (FK a empleado representante)
- pedido (FK a cliente)
- producto (FK a gama_producto)
- detalle_pedido (PK compuesta pedido+producto)
- pago (PK compuesta cliente+id_transaccion)

Autor: (tu nombre)
Fecha: 2025-12-17
"""

import sqlite3
from pathlib import Path


# -------------------------------------------------------------------
# CONFIG
# -------------------------------------------------------------------
RUTA_DB = Path(__file__).parent / "jardineria.db"


# -------------------------------------------------------------------
# DDL
# -------------------------------------------------------------------
DDL = """
PRAGMA foreign_keys = ON;

-- 1) OFICINA
CREATE TABLE IF NOT EXISTS oficina (
  codigo_oficina      TEXT PRIMARY KEY,
  ciudad              TEXT NOT NULL,
  pais                TEXT NOT NULL,
  region              TEXT,
  codigo_postal       TEXT NOT NULL,
  telefono            TEXT NOT NULL,
  linea_direccion1    TEXT NOT NULL,
  linea_direccion2    TEXT
);

-- 2) EMPLEADO
CREATE TABLE IF NOT EXISTS empleado (
  codigo_empleado     INTEGER PRIMARY KEY,
  nombre              TEXT NOT NULL,
  apellido1           TEXT NOT NULL,
  apellido2           TEXT,
  extension           TEXT NOT NULL,
  email               TEXT NOT NULL UNIQUE,
  codigo_oficina      TEXT NOT NULL,
  codigo_jefe         INTEGER,
  puesto              TEXT,

  FOREIGN KEY (codigo_oficina) REFERENCES oficina(codigo_oficina)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (codigo_jefe) REFERENCES empleado(codigo_empleado)
    ON UPDATE CASCADE ON DELETE SET NULL
);

-- 3) GAMA_PRODUCTO
CREATE TABLE IF NOT EXISTS gama_producto (
  gama               TEXT PRIMARY KEY,
  descripcion_texto  TEXT,
  descripcion_html   TEXT,
  imagen             TEXT
);

-- 4) CLIENTE
CREATE TABLE IF NOT EXISTS cliente (
  codigo_cliente              INTEGER PRIMARY KEY,
  nombre_cliente              TEXT NOT NULL,
  nombre_contacto             TEXT,
  apellido_contacto           TEXT,
  telefono                    TEXT NOT NULL,
  fax                         TEXT,
  linea_direccion1            TEXT NOT NULL,
  linea_direccion2            TEXT,
  ciudad                      TEXT NOT NULL,
  region                      TEXT,
  pais                        TEXT,
  codigo_postal               TEXT,
  codigo_empleado_rep_ventas  INTEGER,
  limite_credito              REAL,

  FOREIGN KEY (codigo_empleado_rep_ventas) REFERENCES empleado(codigo_empleado)
    ON UPDATE CASCADE ON DELETE SET NULL
);

-- 5) PEDIDO
CREATE TABLE IF NOT EXISTS pedido (
  codigo_pedido    INTEGER PRIMARY KEY,
  fecha_pedido     TEXT NOT NULL,   -- YYYY-MM-DD
  fecha_esperada   TEXT NOT NULL,
  fecha_entrega    TEXT,
  estado           TEXT NOT NULL,
  comentarios      TEXT,
  codigo_cliente   INTEGER NOT NULL,

  FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 6) PRODUCTO
CREATE TABLE IF NOT EXISTS producto (
  codigo_producto     TEXT PRIMARY KEY,
  nombre              TEXT NOT NULL,
  gama                TEXT NOT NULL,
  dimensiones         TEXT,
  proveedor           TEXT,
  descripcion         TEXT,
  cantidad_en_stock   INTEGER NOT NULL DEFAULT 0 CHECK (cantidad_en_stock >= 0),
  precio_venta        REAL NOT NULL CHECK (precio_venta >= 0),
  precio_proveedor    REAL CHECK (precio_proveedor IS NULL OR precio_proveedor >= 0),

  FOREIGN KEY (gama) REFERENCES gama_producto(gama)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 7) DETALLE_PEDIDO (N:M entre pedido y producto con atributos)
CREATE TABLE IF NOT EXISTS detalle_pedido (
  codigo_pedido     INTEGER NOT NULL,
  codigo_producto   TEXT NOT NULL,
  cantidad          INTEGER NOT NULL CHECK (cantidad > 0),
  precio_unidad     REAL NOT NULL CHECK (precio_unidad >= 0),
  numero_linea      INTEGER NOT NULL CHECK (numero_linea > 0),

  PRIMARY KEY (codigo_pedido, codigo_producto),
  FOREIGN KEY (codigo_pedido) REFERENCES pedido(codigo_pedido)
    ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (codigo_producto) REFERENCES producto(codigo_producto)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- 8) PAGO
CREATE TABLE IF NOT EXISTS pago (
  codigo_cliente   INTEGER NOT NULL,
  forma_pago       TEXT NOT NULL,
  id_transaccion   TEXT NOT NULL,
  fecha_pago       TEXT NOT NULL,   -- YYYY-MM-DD
  total            REAL NOT NULL CHECK (total >= 0),

  PRIMARY KEY (codigo_cliente, id_transaccion),
  FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Índices (rendimiento)
CREATE INDEX IF NOT EXISTS idx_empleado_oficina ON empleado(codigo_oficina);
CREATE INDEX IF NOT EXISTS idx_empleado_jefe ON empleado(codigo_jefe);

CREATE INDEX IF NOT EXISTS idx_cliente_rep ON cliente(codigo_empleado_rep_ventas);

CREATE INDEX IF NOT EXISTS idx_pedido_cliente ON pedido(codigo_cliente);
CREATE INDEX IF NOT EXISTS idx_producto_gama ON producto(gama);

CREATE INDEX IF NOT EXISTS idx_detalle_producto ON detalle_pedido(codigo_producto);
CREATE INDEX IF NOT EXISTS idx_pago_fecha ON pago(fecha_pago);
"""


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------
def crear_db(ruta_db: Path) -> None:
    ruta_db.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(ruta_db)
    try:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.executescript(DDL)
        conn.commit()
    finally:
        conn.close()


def resumen_db(ruta_db: Path) -> None:
    conn = sqlite3.connect(ruta_db)
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
            ORDER BY name;
        """)
        tablas = [r[0] for r in cur.fetchall()]

        print("\n" + "=" * 70)
        print("✅ BD CREADA CORRECTAMENTE")
        print("=" * 70)
        print(f"📄 Ruta: {ruta_db}")
        print(f"📦 Tablas ({len(tablas)}): {', '.join(tablas)}")
        print(f"💾 Tamaño: {ruta_db.stat().st_size / 1024 / 1024:.2f} MB")
    finally:
        conn.close()


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" CREACIÓN BD SQLite - JARDINERÍA")
    print("=" * 70)
    print(f"💾 Se creará en: {RUTA_DB}")

    crear_db(RUTA_DB)
    resumen_db(RUTA_DB)

    print("\n💡 Siguiente paso:")
    print("   - Abre 'jardineria.db' con DB Browser for SQLite")
    print("   - Prueba JOINs entre cliente/pedido/detalle_pedido/producto")
