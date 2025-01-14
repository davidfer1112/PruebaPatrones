


CREATE TABLE POBLACION (
    ANO INT,
    CODIGO_LOCALIDAD INT,
    NOMBRE_LOCALIDAD VARCHAR(255),
    SEXO VARCHAR(50),
    EDAD INT,
    CURSODEVIDA VARCHAR(100),
    GRUPOEDAD VARCHAR(100),
    POBLACION_7 INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/POBLACION.txt'
INTO TABLE POBLACION
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ANO, CODIGO_LOCALIDAD, NOMBRE_LOCALIDAD, SEXO, EDAD, CURSODEVIDA, GRUPOEDAD, POBLACION_7);

SELECT * FROM POBLACION LIMIT 10;

drop table PROGRAMA_1_TEMP;

CREATE TABLE PROGRAMA_1 (
    REGIMEN_DE_AFILIACION VARCHAR(255),
    LOCALIDAD_CALCULADA VARCHAR(255),
    ASEGURADOR VARCHAR(255),
    FECHA_DE_NACIMIENTO_USUARIO VARCHAR(50), 
    SEXO VARCHAR(50),
    FECHA_DE_LA_CONSULTA VARCHAR(50), 
    NACIONALIDAD VARCHAR(100)
);

drop table PROGRAMA_2;

CREATE TABLE PROGRAMA_2 (
    SEXO_BIOLOGICO VARCHAR(50),
    LOCALIDAD VARCHAR(255),
    EAPB VARCHAR(255),
    FECHA_DE_NACIMIENTO DATE,
    PERTENENCIA_ETNICA VARCHAR(100),
    SEXO_BIOLOGICO_1 VARCHAR(50),
    RIESGO_PSICOSOCIAL VARCHAR(50),
    FECHA_DE_LA_CONSULTA DATE,
    TALLA INT
);


ALTER TABLE PROGRAMA_2 MODIFY FECHA_DE_NACIMIENTO VARCHAR(20);
ALTER TABLE PROGRAMA_2 MODIFY FECHA_DE_LA_CONSULTA VARCHAR(20);
ALTER TABLE PROGRAMA_2 MODIFY COLUMN TALLA INT NULL;






CREATE TABLE PROGRAMA_3 (
    LOCALIDADFIC_3 VARCHAR(255),
    NACIONALIDAD_10 VARCHAR(100),
    NOMBREEAPB_27 VARCHAR(255),
    FECHADENACIMIENTO_14 DATE,
    ETNIA_18 VARCHAR(100),
    SEXO_11 VARCHAR(50),
    GENERO_12 VARCHAR(50),
    FECHAINTERVENCION_2 DATE
);

ALTER TABLE PROGRAMA_3 MODIFY COLUMN FECHADENACIMIENTO_14 VARCHAR(50);
ALTER TABLE PROGRAMA_3 MODIFY COLUMN FECHAINTERVENCION_2 VARCHAR(50);


drop table PROGRAMA_4;

CREATE TABLE PROGRAMA_4 (
    LOCALIDAD_FIC VARCHAR(255),
    ESTADO_CIVIL_ VARCHAR(50),
    NOMBRE_EAPB_ VARCHAR(255),
    FECHA_DE_NACIMIENTO_ DATE,
    ETNIA_ VARCHAR(100),
    SEXO_ VARCHAR(100),
    FECHA_INTERVENCION DATE
);

ALTER TABLE PROGRAMA_4 MODIFY COLUMN FECHA_DE_NACIMIENTO_ VARCHAR(50);
ALTER TABLE PROGRAMA_4 MODIFY COLUMN FECHA_INTERVENCION VARCHAR(50);





LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/archivo_limpio2.txt'
INTO TABLE PROGRAMA_2
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(SEXO_BIOLOGICO, LOCALIDAD, EAPB, FECHA_DE_NACIMIENTO, PERTENENCIA_ETNICA, SEXO_BIOLOGICO_1, RIESGO_PSICOSOCIAL, FECHA_DE_LA_CONSULTA, TALLA);




LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/archivo_limpio3.txt'
INTO TABLE PROGRAMA_3
FIELDS TERMINATED BY '|'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(LOCALIDADFIC_3, NACIONALIDAD_10, NOMBREEAPB_27, FECHADENACIMIENTO_14, ETNIA_18, SEXO_11, GENERO_12, FECHAINTERVENCION_2);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/archivo_limpio4.txt'
INTO TABLE PROGRAMA_4
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


CREATE OR REPLACE VIEW VISTA_CONSOLIDADO AS
SELECT 
    LOCALIDAD_CALCULADA AS Localidad,
    SEXO AS Sexo,
    YEAR(STR_TO_DATE(FECHA_DE_NACIMIENTO_USUARIO, '%d/%m/%Y')) AS Edad,
    'PROGRAMA 1' AS Programa,
    ASEGURADOR AS EAPB,
    STR_TO_DATE(FECHA_DE_LA_CONSULTA, '%d/%m/%Y') AS Fecha_Atencion
