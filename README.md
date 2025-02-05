# Deteccion_Transacciones_Fraudulentas

## 📝 Descripción
Este proyecto utiliza técnicas de ciencia de datos para identificar y prevenir transacciones fraudulentas. Aprovechamos algoritmos de aprendizaje automático para analizar patrones de datos y detectar actividades sospechosas.

## 📑 Tabla de Contenidos
- [Deteccion\_Transacciones\_Fraudulentas](#deteccion_transacciones_fraudulentas)
  - [📝 Descripción](#-descripción)
  - [📑 Tabla de Contenidos](#-tabla-de-contenidos)
  - [✨ Características](#-características)
  - [📊 Dataset](#-dataset)
  - [🔧 Tecnologías y Herramientas](#-tecnologías-y-herramientas)
        - [Lenguaje:](#lenguaje)
        - [Bibliotecas de Ciencia de Datos: *(Manipulación de datos)*](#bibliotecas-de-ciencia-de-datos-manipulación-de-datos)
        - [Modelado y evaluación de algoritmos:](#modelado-y-evaluación-de-algoritmos)
        - [Visualización de datos:](#visualización-de-datos)
        - [Modelos de Machine Learning:](#modelos-de-machine-learning)
  - [🚀 Cómo Usar](#-cómo-usar)
  - [📈 Resultados y Métricas](#-resultados-y-métricas)
    - [🔹 Matriz de Confusión](#-matriz-de-confusión)
    - [🔹 Reporte de Clasificación](#-reporte-de-clasificación)

## ✨ Características
- Identificación de patrones de fraude utilizando modelos de aprendizaje automático.
- Visualización de datos para análisis de patrones y tendencias.
- Sistema de alertas en tiempo real.
- Escalabilidad para grandes volúmenes de datos.   

## 📊 Dataset 
Este proyecto utiliza un conjunto de datos de transacciones financieras que contiene información sobre montos, ubicación, tipo de transacción, entre otros atributos. Los datos han sido preprocesados para eliminar valores nulos y sesgados.

**Fuente**: [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023)

**Tamaño**: [324mb]

**Columnas clave**: class, amount, etc.

**Etiquetas**: fraudulento **(1)** y no fraudulento **(0)**.

## 🔧 Tecnologías y Herramientas

Este proyecto ha sido desarrollado utilizando las siguientes tecnologías:

##### Lenguaje: 

[![My Skills](https://skillicons.dev/icons?i=python&theme=dark&perline=15)](https://docs.python.org/)

##### Bibliotecas de Ciencia de Datos: *(Manipulación de datos)*

[![My Skills](https://go-skill-icons.vercel.app/api/icons?i=pandas&theme=dark)](https://pandas.pydata.org/docs/)
[![My Skills](https://go-skill-icons.vercel.app/api/icons?i=numpy&theme=dark)](https://numpy.org/doc/)

##### Modelado y evaluación de algoritmos: 

[![My Skills](https://go-skill-icons.vercel.app/api/icons?i=scikitlearn&theme=dark)](https://scikit-learn.org/)

##### Visualización de datos: 

[![My Skills](https://go-skill-icons.vercel.app/api/icons?i=matplotlib&theme=dark)](https://matplotlib.org/stable/index.html)
[![My Skills](https://go-skill-icons.vercel.app/api/icons?i=seaborn&theme=dark)](https://seaborn.pydata.org/)

##### Modelos de Machine Learning: 

**Logistic Regression**

## 🚀 Cómo Usar
Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1️⃣ Clonar el repositorio
```bash
   git clone https://github.com/tu-usuario/proyecto-transacciones-fraudulentas.git
```
```bash
cd proyecto-transacciones-fraudulentas
```

2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv env
```
```bash
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

```bash
pip install -r requirements.txt
```

3️⃣ Ejecutar el modelo
```bash
python main.py
```

## 📈 Resultados y Métricas

El rendimiento del modelo fue evaluado utilizando diversas métricas para clasificación binaria. A continuación, se presentan los resultados obtenidos:

### 🔹 Matriz de Confusión

|   | Predicción No Fraude | Predicción Fraude |  
|---|---------------------|------------------|  
| **Real No Fraude (0)** | 55,638 | 1,225 |  
| **Real Fraude (1)** | 3,259 | 53,604 |  

### 🔹 Reporte de Clasificación

| Clase | Precisión | Recall | F1-score | Support |  
|---|---|---|---|---|  
| **No Fraude (0)** | 0.94 | 0.98 | 0.96 | 56,863 |  
| **Fraude (1)** | 0.98 | 0.94 | 0.96 | 56,863 |  
| **Accuracy** |  |  | **0.96** | 113,726 |  
| **Macro Avg** | 0.96 | 0.96 | 0.96 | 113,726 |  
| **Weighted Avg** | 0.96 | 0.96 | 0.96 | 113,726 |  

🔹 Área bajo la curva (AUC-ROC)
El AUC-ROC obtenido fue 0.9911, lo que indica un excelente rendimiento del modelo en la clasificación de transacciones fraudulentas.

📊 Además, se generaron gráficos como la curva ROC y la importancia de variables para una mejor interpretación del modelo.