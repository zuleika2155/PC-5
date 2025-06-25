import streamlit as st

# ==== CONFIGURACIÓN GENERAL ====
st.set_page_config(page_title="Portafolio de Zuleika", layout="wide")

# ==== DATOS ====
info = {
    "Pronoun": "ella",
    "Name": "Zuleika",
    "Full_Name": "Zuleika Maytte Napuri Chinga",
    "Intro": "✨ Comunicadora, publicista y apasionada por la creatividad, la tecnología y el impacto social ✨",
    "About": (
        "💖 ¡Hola! Soy Zuleika y me interesa crear experiencias significativas a través de la "
        "comunicación, el diseño y las herramientas digitales. Creo en el poder de las ideas y la "
        "innovación para transformar realidades. Este portafolio es un espacio para mostrar lo que hago, "
        "cómo pienso y lo que quiero seguir construyendo. 💡✨"
    ),
    "City": "🇵🇪 Lima, Perú",
    "Photo": "https://i.imgur.com/h1myKrJ.png",
    "Email": "zuleikanapuri8@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363/"
}

endorsements = {
    "img1": "https://i.imgur.com/Ijd7Kpf.jpeg",
    "img2": "https://i.imgur.com/RM31sfq.jpeg",
    "img3": "https://i.imgur.com/p1KQB0n.jpeg",
    "img4": "https://i.imgur.com/WvAF7Im.jpeg",
    "img5": "https://i.imgur.com/QZ2IEOo.jpeg"
}

# ==== ESTILOS PERSONALIZADOS ====
st.markdown("""
    <style>
        .stApp {
            background-color: #1b3a2a;  /* verde oscuro */
            color: #d4e9d4;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        h1, h2, h3, h4 {
            color: #a8d5a2;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .stSubheader, .stText, .stMarkdown {
            color: #c6e0b4;
        }
        a {
            color: #c1d9a4;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #e6f2d6;
        }
        hr {
            border: 1px solid #888;
            margin: 30px 0;
        }
        img {
            border-radius: 12px;
            margin: 10px 0;
        }
        .highlight-box {
            background-color: #2e5d36;
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        }
        .footer {
            font-size: 12px;
            color: #789262;
            text-align: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ==== CABECERA ====
st.markdown(f"<h1 style='text-align: center;'>{info['Full_Name']} 👩‍🎨</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center;'>{info['Intro']}</h4>", unsafe_allow_html=True)

# Imagen y texto ¡Hola! en columnas
col_img, col_text = st.columns([1, 1])
with col_img:
    st.image(info["Photo"], width=220)
with col_text:
    st.markdown("<h2 style='margin-top: 80px;'>¡Hola!</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px; max-width: 350px;'>{info['About']}</p>", unsafe_allow_html=True)
    st.markdown(f"[LinkedIn Perfil]({info['LinkedIn']})")

st.markdown("<hr>", unsafe_allow_html=True)

# ==== DETALLES DE CONTACTO ====
with st.container():
    st.subheader("📍 Datos de contacto")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"🌆 **Ciudad:** {info['City']}")
        st.markdown(f"📧 **Email:** [{info['Email']}](mailto:{info['Email']})")
    with col2:
        st.markdown("📞 **Teléfono:** +51 938 322 658")  # corregí paréntesis sobrante
        st.markdown("🌐 **Sitio web:** [www.zuleikaportfolio.com](#)")  # añadí url para que sea clickable

st.markdown("<hr>", unsafe_allow_html=True)

# ==== EXPERIENCIA ====
with st.container():
    st.subheader("💼 Experiencia laboral")
    with st.expander("Ver detalles"):
        st.write("""
        🔹 Asistente de comunicaciones en iniciativas culturales y sociales  
        🔹 Voluntariados en proyectos comunitarios de impacto social  
        🔹 Gestión de contenidos y diseño para redes sociales y campañas digitales  
        🔹 Coordinación de eventos y talleres de creatividad
        """)
    st.markdown('<div class="highlight-box"><strong>🎯 Objetivo profesional:</strong> Aplicar la comunicación estratégica, el diseño y la tecnología para impulsar proyectos con sentido, propósito e impacto positivo en la sociedad.</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==== HABILIDADES ====
with st.container():
    st.subheader("🧑‍💻 Habilidades")
    with st.expander("Ver habilidades técnicas y blandas"):
        st.write("""
        🔹 Comunicación estratégica  
        🔹 Creatividad publicitaria  
        🔹 Storytelling  
        🔹 Diseño gráfico, redacción y Canva  
        🔹 Manejo de herramientas digitales y redes sociales  
        🔹 Trabajo en equipo y liderazgo  
        🔹 Resolución de conflictos y adaptabilidad
        """)
    st.subheader("📚 Certificaciones")
    st.write("""
    🎓 Curso de Comunicación Digital en PUCP (2023)  
    🗓️ Certificación en Marketing y Comunicaciones con COREPUCP en la actualidad, puedes seguirnos en Instagram como COREPUCP <3
    """)

st.markdown("<hr>", unsafe_allow_html=True)

# ==== LOGROS ====
with st.container():
    st.subheader("🏆 Logros destacados")
    st.write("""
    🔹 Coordinó campañas universitarias con enfoque inclusivo y social.  
    🔹 Participó activamente en iniciativas estudiantiles que aumentaron el alcance cultural.  
    🔹 Reconocida por liderazgo en proyectos creativos con impacto comunitario.
    """)
    st.markdown('<div class="highlight-box"><strong>💡 Fortalezas:</strong> Empatía, creatividad, sensibilidad social y uso de herramientas comunicativas con propósito.</div>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-box"><strong>⚠️ Áreas de mejora:</strong> Exigente consigo misma, revisa mucho antes de compartir, lo que garantiza calidad y coherencia.</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==== GALERÍA ====
with st.container():
    st.subheader("🖼️ Testimonios visuales y trabajos.")
    cols = st.columns(5)
    cols[0].image(endorsements["img1"], use_column_width=True)
    cols[1].image(endorsements["img2"], use_column_width=True)
    cols[2].image(endorsements["img3"], use_column_width=True)
    cols[3].image(endorsements["img4"], use_column_width=True)
    cols[4].image(endorsements["img5"], use_column_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ==== CONTACTO FINAL ====
with st.container():
    st.subheader("📬 Disponibilidad")
    st.write("Abierta a nuevas oportunidades creativas, sociales o culturales con visión innovadora.")
    st.subheader("📄 Referencias")
    st.write("Referencias disponibles a solicitud. 😊")

# ==== FOOTER ====
st.markdown("""
    <div class="footer">
        &copy; 2025 Zuleika Maytte Napuri Chinga | Portafolio creado con Streamlit
    </div>
""", unsafe_allow_html=True)
