import streamlit as st
from groq import Groq
import PyPDF2
from projetos import BASE_PROJETOS
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


st.set_page_config(page_title="Central de IA - Glória Xavier", layout="wide")

st.title("Central de Inteligência e Comunicação Técnica")
st.caption("Desenvolvido por Glória Xavier | Foco em Tradução de Valor de Negócio")

with st.expander(" Saiba mais sobre esta ferramenta (O que é, como funciona e por que é importante)", expanded=False):
    st.markdown("""
    ### O que é?
    Esta é uma solução de **IA Generativa** desenhada para resolver a lacuna de comunicação entre o time técnico de dados e os stakeholders de negócio. Ela atua como uma tradutora de jargões para diferentes níveis hierárquicos.

    ### Como funciona?
    O sistema utiliza a infraestrutura da **Groq (LPUs)** para rodar o modelo **Llama 3.3 (70B)**. O fluxo segue o princípio de **Engenharia de Prompt**, onde o modelo recebe instruções de sistema que o fazem a agir como um consultor estratégico, e não apenas um chatbot genérico.

    ### Por que é importante?
    Em ambientes corporativos, a capacidade de treinar colaboradores e realizar apresentações exige que dados complexos sejam simplificados sem perda de precisão. Esta ferramenta automatiza e padroniza esse processo.

    """)
st.link_button("Acesse o repositório no Github", "https://github.com/gloriaxgz/data-storyteller-IA")
st.info("""
### Como usar:

1. Escolha uma **Fonte de Conhecimento** (meus próprios projetos, um arquivo PDF ou escreva um texto manual). 
        
2. Selecione o **Público-Alvo** para quem a explicação deve ser gerada. 
        
3. Clique em **Gerar Explicação**.
""")


st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Fonte de Conhecimento")
    modo = st.radio("Selecione de onde a IA deve ler:", 
                    ["Meus Projetos (Portfólio)", "Upload de PDF (Relatório)", "Texto Livre (Consultoria)"],
                    horizontal=True)

    texto_para_processar = ""

    if modo == "Meus Projetos (Portfólio)":
        escolha = st.selectbox("Selecione o projeto do meu currículo:", list(BASE_PROJETOS.keys()))
        texto_para_processar = BASE_PROJETOS[escolha]

    elif modo == "Upload de PDF (Relatório)":
        pdf = st.file_uploader("Faça o upload de um relatório técnico:", type="pdf")
        if pdf:
            leitor = PyPDF2.PdfReader(pdf)
            texto_para_processar = "".join([p.extract_text() for p in leitor.pages])

    else:
        texto_para_processar = st.text_area("Escreva o texto técnico aqui:", placeholder="Ex: O modelo obteve um F1-Score de 0.85 com regularização L2...")

    st.subheader("2. Personalização")
    publico = st.selectbox(
        "Para qual público devemos traduzir?",
        options=[
            "Diretoria Executiva (Foco em ROI e Estratégia)",
            "Equipe de Vendas (Foco em Argumentos de Conversão)",
            "Colaboradores Não-Técnicos (Foco em Treinamento/Didática)",
            "Estudantes de Dados (Foco em Conceitos de Aprendizado)",
            "Cientistas de Dados (Foco em Detalhes Técnicos para um público especializado)"
        ]
    )
    
    gerar = st.button(" Gerar Explicação de Valor")

if gerar:
    if texto_para_processar:
        with st.spinner("A IA está analisando os tokens e gerando o contexto..."):
            try:
                chat = client.chat.completions.create(
    messages=[
        {
            "role": "system", 
            "content": (
                f"Você é uma Tech Lead Sênior com 10 anos de experiência. Seu objetivo é explicar projetos para o público: {publico}. "
                "Siga RIGOROSAMENTE estas diretrizes de nível de profundidade: "
                
                "1. Se o público for 'Diretoria/Executivo': Foque em ROI, mitigação de risco, eficiência operacional e tomada de decisão. Ignore detalhes de código. "
                
                "2. Se o público for 'Estudantes/Cientistas de Dados': Fale de 'especialista para especialista'. "
                "NÃO defina o que é Python, Pandas ou Machine Learning. "
                "FOQUE em: métricas de performance (F1-Score, AUC-ROC), engenharia de atributos, tratamento de dados (outliers, nulos), "
                "escolha do algoritmo e possíveis problemas como overfitting ou data leakage. Use vocabulário técnico avançado. "
                
                "3. Se o público for 'Leigo/Não-Técnico': Use analogias inteligentes, focando na utilidade da ferramenta no dia a dia. "
                
                "Diretriz Geral: Nunca seja condescendente. Se o público é técnico, seja denso. Se é executivo, seja estratégico."
            )
        },
        {
            "role": "user", 
            "content": f"Material base: {texto_para_processar}. Por favor, faça a análise adequada ao nível de senioridade do público."
        }
    ],
    model="llama-3.3-70b-versatile",
    temperature=0.3
)
                st.success(f"✅ Versão para: {publico}")
                st.markdown(chat.choices[0].message.content)
            except Exception as e:
                st.error(f"Erro na conexão: {e}")
    else:
        st.warning("Por favor, forneça um texto ou arquivo antes de gerar.")
