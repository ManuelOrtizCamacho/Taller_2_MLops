# Taller_2_MLops
Desarrollo de Taller 2
Se eliguio esta datset de Kaggle https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset

1. Entendimiento de negocio:

Objetivo de negocio: Identificar los factores más influyentes en el rendimiento académico  para orientar estrategias educativas y políticas escolares.

Objetivo analítico: Construir un modelo predictivo para el GPA utilizando las variables proporcionadas, identificando relaciones significativas y generando insights accionables.


3.

Transformaciones para Variables de Entrada
Normalización y Estandarización:

Normalización: Escala los datos para que estén en un rango fijo.
Estandarización: Escala los datos para que tengan media 0 y desviación estándar 1

Imputación de Valores Faltantes:

Media, Mediana o Moda: Sustituye valores nulos según el tipo de datos.
Imputación con Modelos: Utiliza modelos predictivos para estimar valores faltantes.

Transformaciones para la Variable de Salida 
En problemas de clasificación como este, las transformaciones de la variable objetivo pueden ser menos comunes, pero hay casos en los que son necesarias:

Conversión a Categórica:

Si la variable objetivo es numérica, puede ser necesario convertirla a categorías utilizando buckets o reglas específicas.


Como usamos pycaret, podemos configurar todas esta trasformacion desde el setup.

Imputación de Valores Faltantes (SimpleImputer)
Eliminación de Multicolinealidad

5. Evaluación:



Evaluación del Modelo Seleccionado: Gradient Boosting Classifier (GBC)

El modelo seleccionado, Gradient Boosting Classifier (GBC), fue elegido considerando métricas clave que reflejan su capacidad para realizar predicciones precisas y equilibradas:

Precisión (Accuracy):
El modelo alcanzó una precisión de 92.17%, lo que significa que predice correctamente el 92.17% de los casos. Este alto valor indica que el modelo es confiable en términos de desempeño general.

F1-Score:
El F1-Score es 91.96%, lo que demuestra un balance óptimo entre precisión (Precision) y recuperación (Recall). Esta métrica es especialmente importante cuando es crucial minimizar tanto los falsos positivos como los falsos negativos, como en el caso de clasificar correctamente a los estudiantes en sus categorías de desempeño.

Recuperación (Recall):
Con un valor de 92.17%, el modelo identifica correctamente la mayoría de los casos positivos. Esto asegura que la mayoría de las categorías de notas están siendo capturadas adecuadamente.

El modelo Gradient Boosting Classifier ofrece resultados sólidos y equilibrados, lo que lo hace ideal para su uso en el contexto educativo. Su precisión, combinada con el excelente desempeño en F1-Score y Recall, lo convierte en una herramienta valiosa para clasificar a los estudiantes según su desempeño. Esto puede ser útil para:

Identificar estudiantes con bajo rendimiento para ofrecer apoyo.
Optimizar estrategias pedagógicas basadas en predicciones confiables.


imagenes del la API

Desde telefono 
![image](https://github.com/user-attachments/assets/539e43c5-ef54-4124-80bc-a4e8e52ed45b)
desde pc 






Automatizar procesos de análisis académico.
   
