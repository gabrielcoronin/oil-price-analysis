import streamlit as st
from tabs.introduction.context import ContextTab
from tabs.introduction.softwares import SoftwaresTab
from util.layout import output_layout
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Análise do Preço do Petróleo: Última Década", layout='wide')
output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <h1 style="text-align: center; color: #E1E1E1; font-size: 40px;">Análise do Preço do Petróleo: Última Década</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; color: #B0B0B0; font-size: 18px; margin-bottom: 40px;">
            Explore a evolução do preço do petróleo nos últimos 10 anos, identificando as principais tendências, fatores econômicos e suas implicações globais.
        </div>
    """, unsafe_allow_html=True)

    tab0, tab1 = st.tabs(tabs=['Contexto do Estudo', 'Softwares utilizados'])

    ContextTab(tab0)
    SoftwaresTab(tab1)
