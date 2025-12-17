# Resumen EDA - SQLite (Jardinería)

**Fecha:** 2025-12-17 17:36:34

**Base de datos:** `jardineria.db`

---

## 1. Resumen Ejecutivo

- **Tablas detectadas:** 8
- **Total filas (suma):** 21

### Tablas y filas

| Tabla | Filas | Columnas | PK |
|------|------:|---------:|----|
| `producto` | 4 | 9 | codigo_producto |
| `detalle_pedido` | 3 | 5 | codigo_pedido, codigo_producto |
| `empleado` | 3 | 9 | codigo_empleado |
| `gama_producto` | 3 | 4 | gama |
| `cliente` | 2 | 14 | codigo_cliente |
| `oficina` | 2 | 8 | codigo_oficina |
| `pago` | 2 | 5 | codigo_cliente, id_transaccion |
| `pedido` | 2 | 7 | codigo_pedido |

---

## 2. Esquema por Tabla

### `cliente`

- Filas: **2**
- PK: **codigo_cliente**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_cliente` | `INTEGER` | ❌ | ✅ |
| `nombre_cliente` | `TEXT` | ✅ | ❌ |
| `nombre_contacto` | `TEXT` | ❌ | ❌ |
| `apellido_contacto` | `TEXT` | ❌ | ❌ |
| `telefono` | `TEXT` | ✅ | ❌ |
| `fax` | `TEXT` | ❌ | ❌ |
| `linea_direccion1` | `TEXT` | ✅ | ❌ |
| `linea_direccion2` | `TEXT` | ❌ | ❌ |
| `ciudad` | `TEXT` | ✅ | ❌ |
| `region` | `TEXT` | ❌ | ❌ |
| `pais` | `TEXT` | ❌ | ❌ |
| `codigo_postal` | `TEXT` | ❌ | ❌ |
| `codigo_empleado_rep_ventas` | `INTEGER` | ❌ | ❌ |
| `limite_credito` | `REAL` | ❌ | ❌ |

---

### `detalle_pedido`

- Filas: **3**
- PK: **codigo_pedido, codigo_producto**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_pedido` | `INTEGER` | ✅ | ✅ |
| `codigo_producto` | `TEXT` | ✅ | ✅ |
| `cantidad` | `INTEGER` | ✅ | ❌ |
| `precio_unidad` | `REAL` | ✅ | ❌ |
| `numero_linea` | `INTEGER` | ✅ | ❌ |

---

### `empleado`

- Filas: **3**
- PK: **codigo_empleado**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_empleado` | `INTEGER` | ❌ | ✅ |
| `nombre` | `TEXT` | ✅ | ❌ |
| `apellido1` | `TEXT` | ✅ | ❌ |
| `apellido2` | `TEXT` | ❌ | ❌ |
| `extension` | `TEXT` | ✅ | ❌ |
| `email` | `TEXT` | ✅ | ❌ |
| `codigo_oficina` | `TEXT` | ✅ | ❌ |
| `codigo_jefe` | `INTEGER` | ❌ | ❌ |
| `puesto` | `TEXT` | ❌ | ❌ |

---

### `gama_producto`

- Filas: **3**
- PK: **gama**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `gama` | `TEXT` | ❌ | ✅ |
| `descripcion_texto` | `TEXT` | ❌ | ❌ |
| `descripcion_html` | `TEXT` | ❌ | ❌ |
| `imagen` | `TEXT` | ❌ | ❌ |

---

### `oficina`

- Filas: **2**
- PK: **codigo_oficina**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_oficina` | `TEXT` | ❌ | ✅ |
| `ciudad` | `TEXT` | ✅ | ❌ |
| `pais` | `TEXT` | ✅ | ❌ |
| `region` | `TEXT` | ❌ | ❌ |
| `codigo_postal` | `TEXT` | ✅ | ❌ |
| `telefono` | `TEXT` | ✅ | ❌ |
| `linea_direccion1` | `TEXT` | ✅ | ❌ |
| `linea_direccion2` | `TEXT` | ❌ | ❌ |

---

### `pago`

- Filas: **2**
- PK: **codigo_cliente, id_transaccion**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_cliente` | `INTEGER` | ✅ | ✅ |
| `forma_pago` | `TEXT` | ✅ | ❌ |
| `id_transaccion` | `TEXT` | ✅ | ✅ |
| `fecha_pago` | `TEXT` | ✅ | ❌ |
| `total` | `REAL` | ✅ | ❌ |

---

### `pedido`

- Filas: **2**
- PK: **codigo_pedido**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_pedido` | `INTEGER` | ❌ | ✅ |
| `fecha_pedido` | `TEXT` | ✅ | ❌ |
| `fecha_esperada` | `TEXT` | ✅ | ❌ |
| `fecha_entrega` | `TEXT` | ❌ | ❌ |
| `estado` | `TEXT` | ✅ | ❌ |
| `comentarios` | `TEXT` | ❌ | ❌ |
| `codigo_cliente` | `INTEGER` | ✅ | ❌ |

