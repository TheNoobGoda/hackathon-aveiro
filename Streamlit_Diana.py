
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

# Função para obter eventos de Aveiro
def get_aveiro_events():
    url = "https://www.viralagenda.com/pt/aveiro"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        events = soup.find_all('li', class_='viral-item')
        event_list = []

        for event in events:
            title_element = event.find('span', itemprop='name')
            title = title_element.get_text(strip=True) if title_element else 'Título não encontrado'

            start_time_element = event.find('time', itemprop='startDate')
            start_date = start_time_element['datetime'].split("T")[0] if start_time_element else 'Data de início não encontrada'

            event_hour_element = event.find('div', class_='viral-event-hour')
            event_hour = event_hour_element.get_text(strip=True) if event_hour_element else 'Hora não encontrada'

            location_element = event.find('a', itemprop='location')
            location = location_element.get_text(strip=True) if location_element else 'Local não encontrado'

            category_element = event.find('a', title="Ver eventos desta categoria")
            category = category_element.get_text(strip=True) if category_element else 'Categoria não encontrada'

            event_list.append({
                'title': title,
                'date': start_date,
                'hour': event_hour,
                'location': location,
                'category': category
            })

        return event_list

    except Exception as e:
        return []

# Função para obter dados meteorológicos
def get_weather_data():
    url = "https://www.accuweather.com/pt/pt/aveiro/271914/daily-weather-forecast/271914"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        daily_card = soup.find('div', class_='daily-wrapper')

        if daily_card:
            day_info = daily_card.find('h2', class_='date')
            temp = daily_card.find('div', class_='temp')
            high_temp = temp.find('span', class_='high').get_text(strip=True) if temp else 'Temp alta não encontrada'
            low_temp = temp.find('span', class_='low').get_text(strip=True) if temp else 'Temp baixa não encontrada'
            precip_element = daily_card.find('div', class_='precip')
            precip_prob = precip_element.get_text(strip=True) if precip_element else 'Probabilidade de precipitação não encontrada'

            return {
                'day_info': day_info.get_text(strip=True) if day_info else 'Dia não encontrado',
                'high_temp': high_temp,
                'low_temp': low_temp,
                'precip_prob': precip_prob
            }

        else:
            return None

    except Exception as e:
        return None
    
#########################################################################################################

# Função para fornecer dados turísticos predefinidos (roteiro)
def get_tourism_data():
    # List of main monuments
    monuments = [
        {
            'name': 'Sé de Aveiro',
            'description': 'A historical cathedral with impressive Baroque architecture.',
            'address': 'R. Batalhão Caçadores 10, 3810-164 Aveiro'
        },
        {
            'name': 'Fórum Aveiro',
            'description': 'A popular shopping mall in the city center, known for its open-air spaces and modern design.',
            'address': 'R. de Viseu 1, 3800-230 Aveiro'
        },
        {
            'name': 'Museu de Aveiro',
            'description': 'Museum housed in a former convent, featuring art and historical exhibits about Aveiro.',
            'address': 'Av. Santa Joana Princesa, 3810-329 Aveiro'
        }
    ]

    # List of museums
    museums = [
        {
            'name': 'Museu Marítimo de Ílhavo',
            'description': 'Dedicated to Aveiro’s maritime history and fishing traditions, with exhibitions on cod fishing.',
            'address': 'Av. Dr. Rocha Madahil, 3830-193 Ílhavo'
        },
        {
            'name': 'Museu Arte Nova',
            'description': 'Art Nouveau museum located in a historical building, showcasing a variety of period artworks.',
            'address': 'R. Dr. Barbosa de Magalhães 9-11, 3800-154 Aveiro'
        }
    ]

    # List of popular restaurants
    restaurants = [
        {
            'name': 'Salpoente',
            'type': 'Gourmet Seafood',
            'address': 'Cais de São Roque 83, 3800-256 Aveiro'
        },
        {
            'name': 'O Bairro',
            'type': 'Traditional Portuguese',
            'address': 'R. António Cândido Pinto 7, 3800-139 Aveiro'
        },
        {
            'name': 'Cais Madeirense',
            'type': 'Madeiran Cuisine',
            'address': 'Largo do Rossio 1, 3800-246 Aveiro'
        }
    ]

    # List of things to do
    activities = [
        {
            'name': 'Passeio de Moliceiro',
            'description': 'Take a boat trip through the canals of Aveiro in a traditional Moliceiro, discovering the "Venice of Portugal".'
        },
        {
            'name': 'Visitar a Praia da Barra',
            'description': 'Relax at the Praia da Barra, known for its iconic lighthouse and beautiful long stretch of beach.'
        },
        {
            'name': 'Explorar as Salinas de Aveiro',
            'description': 'Visit the salt pans and learn about traditional salt extraction methods that date back centuries.'
        }
    ]

    return {
        'monuments': monuments,
        'museums': museums,
        'restaurants': restaurants,
        'activities': activities
    }


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

