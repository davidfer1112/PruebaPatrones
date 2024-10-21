import pandas as pd

# Cargar el archivo TXT con separador de tabulaciones
ruta_archivo = 'C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/POBLACION.txt'
df = pd.read_csv(ruta_archivo, sep='\t', header=0)

# Verificar si todas las filas tienen la cantidad correcta de columnas
columnas_esperadas = ["Localidad", "Sexo", "Edad", "Programa", "EAPB", "Fecha_Atencion"]
if set(df.columns) != set(columnas_esperadas):
    print("Las columnas del archivo no coinciden con las esperadas.")
else:
    print("Las columnas son correctas.")

# Eliminar filas con datos faltantes
df = df.dropna(how='any')  # Elimina filas con cualquier dato faltante

# Verificar si hay filas con menos o más columnas de las esperadas
df = df[df.apply(lambda row: len(row) == len(columnas_esperadas), axis=1)]

# Guardar el archivo limpio en formato .txt
df.to_csv('C:/ProgramData/MySQL/MySQL Server 9.0/Uploads/POBLACION_limpio.txt', sep='\t', index=False)

print("Archivo limpio guardado como POBLACION_limpio.txt")
