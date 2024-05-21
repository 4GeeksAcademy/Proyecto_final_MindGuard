import base64
import streamlit as st
import pandas as pd
from utils import obtener_datos_desde_api
from utils import procesar_texto
from utils import predict_result
from streamlit_extras.mention import mention
from streamlit_extras.badges import badge
import logging
from streamlit_lottie import st_lottie

# Función para convertir una imagen a base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Obtener las imágenes como base64
img_2 = get_img_as_base64("imagenes/logo_def-removebg-preview.png")
titulo_img = get_img_as_base64("imagenes/nombre_def-removebg-preview.png")

# Estilo CSS para establecer imágenes de fondo
page_bg_img = f"""
    <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-color: white;
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
            color: black !important;
            font-size: 40px;
        }}
    </style>
    """
# Aplicar estilo de las imágenes de fondo
st.markdown(page_bg_img, unsafe_allow_html=True)
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
        <img src="data:image/png;base64,{img_2}" alt="Logo">
</div>
""", unsafe_allow_html=True)
col = st.sidebar.columns(1)
sd = col[0].container()
with sd:
    badge(type="github", name="Joel1695/Proyecto_Final")



# Título de la aplicación
# CSS para centrar la imagen
st.markdown("""
    <style>
    .title-text {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; 
        margin-bottom: 50px;
    }
    .title-text img {
        max-width: 50%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(f'<div class="title-text"><img src="data:image/png;base64,{titulo_img}" alt="Título"></div>', unsafe_allow_html=True)
    
# Mostrar una imagen
# Agregar el código HTML necesario para importar el reproductor Lottie y mostrar la animación
st.markdown("""
    <style>
    .responsive-lottie {
        width: 100%;
        max-width: 700px;
        height: auto;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

st_lottie_url = "https://lottie.host/842df2a3-1e63-4956-94e7-803bf87758e4/jk7TXnmkQM.json"
st_lottie_component = st_lottie(st_lottie_url, key="lottie")


# Entrada de texto para el enlace
enlace = st.text_input("Enter the link to get data", placeholder="e.g., https://x.com/user_handle")

# Estilo personalizado para el botón
st.markdown(
        """
    <style>
.stButton>button {
  background: #48C9B0; /* background color */
  color: #1ABC9C; /* font color */
  border: 2px solid #1ABC9C; /* border size and color */
  padding: 16px 20px;
  border-radius: 10px; /* round borders */
  position: relative;
  z-index: 1;
  overflow: hidden;
  display: block;
  margin: auto;
  transition: background-color 0.3s ease;
}
.stButton>button {
  background: darken(#48C9B0, 10%);
  color: #fff; /* hover font color */
}
.stButton>button::after {
  content: "";
  background: #1ABC9C; /* hover background color */
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

# Configurar logging para Streamlit
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()  # Esto mostrará el log en el output de Streamlit
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Botón para obtener datos y hacer predicción
if st.button("Get data and predict"):
    if enlace:
        try:
            # Obtener datos desde la API
            datos = obtener_datos_desde_api(enlace) 
            if datos is not None: 
                # Hacer la predicción con el modelo
                resultado_preprocesado = procesar_texto(datos)
                if resultado_preprocesado is not None:
                    resultado_prediccion = predict_result(resultado_preprocesado)
                    resultado_prediccion_porcentaje = round(resultado_prediccion * 100, 2)
                    # Código HTML para la barra de progreso constante con flecha móvil
                    progress_bar_html = f"""
                    <div style="width: 100%; background-color: #ddd; position: relative; height: 30px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                        <div style="width: 100%; height: 30px; background: linear-gradient(to right, #4caf50, #f44336); border-radius: 5px; position: relative;">
                            <span style="position: absolute; top: -25px; left: {resultado_prediccion_porcentaje - 2}%; color: #0F0F0F ; font-weight: bold; font-size: 20px;">{resultado_prediccion_porcentaje}%</span>
                            <div style="width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-top: 10px solid #000; position: absolute; left: {resultado_prediccion_porcentaje - 1}%; top: 30px;"></div>
                        </div>
                    </div>
                    """
                    st.markdown(progress_bar_html, unsafe_allow_html=True)
                    
                    
                    # Mostrar el resultado de la predicción
                    st.markdown(f"<p style='color: black;'>Prediction result:</p>", unsafe_allow_html=True)
                    if resultado_prediccion >= 0.84 :                       
                        st.markdown(f"""
                        <p style='color: black;'>
                            Based on the provided information, there is a <strong>very high probability</strong> that the individual may be experiencing symptoms of a <strong>mental disorder</strong>. We strongly recommend seeking professional advice from a mental health specialist. You can contact the National Institute of Mental Health (NIMH) for assistance.
                        </p>
                        """, unsafe_allow_html=True)
                        #Link y Num del NIMH
                        row = st.columns(2)
                        link1 = row[0].container()
                        with link1:
                            mention(
                            label="NIMH",
                            icon= "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/US-NIH-NIMH-Logo.svg/320px-US-NIH-NIMH-Logo.svg.png",
                            url="https://www.nimh.nih.gov/health",
                            )
                            mention(
                            label="1-866-615-6464 ",
                            icon= "https://cdn-icons-png.flaticon.com/512/724/724664.png",
                            url="tel:1-866-615-6464",
                            )
                    elif  0.68 <= resultado_prediccion < 0.84:
                        st.markdown(f"<p style='color: black;'>The provided information indicates a <strong>hight probability</strong> that the individual may have symptoms associated with a <strong>mental disorder</strong>. It may be beneficial to consult with a mental health professional for further evaluation. For assistance, consider reaching out to the National Institute of Mental Health (NIMH).", unsafe_allow_html=True)   
                        row = st.columns(2)
                        link1 = row[0].container()
                        with link1:
                            mention(
                            label="NIMH",
                            icon= "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/US-NIH-NIMH-Logo.svg/320px-US-NIH-NIMH-Logo.svg.png",
                            url="https://www.nimh.nih.gov/health",
                            )
                            mention(
                            label="1-866-615-6464 ",
                            icon= "https://cdn-icons-png.flaticon.com/512/724/724664.png",
                            url="tel:1-866-615-6464",
                            )
                    elif 0.50 <= resultado_prediccion < 0.68:
                        st.markdown(f"<p style='color: black;'>The results suggest a <strong>moderately high probability</strong> that the individual might be exhibiting symptoms of a <strong>mental disorder</strong>. Consider discussing these findings with a mental health professional to gain more insight. If needed, you can contact the National Institute of Mental Health (NIMH) for more information.</p>", unsafe_allow_html=True)  
                        row = st.columns(2)
                        link1 = row[0].container()
                        with link1:
                            mention(
                            label="NIMH",
                            icon= "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/US-NIH-NIMH-Logo.svg/320px-US-NIH-NIMH-Logo.svg.png",
                            url="https://www.nimh.nih.gov/health",
                            )
                            mention(
                            label="1-866-615-6464 ",
                            icon= "https://cdn-icons-png.flaticon.com/512/724/724664.png",
                            url="tel:1-866-615-6464",
                            )
                    elif 0.34 <= resultado_prediccion < 0.50:
                        st.markdown(f"<p style='color: black;'>There is a <strong>low probability</strong> that the individual may have symptoms of a <strong>mental disorder</strong> based on the provided information. However, if there are any concerns, seeking advice from a mental health professional could still be beneficial. For further guidance, you can contact the National Institute of Mental Health (NIMH).</p>", unsafe_allow_html=True)  
                        row = st.columns(2)
                        link1 = row[0].container()
                        with link1:
                            mention(
                            label="NIMH",
                            icon= "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/US-NIH-NIMH-Logo.svg/320px-US-NIH-NIMH-Logo.svg.png",
                            url="https://www.nimh.nih.gov/health",
                            )
                            mention(
                            label="1-866-615-6464 ",
                            icon= "https://cdn-icons-png.flaticon.com/512/724/724664.png",
                            url="tel:1-866-615-6464",
                            )
                    elif  resultado_prediccion < 0.34:
                        st.markdown(f"<p style='color: black;'>The provided information shows a <strong>very low probability</strong> that the individual is experiencing symptoms of a <strong>mental disorder</strong>. While this is a positive result, always prioritize mental health and consult a professional if there are any worries. If you have any questions, consider reaching out to the National Institute of Mental Health (NIMH).</p>", unsafe_allow_html=True)  
                        row = st.columns(2)
                        link1 = row[0].container()
                        with link1:
                            mention(
                            label="NIMH",
                            icon= "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/US-NIH-NIMH-Logo.svg/320px-US-NIH-NIMH-Logo.svg.png",
                            url="https://www.nimh.nih.gov/health",
                            )
                            mention(
                            label="1-866-615-6464 ",
                            icon= "https://cdn-icons-png.flaticon.com/512/724/724664.png",
                            url="tel:1-866-615-6464",
                            )    
                    # Mensaje de advertencia detallado
                    st.markdown("""
                    <div style="background-color: #ffffcc; padding: 10px; border-radius: 5px; font-size: 14px; color: black;">
                    
                    IMPORTANT!!!
                    
                    1. Not a medical diagnosis: The results provided by Mindguard do not constitute a medical diagnosis. This application is a data-based analysis and prediction tool and should not be used as a substitute for evaluation and diagnosis by a qualified mental health professional.
                    
                    2. Model limitations: Although our model has an accuracy of 84%, results should be interpreted with caution. Factors such as the nature of the tweet content and language peculiarities can affect prediction accuracy.
                    
                    3. Responsible use: The information obtained through this application should be used responsibly. No major decisions should be made based solely on the results provided by the application. If you have concerns about a user's mental health, we recommend seeking professional help. You will find official support and consultation links and phone numbers when you complete the analysis.
                    
                    4. Privacy and security: We respect user privacy. The data analyzed by the application is not stored or shared with third parties. Any private reference, phone number, or any other type of data is removed before the tweet is processed. Data security is a priority for us, and we take measures to ensure it is handled safely.
                    
                    5. Consent: By using this application, you confirm that you understand and accept these conditions. You also confirm that you have the consent of the user whose Twitter profile is being analyzed, if it is not your own account.
                    </div>
                    """, unsafe_allow_html=True)                    
                else:
                    st.warning("The data could not be processed for prediction.")
            else:
                st.warning("The provided link does not appear to be a Twitter profile link.")
        except Exception as e:
            # Registro de errores
            logging.error(f"Error al ejecutar la aplicación: {str(e)}")
            # Mensaje de error
            st.error(f"An error occurred while processing the request. Please check the link you are using or try again later.")                     
    else:
        st.warning("Please enter a valid link.")








