import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Laboratorio 2 - Análisis de Datos", layout="wide")

#VEHICULOS ELECTRICOS
st.title("Análisis de Vehículos Eléctricos")

#Csv cargado
df = pd.read_csv("Electric_Vehicle_Population-2.csv")

#Visualicaion principal
st.header("Lectura y Exploración Inicial")

# Número de filas y columnas
st.subheader("Dimensiones del Dataset")
st.write(f"Filas: {df.shape[0]}")
st.write(f"Columnas: {df.shape[1]}")

# Nombres de columnas
st.subheader("Columnas del Dataset")
st.write(df.columns.tolist())

# Primeras 6 filas
st.subheader("Primeras 6 Filas")
st.dataframe(df.head(6))

# Estadísticas generales
st.subheader("Estadísticas Generales")
st.dataframe(df.describe())

#ingresar nuevos vehiculos
st.header("Ingreso de Vehiculos Nuevos")
with st.form("nuevo_vehiculo"):
    city = st.text_input("Ciudad")
    model_year = st.number_input("Año del Modelo", 2000, 2025)
    make = st.text_input("Marca")
    model = st.text_input("Modelo")
    electric_type = st.text_input("Tipo de Vehículo Eléctrico")
    electric_range = st.number_input("Rango Eléctrico", 0.0)
    base_msrp = st.number_input("Precio Base", 0.0)
    submit = st.form_submit_button("Agregar Vehículo")
    if submit:
        nuevo_registro = {
            "City": city,
            "Model Year": model_year,
            "Make": make,
            "Model": model,
            "Electric_Vehicle_Type": electric_type,
            "Electric_Range": electric_range,
            "Base_MSRP": base_msrp
        }
        df.loc[len(df)] = nuevo_registro
        st.success("Vehículo agregado correctamente")

#filtraciones de datos
st.header("Filtrado de Datos")
# Filtro por año
st.subheader("Filtrar por Año del Modelo")
year_filter = st.slider(
    "Mostrar vehículos anteriores al año:",
    2000,
    2025,
    2015
)
filtered_year = df[df["Model Year"] < year_filter]
st.write(filtered_year)

# Filtro por precio
st.subheader("Filtrar por Precio Base")
price_filter = st.number_input(
    "Mostrar vehículos con precio menor a:",
    min_value=0.0,
    max_value=845000.0,
    value=50000.0
)
filtered_price = df[df["Base_MSRP"] < price_filter]
st.write(filtered_price)

#Rango electrico
st.header("Exploración Avanzada")

# Filtrar por rango electrico
def categoria_rango(rango):
    if rango < 100:
        return "Bajo"
    elif 100 <= rango <= 250:
        return "Medio"
    else:
        return "Alto"
df["RangoCategoria"] = df["Electric_Range"].apply(categoria_rango)

# Conteo por categoría
st.subheader("Conteo por Categoría")
conteo = df["RangoCategoria"].value_counts()
st.write(conteo)

# Grafica
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
conteo.plot(kind="bar", ax=ax)
ax.set_title("Cantidad de Vehículos por Categoría")
ax.set_xlabel("Categoría")
ax.set_ylabel("Cantidad")
st.pyplot(fig)

#analisis de agrupacion
st.subheader("Análisis Agrupado")

agrupado = df.groupby("RangoCategoria").agg({
    "Base_MSRP": "mean",
    "Model Year": "mean",
    "Electric_Range": "std"
})
st.dataframe(agrupado)

#guardado de datos
st.header("Guardar Resultados")
if st.button("Guardar CSV Vehiculo Actualizado"):
    df.to_csv(
        "Electric_Vehicle_Population_Actualizado.csv",
        index=False
    )
    st.success("Archivo guardado correctamente")


#GYMNACIO
st.title("Analisis de Gymnacio")

#Csv cargado
df = pd.read_csv("GymExerciseTracking.csv")

#Visualicaion principal
st.header("Lectura y Exploración Inicial")

# Número de filas y columnas
st.subheader("Dimensiones del Dataset")
st.write(f"Filas: {df.shape[0]}")
st.write(f"Columnas: {df.shape[1]}")

# Nombres de columnas
st.subheader("Columnas del Dataset")
st.write(df.columns.tolist())

# Primeras 6 filas
st.subheader("Primeras 6 Filas")
st.dataframe(df.head(6))

# Estadísticas generales
st.subheader("Estadísticas Generales")
st.dataframe(df.describe())

