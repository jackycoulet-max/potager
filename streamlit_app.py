import streamlit as st
from google import genai

API_KEY = "AQ.Ab8RN6Lnccde43LWZ1qBcksx6YgkqYB7cEigTnsSYx-gftlMNg"

st.title("Le Potager Jurassien")
st.write("Bienvenue Jacky !")

mois = st.selectbox("Mois :", ["Mai", "Juin", "Juillet", "Août", "Septembre"])
legume = st.selectbox("Légume :", ["Courgette", "Tomate", "Poireau", "Carotte", "Salade"])

if st.button("Obtenir mes conseils"):
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Mois : {mois} | Légume : {legume}",
            config={'system_instruction': "Tu es un maraîcher expert de Champagnole. Donne 3 conseils courts à Jacky pour son potager."}
        )
        st.success("CONSEILS DU JURA :")
        st.write(response.text)
    except Exception as e:
        st.error(f"Erreur : {e}")
