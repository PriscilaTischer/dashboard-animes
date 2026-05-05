# 📊 Dashboard Analítico - Ecossistema de Animes

Este projeto consiste em um pipeline de **Processamento de Dados e Automação de Tarefas** visuais. Utilizando uma base de dados robusta com mais de 30 mil registros extraída do Kaggle, o objetivo é extrair inteligência e padrões da indústria de animes.

## 🛠️ Metodologia e Tecnologias Aplicadas

* **Extração e Transformação (ETL) com Pandas:** Limpeza de valores nulos, tratamento de inconsistências e conversão de tipagem de dados (`string` para `datetime`).
* **Visualização de Dados com Plotly:** Construção de gráficos interativos (Linha, Barra Horizontal, Dispersão e Pizza), permitindo análise de correlação entre volume de episódios, qualidade percebida pelo público e formato de mídia.
* **Interface Automática com Streamlit:** Desenvolvimento de um Dashboard em tela única (*single-page application*), projetado com grid layout e navegação por abas para evitar rolagem excessiva e otimizar a experiência de leitura analítica.

## 🚀 Como executar este projeto na sua máquina

Certifique-se de ter o Python instalado. No terminal da sua máquina, siga os passos:

1. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   
##Para Executar
streamlit run dados_dashbord_ANIME.py