#Ingreso de datos
st.header("Ingreso de Personas Nuevas")
with st.form("nuevo_usuario"):
    age = st.number_input("Edad", 10, 100)
    gender = st.selectbox(
        "Género",
        ["Male", "Female"]
    )
    weight = st.number_input("Peso (kg)", 0.0)
    height = st.number_input("Altura (m)", 0.0)
    max_bpm = st.number_input("Max BPM", 0)
    avg_bpm = st.number_input("Average BPM", 0)
    resting_bpm = st.number_input("Resting BPM", 0)
    session_duration = st.number_input(
        "Duración de Sesión",
        0.0
    )
    calories = st.number_input(
        "Calorías Quemadas",
        0.0
    )
    workout_frequency = st.number_input(
        "Frecuencia de Ejercicio",
        0
    )
    fat_percentage = st.number_input(
        "Porcentaje de Grasa",
        0.0,
        100.0
    )
    water_intake = st.number_input(
        "Consumo de Agua",
        0.0
    )
    experience_level = st.number_input(
        "Nivel de Experiencia",
        1,
        10
    )
    bmi = st.number_input("BMI", 0.0)

    submit = st.form_submit_button(
        "Agregar Registro"
    )
    if submit:
        nuevo_registro = {
            "Age": age,
            "Gender": gender,
            "Weight (kg)": weight,
            "Height (m)": height,
            "Max_BPM": max_bpm,
            "Avg_BPM": avg_bpm,
            "Resting_BPM": resting_bpm,
            "Session_Duration (hours)": session_duration,
            "Calories_Burned": calories,
            "Workout_Frequency (days/week)": workout_frequency,
            "Fat_Percentage": fat_percentage,
            "Water_Intake (liters)": water_intake,
            "Experience_Level": experience_level,
            "BMI": bmi
        }
        df.loc[len(df)] = nuevo_registro
        st.success("Registro agregado correctamente")

st.header("Filtrado de Datos")

# Filtro calorías
st.subheader(
    "Filtrar por Calorías Quemadas"
)
calories_filter = st.number_input(
    "Mostrar registros con calorías mayores o iguales a:",
    min_value=0.0,
    value=300.0
)
filtered_calories = df[
    df["Calories_Burned"] >= calories_filter
]
st.dataframe(filtered_calories)

# Filtro grasa corporal
st.subheader(
    "Filtrar por Porcentaje de Grasa"
)
fat_filter = st.slider(
    "Mostrar registros con grasa corporal menor o igual a:",
    0.0,
    100.0,
    30.0
)
filtered_fat = df[
    df["Fat_Percentage"] <= fat_filter
]
st.dataframe(filtered_fat)

#Exploracion de frecuencia
st.header("Exploración Avanzada")

# Nueva variable categórica
def frecuencia_categoria(frecuencia):
    if frecuencia < 3:
        return "Baja"
    elif 3<=frecuencia<=5:
        return "Moderada"
    else:
        return "Alta"
    
df["NivelFrecuencia"] = df[
    "Workout_Frequency (days/week)"
].apply(frecuencia_categoria)

# Conteo por categoría
st.subheader("Conteo por Categoría")
conteo = df["NivelFrecuencia"].value_counts()
st.write(conteo)

#Grafica de barras
st.subheader("Gráfico de Barras")
fig, ax = plt.subplots()
conteo.plot(kind="bar", ax=ax)
ax.set_title(
    "Cantidad de Usuarios por Frecuencia"
)
ax.set_xlabel("Nivel de Frecuencia")
ax.set_ylabel("Cantidad")
st.pyplot(fig)

#agrupacion
st.subheader("Análisis Agrupado")
agrupado = df.groupby(
    "NivelFrecuencia"
).agg({
    "Session_Duration (hours)": "mean",
    "Experience_Level": "mean",
    "BMI": "std"
})
st.dataframe(agrupado)

#Guardado de datos
st.header("Guardar Resultados")
if st.button("Guardar CSV Gym Actualizado"):
    df.to_csv(
        "GymExerciseTracking_Actualizado.csv",
        index=False
    )
    st.success(
        "Archivo guardado correctamente"
    )


#STEAM
st.title("Análisis Steam 2024")
df = pd.read_csv("steam_store_data_2024.csv")

df.columns = df.columns.str.strip().str.lower()
st.write("Columnas detectadas:")
st.write(df.columns)

#Desencriptado de precio
col_precio = None
for col in df.columns:
    if "price" in col:
        col_precio = col
        break
if col_precio is None:
    st.error("No se encontró columna de precio")
    st.stop()
df[col_precio] = df[col_precio].astype(str)
df[col_precio] = df[col_precio].replace('[\$,]', '', regex=True)
df[col_precio] = pd.to_numeric(df[col_precio], errors="coerce")

#desencriptacion de descuento
col_desc = None
for col in df.columns:
    if "salepercentage" in col:
        col_desc = col
        break
if col_desc is not None:
    df[col_desc] = df[col_desc].astype(str)
    df[col_desc] = df[col_desc].replace('%', '', regex=True)
    df[col_desc] = pd.to_numeric(df[col_desc], errors="coerce")
    df[col_desc] = df[col_desc].abs()
else:
    st.warning("No se encontró columna de descuento, se omitirá filtro")
    df["discount_fake"] = 0
    col_desc = "discount_fake"

#Primeras 6 filas
st.subheader("Primeras 6 filas")
st.write(df.head(6))

#estadistica
st.subheader("Estadísticas Generales")
st.dataframe(df.describe())

#Ingreso de datos
st.subheader("Ingreso de nuevo videojuego")
nombre = st.text_input("Nombre del juego")
precio = st.number_input("Precio", min_value=0.0)
descuento = st.number_input("Porcentaje de descuento", min_value=0.0, max_value=100.0)
if st.button("Agregar juego"):
    nuevo = {
        "name": nombre,
        col_precio: precio,
        col_desc: descuento
    }
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    st.success("Juego agregado correctamente")

