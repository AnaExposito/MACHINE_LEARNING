# MACHINE_LEARNING## Entregable
El objetivo de este proyecto es desarrollar un modelo de machine learning, desde la obtención de datos hasta su despliegue.


El proyecto aborda los siguientes tipos de análisis sobre los datos de redes sociales:


Clasificación de Sentimiento: Determinar si una publicación tiene un tono positivo, negativo o neutral.

Análisis de Tópicos: (Potencialmente) Descubrir automáticamente los temas o asuntos más frecuentes tratados en las publicaciones.

Análisis de Idioma: (Potencialmente) Identificar qué idiomas predominan en las publicaciones y cómo varían según la fuente o el tema.

Análisis de Viralidad: (Potencialmente) Investigar qué tipo de contenido (por sentimiento, tema, etc.) tiende a ser más compartido o a generar mayor interacción.

Predicción
El enfoque principal de la predicción en este proyecto es:

Predicción de la Reacción (Sentimiento): Predecir el sentimiento (positivo, negativo, neutral) de una publicación en función del texto de su descripción.


|-- nombre_proyecto_final_ML
    |-- data
    |   |-- raw
    |   |-- processed
    |   |-- train
    |   |-- test
    |
    |-- notebooks
    |   |-- 
    |
    |-- src
    |   |-- processing.py
    |   |-- training.
    |   |-- evaluation.py
    |   |-- ...
    |
    |-- models
    |   |-- trained_model.pkl
    |   |-- model_config.yaml
    |   |-- ...
    |
    |-- app_streamlit
    |   |-- app.py
    |   |-- requirements.txt
    |   |-- ...
    |
    |-- docs
    |   |-- negocio.ppt
    |   |-- ds.ppt
    |   |-- memoria.md
    |   |-- ...
    |
    |
    |-- README.md

```

--Instala las siguientes bibliotecas de Python:
pip install datasets
pip install scikit-learn
pip install nltk
pip install pandas
pip install numpy


---

### **Fuente de Datos**
Los datos utilizados para este proyecto provienen del siguiente conjunto de datos de Hugging Face:

* **Dataset:** [Exorde/exorde-social-media-december-2024-week1](https://huggingface.co/datasets/Exorde/exorde-social-media-december-2024-week1)




