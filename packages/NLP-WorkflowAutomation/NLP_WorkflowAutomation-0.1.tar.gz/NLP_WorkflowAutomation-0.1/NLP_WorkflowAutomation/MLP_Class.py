import deepl
from nltk.sentiment import SentimentIntensityAnalyzer
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from funciones import _create_frequency_matrix, _create_tf_matrix, _create_documents_per_words, _create_idf_matrix, _create_tf_idf_matrix, _score_sentences, _find_average_score, _generate_summary

api_key = '72c35d67-3f34-5172-5933-9bd1df7a1985:fx'

class NLP_WorkflowAutomation:
    def __init__(self, api_key):
        self.api_key = api_key

    def translator(self, text:str, target_lang:str):
        self.text = text
        self.target_lang = target_lang

        '''Realiza una traducción de texto a un idioma especificado utilizando la API de DeepL.

            Parámetros:
            text (str): El texto que se desea traducir.
            target_lang (str): El idioma al que se desea traducir el texto. Debe estar en formato de dos letras, por ejemplo, 'es' para español, 'fr' para francés, etc.

            - Para ver los idiomas disponibles: https://www.deepl.com/es/docs-api/translate-text/translate-text

            Devuelve:
            str: El texto traducido al idioma especificado.

            Ejemplo de Uso:
            translated_text = translator("Hello, how are you?", "es")
            print(translated_text)  # Salida: "Hola, ¿cómo estás?"

            Notas:
            - Para utilizar esta función, se debe contar con una clave de API válida de DeepL. Asegúrate de proporcionar la clave correcta en el código.
            - El idioma de destino debe estar en el formato correcto de dos letras según las especificaciones de DeepL.
            - Esta función utiliza la API de DeepL para realizar la traducción y requiere una conexión a Internet activa.'''
        
        try:

            
            translator = deepl.Translator(self.api_key) 

            language = str.lower(self.target_lang)
            print(self.text, 'to ', language)

            result = translator.translate_text(text, target_lang=language) 
            translated_text = result.text
            
            return translated_text
    
        except deepl.APIError as api_error:
            # Captura otros errores específicos de la API de DeepL
            return f"Error de API de DeepL: {str(api_error)}"
        
    def sentiment_analises(self, message):
        self.message = message
        ''' Realiza un análisis de sentimiento en un mensaje de texto utilizando el SentimentIntensityAnalyzer de NLTK.

            Parámetros:
            message (str): El mensaje de texto que se desea analizar en términos de sentimiento.

            Devuelve:
            None

            Imprime en la consola:
            - "positive" si el sentimiento del mensaje es mayor o igual a 0.2.
            - "neutral" si el sentimiento del mensaje está entre -0.2 (exclusivo) y 0.2 (inclusivo).
            - "negative" si el sentimiento del mensaje es menor o igual a -0.2.

            Ejemplo de Uso:
            sentiment_analyses('I am very happy and excited.')  # Salida: "positive"
            sentiment_analyses('This is a neutral statement.')     # Salida: "neutral"
            sentiment_analyses('I am feeling really sad.')        # Salida: "negative"

            Notas:
            - Esta función utiliza el SentimentIntensityAnalyzer de NLTK para calcular una puntuación de sentimiento compuesta ('compound') en el mensaje de entrada.
            - La puntuación 'compound' se compara con umbrales para determinar si el mensaje es positivo, neutral o negativo.
            - Los umbrales utilizados son >= 0.2 para positivo, < 0.2 y > -0.2 para neutral, y <= -0.2 para negativo.
            - Asegúrate de tener NLTK instalado y configurado adecuadamente para utilizar esta función.
            '''

        sia = SentimentIntensityAnalyzer()
        result_sent = sia.polarity_scores(self.message)
        print(result_sent['compound'])
    
        if result_sent['compound'] >= 0.2:
            print('positive')
        elif (result_sent['compound'] < 0.2) and (result_sent['compound'] > -0.2):
            print('neutral')
        elif result_sent['compound'] <= -0.2:
            print('negative')


    def pdf_to_text(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf
        '''  
            Convierte un archivo PDF en texto.

            Parámetros:
            - ruta_pdf (str): La ruta al archivo PDF que se debe convertir a texto.

            Devuelve:
            - str: El texto extraído del archivo PDF.

            Excepciones:
            - Exception: Si ocurre algún error durante el proceso, se captura y se devuelve como resultado.
            - FileNotFoundError: la ruta no es correcta

            Esta función toma la ruta de un archivo PDF, lo abre en modo lectura binaria,
            y utiliza la biblioteca PyPDF2 para extraer el texto de todas las páginas del PDF.
            El texto extraído se almacena en una cadena y se devuelve como resultado.

            Ejemplo de uso:
            ruta_del_pdf = r'C:\ruta\a\archivo.pdf'
            texto_extraído = pdf_a_texto(ruta_del_pdf)
            print(texto_extraído)
            '''

        try:
            # Abre el archivo PDF 
            with open(ruta_pdf, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                texto = ''
                
                for pagina in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[pagina]
                    texto += page.extract_text()
                    
                return texto
        
        
        except FileNotFoundError:
            return "Error: El archivo PDF no se encontró en la ruta especificada."
        except Exception as e:
            return f"Error inesperado al procesar el archivo PDF: {str(e)}"

class ResumenPDF(NLP_WorkflowAutomation):
    def __init__(self, api_key):
        super().__init__(api_key)

    def summarize_pdf(self, ruta_pdf):
        self.ruta_pdf = ruta_pdf

        # Obtener el texto del PDF
        texto_pdf = self.pdf_to_text(self.ruta_pdf)  # Elimina el argumento adicional "ruta_pdf"

        # Tokenizar el texto
        sentences = sent_tokenize(texto_pdf)
        total_documents = len(sentences)

        # Crear matriz de frecuencias
        freq_matrix = _create_frequency_matrix(sentences)

        # Calcular TermFrequency y generar matriz
        tf_matrix = _create_tf_matrix(freq_matrix)

        # Porcentaje de aparición
        count_doc_per_words = _create_documents_per_words(freq_matrix)

        # Calcular IDF y generar matriz
        idf_matrix = _create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)

        # Calcular TF*IDF y generar matriz
        tf_idf_matrix = _create_tf_idf_matrix(tf_matrix, idf_matrix)

        # Puntuar frase
        sentence_scores = _score_sentences(tf_idf_matrix)

        # Marcar el límite
        threshold = _find_average_score(sentence_scores)

        # Generar el resumen
        resumen = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

        return resumen


