
import pandas as pd
import mysql.connector

# Paso 1: Extract - Cargar el CSV
df = pd.read_csv("movilidad_san_salvador.csv")

# Paso 2: Transform - Validar y transformar los datos
df['fecha'] = pd.to_datetime(df['fecha'])
df['region'] = df['region'].str.title()  # Asegurar formato título

# Paso 3: Load - Cargar los datos a una base de datos MySQL (ejemplo)
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='tu_usuario',
        password='tu_contraseña',
        database='nombre_base_datos'
    )

    cursor = connection.cursor()

    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO movilidad (fecha, region, retail, grocery, parks, transit, workplace, residential)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['fecha'].date(), row['region'], row['retail'], row['grocery'],
            row['parks'], row['transit'], row['workplace'], row['residential']
        ))

    connection.commit()
    print("Datos insertados correctamente.")

except mysql.connector.Error as error:
    print(f"Error al conectar o insertar en la base de datos: {error}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
