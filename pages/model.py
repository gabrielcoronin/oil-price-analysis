import streamlit as st
from tabs.selected_model.lstm_model import LSTMTab
from tabs.selected_model.results import ResultsTab
from util.layout import output_layout

st.set_page_config(page_title="Modelo escolhido", layout='wide')
output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <h1 style='text-align: center; color: #E1E1E1; font-size: 36px;'>Escolha do modelo e resultados</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; color: #B0B0B0; font-size: 18px; margin-bottom: 40px;">
            Nesta seção, apresentamos o modelo utilizado para a previsão do preço do petróleo e os resultados obtidos.
        </div>""", unsafe_allow_html=True)

    tab0, tab1 = st.tabs(
        tabs=[
            "LSTM",
            "Resultados"            
        ]
    )

    LSTMTab(tab0)
    ResultsTab(tab1)
