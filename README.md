# 🌍 ODS 7 & 13: Análise da Intensidade de Carbono da Energia Global

## 📝 Descrição do Projeto
Este projeto é uma aplicação web interativa desenvolvida para analisar o progresso global em relação aos Objetivos de Desenvolvimento Sustentável (ODS) 7 (Energia Limpa) e ODS 13 (Ação Climática). Utilizando dados da Our World in Data (OWID), o dashboard permite explorar a relação entre o consumo de energia per capita e as emissões de CO2, destacando a eficiência de carbono por país.

## 🚀 Como Acessar
[Se você hospedar no Streamlit Community Cloud, coloque o link aqui]

## 🛠️ Tecnologias Utilizadas
* **Backend/Análise:** Python (Pandas)
* **Web Framework:** Streamlit
* **Visualização:** Plotly Express

## 🔬 Análises Principais
O dashboard responde a perguntas-chave de negócio:
1. **Tendência Anual:** Evolução da Intensidade de Carbono por país.
2. **Correlação:** Valor da Correlação de Pearson entre Consumo de Energia e Emissões de CO2.
3. **Progresso:** Top 10 países que mais reduziram a Intensidade de Carbono no longo prazo.

## ⚙️ Como Rodar Localmente
1. Clone o repositório:
   `git clone https://docs.github.com/pt/repositories`
2. Navegue até o diretório:
   `cd projeto-ods-carbono`
3. Crie um ambiente virtual (recomendado):
   `python -m venv venv`
   `source venv/bin/activate`  # Linux/Mac
   `venv\Scripts\activate`      # Windows
4. Instale as dependências:
   `pip install -r requirements.txt`
5. Execute a aplicação:
   `streamlit run app.py`