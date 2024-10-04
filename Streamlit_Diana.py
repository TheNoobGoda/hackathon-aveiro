
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Função para obter dados de qualidade do ar
def get_air_quality_data():
    url = "https://www.accuweather.com/pt/pt/aveiro/271914/air-quality-index/271914"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        air_quality_header = soup.find('h2', class_='air-quality-card__header')
        date_wrapper = soup.find('div', class_='date-wrapper')
        aqi_element = soup.find('div', class_='aq-number')
        quality_type_element = soup.find('p', class_='category-text')  

        air_quality = air_quality_header.get_text(strip=True) if air_quality_header else 'Título não encontrado'
        date = " ".join(date_wrapper.stripped_strings) if date_wrapper else 'Data não encontrada'
        aqi_value = aqi_element.get_text(strip=True) if aqi_element else 'AQI não encontrado'
        quality_type = quality_type_element.get_text(strip=True) if quality_type_element else 'Tipo de qualidade do ar não encontrado' 

        return air_quality, date, aqi_value, quality_type

    except Exception as e:
        return "Erro ao obter os dados", "", "", ""

# Função para interpretar a pesquisa do usuário
def handle_search(query):
    query = query.lower()
    if "qualidade do ar" in query:
        return "Você pode verificar a qualidade do ar clicando no botão 'Qualidade do Ar'."
    elif "tempo" in query or "meteorologia" in query:
        return "Confira a previsão do tempo clicando no botão 'Meteorologia'."
    elif "eventos" in query:
        return "Descubra os eventos mais recentes clicando no botão 'Eventos'."
    else:
        return "Desculpe, não entendi a pesquisa. Tente usar termos como 'qualidade do ar', 'tempo' ou 'eventos'."

#########################################################################################################

# Interface do Streamlit

# Título centralizado com o nome da aplicação
st.markdown("<h1 style='text-align: center;'>AveiroBuddy</h1>", unsafe_allow_html=True)

# Frase de introdução
st.markdown("<p style='text-align: center;'>Olá! Sou o teu novo assistente pessoal, aqui para tornar a tua vida em Aveiro mais simples.</p>", unsafe_allow_html=True)

# Header inicial: "Em que posso ajudar?"
st.subheader("👋 Em que posso ajudar?")

# Barra de pesquisa
search_query = st.text_input("Digite sua pesquisa:")

# Placeholder para a resposta da pesquisa
if search_query:
    search_response = handle_search(search_query)
    st.write(search_response)

# Header para "Sugestões de pesquisas"
st.subheader("✨ Sugestões de Pesquisas ✨")

# Seção de botões de sugestões de pesquisa
st.write("Escolha uma opção para visualizar as informações:")

# Dividindo a tela em colunas
col1, col2, col3, col4, col5 = st.columns(5)

# Placeholder para exibir transições
placeholder = st.empty()

with col1:
    if st.button("🏛️ Serviços Públicos"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🏛️ Serviços Públicos")
            st.write("Aqui você pode encontrar informações sobre os serviços públicos em Aveiro...")

# Botão para Eventos
with col2:
    if st.button("📅 Eventos"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("📅 Eventos em Aveiro")
            st.write("Aqui estão os eventos em Aveiro...")

# Botão para Meteorologia e Qualidade do Ar
with col3:
    if st.button("🌤️ Meteorologia"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🌤️ Previsão do Tempo e Qualidade do Ar")
            st.write("Aqui você pode visualizar a previsão do tempo e a qualidade do ar...")

# Botão para Roteiro Turístico
with col4:
    if st.button("🗺️ Roteiro Turístico"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🗺️ Roteiro Turístico de Aveiro")
            st.write("Aqui estão sugestões de roteiros turísticos em Aveiro...")

# Coluna extra para balanceamento
with col5:
    st.empty()
