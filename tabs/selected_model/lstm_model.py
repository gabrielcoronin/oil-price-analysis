import streamlit as st
from tabs.tab import TabInterface


class LSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-bottom: 30px; padding: 20px; border-radius: 10px;">
                    Optamos por utilizar <strong>Redes Neurais LSTM (Long Short-Term Memory)</strong> para prever os preços do petróleo devido à sua capacidade única de lidar com sequências de dados e capturar dependências de longo prazo. As LSTMs são uma versão avançada das Redes Neurais Recorrentes (RNNs), permitindo que a rede retenha informações por períodos mais longos, o que é crucial para modelar séries temporais, como as flutuações diárias do preço do petróleo.
                    <br><br>
                    Para ilustrar a escolha, imagine a leitura de um livro: à medida que avançamos pelos capítulos, mantemos as informações dos anteriores, ajudando a compreender a história. Da mesma forma, as LSTMs retêm informações do passado para prever eventos futuros, superando as limitações das RNNs tradicionais, que têm dificuldade em lembrar de eventos distantes.
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <h4 style="color: #E1E1E1;">De Forma Mais Técnica</h4>
            """, unsafe_allow_html=True)
            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-bottom: 30px; padding: 20px; border-radius: 10px;">
                    As LSTMs são uma variante das redes neurais recorrentes, projetadas para capturar dependências temporais de longo prazo. Elas são ideais para tarefas como a previsão dos preços do petróleo, que envolve a análise de séries temporais complexas.
                    <br><br>
                    Ao contrário das redes tradicionais, as LSTMs processam sequências completas de dados, utilizando feedback para manter e atualizar as informações relevantes ao longo do tempo, tornando-as perfeitas para modelar padrões complexos.
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <h4 style="color: #E1E1E1;">Arquitetura da Rede LSTM</h4>
                <ul style="color: #B0B0B0; font-size: 18px; padding: 20px; border-radius: 10px;">
                    <li><strong>Porta de Esquecimento:</strong> Decide quais informações do estado anterior devem ser descartadas.</li>
                    <li><strong>Porta de Entrada:</strong> Determina quais novas informações serão armazenadas, combinando a entrada atual com a memória filtrada do estado anterior.</li>
                    <li><strong>Porta de Saída:</strong> Define quais informações serão usadas para gerar a saída final.</li>
                </ul>
            """, unsafe_allow_html=True)

            st.image(
                "assets/img/lstm.png", 
                caption="Algoritmo LSTM: Estrutura e Funcionamento"
            )

            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-top: 30px; padding: 20px; border-radius: 10px;">
                    Esse processo dinâmico de manter, esquecer e atualizar informações permite que as LSTMs gerenciem sequências de dados de maneira eficiente, superando as limitações das redes tradicionais. Como resultado, conseguimos previsões mais precisas e robustas, essenciais para entender as flutuações no preço do petróleo.
                </div>
            """, unsafe_allow_html=True)
