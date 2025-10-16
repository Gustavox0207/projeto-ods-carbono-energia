# 🌍 ODS 7 & 13: Análise da Intensidade de Carbono da Energia Global

## 📝 Descrição do Projeto

Este projeto é uma aplicação web interativa desenvolvida para analisar o progresso global em relação aos Objetivos de Desenvolvimento Sustentável (ODS) 7 (Energia Limpa) e ODS 13 (Ação Climática). Utilizando os dados CO2 and Greenhouse Gas Emissions fornecido pela Our World in Data (OWID), o dashboard permite explorar a relação entre o consumo de energia per capita e as emissões de CO2, destacando a eficiência de carbono por país.

## 🚀 Como Acessar

O dashboard interativo está hospedado gratuitamente no Streamlit Community Cloud e pode ser acessado diretamente aqui:
**[Acesse o Dashboard]**: https://projeto-ods-carbono-energia-kobihfg8fpvyztqd7vjaym.streamlit.app

## 🛠️ Tecnologias Utilizadas

* **Backend/Análise:** Python (Pandas)
* **Web Framework:** Streamlit
* **Visualização:** Plotly Express

## 🔬 Análises Principais

O dashboard responde a perguntas-chave de negócio:
* **Tendência Anual:** Evolução da Intensidade de Carbono por país.
* **Correlação:** Valor da Correlação de Pearson entre Consumo de Energia e Emissões de CO2.
* **Progresso:** Top 10 países que mais reduziram a Intensidade de Carbono no longo prazo.

## ⚙️ Como Rodar Localmente

Para executar a aplicação na sua máquina, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Gustavox0207/projeto-ods-carbono-energia.git
   ```
2.  **Navegue até o diretório:**
    ```bash
    cd projeto-ods-carbono-energia
    ```
3.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate      # Windows
    ```
4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```
