import pandas as pd

# Definir la ruta del archivo
ruta_archivo = 'D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/PROGRAMA_4.txt'

# Cargar el archivo TXT con separador '|'
df = pd.read_csv(ruta_archivo, sep='|', header=0)

# Verificar si las columnas son las esperadas
columnas_esperadas = ["LOCALIDAD_FIC", "ESTADO_CIVIL_", "NOMBRE_EAPB_", 
                      "FECHA_DE_NACIMIENTO_", "ETNIA_", "SEXO_", "FECHA_INTERVENCION"]

if set(df.columns) != set(columnas_esperadas):
    print("Las columnas no coinciden con las esperadas.")
else:
    print("Las columnas son correctas.")

# Reemplazar fechas vacías con un valor por defecto, por ejemplo, '0000-00-00'
df['FECHA_DE_NACIMIENTO_'] = df['FECHA_DE_NACIMIENTO_'].fillna('0000-00-00').astype(str)
df['FECHA_INTERVENCION'] = df['FECHA_INTERVENCION'].fillna('0000-00-00').astype(str)

# Guardar el archivo limpio
df.to_csv('D:/U/Semestre 8/Patrones/Prueba/Desarrollo/parte1/LimpiezaDatos/data/archivo_limpio4.txt', 
          sep='|', index=False, quoting=3, escapechar='\\')

print("Datos limpios y guardados en formato TXT.")
