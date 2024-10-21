import pandas as pd
import os

# Definir la ruta absoluta del archivo de texto
ruta_archivo = 'D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/PROGRAMA_1.txt'

# Cargar el archivo TXT
df = pd.read_csv(ruta_archivo, sep=',', header=0, quotechar='"')

# Verificar que las columnas son correctas
columnas_esperadas = ["REGIMEN_DE_AFILIACION", "LOCALIDAD_CALCULADA", "ASEGURADOR", 
                      "FECHA_DE_NACIMIENTO_USUARIO", "SEXO", "FECHA_DE_LA_CONSULTA", "NACIONALIDAD"]

# Verificar si las columnas coinciden
if set(df.columns) != set(columnas_esperadas):
    print("Las columnas no coinciden con las esperadas.")
else:
    print("Las columnas son correctas.")

# Eliminar filas con datos faltantes
df = df.dropna(how='any')  # Elimina filas con cualquier dato faltante

# Eliminar filas que tengan más o menos columnas de las esperadas
df = df[df.apply(lambda row: len(row) == len(columnas_esperadas), axis=1)]

# Eliminar las comillas dobles de los datos
df.replace('"', '', regex=True, inplace=True)

# Guardar el archivo limpio en formato .txt, con escapechar
df.to_csv('D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/archivo_limpio_sin_comillas.txt', 
          sep=',', index=False, quoting=3, escapechar='\\')  # escapechar para manejar caracteres especiales

print("Datos limpios y guardados en formato TXT sin comillas.")

