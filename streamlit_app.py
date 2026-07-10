import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

st.title("Mon jardin jurassien")
st.image("accueil.png")
st.write("Bienvenue aux jardiniers de la région !")

st.sidebar.header("Parlons Jardin")
mois = st.sidebar.selectbox("Mois :", ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"])
legume = st.sidebar.text_input("Entrez un légume , un fruit , une fleur, un arbuste , un arbre ou une plante aromatique) :", "Poireau")

if st.sidebar.button("Ecoute la terre qui te parle"):
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
            
