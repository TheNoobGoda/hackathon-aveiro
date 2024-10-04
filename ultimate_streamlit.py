#import the llama.cpp pakage 
from llama_cpp import Llama
from functions_helper import *
import requests
from bs4 import BeautifulSoup
import streamlit as st
from LLM_setup import get_bot_ultimate_response
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
from collections import Counter
nltk.download('stopwords')

#load model
llm = Llama(model_path="T.E-8.1.i1-Q4_K_M.gguf", chat_format="llama-2", n_ctx = 2500, max_tokens= 2024)

#for the model to have memory
conversation_history_list = []

#max number of responses that the model remeber
#max_memory = 3


###################

# Load and preprocess the data
def load_prompts(json_file="sample_json.json"):
    with open(json_file, "r") as file:
        data = json.load(file)
    return [entry['prompt'] for entry in data]

# Function to process text and remove stopwords
def preprocess_text(text):
    stop_words = set(stopwords.words('portuguese'))  # Assuming prompts are in Portuguese
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    return filtered_words

# Keyword frequency analysis
def keyword_analysis(prompts):
    all_words = []
    for prompt in prompts:
        all_words.extend(preprocess_text(prompt))
    word_counts = Counter(all_words)
    return word_counts

# Function to categorize prompts by theme
def categorize_prompts(prompts):
    themes = {
        'trânsito': ['trânsito', 'congestionamento', 'acidente', 'estrada', 'tráfego'],
        'eventos': ['evento', 'festival', 'concerto', 'exposição', 'show'],
        'turismo': ['turista', 'museu', 'atração', 'pontos turísticos', 'sítio']
    }
    
    theme_counts = {theme: 0 for theme in themes}
    
    for prompt in prompts:
        words = preprocess_text(prompt)
        for theme, keywords in themes.items():
            if any(word in keywords for word in words):
                theme_counts[theme] += 1
    
    return theme_counts






####################


def get_relevant_topics_from_news(prompt, new_headers_list):

	noticias = new_headers_list

	noticias_formatadas = "\n".join([f"{i+1} - {noticia.strip()}" for i, noticia in enumerate(noticias)])

	model_1 = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"  O teu objetivo é formular uma resposta informativa que deve apenas abordar os titulos de noticias seguintes: {noticias_formatadas}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_1['choices'][0]['message']['content']


def get_relevant_topics_from_facebook(prompt, str_facebook):


	model_facebook = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f" O teu objetivo é formular uma resposta informativa respondendo ao user que deve abordar as seguintes noticias: {str_facebook}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_facebook['choices'][0]['message']['content']


def get_relevant_topics_from_events(prompt, events_list): 


	model_events = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"  O teu objetivo é formular uma resposta informativa com base no imput do utilizador em relação a seguinte lista de eventos: {events_list}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_events['choices'][0]['message']['content']



def get_tempo(prompt, new_tempo): 

	

	

	model_tempo = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"  O teu objetivo é informar o utilizador da a informação do estado to tempo e do ar descritas aqui: {new_tempo}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_tempo['choices'][0]['message']['content']