---

### `producto`

- Filas: **4**
- PK: **codigo_producto**
- Duplicados PK (filas extra): **0**

| Columna | Tipo | NOT NULL | PK |
|--------|------|:--------:|:--:|
| `codigo_producto` | `TEXT` | ❌ | ✅ |
| `nombre` | `TEXT` | ✅ | ❌ |
| `gama` | `TEXT` | ✅ | ❌ |
| `dimensiones` | `TEXT` | ❌ | ❌ |
| `proveedor` | `TEXT` | ❌ | ❌ |
| `descripcion` | `TEXT` | ❌ | ❌ |
| `cantidad_en_stock` | `INTEGER` | ✅ | ❌ |
| `precio_venta` | `REAL` | ✅ | ❌ |
| `precio_proveedor` | `REAL` | ❌ | ❌ |

---

## 3. Nulos por Tabla

### `cliente`

| Columna | Nulos | % |
|--------|------:|--:|
| `fax` | 2 | 100.0% |
| `linea_direccion2` | 2 | 100.0% |
| `region` | 2 | 100.0% |

### `empleado`

| Columna | Nulos | % |
|--------|------:|--:|
| `apellido2` | 2 | 66.7% |
| `codigo_jefe` | 1 | 33.3% |

### `gama_producto`

| Columna | Nulos | % |
|--------|------:|--:|
| `descripcion_html` | 3 | 100.0% |
| `imagen` | 3 | 100.0% |

### `oficina`

| Columna | Nulos | % |
|--------|------:|--:|
| `linea_direccion2` | 2 | 100.0% |

### `pedido`

| Columna | Nulos | % |
|--------|------:|--:|
| `fecha_entrega` | 1 | 50.0% |
| `comentarios` | 1 | 50.0% |

### `producto`

| Columna | Nulos | % |
|--------|------:|--:|
| `dimensiones` | 1 | 25.0% |


---

## 4. Rangos Numéricos

### `cliente`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `codigo_cliente` | 100 | 101 | 100.5 |
| `codigo_empleado_rep_ventas` | 2 | 3 | 2.5 |
| `limite_credito` | 3000.0 | 5000.0 | 4000.0 |

### `detalle_pedido`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `codigo_pedido` | 1000 | 1001 | 1000.3333333333334 |
| `cantidad` | 2 | 10 | 5.666666666666667 |
| `precio_unidad` | 5.5 | 19.99 | 11.163333333333332 |
| `numero_linea` | 1 | 2 | 1.3333333333333333 |

### `empleado`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `codigo_empleado` | 1 | 3 | 2.0 |
| `codigo_jefe` | 1 | 1 | 1.0 |

### `pago`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `codigo_cliente` | 100 | 101 | 100.5 |
| `total` | 40.0 | 94.98 | 67.49000000000001 |

### `pedido`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `codigo_pedido` | 1000 | 1001 | 1000.5 |
| `codigo_cliente` | 100 | 101 | 100.5 |

### `producto`

| Columna | Min | Max | Avg |
|--------|----:|----:|----:|
| `cantidad_en_stock` | 40 | 100 | 65.0 |
| `precio_venta` | 5.5 | 19.99 | 11.997499999999999 |
| `precio_proveedor` | 2.5 | 12.0 | 6.875 |


---

## 5. Foreign Keys Detectadas

| Tabla hija | Columna (from) | Tabla padre | Columna (to) | ON UPDATE | ON DELETE |
|-----------|------------------|------------|--------------|----------|----------|
| `cliente` | `codigo_empleado_rep_ventas` | `empleado` | `codigo_empleado` | `CASCADE` | `SET NULL` |
| `detalle_pedido` | `codigo_producto` | `producto` | `codigo_producto` | `CASCADE` | `RESTRICT` |
| `detalle_pedido` | `codigo_pedido` | `pedido` | `codigo_pedido` | `CASCADE` | `CASCADE` |
| `empleado` | `codigo_jefe` | `empleado` | `codigo_empleado` | `CASCADE` | `SET NULL` |
| `empleado` | `codigo_oficina` | `oficina` | `codigo_oficina` | `CASCADE` | `RESTRICT` |
| `pago` | `codigo_cliente` | `cliente` | `codigo_cliente` | `CASCADE` | `RESTRICT` |
| `pedido` | `codigo_cliente` | `cliente` | `codigo_cliente` | `CASCADE` | `RESTRICT` |
| `producto` | `gama` | `gama_producto` | `gama` | `CASCADE` | `RESTRICT` |

---

## 6. Conclusiones

- Si hay **duplicados de PK**, revisa la lógica de inserción o define PK correctamente.
- Si hay muchas columnas con **nulos**, decide si deben ser opcionales o normalizarse.
- Si no aparecen **FKs**, asegúrate de haber creado el esquema con `FOREIGN KEY` y `PRAGMA foreign_keys=ON`.
