import streamlit as st
from tabs.tab import TabInterface


class SoftwaresTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.markdown("""
                <h3 style="color: #E1E1E1; font-size: 32px; text-align: center;">Utilização do Looker e Streamlit para o MVP</h3>
            """, unsafe_allow_html=True)
            st.markdown('<hr style="border: 1px solid #555;">', unsafe_allow_html=True)    
            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-bottom: 30px;">
                    No desenvolvimento deste trabalho, utilizamos o <strong>Looker Studio</strong> para criar gráficos interativos que oferecem uma visão detalhada das variações no preço do petróleo. Além disso, o <strong>Streamlit</strong> foi a ferramenta escolhida para a construção do MVP (Produto Mínimo Viável), trazendo um dashboard dinâmico e de fácil interação.
                    <br><br>
                    Para a análise dos dados, foram utilizados os dados do site do Instituto de Pesquisa Econômica Aplicada (IPEA) e tratados numa planilha Excel para poder realizar os gráficos no Looker Studio.
                    <br><br>
                    A combinação dessas ferramentas possibilitou a criação de uma plataforma intuitiva, que permite a visualização de dados em tempo real, além de oferecer insights profundos sobre as influências no mercado de petróleo, permitindo uma análise mais ágil e assertiva.
                </div>
            """, unsafe_allow_html=True)
