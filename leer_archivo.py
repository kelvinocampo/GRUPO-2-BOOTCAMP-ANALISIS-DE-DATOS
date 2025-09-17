import pandas as pd
import os

def leer_archivo(ruta_archivo: str):
    # Verificar que el archivo existe
    if not os.path.exists(ruta_archivo):
        print(f"❌ El archivo no existe: {ruta_archivo}")
        return None

    # Detectar la extensión
    extension = os.path.splitext(ruta_archivo)[1].lower()

    try:
        if extension == ".csv":
            df = pd.read_csv(ruta_archivo)
        elif extension in [".xls", ".xlsx"]:
            df = pd.read_excel(ruta_archivo)
        elif extension == ".json":
            df = pd.read_json(ruta_archivo)
        else:
            print(f"⚠️ Tipo de archivo no soportado: {extension}")
            return None

        # Mostrar solo las primeras 10 filas
        print(df.head(10))
        return df

    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None