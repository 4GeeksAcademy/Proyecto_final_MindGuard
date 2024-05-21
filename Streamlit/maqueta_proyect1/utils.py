import streamlit as st
import pandas as pd
import numpy as np
import re
import requests
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch
import logging
from config import API_KEY, API_HOST
def obtener_datos_desde_api(link):
    try:
        # Verificar si el enlace es un enlace de Twitter y extraer el nombre de usuario
        pattern = r'https?://(?:mobile\.)?(?:x\.com|twitter\.com)/([^/?]+)'
        match = re.match(pattern, link)
        
        if not match:
            # Si el enlace no coincide con el patrón de Twitter, registrar un error y retornar None
            error_msg = "El enlace proporcionado no parece ser un enlace de perfil de Twitter."
            logging.error(error_msg)
            print(error_msg)
            return None
        
        username = match.group(1)
        print("Nombre de usuario:", username)
        
        # solicitud a la API
        url = "https://twitter154.p.rapidapi.com/user/tweets"
        querystring = {"username":username,"limit":100,"include_replies":"false","include_pinned":"false"}
        headers = {
            'X-RapidAPI-Key': API_KEY,
            'X-RapidAPI-Host': API_HOST
        }
        response = requests.get(url, headers=headers, params=querystring)
        respuesta = response.json()
        return respuesta
        
    except Exception as e:
        # Manejar cualquier error que ocurra durante la solicitud a la API
        error_msg = f"Error al obtener datos desde la API: {str(e)}"
        logging.error(error_msg)
        print(error_msg)
        return None


def procesar_texto(respuesta):
    try:
        if 'results' not in respuesta:
            # Si la etiqueta 'results' no está presente en la respuesta levantar una excepción
            raise ValueError("La etiqueta 'results' no está presente en la respuesta JSON. No se encontró el usuario en la API.")
        # Procesar los tweets obtenidos de la respuesta              
        tweets = respuesta['results']
        text_only_tweets = []
        for tweet in tweets:
            text_only_tweets.append({'text': tweet['text']})
        tweets = [tweet["text"] for tweet in text_only_tweets]
        tweets = [tweet.replace('\n', ' ') for tweet in tweets]
        tweets = ' '.join(tweets)
        # Definir la ruta al modelo BERT para tokenizar el texto
        modelo_path = 'model_bert1'
        tokenizer = BertTokenizer.from_pretrained(modelo_path)
        # Tokenizar el texto
        encoded_input = tokenizer(tweets, max_length=512, truncation=True, padding="max_length", return_tensors='pt')
        return encoded_input
    except Exception as e:
        # Registrar el error en el archivo de registro
        logging.error(f"Error al procesar el texto: {str(e)}")
        raise


def predict_result(encoded_input):
    # Cargar el modelo BERT
    modelo_path = 'model_bert1'
    model = BertForSequenceClassification.from_pretrained(modelo_path)
    # Realizar una predicción
    with torch.no_grad():
        outputs = model(**encoded_input)
    # Obtener logits
    logits = outputs.logits
  # Convertir logits a probabilidades (opcional)
    import torch.nn.functional as F
    probst = F.softmax(logits, dim=-1)
    #convertir tensor en lista y obtener la probabilidad de ser diagnosticado
    probs = probst.tolist()
    return probs[0][1]