import requests
from bs4 import BeautifulSoup

# ---------------------------------- Informações sobre os eventos a decorrer em Aveiro ----------------------------------

# URL do site onde os eventos estão listados
url = "https://www.viralagenda.com/pt/aveiro"  

# Headers para simular uma solicitação de navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Enviar uma solicitação GET com cabeçalhos
response = requests.get(url, headers=headers)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os elementos 'li' que contêm os eventos
    events = soup.find_all('li', class_='viral-item')

    # Loop para extrair informações sobre cada evento
    for event in events:
        # Extrair o título do evento
        title_element = event.find('span', itemprop='name')
        title = title_element.get_text(strip=True) if title_element else 'Título não encontrado'

        # Extrair a data do evento
        start_time_element = event.find('time', itemprop='startDate')
        start_date = start_time_element['datetime'].split("T")[0] if start_time_element else 'Data de início não encontrada'

        # Extrair a hora do evento
        event_hour_element = event.find('div', class_='viral-event-hour')
        event_hour = event_hour_element.get_text(strip=True) if event_hour_element else 'Hora não encontrada'

        # Extrair o local
        location_element = event.find('a', itemprop='location')
        location = location_element.get_text(strip=True) if location_element else 'Local não encontrado'

        # Extrair a categoria
        category_element = event.find('a', title="Ver eventos desta categoria")
        category = category_element.get_text(strip=True) if category_element else 'Categoria não encontrada'

        print(f"Título: {title}")
        print(f"Data de Início: {start_date}")
        print(f"Hora do Evento: {event_hour}")
        print(f"Local: {location}")
        print(f"Categoria: {category}") 
        print("-" * 40)  # Separador entre eventos
else:
    print(f"Falha ao recuperar a página da web. Código de status: {response.status_code}")


# -------------------------------------------- Meteorologia em Aveiro -------------------------------------------

# URL do site AccuWeather para a previsão do tempo em Aveiro utilizando o AccuWeather
#url = "https://www.accuweather.com/pt/pt/aveiro/271914/daily-weather-forecast/271914"
url = "https://www.accuweather.com/pt/pt/aveiro/271914/daily-weather-forecast/271914"

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

    # Extrair informações meteorológicas
    date_element = soup.find('p', class_='module-title')
    daily_card = soup.find('div', class_='daily-wrapper')

    # Verificar se os elementos foram encontrados e extrair o texto
    date = date_element.get_text(strip=True) if date_element else 'Data não encontrada'
    
    # Extraindo informações do cartão diário
    if daily_card:
        day_info = daily_card.find('h2', class_='date')
        temp = daily_card.find('div', class_='temp')
        phrase = daily_card.find('div', class_='phrase')
        
        # Extraindo as informações de temperatura
        high_temp = temp.find('span', class_='high').get_text(strip=True) if temp else 'Temp alta não encontrada'
        low_temp = temp.find('span', class_='low').get_text(strip=True) if temp else 'Temp baixa não encontrada'
        
        # Extraindo outras informações
        precip_element = daily_card.find('div', class_='precip')
        precip_prob = precip_element.get_text(strip=True) if precip_element else 'Probabilidade de precipitação não encontrada'
        
        # Exibir as informações meteorológicas
        print(f"Dia: {day_info.get_text(strip=True) if day_info else 'Dia não encontrado'}")
        print(f"Temperatura Máxima: {high_temp}")
        print(f"Temperatura Mínima: {low_temp}")
        print(f"Probabilidade de Precipitação: {precip_prob}")

    else:
        print("Cartão diário não encontrado.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a solicitação: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
#-------------------------------------- Qualidade do ar em Aveiro ----------------------------------------------

# URL do site AccuWeather para o índice de qualidade do ar em Aveiro utilizando o AccuWeather
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
    date = date_wrapper.get_text(strip=True) if date_wrapper else 'Data não encontrada'
    aqi_value = aqi_element.get_text(strip=True) if aqi_element else 'AQI não encontrado'
    quality_type = quality_type_element.get_text(strip=True) if quality_type_element else 'Tipo de qualidade do ar não encontrado' 


    # Exibir as informações de qualidade do ar
    print(f"{air_quality}")
    print(f"Data: {date}")
    print(f"Índice de Qualidade do Ar: {aqi_value}")
    print(f"Tipo de Qualidade do Ar: {quality_type}")
    
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a solicitação: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


