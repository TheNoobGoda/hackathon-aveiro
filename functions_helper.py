import requests
from bs4 import BeautifulSoup


def get_tempo_scraping():
    """

    """

    # URL do site AccuWeather para a previsão do tempo em Aveiro utilizando o AccuWeather
    #url = "https://www.accuweather.com/pt/pt/aveiro/271914/daily-weather-forecast/271914"
    url = "https://www.accuweather.com/pt/pt/aveiro/271914/daily-weather-forecast/271914"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    tempo_str = ""

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrair informações meteorológicas
        daily_card = soup.find('div', class_='daily-wrapper')
        if daily_card:
            day_info = daily_card.find('h2', class_='date')
            temp = daily_card.find('div', class_='temp')
            
            # Extrair informações de temperatura
            high_temp = temp.find('span', class_='high').get_text(strip=True) if temp else 'Temp alta não encontrada'
            low_temp = temp.find('span', class_='low').get_text(strip=True) if temp else 'Temp baixa não encontrada'
            
            # Extrair informações de precipitação
            precip_element = daily_card.find('div', class_='precip')
            precip_prob = precip_element.get_text(strip=True) if precip_element else 'Probabilidade de precipitação não encontrada'
            
            #print(f"Dia: {day_info.get_text(strip=True) if day_info else 'Dia não encontrado'}")
            #print(f"Temperatura Máxima: {high_temp}")
            #print(f"Temperatura Mínima: {low_temp}")
            #print(f"Probabilidade de Precipitação: {precip_prob}")



            tempo_str = f"Dia: {day_info.get_text(strip=True) if day_info else 'Dia não encontrado'}, Temperatura Máxima: {high_temp}, Temperatura Mínima: {low_temp}, Probabilidade de Precipitação: {precip_prob}"

        else:
            print("Cartão diário não encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


        # URL do site AccuWeather para o índice de qualidade do ar em Aveiro utilizando o AccuWeather
    url = "https://www.accuweather.com/pt/pt/aveiro/271914/air-quality-index/271914"  
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    qualidade_ar_srt = ""

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrair informações da qualidade do ar
        air_quality_header = soup.find('h2', class_='air-quality-card__header')
        date_wrapper = soup.find('div', class_='date-wrapper')
        aqi_element = soup.find('div', class_='aq-number')
        quality_type_element = soup.find('p', class_='category-text')  

        # Verificar se os elementos foram encontrados e extrair a informação
        air_quality = air_quality_header.get_text(strip=True) if air_quality_header else 'Título não encontrado'
        date = date_wrapper.get_text(strip=True) if date_wrapper else 'Data não encontrada'
        aqi_value = aqi_element.get_text(strip=True) if aqi_element else 'AQI não encontrado'
        quality_type = quality_type_element.get_text(strip=True) if quality_type_element else 'Tipo de qualidade do ar não encontrado' 

        print(f"{air_quality}")
        print(f"Data: {date}")
        print(f"Índice de Qualidade do Ar: {aqi_value}")
        print(f"Tipo de Qualidade do Ar: {quality_type}")


        qualidade_ar_srt = f"Qualidade do ar: { air_quality}, Data: {date}, Índice de Qualidade do Ar: {aqi_value}, Tipo de Qualidade do Ar: {quality_type}    "
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return f"{tempo_str} ,{ qualidade_ar_srt}"



def get_eventos():
    """

    """

        # URL do site onde os eventos estão listados
    url = "https://www.viralagenda.com/pt/aveiro"  

    # Headers para simular uma solicitação de navegador
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    list_events = []

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

            # Extrair o local do evento
            location_element = event.find('a', itemprop='location')
            location = location_element.get_text(strip=True) if location_element else 'Local não encontrado'

            # Extrair a categoria do evento
            category_element = event.find('a', title="Ver eventos desta categoria")
            category = category_element.get_text(strip=True) if category_element else 'Categoria não encontrada'

            list_events.append(f"Título: {title}, Data de Início: {start_date}, Hora do Evento: {event_hour}, Local: {location}, Categoria: {category}")

            #print(f"Título: {title}")
            #print(f"Data de Início: {start_date}")
            #print(f"Hora do Evento: {event_hour}")
            #print(f"Local: {location}")
            #print(f"Categoria: {category}") 
            #print("-" * 40)  # Separador entre eventos
    else:
        print(f"Falha ao recuperar a página da web. Código de status: {response.status_code}")


    return list_events


def get_facebook_news():


    # Replace this with your API token  
    API_TOKEN = 'apify_api_Hui1YjAM1cjLRzmYJ9F65IXyoulxUi4GDNGu'

    # Corrected Actor ID for the Facebook Page Scraper
    ACTOR_ID = 'apify~facebook-posts-scraper'

    # The Facebook page you want to scrape
    START_URL = 'https://www.facebook.com/noticiasdeaveiro/?locale=pt_PT'

    # API endpoint to trigger the scraper
    url = f'https://api.apify.com/v2/acts/{ACTOR_ID}/runs?token={API_TOKEN}'

    # Headers
    headers = {'Content-Type': 'application/json'}

    # Body (scraper configuration)
    payload = {
        "startUrls": [
            { "url": START_URL }
        ],
        "maxPosts": 10,       # Max posts to scrape
        "includeComments": False   # Set to True if you want comments
    }

    # Make the request to start the scraper
    response = requests.post(url, headers=headers, json=payload)

    # Get the run ID from the response
    data = response.json()

    # print(type(data))
    # print("")
    # print(data)


    DATASET_ID = 'HZ2Pb7WSKtphMNyKX'
    API_TOKEN = 'apify_api_Hui1YjAM1cjLRzmYJ9F65IXyoulxUi4GDNGu'

    # API endpoint to get dataset results
    url = f'https://api.apify.com/v2/datasets/{DATASET_ID}/items?token={API_TOKEN}'

    # Make the request to fetch the results
    response = requests.get(url)

    # Get the data in JSON format
    data = response.json()

    ultimate_str = ""

    # Print the titles of the posts

    for post in data:
        # print(post.get('postText', 'No title available'))
        #print("-------------------------------------------------------------------------------------------")

        post_str = ""
        try:
            post_str += "text: " + post['text'] 
        except:
            continue
        
        try:
            post_str += " previewTitle: " + post['previewTitle']
            
        except:
            continue

        try:
            post_str += 'previewDescription: ' + post['previewDescription']
            
        except:
            continue

    
        ultimate_str += post_str +  "\n"
    
    return ultimate_str

	




def get_nocicias_aveiro_news():

    titles_list = []
    url = "https://www.noticiasdeaveiro.pt/category/regiao/aveiro/"
    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    # Send a GET request with headers
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
    # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
    # Find all 'a' tags with class 'td-image-wrap' or 'td-module-thumb'
        titles = soup.find_all('a', class_='td-image-wrap')
    # Loop through and print out each title (from the 'title' attribute or text)
        for title in titles:
            titles_list.append(title['title'])
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return titles_list
	
	
	



# def david():
# 	"""

# 	"""

# 	"""
# 	????
# 	"""