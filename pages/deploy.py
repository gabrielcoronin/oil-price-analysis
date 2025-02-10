import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import date, datetime, timedelta
import holidays
from util.utils import load_and_preprocess_data, load_lstm_model, predict, scale_data

st.set_page_config(page_title="Previsão do Petróleo", layout='wide')

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
model_path = os.path.join(base_dir, 'models', 'LSTMModel.keras')
scaler_path = os.path.join(base_dir, 'models', 'scaler.joblib')

model_lstm, scaler = load_lstm_model(model_path, scaler_path)
if model_lstm is None:
    st.stop()

DATA_INICIAL = date.today()
LIMITE_DIAS = 15
br_feriados = holidays.Brazil(years=DATA_INICIAL.year)

def is_weekend_or_holiday(d):
    return d.weekday() >= 5 or d in br_feriados

def get_business_days_list(start_date, num_business_days):
    current_date = start_date
    business_days = []
    while len(business_days) < num_business_days:
        while is_weekend_or_holiday(current_date):
            current_date += timedelta(days=1)
        business_days.append(current_date)
        current_date += timedelta(days=1)
    return business_days

st.markdown("<h1 style='text-align: center; color: white;'>Previsão do Preço do Petróleo</h1>", unsafe_allow_html=True)

dias_uteis = st.slider("Selecione o número de dias úteis:", min_value=1, max_value=LIMITE_DIAS, value=5)
business_days_list = get_business_days_list(DATA_INICIAL, dias_uteis)
start_date, end_date = business_days_list[0], business_days_list[-1]

if st.button("Selecionar Data"):
    st.session_state.mostrar_popup = True

if st.session_state.get("mostrar_popup", False):
    with st.expander("📆 Confirme a Seleção", expanded=True):
        st.write(f"**Data Inicial:** {start_date.strftime('%Y-%m-%d')}")
        st.write(f"**Data Final:** {end_date.strftime('%Y-%m-%d')}")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✅ Confirmar", key="confirmar"):
                st.session_state.mostrar_popup = False
                st.session_state.gerar_previsao = True

        with col2:
            if st.button("❌ Cancelar", key="cancelar"):
                st.session_state.mostrar_popup = False
                st.session_state.gerar_previsao = False

if st.session_state.get("gerar_previsao", False):
    st.success("Data confirmada! Gerando previsão... ⏳")

    startDate = f"{DATA_INICIAL.year - 10}-{DATA_INICIAL.month}-{DATA_INICIAL.day}"
    url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
    df = load_and_preprocess_data(url, startDate)

    if df is None or df.empty:
        st.error("Erro ao obter dados do IPEA.")
        st.stop()

    scaled_data, scaler = scale_data(df)

    try:
        days_to_predict = len(business_days_list)
        forecast = predict(days_to_predict, scaled_data, sequence_length=10).round(2)

        trace1 = go.Scatter(x=df['date'], y=df['price'], mode='lines', name='Dados Históricos', line=dict(color='#64b5f6', width=3))
        trace2 = go.Scatter(x=business_days_list, y=forecast, mode='lines', name='Previsão LSTM', line=dict(color='#ffeb3b', width=3, dash='dot'))

        layout = go.Layout(
            title="Previsão do Preço do Petróleo",
            xaxis={'title': "Data", 'color': '#e0e0e0', 'tickangle': 45},
            yaxis={'title': "Preço (R$)", 'color': '#e0e0e0'},
            plot_bgcolor='#1f1f1f',
            paper_bgcolor='#1f1f1f',
            font=dict(color='#e0e0e0'),
            hovermode='closest',
            legend=dict(bgcolor='rgba(0,0,0,0)', bordercolor='#e0e0e0', borderwidth=1),
            margin=dict(t=50, b=50, l=50, r=50)
        )
        fig = go.Figure(data=[trace1, trace2], layout=layout)

        col1, col2 = st.columns([8, 2])
        with col1:
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            forecast_df = pd.DataFrame({
                "Data": [d.strftime("%Y-%m-%d") for d in business_days_list],
                "Preço Previsto (R$)": [f"{x:.2f}" for x in forecast]
            })
            st.write(forecast_df.set_index("Data"))

        st.success("Previsão gerada com sucesso!")

    except Exception as e:
        st.error(f"Erro ao gerar a previsão: {e}")
