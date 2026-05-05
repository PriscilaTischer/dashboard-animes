import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
#CONFIGURAÇÃO DA PÁGINA E LAYOUT
# ==========================================
# Mantendo tudo em tela única (Wide)
st.set_page_config(page_title="Dashboard Animes", layout="wide")
st.title("📊 Análise de Dados: Animes")

# ==========================================
#EXTRAÇÃO E TRANSFORMAÇÃO DE DADOS (ETL)
# ==========================================
@st.cache_data
def carregar_e_tratar_dados():
    # EXTRAÇÃO: Lendo o arquivo original
    df = pd.read_csv("anime_dataset.csv")
    
    # TRANSFORMAÇÃO: Limpeza básica e conversão 
    df = df.dropna(subset=['aired_from', 'year', 'score', 'episodes', 'source'])
    df['aired_from'] = pd.to_datetime(df['aired_from'], errors='coerce')
    df['year'] = df['year'].astype(int)
    
    # Ordenando por popularidade
    df = df.sort_values(by='popularity')
    
    return df

df_animes = carregar_e_tratar_dados()

# ==========================================
#FILTRO DE DADOS INTERATIVO
# ==========================================
st.sidebar.header("Filtros do Dashboard")
anos_disponiveis = sorted(df_animes['year'].unique(), reverse=True) 
ano_selecionado = st.sidebar.selectbox("Selecione o Ano de Lançamento:", anos_disponiveis)

df_filtrado = df_animes[df_animes['year'] == ano_selecionado]

#TOP 10 
df_top10 = df_filtrado.head(10)

#PALETA DE CORES: Definindo tons de Azul e Laranja
cores_azul_laranja = ['#1f77b4', '#ff7f0e', '#5b9bd5', '#ed7d31', '#9dc3e6', '#f4b084']

# ==========================================
#VISUALIZAÇÃO E MONTAGEM DO DASHBOARD 
# ==========================================
aba_destaques, aba_graficos, aba_dados = st.tabs(["🏆 Top 5 do Ano", "📈 Graficos", "📋 Tabela:Base de Dados Bruta"])

with aba_destaques:
    st.subheader(f"Os 5 Animes Mais Bem Avaliados de {ano_selecionado}")
    df_top5_visual = df_filtrado.nlargest(5, 'score')
    
    cols = st.columns(5)
    for index, (i, row) in enumerate(df_top5_visual.iterrows()):
        with cols[index]:
            st.image(row['image_url'], use_container_width=True)
            st.markdown(f"**{row['title']}**")
            st.caption(f"⭐ Nota: {row['score']} | 🎬 Eps: {row['episodes']}")

with aba_graficos:
    linha1_col1, linha1_col2 = st.columns(2)
    linha2_col1, linha2_col2 = st.columns(2)
    
    with linha1_col1:
        # Gráfico de Linha - Cor Azul 
        df_linha = df_top10.sort_values(by='aired_from')
        fig_linha = px.line(df_linha, x='aired_from', y='score', hover_name='title', markers=True,
                           title=f"Evolução das Notas (Top 10 - {ano_selecionado})",
                           color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig_linha, use_container_width=True)
        # Texto Explicativo
        st.caption("💡 **Este gráfico mostra a progressão de qualidade no período. Permite ver se os animes lançados no final do ano foram melhores ou piores que os do começo.")
        
    with linha1_col2:
        # Gráfico de Barra (Horizontal) - Cor Laranja (Agora Top 10)
        fig_barra = px.bar(df_top10, x='episodes', y='title', orientation='h',
                           title="Volume de Episódios por Obra (Top 10)",
                           color_discrete_sequence=['#ff7f0e'])
        fig_barra.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_barra, use_container_width=True)
        # Texto Explicativo 
        st.caption("💡 **Este gráfico compara a extensão das obras mais populares, permitindo identificar rapidamente quais são os projetos mais longos.")

    with linha2_col1:
        # Gráfico de Dispersão
        fig_dispersao = px.scatter(df_filtrado, x='episodes', y='score', color='source', hover_name='title',
                                   title="Correlação: Duração vs Avaliação Pública",
                                   color_discrete_sequence=cores_azul_laranja)
        st.plotly_chart(fig_dispersao, use_container_width=True)
        # Texto Explicativo
        st.caption("💡 **Este gráfico ajuda a descobrir padrões. Por exemplo: será que animes com muitos episódios tendem a ter notas menores porque perdem a qualidade?")

    with linha2_col2:
        # Gráfico de Pizza
        fig_pizza = px.pie(df_filtrado, names='source', title="Material Original (Mangá, Jogo, etc)",
                           color_discrete_sequence=cores_azul_laranja)
        st.plotly_chart(fig_pizza, use_container_width=True)
        # Texto Explicativo
        st.caption("💡 **Este gráfico mapeia a fatia de mercado da indústria. Mostra de onde vieram as histórias (se a maioria foi adaptada de Mangás, Jogos ou material original).")

with aba_dados:
    st.subheader(f"Dados Tabulares - Ano {ano_selecionado}")
    colunas_visiveis = ['title', 'source', 'episodes', 'score', 'popularity', 'aired_from', 'genres']
    st.dataframe(df_filtrado[colunas_visiveis], use_container_width=True)