# Interface do Streamlit com Emojis ✨
st.title("✨ Sugestões de Pesquisas ✨")

# Barra de pesquisa
st.write("Pesquise sobre qualidade do ar, eventos ou meteorologia:")
search_query = st.text_input("Digite sua pesquisa:")

# Placeholder para a resposta da pesquisa
if search_query:
    search_response = handle_search(search_query)
    st.write(search_response)

st.write("Escolha uma opção para visualizar as informações:")
col1, col2, col3, col4, col5 = st.columns(5)

# Placeholder para exibir transições
placeholder = st.empty()


# Botão para Qualidade do Ar
with col1:
    if st.button("Qualidade do Ar"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("Índice de Qualidade do Ar - Aveiro")
            air_quality, date, aqi_value, quality_type = get_air_quality_data()

            if air_quality != "Erro ao obter os dados":
                st.write(f"🌍 **{air_quality}**")
                st.write(f"📅 Data: {date}")
                st.write(f"🌡️ Índice de Qualidade do Ar: {aqi_value}")
                st.write(f"🔎 Tipo de Qualidade do Ar: {quality_type}")
            else:
                st.error("Erro ao obter os dados de qualidade do ar.")

# Botão para Eventos
with col2:
    if st.button("Eventos"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("📅 Eventos em Aveiro")
            events = get_aveiro_events()

            if events:
                for event in events:
                    st.write(f"🎉 **Título**: {event['title']}")
                    st.write(f"📆 **Data**: {event['date']}")
                    st.write(f"⏰ **Hora**: {event['hour']}")
                    st.write(f"📍 **Local**: {event['location']}")
                    st.write(f"🏷️ **Categoria**: {event['category']}")
                    st.write("---")
            else:
                st.error("Erro ao obter os eventos ou nenhum evento encontrado.")

# Botão para Meteorologia
with col3:
    if st.button("Meteorologia"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🌤️ Previsão do Tempo em Aveiro")
            weather = get_weather_data()

            if weather:
                st.write(f"📅 **Dia**: {weather['day_info']}")
                st.write(f"🌡️ **Temperatura Máxima**: {weather['high_temp']}")
                st.write(f"🌡️ **Temperatura Mínima**: {weather['low_temp']}")
                st.write(f"☔ **Probabilidade de Precipitação**: {weather['precip_prob']}")
            else:
                st.error("Erro ao obter os dados meteorológicos.")




with col4:
    with st.container():
        if st.button("Serviços Públicos"):
            placeholder.empty()  # Limpar qualquer conteúdo anterior
            with placeholder.container():
                st.subheader("🏛️ Serviços Públicos")

                # Opções de serviços públicos
                service_options = ["Saúde", "Documentação", "Escola", "Números telefónicos úteis"]
                
                # Permitir seleção de serviço
                selected_service = st.radio("Escolha um serviço:", service_options)

                # Exibição das informações conforme a opção escolhida
                if selected_service == "Saúde":
                    st.subheader("🏥 Serviços de Saúde")
                    st.write("📞 Em caso de emergência, ligue para o número: **SNS 24 - 808 24 24 24**")
                    st.write("🏥 **Hospitais Públicos em Aveiro:**")
                    st.write("1. **Hospital Infante D. Pedro** - Avenida da República, 3810-200 Aveiro")
                    st.write("2. **Hospital de São Sebastião** - R. Dr. Miguel Bombarda 119, 3800-220 Aveiro")
                    st.write("3. **Centro de Saúde de Aveiro** - R. de São Bernardo, 3810-207 Aveiro")

                elif selected_service == "Documentação":
                    st.subheader("📄 Informações sobre Documentação")
                    st.write("Aqui estão algumas informações sobre serviços de documentação em Aveiro:")
                    st.write("1. **Cartório Notarial:**")
                    st.write("   - Realiza atos notariais, como escrituras e reconhecimento de assinaturas.")
                    st.write("   - Endereço: R. de Viseu, 3800-230 Aveiro")
                    st.write("2. **Conservatória do Registo Civil:**")
                    st.write("   - Trata do registo de nascimentos, casamentos e óbitos.")
                    st.write("   - Endereço: R. de Cinfães, 3800-101 Aveiro")
                    st.write("3. **Câmara Municipal de Aveiro:**")
                    st.write("   - Oferece serviços de licenciamento e documentação municipal.")
                    st.write("   - Endereço: Av. de Portugal, 3800-202 Aveiro")

                elif selected_service == "Escola":
                    st.subheader("🏫 Informações sobre Escolas")
                    st.write("Aqui estão algumas informações sobre escolas públicas, privadas e papelarias em Aveiro.")
                    st.write("1. **Escola Secundária de Aveiro**")
                    st.write("   - Endereço: R. das Olas, 3810-016 Aveiro")
                    st.write("2. **Escola Básica de Cacia**")
                    st.write("   - Endereço: R. da Escola, 3830-070 Cacia")
                    st.write("3. **Papelaria da Praça**")
                    st.write("   - Oferece material escolar e serviços de impressão.")
                    st.write("   - Endereço: Praça do Mercado, 3800-200 Aveiro")

                elif selected_service == "Números telefónicos úteis":
                    st.subheader("📞 Informações sobre Números Telefónicos Úteis")
                    st.write("Aqui estão alguns números telefónicos úteis em Aveiro.")
                    st.write("1. **Polícia:** 112")
                    st.write("2. **Bombeiros:** 117")
                    st.write("3. **Hospital Infante D. Pedro:** 234 420 000")
                    st.write("4. **Centro de Saúde de Aveiro:** 234 424 200")



with col5:
    if st.button("Roteiro Turístico"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🗺️ Roteiro Turístico de Aveiro")
            
            tourism_data = get_tourism_data()
            
            st.write("### 🏛️ Principais Monumentos:")
            for monument in tourism_data['monuments']:
                st.write(f"**{monument['name']}**: {monument['description']}")
                st.write(f"📍 Endereço: {monument['address']}")
                st.write("---")
            
            st.write("### 🖼️ Museus:")
            for museum in tourism_data['museums']:
                st.write(f"**{museum['name']}**: {museum['description']}")
                st.write(f"📍 Endereço: {museum['address']}")
                st.write("---")

            st.write("### 🍽️ Restaurantes Recomendados:")
            for restaurant in tourism_data['restaurants']:
                st.write(f"**{restaurant['name']}** ({restaurant['type']})")
                st.write(f"📍 Endereço: {restaurant['address']}")
                st.write("---")
            
            st.write("### 🎉 Atividades Imperdíveis:")
            for activity in tourism_data['activities']:
                st.write(f"**{activity['name']}**: {activity['description']}")
                st.write("---")
