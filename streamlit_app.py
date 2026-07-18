import streamlit as st
import google.generativeai as genai
import os

# 1. Configuration de la page (Nom et icône de l'onglet)
st.set_page_config(page_title="Jardin du Jura", page_icon="🌱")

# Récupération de la clé API secrète
API_KEY = st.secrets["GEMINI_API_KEY"]

# Interface d'accueil
st.title("Mon jardin jurassien 🏔️")
st.image("accueil.png", width=350)  # Ta photo avec Schnaps, bien calibrée pour le mobile !
st.write("### Bienvenue aux jardiniers de la région !")

# FORMULAIRE SUR LA PAGE PRINCIPALE (Plus de menu caché sur mobile !)
st.write("---")
st.write("### 🌿 Vos choix de jardinage :")

mois = st.selectbox(
    "Choisissez le mois :",
    ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
)

legume = st.selectbox(
    "Choisissez un légume, fruit, fleur ou arbuste :",
    ["Tomate", "Courgette", "Salade", "Carotte", "Pomme de terre", "Haricot", "Fraise", "Framboise", "Arbre fruitier", "Fleurs de saison"]
)

# BOUTON D'ACTION
st.write("---")
if st.button("🧙‍♂️ Demander conseil au vieux sage", use_container_width=True):
    with st.spinner("Le vieux sage enfile ses bottes et consulte ses grimoires jurassiens..."):
        try:
            # 1. On donne d'abord la clé API à Google
            genai.configure(api_key=API_KEY)
            
            # 2. On définit le modèle et ses instructions de comportement
            model = genai.GenerativeModel(
                model_name='gemini-2.5-flash',
                system_instruction="""Tu es un vieux jardinier sage et passionné du Jura. 
Structure ta réponse ainsi : 
1. Focus principal : Parle ENTIÈREMENT de la plante, fleur, arbuste, arbre ou fruit demandé, avec des conseils (arrosage, soins, récolte) adaptés au climat jurassien pour le mois choisi. Ajoute une idée sympa (recette, astuce) si adapté. 
2. Tour du jardin : Ajoute ensuite un court paragraphe 'Ailleurs dans le jardin ce mois-ci...' avec 2 ou 3 conseils généraux rapides. 

Très important : Illustre généreusement tes conseils avec des émojis et des petits symboles colorés de saison (des fraises, des fleurs, des feuilles, des outils de jardinage, des soleils, des gouttes d'eau, etc.) pour rendre la lecture très agréable, poétique et vivante !"""
            )
            
            # 3. On lui demande enfin de générer le texte
            response = model.generate_content(f"Mois : {mois} | Produit : {legume}")
            st.success("Les conseils du vieux sage :")
            st.write(response.text)
        except Exception as e:
            st.error(f"Oups, un petit souci technique : {e}")
