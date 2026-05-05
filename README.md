#  Dashboard Analítico de Animes

📌 **Status:** ✅ Concluído
🎓 **Instituição:** Universidade Federal de Itajubá (UNIFEI)  
📚 **Curso:** Bacharelado em Ciência e Tecnologia

---

## 📝 Resumo do Projeto
Este repositório documenta uma atividade da disciplina de **Programação para Ciência de Dados**, com foco em **Processamento de Dados e Automação** de relatórios visuais.

O objetivo foi ir muito além dos requisitos acadêmicos básicos, escolhendo um dataset não convencional (mais de 30 mil registros da indústria de animes extraídos do Kaggle) para desenvolver um **Dashboard Interativo**. O projeto realiza o tratamento corporativo da base (ETL) e a visualização dinâmica de indicadores, permitindo uma análise rápida e intuitiva para apoio à tomada de decisão.

---

## 🚀 Tecnologias e Ferramentas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🛠️ Principais Funcionalidades

### 📊 Visualização de Dados
- Dashboard interativo em tela única (*Single-Page Application*) estruturado em abas e colunas.
- Gráficos dinâmicos e interativos (Linha, Barra Horizontal, Dispersão e Pizza) utilizando **Plotly**.
- Exibição automatizada de um Top 10 consumindo capas via URL das imagens.

### 💾 Engenharia de Dados (ETL)
- Extração e limpeza de valores nulos utilizando **Pandas**.
- Conversão avançada de tipagem de dados (`string` para `datetime`).
- Filtro iterativo (`selectbox`) para exploração de dados baseados no ano de lançamento.

### 📈 Análise e Storytelling
- Monitoramento da progressão de qualidade das obras ao longo dos meses.
- Análise de correlação entre formato de mídia, volume de episódios e avaliação pública.
- Legendas de *Data Storytelling* automatizadas para facilitar a leitura gerencial dos gráficos.

---

## 📂 Estrutura do Repositório
- `anime_dataset.csv` – Base de dados bruta original.
- `dados_dashbord_ANIME.py` – Código principal da aplicação contendo o pipeline de ETL e o Frontend.
- `requirements.txt` – Lista de dependências e bibliotecas do projeto.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
- Python instalado na sua máquina.

### Instalação das Dependências
Após fazer o download dos arquivos, abra o terminal na pasta do projeto e instale as bibliotecas necessárias executando:

```bash
pip install -r requirements.txt
