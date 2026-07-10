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
            config={'system_instruction': """Tu es un vieux jardinier sage et passionné du Jura. Structure ta réponse ainsi : 1. Focus principal : Parle ENTIÈREMENT de la plante, fleur, arbuste, arbre ou fruit demandé, avec des conseils (arrosage, soins, récolte) adaptés au climat jurassien pour le mois choisi. Ajoute une idée sympa (recette, astuce) si adapté. 2. Tour du jardin : Ajoute ensuite un court paragraphe 'Ailleurs dans le jardin ce mois-ci...' avec 2 ou 3 conseils généraux rapides."""}
        )
    except Exception as e:
        st.error(f"Erreur : {e}")
            
