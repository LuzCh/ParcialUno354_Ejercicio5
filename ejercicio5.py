# Cargar el dataset
import pandas as pd

# Cargar tu dataset
df = pd.read_csv('output_datos_normalizados.csv', encoding='ISO-8859-1')

# Definir las columnas a procesar
columnas = [2, 7, 8, 9, 10, 11, 12, 13, 14, 15]

columnas_n = ["Running time","Budget","Box Office","Actors Box Office %","Director Box Office %","Earnings","Oscar and Golden Globes nominations","Oscar and Golden Globes awards","Release year","IMDb score"]
# Definir el valor de penalización
l1_penalty = 0.1  
l2_penalty = 0.1  

l1_values = []
l2_values = []


# Recorrer las columnas especificadas
for col in columnas:
    data = df.iloc[:, col]

    # Calcular la penalización L1
    l1 = sum(abs(data)) + l1_penalty
    l1_values.append(l1)

    # Calcular la penalización L2
    l2 = sum(data ** 2) + l2_penalty
    l2_values.append(l2)

# Mostrar los resultados
cont = -1
for idx, col in enumerate(columnas):
    cont += 1
    print(f"Columna {col} - {columnas_n[cont]} - L1: {l1_values[idx]}, L2: {l2_values[idx]}")
