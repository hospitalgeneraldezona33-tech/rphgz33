import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Identificador de Residuos Peligrosos del Hospital General de Zona No.33 del IMSS Nuevo León",
    page_icon="imss_icon.png",
    layout="centered"
)

# --- Título principal ---
st.title("🏥 Identificador de Residuos Peligrosos del Hospital General de Zona No.33 del IMSS Nuevo León")

st.write("""
Esta aplicación permite identificar los **Residuos Peligrosos Biológico-Infecciosos (RPBI)** conforme a la **NOM-087-SEMARNAT-SSA1-2002**
y los **Residuos Peligrosos** de acuerdo a la **NOM-052-SEMARNAT-2005**.  
Selecciona o busca el residuo para visualizar su información.
""")

# --- Diccionario RPBI según NOM-087 ---
RPBI_TIPOS = {
    "Sangre y derivados": {
        "clasificación": "Líquidos biológico-infecciosos",
        "contenedor": "Bolsa roja",
        "ejemplos": "Bolsas de transfusión, Muestras de sangre, Muestra de sangre, Bolsas de sangre, Bolsa de sangre, Sueros sanguíneos, Suero sanguíneo, Plasmas sanguíneos, Plasma sanguíneo, Concentrados plaquetarios, Concentrados de factores de coagulación, albúmina, Hemoderivados, Restantes de sangre coagulada, Restante de sangre coagulada, Residuos de transfusiones, Muestras hemolizadas, Sangre líquida residual, Producto hemático caducado, Fracciones plasmáticas, Tubos con sangre coagulada,  material con sangre fresca.",
        "imagen": "imagenes/sangre.png",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    },
    "Cultivos y cepas": {
        "clasificación": "Residuos patológicos y de laboratorio",
        "contenedor": "Bolsa roja o contenedor rígido rojo",
        "ejemplos": "Placas de Petri, medios de cultivo, Tubos de cultivo, Frascos de cultivo, Pipetas contaminadas, Puntas de micropipeta contaminadas, material de laboratorio contaminado.",
        "imagen": "imagenes/cultivos.png",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    },
    "Residuos no anatómicos": {
        "clasificación": "Material de curación contaminado",
        "contenedor": "Bolsa roja",
        "ejemplos": "Gasas, apósitos, guantes, sondas, catéteres contaminados, Jeringas sin aguja, Tubos de ensayo contaminados, Frascos de muestra contaminados, Batas desechables contaminadas, Gorros desechables contaminados, Cubrebotas contaminados, Campos quirúrgicos contaminados, Tubos de drenaje contaminados, Bolsas de suero vacías contaminadas, Filtros de respiradores contaminados,  .",
        "imagen": "imagenes/no_anatomicos.jpg",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    },
    "Residuos punzocortantes": {
        "clasificación": "Objetos cortantes o punzantes contaminados",
        "contenedor": "Contenedor rígido de color rojo",
        "ejemplos": "Agujas, bisturís, lancetas, hojas de afeitar, Agujas hipodérmicas, Aguja hipodérmica, Bisturís, Navajas, Vidrios rotos contaminados, láminas de microscopio, Capilares de vidrio contaminados.",
        "imagen": "imagenes/punzocortantes.png",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    },
    "Tejidos y órganos humanos": {
        "clasificación": "Residuos patológicos",
        "contenedor": "Bolsa amarilla",
        "ejemplos": "Piezas anatómicas, Tejidos humanos, riñón, riñónes, Hígado, útero, Miembros amputados, Miembro amputado, órganos, placenta, fragmentos óseos, Restos fetales, Producto de aborto, Fragmentos de tejidos extraídos.",
        "imagen": "imagenes/tejidos.png",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    },
    "Animales de experimentación": {
        "clasificación": "Residuos biológico-infecciosos animales",
        "contenedor": "Bolsa amarilla o contenedor rígido amarillo",
        "ejemplos": "Cadáveres o partes de animales utilizados en pruebas.",
        "imagen": "imagenes/animales.png",
        "norma": "NOM-087-SEMARNAT-SSA1-2002"
    }
}

