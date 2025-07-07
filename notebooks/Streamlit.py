
import pickle
import streamlit as st
import pandas as pd


import streamlit as st

st.title("Bienvenido al modelo de predicción de emociones")
st.markdown(
    """ 
Aquí podrás predecir las emociones de tus proximos post. Tus clientes estarán encantados con tus publicaciones! 
    """
)



if st.button("Send likes!"):
    st.balloons()

st.text_input('Introduce el texto de tu publicación')
st.button ('enviar')


with open('random_forest_model.pkl', 'rb') as f:
    model_rf_loaded = pickle.load(f)

with open('count_vectorizer.pkl', 'rb') as f:
    vectorizer_loaded = pickle.load(f)
print("Modelo y vectorizador cargados con éxito.")