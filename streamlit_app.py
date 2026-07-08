import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

st.title("Le Potager Jurassien")
st.write("Bienvenue Jacky !")

mois = st.selectbox("Mois :", ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"])
legume = st.text_input("Entrez un légume ou un fruit :", "Poireau")

if st.button("Obtenir mes conseils"):
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Mois : {mois} | Légume : {legume}",
            config={'system_instruction': "Tu es un maraîcher expert de Champagnole. Donne 3 conseils courts à Jacky pour son potager ou son verger."}
        )
        st.success("CONSEILS DU JURA :")
        st.write(response.text)
    except Exception as e:
        st.error(f"Erreur : {e}")
            
