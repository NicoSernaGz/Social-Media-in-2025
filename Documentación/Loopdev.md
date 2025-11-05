# TAREAS DEV

🎯 **Objetivo general**

Desplegar y ejecutar un entorno de análisis de datos colaborativo que permita al equipo técnico del curso desarrollar el proyecto final de análisis de datos, abarcando desde la obtención de fuentes públicas hasta la entrega del informe final y notebook.

El propósito es consolidar el flujo completo de trabajo en análisis de datos (ETL, análisis, visualización y documentación).

---

## 🔧 **Tareas para el equipo de desarrollo**

### 🧱 **Tarea 1: Configuración del entorno de desarrollo y repositorio**

🎯 *Objetivo*
Preparar el entorno de trabajo colaborativo para el equipo de análisis y garantizar la correcta gestión de versiones del proyecto.

🧩 *Criterios de aceptación*

* Configurar entorno de trabajo en **Python 3.x**, con librerías instaladas: `pandas`, `numpy`, `matplotlib`, `seaborn`, `jupyter`, `openpyxl`.
* Crear repositorio en GitHub o GitLab con estructura base del proyecto (`data/`, `notebooks/`, `docs/`, `outputs/`).
* Configurar `.gitignore` y lineamientos de commits.
* Crear y compartir notebook base (`main_analysis.ipynb`) con plantilla de estructura (importación, exploración, análisis, visualización).

---

### 🧱 **Tarea 2: Recolección e integración de datos públicos**

🎯 *Objetivo*
Identificar, descargar y almacenar las fuentes de datos públicas necesarias según la línea de investigación seleccionada.

🧩 *Criterios de aceptación*

* Identificar al menos **dos fuentes confiables** (por ejemplo: DANE, UPME, MinTIC, Banco Mundial).
* Automatizar descarga de datos si están disponibles vía API (usar `requests` o `curl`).
* Guardar datasets crudos en `data/raw/`.
* Registrar metadatos: fuente, fecha de descarga, campos relevantes, formato y tamaño.
* Generar script `data_loader.py` que permita cargar los archivos en DataFrame para análisis.

---

### 🧱 **Tarea 3: Exploración y limpieza de datos (ETL básico)**

🎯 *Objetivo*
Depurar y preparar los datos para análisis, asegurando coherencia estructural y calidad de los registros.

🧩 *Criterios de aceptación*

* Crear notebook `data_cleaning.ipynb` con pasos de inspección (`df.info()`, `df.describe()`).
* Implementar eliminación o imputación de valores nulos.
* Corregir tipos de datos (fechas, enteros, strings, flotantes).
* Detectar y remover duplicados.
* Aplicar normalización o escalado si se requieren comparaciones numéricas.
* Guardar resultados limpios en `data/processed/`.

---

### 🧱 **Tarea 4: Análisis descriptivo y estadístico**

🎯 *Objetivo*
Aplicar técnicas estadísticas para comprender las tendencias y patrones dentro de los datos.

🧩 *Criterios de aceptación*

* Crear notebook `descriptive_analysis.ipynb`.
* Calcular métricas básicas (media, mediana, moda, desviación estándar, varianza, percentiles).
* Generar correlaciones y distribuciones relevantes.
* Identificar tendencias por regiones, periodos o categorías según el tema.
* Guardar resultados intermedios y gráficas en `outputs/analysis/`.

---

### 🧱 **Tarea 5: Visualización de resultados**

🎯 *Objetivo*
Representar de manera gráfica los hallazgos del análisis de datos.

🧩 *Criterios de aceptación*

* Usar **Matplotlib** o **Seaborn** para graficar histogramas, gráficos de barras, líneas de tiempo y correlaciones.
* Implementar funciones reutilizables para generar visualizaciones estandarizadas.
* Guardar las visualizaciones como imágenes (`.png` o `.svg`) en `outputs/visuals/`.
* Validar que las gráficas tengan títulos, leyendas y ejes correctamente etiquetados.

---

### 🧱 **Tarea 6: Interpretación y generación del informe técnico**

🎯 *Objetivo*
Consolidar los hallazgos del análisis y construir el informe final técnico con narrativa clara y conclusiones respaldadas en datos.

🧩 *Criterios de aceptación*

* Crear plantilla en Markdown o Word (`report_template.md` o `.docx`) con estructura:

  * Portada y autores
  * Introducción y justificación
  * Fuentes de datos
  * Metodología y técnicas aplicadas
  * Resultados principales
  * Conclusiones y recomendaciones
* Exportar a PDF como entrega final (`ProyectoFinal_[Tema].pdf`).
* Adjuntar Notebook limpio (`main_analysis.ipynb`) con comentarios y celdas ejecutadas.

---

### 🧱 **Tarea 7: Validación y control de calidad**

🎯 *Objetivo*
Verificar la coherencia, reproducibilidad y consistencia del trabajo final antes de su entrega.

🧩 *Criterios de aceptación*

* Validar que los scripts y notebooks se ejecuten sin errores en un entorno limpio.
* Revisar integridad de datos: totales, conteos y coherencia con fuentes originales.
* Revisar ortografía, formato de gráficos y etiquetas.
* Asegurar que los hallazgos del informe coincidan con los resultados del notebook.

---

### 🧱 **Tarea 8: Entrega y publicación**

🎯 *Objetivo*
Empaquetar y entregar los resultados finales de acuerdo con las especificaciones del proyecto.

🧩 *Criterios de aceptación*

* Comprimir carpeta final (`ProyectoFinal_[Equipo].zip`) incluyendo:

  * PDF del informe
  * Notebook principal
  * Carpeta de datos limpios (`data/processed`)
  * Visualizaciones generadas (`outputs/visuals`)
* Subir la entrega a Moodle y registrar la fecha de carga.
* Documentar los enlaces de referencia en `README.md` del repositorio.