FROM PROGRAMA_1

UNION ALL

SELECT 
    LOCALIDAD AS Localidad,
    SEXO_BIOLOGICO AS Sexo,
    YEAR(STR_TO_DATE(FECHA_DE_NACIMIENTO, '%d/%m/%Y')) AS Edad,
    'PROGRAMA 2' AS Programa,
    EAPB AS EAPB,
    STR_TO_DATE(FECHA_DE_LA_CONSULTA, '%d/%m/%Y') AS Fecha_Atencion
FROM PROGRAMA_2

UNION ALL

SELECT 
    LOCALIDADFIC_3 AS Localidad,
    SEXO_11 AS Sexo,
    YEAR(STR_TO_DATE(FECHADENACIMIENTO_14, '%d/%m/%Y')) AS Edad,
    'PROGRAMA 3' AS Programa,
    NOMBREEAPB_27 AS EAPB,
    STR_TO_DATE(FECHAINTERVENCION_2, '%d/%m/%Y') AS Fecha_Atencion
FROM PROGRAMA_3;


Drop view VISTA_INDICADORES;


CREATE VIEW VISTA_INDICADORES AS
SELECT
    YEAR(Fecha_Atencion) AS ANO,
    Localidad,
    FLOOR(Edad / 5) * 5 AS EDAD_QUINQUENIOS,
    COUNT(*) AS NUMERADOR,
    (SELECT POBLACION_7 
     FROM POBLACION P 
     WHERE P.CODIGO_LOCALIDAD = C.Localidad 
       AND P.ANO = YEAR(C.Fecha_Atencion) 
       AND P.EDAD = FLOOR(C.Edad / 5) * 5
     LIMIT 1) AS DENOMINADOR,
    (COUNT(*) / 
     (SELECT POBLACION_7 
      FROM POBLACION P 
      WHERE P.CODIGO_LOCALIDAD = C.Localidad 
        AND P.ANO = YEAR(C.Fecha_Atencion) 
        AND P.EDAD = FLOOR(C.Edad / 5) * 5
      LIMIT 1)) * 100 AS TASA
FROM VISTA_CONSOLIDADO C
GROUP BY ANO, Localidad, EDAD_QUINQUENIOS;





SELECT * INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/VISTA_CONSOLIDADO.txt'
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
FROM VISTA_CONSOLIDADO;

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));


SELECT * INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/VISTA_INDICADORES.txt'
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
FROM VISTA_INDICADORES;

SET SESSION sql_mode=(SELECT REPLACE(@@SESSION.sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT @@SESSION.sql_mode;



CREATE OR REPLACE VIEW VISTA_CONSOLIDADO AS
SELECT 
    LOCALIDAD_CALCULADA AS Localidad,
    SEXO AS Sexo,
    CASE 
        WHEN FECHA_DE_NACIMIENTO_USUARIO REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$' 
        THEN YEAR(STR_TO_DATE(FECHA_DE_NACIMIENTO_USUARIO, '%d/%m/%Y'))
        ELSE NULL
    END AS Edad,
    'PROGRAMA 1' AS Programa,
    ASEGURADOR AS EAPB,
    CASE 
        WHEN FECHA_DE_LA_CONSULTA REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$' 
        THEN STR_TO_DATE(FECHA_DE_LA_CONSULTA, '%d/%m/%Y')
        ELSE NULL
    END AS Fecha_Atencion
FROM PROGRAMA_1
UNION ALL
SELECT 
    LOCALIDAD AS Localidad,
    SEXO_BIOLOGICO AS Sexo,
    CASE 
        WHEN FECHA_DE_NACIMIENTO REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
        THEN YEAR(STR_TO_DATE(FECHA_DE_NACIMIENTO, '%d/%m/%Y'))
        ELSE NULL
    END AS Edad,
    'PROGRAMA 2' AS Programa,
    EAPB AS EAPB,
    CASE 
        WHEN FECHA_DE_LA_CONSULTA REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$' 
        THEN STR_TO_DATE(FECHA_DE_LA_CONSULTA, '%d/%m/%Y')
        ELSE NULL
    END AS Fecha_Atencion
FROM PROGRAMA_2
UNION ALL
SELECT 
    LOCALIDADFIC_3 AS Localidad,
    SEXO_11 AS Sexo,
    CASE 
        WHEN FECHADENACIMIENTO_14 REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$'
        THEN YEAR(STR_TO_DATE(FECHADENACIMIENTO_14, '%d/%m/%Y'))
        ELSE NULL
    END AS Edad,
    'PROGRAMA 3' AS Programa,
    NOMBREEAPB_27 AS EAPB,
    CASE 
        WHEN FECHAINTERVENCION_2 REGEXP '^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$' 
        THEN STR_TO_DATE(FECHAINTERVENCION_2, '%d/%m/%Y')
        ELSE NULL
    END AS Fecha_Atencion
FROM PROGRAMA_3;


