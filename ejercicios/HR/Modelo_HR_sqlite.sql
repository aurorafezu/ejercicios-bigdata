PRAGMA foreign_keys = ON;

-- ------------------------------------------------------------
-- DROP (por si lo ejecutas más de una vez)
-- ------------------------------------------------------------
DROP VIEW IF EXISTS emp_details_view;

DROP TABLE IF EXISTS job_history;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS regions;

-- ------------------------------------------------------------
-- REGIONS
-- ------------------------------------------------------------
CREATE TABLE regions (
  region_id   INTEGER NOT NULL,
  region_name TEXT,
  PRIMARY KEY (region_id)
);

-- ------------------------------------------------------------
-- COUNTRIES
-- ------------------------------------------------------------
CREATE TABLE countries (
  country_id   TEXT NOT NULL,          -- CHAR(2) en Oracle
  country_name TEXT,
  region_id    INTEGER,

  PRIMARY KEY (country_id),
  FOREIGN KEY (region_id) REFERENCES regions(region_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- LOCATIONS
-- ------------------------------------------------------------
CREATE TABLE locations (
  location_id    INTEGER NOT NULL,      -- NUMBER(4)
  street_address TEXT,
  postal_code    TEXT,
  city           TEXT NOT NULL,
  state_province TEXT,
  country_id     TEXT,

  PRIMARY KEY (location_id),
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- DEPARTMENTS
-- Nota: manager_id referencia employees, pero employees aún no existe.
-- En SQLite, lo resolvemos creando la FK después con recreación es engorroso.
-- Solución práctica: dejamos manager_id y lo validas por lógica o queries.
-- (Si quieres FK real, te preparo migración con tabla temporal.)
-- ------------------------------------------------------------
CREATE TABLE departments (
  department_id   INTEGER NOT NULL,     -- NUMBER(4)
  department_name TEXT NOT NULL,
  manager_id      INTEGER,              -- NUMBER(6)
  location_id     INTEGER,

  PRIMARY KEY (department_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- JOBS
-- ------------------------------------------------------------
CREATE TABLE jobs (
  job_id      TEXT NOT NULL,            -- VARCHAR2(10)
  job_title   TEXT NOT NULL,
  min_salary  INTEGER,
  max_salary  INTEGER,

  PRIMARY KEY (job_id),
  CHECK (min_salary IS NULL OR min_salary >= 0),
  CHECK (max_salary IS NULL OR max_salary >= 0),
  CHECK (min_salary IS NULL OR max_salary IS NULL OR min_salary <= max_salary)
);

-- ------------------------------------------------------------
-- EMPLOYEES
-- ------------------------------------------------------------
CREATE TABLE employees (
  employee_id     INTEGER NOT NULL,     -- NUMBER(6)
  first_name      TEXT,
  last_name       TEXT NOT NULL,
  email           TEXT NOT NULL,
  phone_number    TEXT,
  hire_date       TEXT NOT NULL,        -- DATE -> TEXT (ISO 'YYYY-MM-DD')
  job_id          TEXT NOT NULL,
  salary          REAL,
  commission_pct  REAL,
  manager_id      INTEGER,
  department_id   INTEGER,

  PRIMARY KEY (employee_id),
  UNIQUE (email),

  -- CHECK original: salary > 0
  CHECK (salary IS NULL OR salary > 0),

  FOREIGN KEY (department_id) REFERENCES departments(department_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL,

  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- JOB_HISTORY
-- ------------------------------------------------------------
CREATE TABLE job_history (
  employee_id    INTEGER NOT NULL,
  start_date     TEXT NOT NULL,
  end_date       TEXT NOT NULL,
  job_id         TEXT NOT NULL,
  department_id  INTEGER,

  PRIMARY KEY (employee_id, start_date),

  CHECK (end_date > start_date),

  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  FOREIGN KEY (department_id) REFERENCES departments(department_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

-- ------------------------------------------------------------
-- VIEW (sin WITH READ ONLY)
-- ------------------------------------------------------------
CREATE VIEW emp_details_view AS
SELECT
  e.employee_id,
  e.job_id,
  e.manager_id,
  e.department_id,
  d.location_id,
  l.country_id,
  e.first_name,
  e.last_name,
  e.salary,
  e.commission_pct,
  d.department_name,
  j.job_title,
  l.city,
  l.state_province,
  c.country_name,
  r.region_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN jobs j        ON j.job_id = e.job_id
JOIN locations l   ON d.location_id = l.location_id
JOIN countries c   ON l.country_id = c.country_id
JOIN regions r     ON c.region_id = r.region_id;

-- ------------------------------------------------------------
-- ÍNDICES útiles (PK/UNIQUE ya crean índices implícitos)
-- ------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_countries_region   ON countries(region_id);
CREATE INDEX IF NOT EXISTS idx_locations_country  ON locations(country_id);
CREATE INDEX IF NOT EXISTS idx_departments_loc    ON departments(location_id);

CREATE INDEX IF NOT EXISTS idx_employees_dept     ON employees(department_id);
CREATE INDEX IF NOT EXISTS idx_employees_job      ON employees(job_id);
CREATE INDEX IF NOT EXISTS idx_employees_manager  ON employees(manager_id);

CREATE INDEX IF NOT EXISTS idx_jobhist_job        ON job_history(job_id);
CREATE INDEX IF NOT EXISTS idx_jobhist_dept       ON job_history(department_id);
