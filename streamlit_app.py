import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Show an external HTML", page_icon=":guardsman:", layout="wide")
path_to_html = "./main.html" 

with open(path_to_html,'r', encoding='utf-8') as f: 
    html_data = f.read()

st.header("Mon projet SQL")

with st.expander("Cliquez pour voir le diagramme UML de la base de données"):
    st.image("diagram_UML.png", caption="Diagramme UML de la base de données")


components.html(html_data, scrolling=True, height=600, width=1500)

st.markdown("""# Conclusion de l'Analyse de Données SQL
**Par : Ibrahima Sory DIALLO**

---

### Pour aller plus loin
N'hésitez pas à explorer davantage le schéma de la base de données, à expérimenter différentes optimisations de requêtes ou à proposer des améliorations pour accroître l'efficacité et la performance du système. 

L'analyse de données est un processus itératif : chaque nouvelle question peut révéler une pépite pour notre stratégie de recrutement !

---

### 🤝 Restons en contact
Si vous avez des questions sur cette analyse ou si vous souhaitez collaborer sur des projets similaires, vous pouvez me joindre via :

* [**LinkedIn**](https://www.linkedin.com/in/ibrahima-sory-diallo-isd/)
* 📧 [**Envoyer un Email**](mailto:isddiallopro@gmail.com)

---
*Projet réalisé dans le cadre d'un projet d'école (2026).*

""")