def get_general_information(prompt):

    #informacao_aveiro = "bruh"

    informacao_aveiro = "Aveiro é uma cidade portuguesa localizada na região Centro, sendo a capital do distrito homônimo e parte da sub-região de Aveiro, na antiga província da Beira Litoral. Em 2021, a cidade contava com 62.653 habitantes, sendo a sede de um município com uma área de 197,58 km², uma população total de 80.978 habitantes e uma densidade de 410 hab./km². Aveiro é composta por 10 freguesias e é um importante centro urbano, portuário, ferroviário, universitário e turístico, com ligações próximas a cidades como Coimbra (63 km), Porto (70 km) e Lisboa (255 km). O município faz fronteira com Murtosa, Albergaria-a-Velha, Águeda, Oliveira do Bairro, Vagos, Ílhavo e o Oceano Atlântico. Aveiro tem uma história rica, com episódios marcantes, como a escaramuça em 1384 durante a crise dinástica de 1383-1385, quando tropas portuguesas da Ordem de Cristo enfrentaram e derrotaram uma expedição castelhana. No final do século XVI e início do XVII, a instabilidade no canal que ligava a Ria de Aveiro ao mar causou problemas de salubridade e declínio populacional, levando muitos habitantes a emigrar. Apesar disso, em plena dominação filipina, foi construída a Igreja da Misericórdia, um dos templos mais notáveis da cidade. Em 1759, Aveiro foi elevada à categoria de cidade por D. José I, após a condenação por traição do último duque de Aveiro. Posteriormente, a cidade foi distinguida com importantes condecorações, incluindo ser feita Oficial da Ordem Militar da Torre e Espada em 1919 e Membro-Honorário da Ordem da Liberdade em 1998. Durante o período ditatorial, Aveiro desempenhou um papel importante na pesca do bacalhau. Aveiro é um município territorialmente descontínuo, incluindo algumas ilhas na Ria de Aveiro e uma parte da península de São Jacinto, com cerca de 25 km de extensão, que separa a ria do oceano. Faz fronteira com municípios como Ílhavo, Murtosa, Albergaria-a-Velha, Oliveira do Bairro, Vagos e Águeda, além de possuir limites aquáticos através da ria. A cidade oferece uma vasta gama de atrações culturais, naturais e gastronômicas. Entre os monumentos, destacam-se a Sé de Aveiro, uma catedral de estilo barroco; o Museu de Aveiro, que funciona num antigo convento e preserva a história da princesa Santa Joana; a Igreja da Misericórdia, com interiores decorados com azulejos; e a Capela de São Gonçalinho, conhecida pela festa onde se atiram cavacas do telhado. Outros destaques são o Teatro Aveirense e a Estação de Comboios de Aveiro, famosa pelos seus painéis de azulejos. A gastronomia de Aveiro é marcada pelos Ovos Moles, um doce tradicional feito de gemas de ovo e açúcar. Também se destacam as Tripas de Aveiro, as Enguias (servidas fritas ou em caldeirada), o Bacalhau à Lagareiro e o Arroz de Marisco. A cidade é também conhecida pelos seus mercados e áreas comerciais, como o Forum Aveiro e o Glicínias Plaza. Entre as atividades populares estão os passeios de Moliceiro pelos canais, as visitas às Salinas de Aveiro e ao Ecomuseu Marinha da Troncalhada, e a observação de aves na Ria de Aveiro. Para os amantes da natureza, há espaços como a Reserva Natural das Dunas de São Jacinto e a Ria de Aveiro, com sua biodiversidade. A cidade também promove o uso de bicicletas, com uma extensa ciclovia. Aveiro é cercada por diversas áreas de lazer, como o Jardim Infante Dom Pedro, um parque central ideal para relaxar, e as praias de Costa Nova, famosa pelas suas casas coloridas (palheiros), e Praia da Barra, onde se localiza o farol mais alto de Portugal. Além disso, a cidade abriga a Universidade de Aveiro, reconhecida por sua arquitetura moderna. Outros pontos de interesse incluem a Fábrica Centro Ciência Viva, um museu interativo de ciência, o Centro de Congressos de Aveiro e o Museu da Vista Alegre, em Ílhavo, dedicado à fábrica de porcelana de renome mundial. Em resumo, Aveiro combina história, cultura, natureza e uma gastronomia única, sendo um destino que oferece atividades para todos os gostos, desde o turismo cultural até o ecológico e de lazer."
    model_2 = llm.create_chat_completion(
        messages = [
        				{"role": "system", "content": f"  Tu és um guia geral da cidade chamada Aveiro localizada em portugal. Aqui está variadade de imformações acerca da cidade que podem ser uteis para formular as respostas: {informacao_aveiro}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
    return model_2['choices'][0]['message']['content']


def get_bot_assistant(prompt):

	
	model_3 = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"  Tu é um assistente, que tem o objetivo de auxiliar o user em qualquer pedido  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_3['choices'][0]['message']['content']


#---------------------------------------\ buttoms functions \------------------------


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


# # Title of the chatbot
# st.title("Pergunata-me algo sobre Aveiro :)")

# # Initialize the chat history if not already available
# if "messages" not in st.session_state:
#     st.session_state.messages = []



# # Get user input from Streamlit text input box
# user_input = st.text_input("You: ", "", key="input")

# # When the user provides input, process the chatbot response
# if user_input:
#     # Save the user's message to chat history
#     st.session_state.messages.append({"role": "User", "text": user_input})

#     # Generate bot response
#     bot_response = get_bot_ultimate_response(user_input)
#     st.session_state.messages.append({"role": "Aveiro Bro", "text": bot_response})

#     # Clear the input box after submission (handled by the Streamlit key feature)

# # Display chat history (user and bot messages)
# for message in st.session_state.messages:
#     if message["role"] == "User":
#         st.markdown(f"**You:** {message['text']}")
#     else:
#         st.markdown(f"**Aveiro Bro:** {message['text']}")


# Set the page layout to wide so it looks cleaner
st.set_page_config(layout="wide")

# Title of the chatbot at the top
st.markdown("<h1 style='text-align: center;'>AveiroBuddy</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Olá! Sou o teu novo assistente pessoal, aqui para tornar a tua vida em Aveiro mais simples.</p>", unsafe_allow_html=True)

st.subheader("👋 Em que posso ajudar? 🤓")

# Initialize chat history in session state if it's not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []




# Function to simulate bot response (you can integrate with an actual chatbot later)


# Layout for chat interface
chat_container = st.container()


# Display chat messages in the chat container
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "User":
            st.markdown(f"**You:** {message['text']}")
        else:
            st.markdown(f"**Bot:** {message['text']}")

# Sticky input at the bottom using a form to handle submission
  # Adds a horizontal line separator

# Bottom input area for user's message
with st.form(key='chat_input', clear_on_submit=True):
    user_input = st.text_input("Digite a sua mensagem...", key="input")
    submit_button = st.form_submit_button(label="Send")

# Handle form submission
if submit_button and user_input:
    # Append user input to the message history
    st.session_state.messages.append({"role": "User", "text": user_input})

    # Get bot response
    bot_response = get_bot_ultimate_response(user_input)
    st.session_state.messages.append({"role": "Bot", "text": bot_response})

    # Scroll down to the latest messages
    st.experimental_rerun()  # Refresh the app to display the new messages



st.subheader("✨ Sugestões de Pesquisas ✨")

st.write("Escolha uma opção para visualizar as informações:")

st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)

placeholder = st.empty()




# Botão para Qualidade do Ar
# with col1:
#     if st.button("Qualidade do Ar"):
#         placeholder.empty()  # Limpar qualquer conteúdo anterior
#         with placeholder.container():
#             st.subheader("Índice de Qualidade do Ar - Aveiro")
#             air_quality, date, aqi_value, quality_type = get_air_quality_data()

#             if air_quality != "Erro ao obter os dados":
#                 st.write(f"🌍 **{air_quality}**")
#                 st.write(f"📅 Data: {date}")
#                 st.write(f"🌡️ Índice de Qualidade do Ar: {aqi_value}")
#                 st.write(f"🔎 Tipo de Qualidade do Ar: {quality_type}")
#             else:
#                 st.error("Erro ao obter os dados de qualidade do ar.")

# Botão para Eventos
with col1:
    if st.button("📅 Eventos"):
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
# with col3:
#     if st.button("Meteorologia"):
#         placeholder.empty()  # Limpar qualquer conteúdo anterior
#         with placeholder.container():
#             st.subheader("🌤️ Previsão do Tempo em Aveiro")
#             weather = get_weather_data()

#             if weather:
#                 st.write(f"📅 **Dia**: {weather['day_info']}")
#                 st.write(f"🌡️ **Temperatura Máxima**: {weather['high_temp']}")
#                 st.write(f"🌡️ **Temperatura Mínima**: {weather['low_temp']}")
#                 st.write(f"☔ **Probabilidade de Precipitação**: {weather['precip_prob']}")
#             else:
#                 st.error("Erro ao obter os dados meteorológicos.")
# Botão para Meteorologia e Qualidade do Ar
with col2:
    if st.button("🌤️ Meteorologia"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.subheader("🌤️ Tempo e Qualidade do Ar em Aveiro Atualmente")
            
            # Obter dados meteorológicos
            weather = get_weather_data()

            if weather:
                st.write(f"📅 **Dia**: {weather['day_info']}")
                st.write(f"🌡️ **Temperatura Máxima**: {weather['high_temp']}")
                st.write(f"🌡️ **Temperatura Mínima**: {weather['low_temp']}")
                st.write(f"☔ **Probabilidade de Precipitação**: {weather['precip_prob']}")
            else:
                st.error("Erro ao obter os dados meteorológicos.")

            # Obter dados de qualidade do ar
            air_quality, date, aqi_value, quality_type = get_air_quality_data()

            if air_quality != "Erro ao obter os dados":
                st.write(f"🌡️ Índice de Qualidade do Ar: {aqi_value} - {quality_type}")
            else:
                st.error("Erro ao obter os dados de qualidade do ar.")




with col3:
    with st.container():
        if st.button("🏛️ Serviços Públicos"):
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



with col4:
    if st.button("🗺️ Roteiro Turístico"):
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

 # Navigate to analysis page
with col5:
    if st.button("🔎 Análise das prompts"):
        placeholder.empty()  # Limpar qualquer conteúdo anterior
        with placeholder.container():
            st.title("Análise de Dados AveiroBuddy")

            # Load prompts
            prompts = load_prompts()

            # Keyword Analysis Section
            st.header("Análise de Frequência de Palavras")

            if prompts:
                word_counts = keyword_analysis(prompts)

                # Displaying a histogram
                top_keywords = word_counts.most_common(10)  # Top 10 keywords
                keywords, counts = zip(*top_keywords)

                st.subheader("Palavras Mais Frequentes nos Prompts")

                fig, ax = plt.subplots()
                ax.barh(keywords, counts)
                ax.set_xlabel('Frequência')
                ax.set_title('Palavras Mais Frequentes nos Prompts dos Usuários')
                st.pyplot(fig)

                # Display Word Cloud
                st.subheader("Nuvem de Palavras")
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                st.pyplot(plt)
            else:
                st.write("Nenhum prompt disponível para análise.")

            # Theme Analysis Section
            st.header("Análise de Temas")
            theme_counts = categorize_prompts(prompts)

            # Displaying theme counts
            st.subheader("Temas dos Prompts")
            theme_names, theme_values = zip(*theme_counts.items())

            fig, ax = plt.subplots()
            ax.bar(theme_names, theme_values)
            ax.set_xlabel('Temas')
            ax.set_ylabel('Contagem')
            ax.set_title('Distribuição dos Temas nos Prompts dos Usuários')
            st.pyplot(fig)
