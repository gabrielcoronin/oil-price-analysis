import streamlit as st
from tabs.analysis.eda import EDATab
from tabs.analysis.feature_engineering import FeatureEngineeringTab
from tabs.analysis.looker import LookerAnalysisTab
from tabs.analysis.machine_learning import MachineLearningTab
from tabs.analysis.pre_processing import PreProcessingTab
from util.layout import output_layout

st.set_page_config(page_title="Exploração e Ideias | Análise do Preço do Petróleo", layout='wide')
output_layout()

with open('assets/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <h1 style='text-align: center; color: #E1E1E1; font-size: 36px;'>Exploração e Ideias</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; color: #B0B0B0; font-size: 18px; margin-bottom: 40px;">
            Bem-vindo à análise detalhada do preço do petróleo. Aqui, você poderá explorar dados interativos, entender as tendências do mercado e testar diferentes modelos preditivos. Cada seção oferece uma visão abrangente das etapas do processo, desde o pré-processamento dos dados até a construção de modelos preditivos, passando pela análise exploratória e feature engineering.
        </div>
    """, unsafe_allow_html=True)

    tab0, tab1, tab2, tab3, tab4 = st.tabs(
        tabs=[
            "Pré-processamento dos Dados",
            "Análise Exploratória de Dados",
            "Feature Engineering",
            "Machine Learning",
            "Análise no Looker Studio", 
        ]
    )

    PreProcessingTab(tab0)
    EDATab(tab1)
    FeatureEngineeringTab(tab2)
    MachineLearningTab(tab3)
    LookerAnalysisTab(tab4)
