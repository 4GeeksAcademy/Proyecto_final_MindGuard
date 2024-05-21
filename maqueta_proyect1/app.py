import base64
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.badges import badge
from streamlit_extras.mention import mention
from streamlit_extras.keyboard_text import key
from streamlit_extras.keyboard_text import load_key_css
# Función para obtener una imagen en formato base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Función principal de la aplicación
def main():
    # Obtener las imágenes en formato base64
    img = get_img_as_base64("imagenes/side.jpg")
    img_2 = get_img_as_base64("imagenes/side.jpg")
    titulo_img = get_img_as_base64("imagenes/nombre_def-removebg-preview.png")  
    logo_img = get_img_as_base64("imagenes/logo_def-removebg-preview.png")

    # CSS para centrar el contenido en la barra lateral
    
    
    st.markdown("""
    <style>
    .sidebar-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 10px 0;
    }
    .sidebar-content img {
        max-width: 80%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    # Insertar el logo y el texto "Bienvenidos" en la parte superior de la barra lateral
    st.sidebar.markdown(f"""
    <div class="sidebar-content">
        <h2>Welcome</h2>
        <img src="data:image/png;base64,{logo_img}" alt="Logo">
    </div>
    """, unsafe_allow_html=True)
    col = st.sidebar.columns(1)
    sd = col[0].container()
    with sd:
        badge(type="github", name="Joel1695/Proyecto_Final")
        
    # Estilo de fondo para la página
    page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("data:image/png;base64,{img}");
            background-position: center; 
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-color: #1D8699;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }}
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}
        [data-testid="stToolbar"] {{
            right: 2rem;
        }}
        .stMarkdown {{
            color: white !important;
            font-size: 40px;
        }}
    </style>
    """
    # Renderizar el estilo de fondo y el título
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # CSS para centrar la imagen del título y ajustar el espaciado
    st.markdown("""
    <style>
    .title-text {
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
        margin-bottom: 40px; /* Ajustar espacio debajo del título */
    }
    .title-text img {
        max-width: 70%; /* Ajusta este valor según el tamaño deseado */
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="title-text"><img src="data:image/png;base64,{titulo_img}" alt="Title"></div>', unsafe_allow_html=True)
    
    # Definir el texto
    texto = """
    # Welcome to MindGuard

    This is a web application designed to analyze patterns of written expression on X (Twitter) and predict potential psychological disorders. 
    
    The goal is to detect signs of any kind of mental disorder early, so the user has this information to take action in the process of seeking professional help if necessary.
    
    Our artificial intelligence model has been trained with a dataset of over 3.5 million tweets and has an accuracy of 84%.

    ## How does it work?

    It's very simple. You just need to enter the Twitter account handle you are interested in into the text field and press the start analysis button.

    Our AI model will analyze the user's last 20 messages and, based on them, it will calculate the probability that the author of those messages may have some emotional disorder. 

    You will also find useful links to seek help and information if you need it.
    """
    # Usar HTML y CSS para centrar el contenido
    st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
        flex-direction: column;
        text-align: center;
        max-width: 800px;
        margin: auto;
        padding-bottom: 20px; /* Ajustar espacio debajo del texto */
    }
    </style>
    <div class="centered">
        """ + texto + """
    </div>
    """, 
    unsafe_allow_html=True
)
    # Personalizar el estilo del botón 
    st.markdown(
        """
    <style>
    .stButton>button {
    background: #48C9B0; /* color de fondo */
    color: #fff; /* color de fuente */
    border: 2px solid #1ABC9C; /* tamaño y color de borde */
    padding: 16px 20px;
    border-radius: 10px; /* redondear bordes */
    position: relative;
    z-index: 1;
    overflow: hidden;
    display: block;
    margin: 0 auto 10px; /* Ajustar espacio entre el botón y otros elementos */
    transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
    background: #1ABC9C; /* color de fondo al pasar el mouse */
    color: #fff; /* color de fuente al pasar el mouse */
    }
    .stButton>button::after {
    content: "";
    background: #1ABC9C; /* color de fondo hover */
    position: absolute;
    z-index: -1;
    padding: 16px 20px;
    display: block;
    top: 0;
    bottom: 0;
    left: -100%;
    right: 100%;
    -webkit-transition: all 0.35s;
    transition: all 0.35s;
    }
    .stButton>button:hover::after {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    -webkit-transition: all 0.35s;
    transition: all 0.35s;
    }
        </style>
        """,
            unsafe_allow_html=True,
        )
    
    # Botón para "Start Analysis" con estilo personalizado
    start_analysis_button = st.button("Start Analysis")

    # Si se presiona el botón, mostrar el contenido del análisis
    if start_analysis_button:
        analysis_page()
    


    st.markdown('<div class="centered-columns">', unsafe_allow_html=True)
    # Crear contenedores para menciones a LinkedIn
    row1 = st.columns(3)
    Celia = row1[1].container()
    Celia.markdown('<div style="color: white; font-size: 30px;">Celia García</div>', unsafe_allow_html=True)
    with Celia:
        mention(
        label="LinkedIn",
        icon= "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        url="https://www.linkedin.com/in/celia-garc%C3%ADa-gimeno-b03687152/",
    )
        mention(
        label="GitHub",
        icon="github",
        url="https://github.com/Celia-code13",
    )
    joel = row1[2].container()
    joel.markdown('<div style="color: white; font-size: 30px;">Joel De Andrade</div>', unsafe_allow_html=True)
    with joel:
        mention(
        label="LinkedIn",
        icon="https://cdn-icons-png.flaticon.com/512/174/174857.png",
        url="https://www.linkedin.com/in/joel-de-andrade-175663152/",
    )
        mention(
        label="GitHub",
        icon="github",
        url="https://github.com/Joel1695",
    )
    David = row1[0].container()
    David.markdown('<div style="color: white; font-size: 30px;">David González</div>', unsafe_allow_html=True)
    with David:
        mention(
        label="LinkedIn",
        icon="https://cdn-icons-png.flaticon.com/512/174/174857.png",
        url="https://www.linkedin.com/in/david-gonz%C3%A1lez-2535a62b1/",
    )
        mention(
        label="GitHub",
        icon="github",
        url="https://github.com/Dgasensi",
    )

def analysis_page():
    switch_page("predict_twitter")

if __name__ == "__main__":
    main()
    

