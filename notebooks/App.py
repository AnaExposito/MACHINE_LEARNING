import pickle
import streamlit as st
import pandas as pd
import os

st.title("Bienvenido al modelo de predicción de emociones")
st.markdown(
    """ 
Aquí podrás predecir las emociones de tus proximos post. Tus clientes estarán encantados con tus publicaciones! 
    """
)


if st.button("Send likes!"):
    st.balloons()

user_input = st.text_input('Introduce el texto de tu publicación')


@st.cache_resource
def load_model():
    modelo_path = "c:/Users/infoa/Documents/THE_BRIDGE/MACHINE_LEARNING/notebooks/random_forest_model.pkl"
    vectorizer_path = "c:/Users/infoa/Documents/THE_BRIDGE/MACHINE_LEARNING/notebooks/count_vectorizer.pkl"
    
    with open(modelo_path, 'rb') as f:
        model = pickle.load(f)
    with open(vectorizer_path, 'rb') as f:
        # Aquí también deberías cambiar el nombre de la variable para que no sea la ruta
        vectorizer = pickle.load(f) 
    return model, vectorizer

# Llama a la función load_model y asigna los resultados a variables accesibles
model, vectorizer = load_model()


if st.button('Enviar'):
    if user_input.strip():
        X = vectorizer.transform([user_input])
        prediction = model.predict(X)[0]
        st.success(f"Emoción predicha: **{prediction}**")
    else:
        st.warning("Por favor, introduce un texto para predecir.")