import streamlit as st
import google.generativeai as genai
import os

# 1. LA LIGNE MAGIQUE : Elle donne le vrai nom et l'icône à l'application
st.set_page_config(page_title="Jardin du Jura", page_icon="🌱")

# Récupération de la clé API secrète
API_KEY = st.secrets["GEMINI_API_KEY"]

# Interface d'accueil
st.title("Mon jardin jurassien 🏔️")
st.image("accueil.png")  # Ta jolie photo du jardin
st.write("### Bienvenue aux jardiniers de la région !")

# BARRE LATÉRALE : On y laisse UNIQUEMENT les choix (pas de bouton ici !)
st.sidebar.title("🌿 Parlons Jardin")

mois = st.sidebar.selectbox(
    "Choisissez le mois :",
    ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
)

legume = st.sidebar.selectbox(
    "Choisissez la plante ou le légume :",
    ["Tomate", "Courgette", "Salade", "Carotte", "Pomme de terre", "Haricot", "Fraise", "Framboise", "Arbre fruitier", "Fleurs de saison"]
)

# PAGE PRINCIPALE : Le bouton est maintenant ici, gros et bien visible sous la photo !
st.write("---")
if st.button("🧙‍♂️ Demander conseil au vieux sage", use_container_width=True):
    with st.spinner("Le vieux sage enfile ses bottes et consulte ses grimoires jurassiens..."):
        try:
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"Mois : {mois} | Produit : {legume}",
                config={'system_instruction': """Tu es un vieux jardinier sage et passionné du Jura. 
Structure ta réponse ainsi : 
1. Focus principal : Parle ENTIÈREMENT de la plante, fleur, arbuste, arbre ou fruit demandé, avec des conseils (arrosage, soins, récolte) adaptés au climat jurassien pour le mois choisi. Ajoute une idée sympa (recette, astuce) si adapté. 
2. Tour du jardin : Ajoute ensuite un court paragraphe 'Ailleurs dans le jardin ce mois-ci...' avec 2 ou 3 conseils généraux rapides. 

Très important : Illustre généreusement tes conseils avec des émojis et des petits symboles colorés de saison (des fraises, des fleurs, des feuilles, des outils de jardinage, des soleils, des gouttes d'eau, etc.) pour rendre la lecture très agréable, poétique et vivante !"""}
            )
            st.success("Les conseils du vieux sage :")
            st.write(response.text)
        except Exception as e:
            st.error(f"Oups, un petit souci technique : {e}")
