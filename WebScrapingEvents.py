import requests
from bs4 import BeautifulSoup

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

        # Extrair a data e hora de início
        start_time_element = event.find('time', itemprop='startDate')
        start_time = start_time_element['datetime'] if start_time_element else 'Data de início não encontrada'

        # Extrair a hora do evento
        event_hour_element = event.find('div', class_='viral-event-hour')
        event_hour = event_hour_element.get_text(strip=True) if event_hour_element else 'Hora não encontrada'

        # Extrair o local
        location_element = event.find('a', itemprop='location')
        location = location_element.get_text(strip=True) if location_element else 'Local não encontrado'

        # Exibir as informações do evento
        print(f"Título: {title}")
        print(f"Data e Hora de Início: {start_time}")
        print(f"Hora do Evento: {event_hour}")
        print(f"Local: {location}")
        print("-" * 40)  # Separador entre eventos
else:
    print(f"Falha ao recuperar a página da web. Código de status: {response.status_code}")
