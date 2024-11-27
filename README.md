# Taller_2_MLops
Desarrollo de Taller 2
Se eliguio esta datset de Kaggle https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset

1. Entendimiento de negocio:

Objetivo de negocio: Identificar los factores más influyentes en el rendimiento académico (GPA) para orientar estrategias educativas y políticas escolares.

Objetivo analítico: Construir un modelo predictivo para el GPA utilizando las variables proporcionadas, identificando relaciones significativas y generando insights accionables.



5. Evaluación:

Se tomaron estas dos metricas envase a la problematica :

El Error Absoluto Medio (MAE) es una métrica que nos indica, cuánto se desvían las predicciones del modelo respecto a los valores reales, expresandolo en las mismas unidades de la variable objetivo. Este indicador es útil para evaluar si el rango de error del modelo es aceptable para el problema que se está resolviendo debiod que es una clasificacion respecto a la nota si el MAE fuera muy grande , no podriamos clasificar bien a los estudiantes.

El Coeficiente de Determinación (R²) mide la proporción de la variabilidad en los datos que es explicada por el modelo. Un valor alto de R² sugiere que el modelo está capturando correctamente las tendencias y patrones de los datos, proporcionando predicciones confiables esto es super importante debido a que necesitamos asegurar que el modelo este prediciendo la nota corecta.

Con estas metricas se eleguio el el modelo Gradient Boosting Regressor (GBR) donde:

El modelo presenta el menor MAE (0.2750), lo que indica que sus predicciones están, en promedio, más cerca de los valores reales.
Esto se traduce en resultados más exactos y útiles para la toma de decisiones y su R² (0.7356) es el más alto, lo que significa que el modelo explica el 73.56% de la variabilidad de los datos.
Esto sugiere que el modelo tiene un excelente ajuste a los datos y puede generalizar bien bajo condiciones similares.




   
