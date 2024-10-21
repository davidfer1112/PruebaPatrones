import pandas as pd
import os

# Rutas a los archivos de Excel
archivos = [
    r"D:/U/Semestre 8/Patrones/Prueba/Desarrollo/Capital.xlsx",
    r"D:/U/Semestre 8/Patrones/Prueba/Desarrollo/SUR.xlsx"
]

# Función para validar las columnas en Capital
def validar_datos_capital(df):
    errores = []
    
    # Validaciones para Capital
    df['PRIMER NOMBRE'] = df['PRIMER NOMBRE'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['SEGUNDO NOMBRE'] = df['SEGUNDO NOMBRE'].apply(lambda x: str(x) if isinstance(x, str) or pd.isna(x) else "Inválido")
    df['PRIMER APELLIDO'] = df['PRIMER APELLIDO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['SEGUNDO APELLIDO'] = df['SEGUNDO APELLIDO'].apply(lambda x: str(x) if isinstance(x, str) or pd.isna(x) else "Inválido")

    df['FECHA DE NACIMIENTO'] = df['FECHA DE NACIMIENTO'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df['FECHA DE NACIMIENTO'] = df['FECHA DE NACIMIENTO'].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['MEDICAMENTO ENTREGADO'] = df['MEDICAMENTO ENTREGADO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['FECHA DE ENTREGA'] = df['FECHA DE ENTREGA'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df['FECHA DE ENTREGA'] = df['FECHA DE ENTREGA'].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['MOTIVO DE ENTREGA'] = df['MOTIVO DE ENTREGA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['TIPO DE DOCUMENTO'] = df['TIPO DE DOCUMENTO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")

    # Validación de números de documento solo con dígitos
    df['NUMERO DE DOCUMENTO'] = df['NUMERO DE DOCUMENTO'].apply(lambda x: str(x) if isinstance(x, str) and x.isdigit() else "Inválido")

    df['DIRECCION RESIDENCIA'] = df['DIRECCION RESIDENCIA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['NOMBRE LOCALIDAD RESIDENCIA'] = df['NOMBRE LOCALIDAD RESIDENCIA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['NOMBRE DE SUBRED QUE ENTREGA'] = df['NOMBRE DE SUBRED QUE ENTREGA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")

    df['FECHA DE LA ORDEN MEDICA'] = df['FECHA DE LA ORDEN MEDICA'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df['FECHA DE LA ORDEN MEDICA'] = df['FECHA DE LA ORDEN MEDICA'].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['POBLACION PRIORIZADA'] = df['POBLACION PRIORIZADA'].apply(lambda x: str(x) if x in ['SI', 'NO'] else "Inválido")
    
    return df

# Función para validar las columnas en SUR
def validar_datos_sur(df):
    errores = []
    
    # Validaciones para SUR
    df['PRIMER NOMBRE'] = df['PRIMER NOMBRE'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['SEGUNDO NOMBRE'] = df['SEGUNDO NOMBRE'].apply(lambda x: str(x) if isinstance(x, str) or pd.isna(x) else "Inválido")
    df['PRIMER APELLIDO'] = df['PRIMER APELLIDO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['SEGUNDO APELLIDO'] = df['SEGUNDO APELLIDO'].apply(lambda x: str(x) if isinstance(x, str) or pd.isna(x) else "Inválido")
    
    # Verifica si la columna está nombrada correctamente
    if 'FECHA DE NACIMIEN' in df.columns:
        fecha_nacimiento_col = 'FECHA DE NACIMIEN'
    elif 'FECHA DE NACIMIENTO' in df.columns:
        fecha_nacimiento_col = 'FECHA DE NACIMIENTO'
    else:
        errores.append("Columna 'FECHA DE NACIMIEN' no encontrada")
        return errores
    
    df[fecha_nacimiento_col] = df[fecha_nacimiento_col].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df[fecha_nacimiento_col] = df[fecha_nacimiento_col].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['MEDICAMENTO ENTREGADO'] = df['MEDICAMENTO ENTREGADO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['FECHA DE ENTREGA'] = df['FECHA DE ENTREGA'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df['FECHA DE ENTREGA'] = df['FECHA DE ENTREGA'].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['MOTIVO DE ENTREGA'] = df['MOTIVO DE ENTREGA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['TIPO DE DOCUMENTO'] = df['TIPO DE DOCUMENTO'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")

    # Validación de números de documento solo con dígitos
    df['NUMERO DE DOCUMENTO'] = df['NUMERO DE DOCUMENTO'].apply(lambda x: str(x) if isinstance(x, str) and x.isdigit() else "Inválido")

    df['DIRECCION RESIDENCIA'] = df['DIRECCION RESIDENCIA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")
    df['NOMBRE LOCALIDAD RESIDENCIA'] = df['NOMBRE LOCALIDAD RESIDENCIA'].apply(lambda x: str(x) if isinstance(x, str) else "Inválido")

    df['FECHA DE LA ORDEN MEDICA'] = df['FECHA DE LA ORDEN MEDICA'].apply(lambda x: pd.to_datetime(x, format='%d/%m/%Y', errors='coerce'))
    df['FECHA DE LA ORDEN MEDICA'] = df['FECHA DE LA ORDEN MEDICA'].apply(lambda x: str(x) if pd.notna(x) else "Inválido")

    df['POBLACION PRIORIZADA'] = df['POBLACION PRIORIZADA'].apply(lambda x: str(x) if x in ['SI', 'NO'] else "Inválido")
    
    return df

# Procesamos los archivos
for archivo in archivos:
    print(f"Procesando {archivo}...")
    
    # Leer el archivo Excel
    df = pd.read_excel(archivo)
    
    # Verificar si es Capital o SUR
    if 'Capital' in archivo:
        df = validar_datos_capital(df)
    else:
        df = validar_datos_sur(df)
    
    # Guardamos los resultados corregidos en un nuevo archivo
    nombre_salida = archivo.replace('.xlsx', '_corregido.xlsx')
    df.to_excel(nombre_salida, index=False)
    print(f"Archivo corregido guardado como: {nombre_salida}")
