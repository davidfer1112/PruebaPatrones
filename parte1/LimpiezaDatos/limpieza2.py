import pandas as pd
import os

# Definir la ruta absoluta del archivo de texto
ruta_archivo = 'D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/PROGRAMA_2.txt'

# Cargar el archivo TXT con separador '|' 
df = pd.read_csv(ruta_archivo, sep='|', header=0)

# Verificar que las columnas son correctas
columnas_esperadas = ["SEXO_BIOLOGICO", "LOCALIDAD", "EAPB", "FECHA_DE_NACIMIENTO", 
                      "PERTENENCIA_ETNICA", "SEXO_BIOLOGICO_1", "RIESGO_PSICOSOCIAL", 
                      "FECHA_DE_LA_CONSULTA", "TALLA"]

# Verificar si las columnas coinciden
if set(df.columns) != set(columnas_esperadas):
    print("Las columnas no coinciden con las esperadas.")
else:
    print("Las columnas son correctas.")

# Eliminar filas con datos faltantes
df = df.dropna(how='any')  # Elimina filas con cualquier dato faltante

# Limpiar la columna 'TALLA': eliminar caracteres no numéricos excepto el punto y convertir a enteros
df['TALLA'] = df['TALLA'].astype(str).str.replace(r'[^0-9]', '', regex=True).astype(float).astype('Int64')

# Verificar si alguna fila tiene más o menos columnas de las esperadas
df = df[df.apply(lambda row: len(row) == len(columnas_esperadas), axis=1)]

# Guardar el archivo limpio en formato .txt, manteniendo el separador '|'
df.to_csv('D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/archivo_limpio2.txt', 
          sep='|', index=False, quoting=3)  # quoting=3 asegura que no se agreguen comillas

print("Datos limpios y guardados en formato TXT.")
