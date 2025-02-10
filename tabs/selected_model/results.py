import streamlit as st
from tabs.tab import TabInterface

class ResultsTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:      
            st.markdown("""
                <div style="text-align: justify; color: #B0B0B0; font-size: 18px; line-height: 1.6; margin-bottom: 30px; padding: 20px; border-radius: 10px;">
                    Este projeto nos proporcionou uma experiência enriquecedora e desafiadora, unindo teoria e prática para resolver um problema real de análise e previsão do preço do petróleo.
                    <br><br>
                    Conseguimos desenvolver um dashboard interativo no Looker, permitindo a visualização intuitiva e estratégica dos dados, além de insights relevantes sobre fatores que impactam a variação dos preços, como crises econômicas, conflitos geopolíticos e oscilações na demanda global de energia.
                    <br><br>
                    Para a modelagem preditiva, empregamos uma Rede Neural LSTM (Long Short-Term Memory), um modelo altamente eficiente para séries temporais. Nossa solução alcançou uma precisão de 93%, demonstrando sua robustez na previsão diária do preço do petróleo. Esse resultado reforça a eficácia da LSTM na captura de padrões complexos ao longo do tempo, tornando-se uma ferramenta valiosa para a tomada de decisões estratégicas no setor energético.
                    <br><br>
                    Além da modelagem e visualização de dados, planejamos a implantação do modelo em produção e criamos um MVP funcional utilizando Streamlit, garantindo que as previsões possam ser acessadas de forma prática e dinâmica pelos usuários.
                    <br><br>
                    O processo foi documentado em um vídeo explicativo, onde detalhamos cada etapa do projeto, desde a coleta e análise dos dados até a implementação final.
                    <br><br>
                    Ao longo deste projeto, enfrentamos desafios reais que nos permitiram aprofundar nossos conhecimentos em Data Science, Machine Learning e Visualização de Dados. Trabalhar com dados do mundo real, lidar com a variabilidade dos preços do petróleo e estruturar um modelo preditivo robusto exigiu um alto nível de análise crítica e tomada de decisão. O resultado final demonstra o potencial de soluções baseadas em IA para agregar valor real ao mercado e auxiliar na tomada de decisões estratégicas.
                </div>
            """, unsafe_allow_html=True)
