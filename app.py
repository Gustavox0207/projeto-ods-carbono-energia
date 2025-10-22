import streamlit as st
import pandas as pd
import plotly.express as px

# Carregamento de Dados e Pré-processamento
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
    df = pd.read_csv(url)

    colunas_foco = [
        'country', 'year', 'co2_per_capita', 'energy_per_capita',
        'gdp', 'population'
    ]
    df = df[colunas_foco].copy()

    df = df[df['year'] >= 1990]
    df.dropna(subset=['energy_per_capita', 'co2_per_capita'], inplace=True)

    # Intensidade de Carbono da Energia
    df['co2_intensity'] = df['co2_per_capita'] / df['energy_per_capita'] * 1000 # kg de CO₂ por kWh

    return df

df = load_data()

# Função para a Tabela de Progresso (Calculada uma única vez, fora do loop principal)
def calcular_progresso(df, ano_inicio=2000):
    ano_fim = df['year'].max()

    df_progresso = df[df['year'].isin([ano_inicio, ano_fim])].copy()
    df_pivot = df_progresso.pivot_table(
        index='country',
        columns='year',
        values='co2_intensity'
    ).dropna()

    df_pivot['Progresso (%)'] = (
        (df_pivot[ano_inicio] - df_pivot[ano_fim]) / df_pivot[ano_inicio]
    ) * 100

    df_resultados = df_pivot.sort_values(by='Progresso (%)', ascending=False)

    return df_resultados[['Progresso (%)']].round(2), ano_inicio, ano_fim

# Configuração da Página e Títulos
st.set_page_config(layout="wide")
st.title("ODS 7 & 13: Intensidade de Carbono da Energia Global 🌍")
st.markdown("Análise da relação entre consumo de energia e emissões de CO2 per capita (Fonte: OWID CO2 Data)")

# Sidebar e definição das variáveis de filtro

st.sidebar.header("Filtros")

# Filtro de País
paises_disponiveis = sorted(df['country'].unique().tolist())
paises_selecionados = st.sidebar.multiselect(
    "Selecione Países:",
    options=paises_disponiveis,
    default=['Brazil', 'United States', 'China', 'Germany', 'Russia']
)

# Filtro de Ano
ano_min = int(df['year'].min())
ano_max = int(df['year'].max())
ano_selecionado = st.sidebar.slider(
    "Selecione o Ano:",
    min_value=ano_min,
    max_value=ano_max,
    value=ano_max
)

# Aplica os filtros Pandas (AGORA 'df_ano' e 'df_filtrado' ESTÃO DEFINIDOS!)
df_filtrado = df[df['country'].isin(paises_selecionados)]
df_ano = df[df['year'] == ano_selecionado]

# KPIs (Correlação) - Usa 'df_ano' e 'ano_selecionado'
st.subheader("Métrica Chave: Correlação entre Consumo de Energia e Emissões")

if not df_ano.empty:
    correlacao = df_ano[['energy_per_capita', 'co2_per_capita']].corr().iloc[0, 1]

    valor_kpi = f"{correlacao:.3f}"

    if correlacao >= 0.7:
        interpretacao = "Forte correlação positiva: Maior consumo de energia está fortemente ligado a mais CO2."
    else:
        interpretacao = "Correlação moderada/fraca: O consumo de energia está menos ligado às emissões de CO2."

    col_kpi = st.columns(1)
    with col_kpi[0]:
        st.metric(
            label=f"Correlação (Pearson) em {ano_selecionado}",
            value=valor_kpi,
            delta=interpretacao
        )


# VISUALIZAÇÕES E TABELAS
# VISUALIZAÇÃO 1: Tendência Anual
st.subheader(f"1. Evolução da Intensidade de Carbono (1990 - {ano_max})")
st.markdown("*(Kg de CO2 per capita por unidade de energia consumida)*")
if not df_filtrado.empty:
    fig1 = px.line(
        df_filtrado,
        x='year',
        y='co2_intensity',
        color='country',
        title='Intensidade de Carbono por País (Redução = Progresso)',
        labels={'co2_intensity': 'Intensidade de Carbono (proxy)', 'year': 'Ano'}
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.warning("Selecione pelo menos um país para visualizar a tendência.")

# VISUALIZAÇÃO 2: Comparação
st.subheader(f"2. Consumo de Energia vs. CO2 per Capita (Ano: {ano_selecionado})")
if not df_ano.empty:
    fig2 = px.scatter(
        df_ano,
        x='energy_per_capita',
        y='co2_per_capita',
        size='population',
        color='country',
        hover_name='country',
        title='Relação entre Consumo de Energia e Emissões',
        labels={'co2_per_capita': 'CO2 per Capita (toneladas)', 'energy_per_capita': 'Energia per Capita (kWh)'}
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("Não há dados completos para o ano selecionado.")

# VISUALIZAÇÃO 3: Tabela de Progresso
st.subheader("3. Progresso na Redução da Intensidade de Carbono")

df_progresso, ano_inicio, ano_fim = calcular_progresso(df)

st.markdown(f"**Top 10 Países que Mais Reduziram a Intensidade de Carbono ({ano_inicio} a {ano_fim}):**")
st.dataframe(df_progresso.head(10), use_container_width=True)
st.markdown(f"*(Valores negativos indicam redução da Intensidade de Carbono, o que é um progresso positivo para o ODS 7/13.)*")
