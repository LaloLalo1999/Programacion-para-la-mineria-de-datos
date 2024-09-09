import pandas as pd

# Nombre del archivo a procesar
filename = "datos_abiertos_2024_08.csv"

# Leer el archivo CSV
df = pd.read_csv(filename)

# Eliminar filas sin género asignado
df = df[df['Genero'].notna()]

# Cambiar rango de años de nacimiento "1995-1999" por "2022"
df.loc[df['Año_de_nacimiento'].isin(['1995', '1996', '1997', '1998', '1999']), 'Año_de_nacimiento'] = '2022'

# Guardar el archivo CSV procesado
df.to_csv("datos_procesados.csv", index=False)

print("El archivo 'datos_procesados.csv' ha sido generado con éxito.")