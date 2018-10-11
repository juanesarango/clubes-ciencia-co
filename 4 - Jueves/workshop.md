# Análisis de Tendencias

Según este artículo, de [FiveThirtyEigth](https://fivethirtyeight.com/features/how-fast-youll-abandon-your-new-years-resolutions/), las personas que se proponen resoluciones de año tienden a perder rápido sus objetivos:

![](https://fivethirtyeight.com/wp-content/uploads/2014/12/chalabi-new-year-datalab-chart-1.png?w=1150)

## Objetivo

El objetivo de este taller es analizar como es este comportamiento en los colombianos 🇨🇴.

Vamos a utilizar [**Google Trends**](https://trends.google.com), que es un recurso que nos muestra los intereses de los usuarios según las búsquedas que realizan en google de Palabras Claves.

Estos datos pueden ser visualizados por regiones y por temporadas en el tiempo.

Para este ejercicio visualizaremos cómo los colombianos han mostrado interés a través del tiempo por palabras claves como:

* gimnasio 🏋  
* dieta 🍏
* finanzas 💵

Por lo general estas palabras están relacionadas con objetivos que las personas se ponen como resoluciones de principio de año para mejorar aspectos de su estilo de vida.

## Tutorial


### Importart Datos en Python 

Primero obtenemos los datos de Google Trends:

https://trends.google.com/trends/explore?date=all&q=diet,gym,finance

Importamos las librerias de python:

```python
# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set()
```

Importar el archivo de texto en python como una dataframe (tabla)

```python
df = pd.read_csv('data/multiTimeline.csv', skiprows=1)
df.head()
```

Para ver información sobre los datos tabulados:

```python
df.info()
```

### Arreglar los datos

Limpiar el nombre de columnas para que tengan nombres sin espacios en blanco:

```python
df.columns = ['month', 'diet', 'gym', 'finance']
df.head()
```

Como `month` sale como tipo de dato `Object`, la idea es convertirlo en tipo `DateTime` que es el usado para tiempos. Y volver dicha columna como el índice:

```python
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
df.head()
```

### Análisis de Datos

```python
df.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);
```
*Tener en cuenta que los números son relativos. Si muestra 100 indica que es el momento más popular. Si muestra 4 quiere decir que es 4% tan popular como lo fue en su mayor momento.*


```python
df[['diet']].plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20)
```

Ahora para analizar las tendencias y las líneas de tiempo