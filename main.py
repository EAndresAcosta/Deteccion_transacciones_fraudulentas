import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Cargar el modelo y el scaler guardado
modelo = joblib.load("model/modelo_fraude.joblib")
scaler = joblib.load("model/scaler.joblib")

# Entrenar y ajustar el LabelEncoder si no lo tienes guardado
label_encoder = LabelEncoder()

# Ajustar el encoder con las categorías de 'tipo_tarjeta' que usaste al entrenar el modelo
label_encoder.fit(["Crédito", "Débito"])  # Ajusta con las categorías que tienes en tus datos de entrenamiento

# Guardar el LabelEncoder para futuras ejecuciones
#joblib.dump(label_encoder, "model/label_encoder.joblib")

# Crear el nuevo dato (ejemplo de transacción)
ejemplo_transaccion = {
    "monto_transaccion": 5000,
    "tipo_tarjeta": "Crédito",  # Valor categórico
    "hora": 23
}

# Paso 1: Codificar la variable categórica 'tipo_tarjeta'
ejemplo_transaccion['tipo_tarjeta'] = label_encoder.transform([ejemplo_transaccion['tipo_tarjeta']])[0]

# Paso 2: Asegúrate de que las columnas estén en el mismo orden que las del conjunto de entrenamiento
# Estas son las características que tu modelo y scaler esperan
columnas_esperadas = ['V4', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V2', 'V3', 'V7', 'V21', 'monto_transaccion', 'hora']

# Si el nuevo dato no tiene todas las columnas necesarias, completa con valores faltantes
# Asegúrate de tener todas las columnas en el DataFrame en el orden correcto
datos_nuevos = pd.DataFrame([ejemplo_transaccion])

# Asegurarse de que las columnas estén presentes en el DataFrame y en el orden correcto
# Crear las columnas faltantes con valor 0 si no están presentes
for columna in columnas_esperadas:
    if columna not in datos_nuevos.columns:
        datos_nuevos[columna] = 0

# Reordenar las columnas para que coincidan con las del entrenamiento
datos_nuevos = datos_nuevos[columnas_esperadas]

# Paso 3: Escalar las variables numéricas (si es necesario)
# Asegúrate de que las columnas numéricas estén correctamente escaladas
datos_nuevos[['monto_transaccion', 'hora']] = scaler.transform(datos_nuevos[['monto_transaccion', 'hora']])

# Paso 4: Hacer la predicción
prediccion = modelo.predict(datos_nuevos)

# Paso 5: Mostrar el resultado
resultado = "Fraude" if prediccion[0] == 1 else "No Fraude"
print(f"Resultado de la predicción: {resultado}")