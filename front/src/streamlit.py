import streamlit as st
import requests

st.title('Hello World App')

# Faire une requête GET vers l'API backend
try:
    response = requests.get('http://localhost:8000/hello')
    if response.status_code == 200:
        result = response.json()
        st.write(f'Réponse de l\'API : {result}')
    else:
        st.error(f'Erreur lors de la requête : {response.status_code}')
except requests.exceptions.RequestException as e:
    st.error(f'Erreur de connexion : {str(e)}')
