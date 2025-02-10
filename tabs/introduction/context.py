import streamlit as st
from tabs.tab import TabInterface


class ContextTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.markdown("""
                <h3 style="color: #E1E1E1; font-size: 32px; text-align: center;">Entendendo as Oscilações do Mercado de Petróleo</h3>
            """, unsafe_allow_html=True)
            st.markdown('<hr style="border: 1px solid #555;">', unsafe_allow_html=True)            
            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-bottom: 30px;">
                    O mercado de petróleo é um dos mais voláteis e estratégicos da economia global, sujeito a oscilações que podem impactar desde o preço dos combustíveis até o custo de produção em diversas indústrias. Fatores como tensões geopolíticas, crises econômicas, avanços tecnológicos e mudanças na demanda energética influenciam diretamente a cotação do barril, tornando sua precificação um desafio constante para empresas, investidores e governos. 
                    <br><br>
                    A instabilidade nesse setor não ocorre por acaso. A interdependência entre países produtores e consumidores, as decisões de grandes organizações como a OPEP (Organização dos Países Exportadores de Petróleo) e as transformações no cenário energético mundial contribuem para um mercado dinâmico e imprevisível. Além disso, eventos inesperados, como conflitos internacionais ou desastres naturais, podem desencadear variações abruptas nos preços, exigindo estratégias ágeis para adaptação. 
                    <br><br>
                    Este artigo apresenta um Dashboard interativo que une Storytelling e Machine Learning para prever os preços diários do petróleo, fornecendo insights sobre os fatores que impulsionam essas oscilações. Ao entender melhor o comportamento do mercado, é possível antecipar riscos e identificar oportunidades no cenário energético global.
                </div>
            """, unsafe_allow_html=True)            
