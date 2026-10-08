# Hugo Fabian NC = 0040
# NL = 17 Venado
import os
import cv2
import numpy as np

# Ruta del archivo
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "../imagenes/venado.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    exit()

# Preprocesamiento
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris_float = np.float32(gris)

# Detección de Harris
esquinas = cv2.cornerHarris(gris_float, 2, 3, 0.04)
esquinas = cv2.dilate(esquinas, None)

# Umbral 1: Bajo para obtener MUCHOS puntos
umbral = 0.005 * esquinas.max()

resultado = imagen.copy()
resultado[esquinas > umbral] = [0, 0, 255]  # Puntos Rojos

# Mostrar imagen original y resultado
cv2.imshow("Venado 0040 - Imagen Original", imagen)
cv2.imshow("Venado 0040 - Umbral 0.005 (Muchos Puntos)", resultado)

# Guardar
ruta_guardado = os.path.join(directorio_actual, "../resultados/esquinas_muchos.jpg")
os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)
cv2.imwrite(ruta_guardado, resultado)

cantidad_esquinas = np.sum(esquinas > umbral)
print("Detección terminada (Umbral 0.005).")
print("Puntos detectados:", cantidad_esquinas)
print("Hugo Fabian = 0040")

cv2.waitKey(0)
cv2.destroyAllWindows()

# Hugo Fabian NC = 0040
# NL = 17 Venado
import os
import cv2
import numpy as np

# Ruta del archivo
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "../imagenes/venado.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    exit()

# Preprocesamiento
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris_float = np.float32(gris)

# Detección de Harris
esquinas = cv2.cornerHarris(gris_float, 2, 3, 0.04)
esquinas = cv2.dilate(esquinas, None)

# Umbral 2: Medio para obtener PUNTOS MEDIOS
umbral = 0.05 * esquinas.max()

resultado = imagen.copy()
resultado[esquinas > umbral] = [0, 255, 0]  # Puntos Verdes

# Mostrar imagen original y resultado
cv2.imshow("Venado 0040 - Imagen Original", imagen)
cv2.imshow("Venado 0040 - Umbral 0.05 (Puntos Medios)", resultado)

# Guardar
ruta_guardado = os.path.join(directorio_actual, "../resultados/esquinas_medios.jpg")
os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)
cv2.imwrite(ruta_guardado, resultado)

cantidad_esquinas = np.sum(esquinas > umbral)
print("Detección terminada (Umbral 0.05).")
print("Puntos detectados:", cantidad_esquinas)
print("Hugo Fabian = 0040")

cv2.waitKey(0)
cv2.destroyAllWindows()

# Hugo Fabian NC = 0040
# NL = 17 Venado
import os
import cv2
import numpy as np

# Ruta del archivo
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "../imagenes/venado.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print(f"Error: no se pudo cargar la imagen desde: {ruta_imagen}")
    exit()

# Preprocesamiento
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris_float = np.float32(gris)

# Detección de Harris
esquinas = cv2.cornerHarris(gris_float, 2, 3, 0.04)
esquinas = cv2.dilate(esquinas, None)

# Umbral 3: Alto para obtener POCOS puntos
umbral = 0.15 * esquinas.max()

resultado = imagen.copy()
resultado[esquinas > umbral] = [255, 0, 0]  # Puntos Azules

# Mostrar imagen original y resultado
cv2.imshow("Venado 0040 - Imagen Original", imagen)
cv2.imshow("Venado 0040 - Umbral 0.15 (Pocos Puntos)", resultado)

# Guardar
ruta_guardado = os.path.join(directorio_actual, "../resultados/esquinas_pocos.jpg")
os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)
cv2.imwrite(ruta_guardado, resultado)

cantidad_esquinas = np.sum(esquinas > umbral)
print("Detección terminada (Umbral 0.15).")
print("Puntos detectados:", cantidad_esquinas)
print("Hugo Fabian = 0040")

cv2.waitKey(0)
cv2.destroyAllWindows()