# --- Diccionario Residuos Peligrosos NOM-052 ---
RESIDUOS_PELIGROSOS = {
    "Corrosivo": {
        "clasificación": "Sustancias que destruyen materiales o tejidos vivos por acción química.",
        "contenedor": "Envase resistente a la corrosión, perfectamente cerrado y etiquetado.",
        "ejemplos": "Ácidos, bases fuertes, limpiadores industriales, Ácidos clorhídricos usados, Ácidos sulfúricos residuales, Soluciones ácidas contaminadas, Hidróxidos de sodio residuales, Desincrustantes corrosivos, Detergentes alcalinos concentrados, Líquidos decapantes, Reactivos ácidos.",
        "imagen": "imagenes/corrosivo.png",
        "norma": "NOM-052-SEMARNAT-2005"
    },
    "Reactivo": {
        "clasificación": "Residuos que reaccionan violentamente al contacto con agua, aire u otras sustancias.",
        "contenedor": "Recipiente hermético y ventilado con etiqueta de reactivo.",
        "ejemplos": "Peróxidos, cianuros, materiales pirofóricos, Reactivos de laboratorio caducados, Nitratos inestables, Compuestos oxidantes, Mezclas químicas inestables.",
        "imagen": "imagenes/reactivo.png",
        "norma": "NOM-052-SEMARNAT-2005"
    },
    "Inflamable": {
        "clasificación": "Materiales que se encienden fácilmente por calor, fricción o chispas.",
        "contenedor": "Recipiente metálico cerrado o envase de seguridad para inflamables.",
        "ejemplos": "Solventes, alcoholes, trapos con aceite, estopas con aceite, gasolina, pinturas, Alcoholes etílicos residuales, Alcoholes isopropílicos usados, Éteres residuales, Tinners usados, Aceite lubricante usado.",
        "imagen": "imagenes/inflamable.png",
        "norma": "NOM-052-SEMARNAT-2005"
    },
    "Tóxico": {
        "clasificación": "Sustancias que pueden causar daño a la salud o al ambiente.",
        "contenedor": "Envase cerrado, etiquetado con símbolo de toxicidad.",
        "ejemplos": "Medicamentos caducos, balastras, cera gastada, lamparas fluorecentes, pesticidas, metales pesados, Medicamentos citotóxicos, Ampolletas contaminadas con medicamento, Soluciones con mercurio, Termómetro con mercurio roto, Pilas alcalinas usadas, Cartuchos de tóner usados, Materiales con plomo, Desinfectantes caducados, isolventes, Solución fijadora usada, Solución reveladora usada, Formaldehído residual, formol, Xileno usado, xilol, Cloro residual, Amoniaco residual, Solvente orgánico, Detergente químico concentrado.",
        "imagen": "imagenes/toxico.png",
        "norma": "NOM-052-SEMARNAT-2005"
    }
}

# --- Selección del tipo de residuo ---
st.subheader("🧩 Selecciona o busca el tipo de residuos")

tipo_residuo = st.radio(
    "Elige el tipo de residuos a identificar:",
    ("RPBI (NOM-087)", "Residuos Peligrosos (NOM-052)")
)

# --- Asignar diccionario según tipo ---
if tipo_residuo == "RPBI (NOM-087)":
    diccionario = RPBI_TIPOS
else:
    diccionario = RESIDUOS_PELIGROSOS

# --- Selector de residuo ---
opcion = st.selectbox("Selecciona un residuo:", ["--- Selecciona ---"] + list(diccionario.keys()))

# --- Buscador por palabra clave ---
st.markdown("### 🔍 Búsqueda por palabra clave")
busqueda = st.text_input("Escribe una palabra relacionada (ej. 'aguja', 'ácido', 'gasolina', 'placenta') y da click en el botón buscar")
buscar_boton = st.button("Buscar")

# Unificar ambos diccionarios para búsqueda general
TODOS_RESIDUOS = {**RPBI_TIPOS, **RESIDUOS_PELIGROSOS}

resultado_busqueda = None

if buscar_boton:
    if busqueda:
        for nombre, datos in TODOS_RESIDUOS.items():
            if (busqueda.lower() in nombre.lower()) or (busqueda.lower() in datos["ejemplos"].lower()):
                resultado_busqueda = (nombre, datos)
                break
        if not resultado_busqueda:
            st.error("🚫 No se encontró ningún resultado para la palabra ingresada, verifica la escritura u ortografia.")
    else:
        st.warning("Por favor, escribe una palabra antes de buscar.")

# --- Mostrar resultado del selector o búsqueda ---
if opcion != "--- Selecciona ---":
    datos = diccionario[opcion]
    st.success(f"**Residuo identificado:** {opcion}")
    st.image(datos["imagen"], width=1300)
    st.write(f"**Clasificación:** {datos['clasificación']}")
    st.write(f"**Contenedor recomendado:** {datos['contenedor']}")
    st.write(f"**Ejemplos:** {datos['ejemplos']}")
    st.info(f"**Norma aplicable:** {datos['norma']}")

elif resultado_busqueda:
    nombre, datos = resultado_busqueda
    st.success(f"**Resultado encontrado:** {nombre}")
    st.image(datos["imagen"], width=1300)
    st.write(f"**Clasificación:** {datos['clasificación']}")
    st.write(f"**Contenedor recomendado:** {datos['contenedor']}")
    st.write(f"**Ejemplos:** {datos['ejemplos']}")
    st.info(f"**Norma aplicable:** {datos['norma']}")

else:
    st.info("Selecciona un residuo o utiliza el buscador para iniciar la búsqueda.")

st.markdown("---")
st.caption("Desarrollado para fines educativos y de apoyo a la gestión ambiental del Hospital General de Zona No.33 del IMSS, Nuevo León.")
