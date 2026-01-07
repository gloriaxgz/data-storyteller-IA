# DataStoryteller-IA: Tradutor de Insights Técnicos

Este projeto é uma aplicação de **IA Generativa** desenvolvida para converter análises de dados e jargões técnicos em narrativas estratégicas para diferentes públicos. 

O objetivo principal é otimizar a comunicação entre times de dados e áreas de negócio, garantindo que o valor dos modelos de Machine Learning seja compreendido por tomadores de decisão, equipes de vendas ou colaboradores em treinamento.

---

##  Stack Tecnológica

| Tecnologia | Descrição |
| :--- | :--- |
| Linguagem | Python |
| Interface | Streamlit |
| Motor de IA | Llama 3.3 (70B) via Groq Cloud |
| Infraestrutura | LPU (Language Processing Units) para inferência de baixíssima latência |
| Processamento de Documentos | PyPDF2 | 
---

## Funcionalidades

- **Portfólio Contextualizado:** integração direta com os resumos técnicos dos meus projetos de Risco de Crédito e Marketing Bancário.
- **Upload de Relatórios:** extração automática de texto de arquivos PDF para tradução imediata.
- **Consultoria Livre:** interface de chat para simplificação de termos técnicos isolados.
- **Persona Adaptativa:** o sistema ajusta automaticamente a densidade técnica e o vocabulário com base no nível de senioridade do público escolhido (do executivo ao cientista de dados).

---

## Diferenciais Técnicos e Arquitetura

Este projeto foi construído focando em evitar os problemas comuns de interfaces genéricas de IA:

1. **Prompt Engineering Avançado:** utilização de *System Instructions* para definir personas específicas, aplicando técnicas de *Chain of Thought* para garantir que a IA analise a métrica técnica antes de criar a analogia.
2. **Controle de Determinismo:** configuração de `temperature=0.3` para mitigar alucinações e garantir que a explicação seja fiel aos dados brutos.
3. **Eficiência de Inferência:** escolha da infraestrutura Groq para demonstrar conhecimento em hardware acelerado para modelos de linguagem (LLMs).
4. **Arquitetura Transformer:** o projeto explora o mecanismo de **Atenção** do Llama 3 para correlacionar métricas de performance (como F1-Score e AUC-ROC) com impactos de negócio.

---

##  Como Executar

1. Clone o repositório:
   ```
   git clone https://github.com/gloriaxgz/DataStoryteller-IA.git

2. **Instale as dependências:**

  ```
   pip install -r requirements.txt
  ```  
4. Configure sua API Key da Groq em um arquivo .env ou secrets.toml.

5. **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    # ou
    streamlit run streamlit_app.py
    ```

A aplicação será aberta automaticamente no seu navegador padrão.
