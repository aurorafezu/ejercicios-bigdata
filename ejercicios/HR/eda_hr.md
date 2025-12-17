# Análisis Exploratorio de Datos (EDA) – HR

**Base de datos:** `hr.db`

**Fecha:** 2025-12-17 18:41:45

---

## 1. Resumen Ejecutivo

- **Tablas analizadas:** 7
- **Total de registros (suma):** 31
- **Modelo:** HR normalizado (3FN)

## 2. Tablas y Volumen de Datos

| Tabla | Filas |
|------|------:|
| countries | 8 |
| departments | 4 |
| employees | 4 |
| job_history | 1 |
| jobs | 4 |
| locations | 6 |
| regions | 4 |

## 3. Estructura de las Tablas

### Tabla `countries`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| country_id | TEXT | ✔ | 0 |
| country_name | TEXT |  | 0 |
| region_id | INTEGER |  | 0 |

### Tabla `departments`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| department_id | INTEGER | ✔ | 0 |
| department_name | TEXT |  | 0 |
| manager_id | INTEGER |  | 1 |
| location_id | INTEGER |  | 0 |

### Tabla `employees`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| employee_id | INTEGER | ✔ | 0 |
| first_name | TEXT |  | 0 |
| last_name | TEXT |  | 0 |
| email | TEXT |  | 0 |
| phone_number | TEXT |  | 0 |
| hire_date | TEXT |  | 0 |
| job_id | TEXT |  | 0 |
| salary | REAL |  | 0 |
| commission_pct | REAL |  | 4 |
| manager_id | INTEGER |  | 1 |
| department_id | INTEGER |  | 0 |

### Tabla `job_history`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| employee_id | INTEGER | ✔ | 0 |
| start_date | TEXT | ✔ | 0 |
| end_date | TEXT |  | 0 |
| job_id | TEXT |  | 0 |
| department_id | INTEGER |  | 0 |

### Tabla `jobs`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| job_id | TEXT | ✔ | 0 |
| job_title | TEXT |  | 0 |
| min_salary | INTEGER |  | 0 |
| max_salary | INTEGER |  | 0 |

### Tabla `locations`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| location_id | INTEGER | ✔ | 0 |
| street_address | TEXT |  | 0 |
| postal_code | TEXT |  | 0 |
| city | TEXT |  | 0 |
| state_province | TEXT |  | 2 |
| country_id | TEXT |  | 0 |

### Tabla `regions`

| Columna | Tipo | PK | Nulos |
|--------|------|----|------:|
| region_id | INTEGER | ✔ | 0 |
| region_name | TEXT |  | 0 |

## 4. Relaciones (Claves Foráneas)

### countries

- `countries.region_id` → `regions.region_id`

### departments

- `departments.location_id` → `locations.location_id`

### employees

- `employees.manager_id` → `employees.employee_id`
- `employees.job_id` → `jobs.job_id`
- `employees.department_id` → `departments.department_id`

### job_history

- `job_history.department_id` → `departments.department_id`
- `job_history.job_id` → `jobs.job_id`
- `job_history.employee_id` → `employees.employee_id`

### locations

- `locations.country_id` → `countries.country_id`

## 5. Análisis Numérico – Salarios

- **Salario mínimo:** 6000.0
- **Salario máximo:** 24000.0
- **Salario medio:** 14000.0

## 6. Calidad de Datos

### Columnas con valores nulos

- `departments.manager_id` → 1 nulos
- `employees.commission_pct` → 4 nulos
- `employees.manager_id` → 1 nulos
- `locations.state_province` → 2 nulos

## 7. Conclusiones

- La base de datos HR presenta un diseño normalizado en 3FN.
- Las relaciones están correctamente definidas mediante claves foráneas.
- El volumen de datos es adecuado para prácticas de JOINs y EDA.
- Existen valores nulos esperables (ej. commission_pct, manager_id).
- El modelo es apto para análisis analítico y visualización.