#Filtros
st.subheader("Filtros")
precio_filtro = st.number_input("Precio mayor a:", 0.0)
st.dataframe(df[df[col_precio] > precio_filtro])
descuento_filtro = st.number_input("Descuento menor a:", 0.0)
st.dataframe(df[df[col_desc] < descuento_filtro])

#Categorias
def clasificar(p):
    if pd.isna(p):
        return "Desconocido"
    elif p < 10:
        return "Baja"
    elif p <= 24:
        return "Media"
    else:
        return "Alta"
df["gamajuego"] = df[col_precio].apply(clasificar)
conteo = df["gamajuego"].value_counts()
st.write(conteo)
fig, ax = plt.subplots()
conteo.plot(kind="bar", ax=ax)
ax.set_title("Gama de juegos")
st.pyplot(fig)

#Agrupacion
st.subheader("Análisis agrupado")
st.write(df.groupby("gamajuego").agg({
    col_precio: ["mean", "std"],
    col_desc: "mean"
}))

#Guardar csv
if st.button("Guardar CSV steam"):
    df.to_csv("steam_store_data_2024_Actualizado.csv", index=False)
    st.success("Guardado correctamente")


#NETFLIX
st.title("Análisis de Netflix")

#Cargar scv
df = pd.read_csv("netflix_titles.csv")
st.subheader("Exploración inicial")

#exploracion
st.write("Filas y columnas:", df.shape)
st.write("Columnas:")
st.write(df.columns.tolist())

#primeras 6 filas
st.write("Primeras 6 filas:")
st.dataframe(df.head(6))

#estadistica general
st.write("Estadísticas:")
st.write(df.describe())

#Desencriptacion de la duracion
df["duration"] = df["duration"].fillna("").astype(str)

#extraer minutos
df["minutes"] = df["duration"].str.extract(r'(\d+)\s*min')
df["minutes"] = pd.to_numeric(df["minutes"], errors="coerce")

# Extraer temporadas
df["seasons"] = df["duration"].str.extract(r'(\d+)\s*Season')
df["seasons"] = pd.to_numeric(df["seasons"], errors="coerce")

# Convertir fecha
df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')
df["year_added"] = df["date_added"].dt.year

#Ingreso nuevo
st.subheader("Agregar nuevo contenido")

titulo = st.text_input("Título")
tipo = st.selectbox("Tipo", ["Movie", "TV Show"])
duracion = st.number_input("Duración (minutos)", min_value=1)
rating = st.text_input("Clasificación (Ej: PG, R, TV-MA)")
anio = st.number_input("Año agregado", min_value=1900, max_value=2026)

if st.button("Agregar contenido"):
    nuevo = {
        "title": titulo,
        "type": tipo,
        "duration": duracion,
        "rating": rating,
        "year_added": anio
    }
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    st.success("Contenido agregado")

#Filtros
st.subheader(" Filtros")

duracion_filtro = st.number_input("Mostrar contenido con duración mayor a: (en minutos)")
df_duracion = df[df["minutes"] > duracion_filtro]
st.write("Resultados:")
st.dataframe(df_duracion)

anio_filtro = st.number_input("Mostrar contenido antes del año:")
df_anio = df[df["year_added"] < anio_filtro]
st.write("Resultados:")
st.dataframe(df_anio)

#Exploraciono avanzada
st.subheader("Exploración avanzada")

def clasificar_audiencia(r):
    if r in ["G", "TV-Y", "TV-G", "TV-Y7", "TV-Y7-FV"]:
        return "Niños"
    elif r in ["PG", "TV-PG"]:
        return "Adolescentes"
    elif r in ["PG-13", "TV-14"]:
        return "Adultos Jóvenes"
    elif r in ["R", "TV-MA", "NC-17"]:
        return "Adultos"
    else:
        return "Otro"

df["TipoAudiencia"] = df["rating"].apply(clasificar_audiencia)

# Conteo
conteo = df["TipoAudiencia"].value_counts()
st.write("Conteo por categoría:")
st.write(conteo)

# Gráfico
fig, ax = plt.subplots()
conteo.plot(kind="bar", ax=ax)
ax.set_title("Contenido por tipo de audiencia")
ax.set_xlabel("Audiencia")
ax.set_ylabel("Cantidad")
st.pyplot(fig)

#Analisis de agrupacion
st.subheader("Análisis agrupado")

# Asegurar que rating existe
if "rating" not in df.columns:
    st.error("No existe la columna rating")
    st.stop()

df["tipoaudiencia"] = df["rating"].apply(clasificar_audiencia)

# Verificar que sí existe
agrupado = df.groupby("tipoaudiencia").agg({
    "minutes": "mean",
    "type": lambda x: x.mode()[0] if not x.mode().empty else "N/A"
})
st.write(agrupado)

#Guardado de csv
st.subheader("Guardar resultados")

if st.button("Guardar csv Netflix "):
    df.to_csv("netflix_titles_Actualizado.csv", index=False)
    st.success("Archivo guardado correctamente")
