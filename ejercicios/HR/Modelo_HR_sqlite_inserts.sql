PRAGMA foreign_keys = ON;

-- =========================================================
-- REGIONS
-- =========================================================
--INSERT INTO regions VALUES (1,'Europe');
--INSERT INTO regions VALUES (2,'Americas');
--INSERT INTO regions VALUES (3,'Asia');
--INSERT INTO regions VALUES (4,'Middle East and Africa');

-- =========================================================
-- COUNTRIES
-- =========================================================
--INSERT INTO countries VALUES ('IT','Italy',1);
--INSERT INTO countries VALUES ('US','United States of America',2);
--INSERT INTO countries VALUES ('CA','Canada',2);

-- =========================================================
-- LOCATIONS
-- =========================================================
--INSERT INTO locations VALUES (1000,'Via Roma 1','00100','Roma',NULL,'IT');
--INSERT INTO locations VALUES (1400,'2014 Jabberwocky Rd','26192','Southlake','Texas','US');
--INSERT INTO locations VALUES (1700,'2004 Charade Rd','98199','Seattle','Washington','US');
--INSERT INTO locations VALUES (1800,'147 Spadina Ave','M5V 2L7','Toronto','Ontario','CA');

-- =========================================================
-- JOBS
-- =========================================================
INSERT INTO jobs VALUES ('AD_PRES','President',20000,40000);
INSERT INTO jobs VALUES ('AD_VP','Administration Vice President',15000,30000);
INSERT INTO jobs VALUES ('IT_PROG','Programmer',4000,10000);
INSERT INTO jobs VALUES ('SA_REP','Sales Representative',6000,12000);

-- =========================================================
-- DEPARTMENTS
-- (location_id EXISTE)
-- =========================================================
INSERT INTO departments VALUES (10,'Administration',NULL,1700);
INSERT INTO departments VALUES (60,'IT',NULL,1400);
INSERT INTO departments VALUES (80,'Sales',NULL,1700);
INSERT INTO departments VALUES (90,'Executive',NULL,1700);

-- =========================================================
-- EMPLOYEES
-- =========================================================
INSERT INTO employees VALUES
(100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,NULL,NULL,90);

INSERT INTO employees VALUES
(101,'Neena','Kochhar','NKOCHHAR','515.123.4568','2005-09-21','AD_VP',17000,NULL,100,90);

INSERT INTO employees VALUES
(102,'Lex','De Haan','LDEHAAN','515.123.4569','2001-01-13','SA_REP',9000,NULL,100,80);

INSERT INTO employees VALUES
(103,'Alexander','Hunold','AHUNOLD','590.423.4567','2006-01-03','IT_PROG',6000,NULL,102,60);

-- =========================================================
-- ACTUALIZAR MANAGERS
-- =========================================================
UPDATE departments SET manager_id = 100 WHERE department_id = 90;
UPDATE departments SET manager_id = 101 WHERE department_id = 60;
UPDATE departments SET manager_id = 102 WHERE department_id = 80;

-- =========================================================
-- JOB_HISTORY
-- (job_id EXISTE)
-- =========================================================
INSERT INTO job_history VALUES
(103,'2004-01-01','2006-01-01','IT_PROG',60);
