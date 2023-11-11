### NLP Workflow Automation

Este script Python proporciona un conjunto de funciones para realizar tareas comunes de procesamiento de lenguaje natural (NLP). Desde traducción de texto hasta análisis de sentimiento y resúmenes de archivos PDF, esta herramienta versátil simplifica la automatización de flujos de trabajo NLP.

#### Características

1. Traducción de Texto: Utiliza la API de DeepL para traducir texto a diferentes idiomas.

- translated_text = translator("Hello, how are you?", "es")

2. Análisis de Sentimiento: Utiliza el SentimentIntensityAnalyzer de NLTK para determinar si un mensaje es positivo, neutral o negativo.

- sentiment_analyses('I am very happy and excited.')  # Salida: "positive"

3. Conversión de PDF a Texto: Convierte archivos PDF en texto utilizando PyPDF2.

- texto_extraído = pdf_to_text(ruta_del_pdf)

4. Resumen de PDF: Genera un resumen del contenido de un archivo PDF.

- resumen = summarize_pdf(ruta_del_pdf)

#### Requisitos

Clave de API de DeepL para la función de traducción.
Instalación de las bibliotecas Python necesarias: deepl, nltk, y PyPDF2.

#### Uso

1. Clona este repositorio:

- git clone https://github.com/tu_usuario/tu_repo.git
  
2. Configura tu clave de API de DeepL en el script.

3. Ejecuta el script con Python:

- python nombre_del_script.py

Asegúrate de cumplir con los requisitos y disfruta de la automatización de tus tareas NLP con este script versátil. ¡Diviértete automatizando!

