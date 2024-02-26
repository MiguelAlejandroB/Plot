import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Especifica el nombre del archivo Excel (si está en el mismo directorio que el script)
archivo_excel = "Datos Humedad Suelo ValleCauca y PuertoLopez 2024 Taller (1).xlsx"

# Lee el archivo Excel y carga los datos en un DataFrame de Pandas, saltando las tres primeras filas
df = pd.read_excel(archivo_excel, skiprows=2)
tiempo= df.iloc[:, 0]
precipitacion = df.iloc[:, 4]
humedad = df.iloc[:, 11]
# Crear la figura y los ejes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Graficar la humedad en el primer eje (izquierdo)
ax1.plot( tiempo,precipitacion, color='b', label='Precipitación (mm)')
ax1.set_xlabel('Precipitación (mm)')
ax1.set_ylabel('Tiempo (Cada 15 min)')
ax1.tick_params(axis='y')

# Crear un segundo eje para la humedad (derecho)
ax2 = ax1.twinx()
ax2.plot( tiempo,humedad, color='r', label='Humedad (%)')
ax2.set_ylabel('Humedad (%)')
ax2.tick_params(axis='y')

# Mostrar leyendas
fig.legend(loc="upper right")
# Guardar el plot en un archivo
plt.savefig('HumedadPrecipitacion.png')  # Cambia 'nombre_del_archivo.png' por el nombre que desees y la extensión adecuada
# Mostrar el gráfico
plt.show()



