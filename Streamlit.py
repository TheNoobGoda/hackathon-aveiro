# Função para obter os dados de qualidade do ar
def get_air_quality_data():
    # URL do site AccuWeather para o índice de qualidade do ar em Aveiro
    url = "https://www.accuweather.com/pt/pt/aveiro/271914/air-quality-index/271914"  

    # Headers para simular uma solicitação de navegador
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Enviar uma solicitação GET com cabeçalhos
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

        # Analisar o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrair informações da qualidade do ar
        air_quality_header = soup.find('h2', class_='air-quality-card__header')
        date_wrapper = soup.find('div', class_='date-wrapper')
        aqi_element = soup.find('div', class_='aq-number')
        quality_type_element = soup.find('p', class_='category-text')  

        # Verificar se os elementos foram encontrados e extrair o texto
        air_quality = air_quality_header.get_text(strip=True) if air_quality_header else 'Título não encontrado'
        date = " ".join(date_wrapper.stripped_strings) if date_wrapper else 'Data não encontrada'
        aqi_value = aqi_element.get_text(strip=True) if aqi_element else 'AQI não encontrado'
        quality_type = quality_type_element.get_text(strip=True) if quality_type_element else 'Tipo de qualidade do ar não encontrado' 

        return air_quality, date, aqi_value, quality_type

    except requests.exceptions.RequestException as e:
        return "Erro ao fazer a solicitação", "", "", ""
    except Exception as e:
        return "Ocorreu um erro", "", "", ""

# Interface Gráfica com Streamlit
st.title("Índice de Qualidade do Ar - Aveiro")
st.write("Este aplicativo exibe o Índice de Qualidade do Ar (AQI) para a cidade de Aveiro.")

# Botão para atualizar os dados
if st.button("Atualizar dados"):
    # Obter os dados de qualidade do ar
    air_quality, date, aqi_value, quality_type = get_air_quality_data()

    # Exibir as informações
    st.subheader(air_quality)
    st.write(f"Data: {date}")
    st.write(f"Índice de Qualidade do Ar: {aqi_value}")
    st.write(f"Tipo de Qualidade do Ar: {quality_type}")
else:
    st.write("Clique no botão acima para obter os dados mais recentes.")
