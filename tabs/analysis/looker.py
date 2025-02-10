import os
import streamlit as st

class LookerAnalysisTab:
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown("<h1 style='text-align: center; color: #E1E1E1;'>Análise do Preço do Petróleo no Looker Studio</h1>", unsafe_allow_html=True)
            
            st.markdown("""
                <div style="text-align: center; color: #B0B0B0; font-size: 18px; line-height: 1.6;">
                    Realizamos uma análise detalhada sobre a evolução do preço do petróleo ao longo dos anos utilizando o Looker Studio. 
                    Através de gráficos interativos, exploramos as tendências e padrões dos preços, o que nos permitiu obter insights 
                    relevantes sobre os fatores que influenciam o mercado de petróleo.
                </div>
            """, unsafe_allow_html=True)

            url = "https://lookerstudio.google.com/reporting/4542dd62-3124-4f45-88f7-a0edf24d9325/page/gK5kE?s=mRSFyfNmscA"
            st.markdown(f"""
                <div style="text-align: center; margin-top: 30px;">
                    <a href="{url}" target="_blank" style="background-color: #444444; color: #E1E1E1; padding: 14px 28px; text-align: center; text-decoration: none; display: inline-block; border-radius: 12px; font-size: 18px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <strong>Acessar análise no Looker Studio</strong>
                    </a>
                </div>
            """, unsafe_allow_html=True)
            
            image_path = os.path.join('assets', 'img', 'looker_logo.png')
            if os.path.exists(image_path):
                st.image(image_path, width=300, use_container_width=True)
            else:
                st.error("Imagem não encontrada. Verifique o caminho da imagem.")
