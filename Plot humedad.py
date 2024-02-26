import pandas as pd

# Especifica el nombre del archivo Excel (si está en el mismo directorio que el script)
archivo_excel = "Datos Humedad Suelo ValleCauca y PuertoLopez 2024 Taller (1).xlsx"

# Lee el archivo Excel y carga los datos en un DataFrame de Pandas
data_frame = pd.read_excel(archivo_excel)

#print(data_frame.head())
