# 01_README.md: Pregunta de Investigación

## Tema de Investigación
Análisis del Desarrollo Político y Económico en la región del Magreb.

## Pregunta Principal
**¿Qué relación existe entre el nivel de democracia y el desarrollo económico en los países del Magreb (Argelia, Marruecos, Túnez, Libia y Mauritania) durante el periodo 2000-2022?**

### Sub-preguntas de Análisis
1.  ¿Se observa un cambio significativo y duradero en el nivel de democracia de **Túnez** tras la **Primavera Árabe** en comparación con sus vecinos?
2.  ¿Existe una correlación estadística entre el **PIB per cápita**, la **percepción de corrupción** y el **índice de democracia** en la región?
3.  ¿Cómo ha impactado el **desempleo juvenil** en este panorama político-económico?

## Dataset y Variables
-   **Dataset:** Quality of Government (QoG) Standard Dataset - Enero 2024.
-   **Países Seleccionados:**
    -   Argelia (`DZA`)
    -   Marruecos (`MAR`)
    -   Túnez (`TUN`)
    -   Libia (`LBY`)
    -   Mauritania (`MRT`)
-   **Variables de Interés:**
    -   `vdem_libdem`: Índice de Democracia Liberal.
    -   `gle_cgdpc`: PIB per cápita.
    -   `ti_cpi`: Índice de Percepción de Corrupción.
    -   `bti_ci`: Índice de Consenso del Bertelsmann Transformation Index.
    -   `wdi_ynet`: Desempleo juvenil.
-   **Variable Derivada:**
    -   `nivel_democracia`: Categorización del índice `vdem_libdem` en "Autoritario", "Híbrido" y "Democracia/Transición".
    -   `periodo_historico`: Separación de los datos en "Pre-Primavera (2000-2010)" y "Post-Primavera (2011-2022)".
