# 03_RESULTADOS.md: Análisis y Visualización

## 3.1. Gráfico 1: Evolución de la Democracia en el Magreb

![Evolución de la Democracia](resultados/1_evolucion_democracia.png)

### Interpretación
En este gráfico se observa la evolución del índice de democracia liberal para los cinco países del Magreb. El patrón más evidente y dramático es la **divergencia radical** de los países a partir de 2011.

-   **Túnez (El caso de éxito):** La línea de Túnez muestra un crecimiento exponencial a partir de 2011, coincidiendo con el inicio de la **Primavera Árabe**. Pasa de ser un régimen autoritario a consolidarse como una democracia en transición, siendo el único país del grupo que logra un cambio positivo y sostenido.
-   **Libia (El caso fallido):** Por el contrario, Libia sufre un colapso total. El mismo evento que impulsó a Túnez provoca en Libia una guerra civil que desintegra el estado, haciendo que su índice de democracia caiga a prácticamente cero.
-   **Los vecinos (Estabilidad autoritaria):** Mientras tanto, países como **Argelia** y **Marruecos** muestran una sorprendente estabilidad en sus bajos niveles de democracia. A pesar de las protestas regionales, sus regímenes lograron mantenerse sin cambios estructurales significativos.

Este gráfico responde de forma contundente a nuestra primera sub-pregunta: el impacto de la Primavera Árabe fue muy diferente en cada país, con Túnez como el único beneficiado en términos democráticos.

### Prompt de IA para este gráfico
> "Dame el código en Python con Seaborn para crear un gráfico de líneas que muestre la evolución de la variable 'vdem_libdem' a lo largo de los años ('year'), diferenciando cada país ('cname') con un color distinto."

---

## 3.2. Gráfico 2: Relación entre Riqueza y Democracia

![PIB vs Democracia](resultados/2_pib_vs_democracia.png)

### Interpretación
Este gráfico de dispersión nos ayuda a explorar si los países más ricos tienden a ser más democráticos. Cada punto es un país en un año concreto.

A simple vista, **no se observa una relación clara y directa**. Por ejemplo, vemos puntos de **Libia** con un PIB per cápita relativamente alto (por el petróleo) pero con niveles de democracia cercanos a cero. Por otro lado, **Túnez** logra aumentar significativamente su democracia (moviéndose hacia la derecha en el gráfico) sin un aumento proporcional en su riqueza.

Esto sugiere que, al menos en la región del Magreb, **el desarrollo económico no es una causa directa de la democratización**. Otros factores, como los movimientos sociales o la estabilidad institucional, parecen ser mucho más determinantes.

### Prompt de IA para este gráfico
> "Necesito un gráfico de dispersión (scatterplot) para comparar el PIB per cápita ('gle_cgdpc') con el índice de democracia ('vdem_libdem'). Quiero que cada país tenga un color diferente y que el tamaño de los puntos represente el año, para ver la evolución."

---

## 3.3. Gráfico 3: Matriz de Correlación

![Matriz de Correlación](resultados/3_correlacion_variables.png)

### Interpretación
El mapa de calor nos permite cuantificar la relación entre las variables. Los valores cercanos a 1 (azul oscuro) indican una correlación positiva fuerte, y los cercanos a -1 (rojo oscuro) una correlación negativa fuerte.

-   Confirmamos lo que vimos antes: la correlación entre **Democracia y PIB es muy baja (0.1)**. No hay una relación estadística fuerte.
-   La correlación más interesante es la que existe entre **Democracia y No-Corrupción (0.48)**. Es una correlación positiva moderada, lo que sugiere que los países con instituciones más democráticas tienden a ser percibidos como menos corruptos.
-   También destaca la correlación **negativa (-0.3) entre Democracia y Desempleo Juvenil**, aunque es más débil. Podría indicar que los regímenes menos democráticos tienen más problemas para integrar a los jóvenes en el mercado laboral.

### Prompt de IA para este gráfico
> "Quiero un mapa de calor (heatmap) con Seaborn que muestre la matriz de correlación de mis variables numéricas. Asegúrate de que se muestren los valores numéricos dentro de cada celda (annot=True) y usa un mapa de color 'coolwarm'."

---

## 3.4. Gráfico 4: Impacto de la Primavera Árabe

![Impacto Primavera Árabe](resultados/4_impacto_primavera_arabe.png)

### Interpretación
Este gráfico de barras es la evidencia más clara y contundente del impacto del evento de 2011. Compara el nivel de democracia promedio de cada país antes y después de la Primavera Árabe.

Se observa un **salto gigantesco en el nivel de democracia promedio de Túnez** en el periodo "Post-Primavera". Es el único país donde la barra azul es significativamente más alta que la naranja.

En contraste, el resto de países o bien se mantienen prácticamente igual (**Marruecos, Argelia**) o empeoran drásticamente (**Libia**).

Este gráfico responde de forma definitiva a nuestra sub-pregunta, confirmando visualmente que el evento tuvo un **impacto democratizador real y medible solo en Túnez**, mientras que el resto de la región siguió su propio camino.

### Prompt de IA para este gráfico
> "Necesito un gráfico de barras para comparar el nivel de democracia promedio ('vdem_libdem') por país ('cname') antes y después de 2011. Ya tengo una columna 'periodo_historico' que lo divide. Usa esa columna para el 'hue' en Seaborn."
