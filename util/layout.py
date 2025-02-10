import streamlit as st
from st_pages import show_pages, Page

def output_layout():
    show_pages(
        [
            Page("./main.py", "Contexto e Softwares utilizados", ":computer:", use_relative_hash=True),
            Page(
                "./pages/analysis.py",
                "Exploração e Ideias",
                ":chart_with_upwards_trend:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/model.py",
                "Escolha do modelo e resultados",
                ":gear:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/deploy.py",
                "Deploy",
                ":rocket:", 
                use_relative_hash=True,
            ),
        ]
    )

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
