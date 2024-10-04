#import the llama.cpp pakage 
from llama_cpp import Llama
from functions_helper import *
import requests
from bs4 import BeautifulSoup

#load model
llm = Llama(model_path="T.E-8.1.i1-Q4_K_M.gguf", chat_format="llama-2", n_ctx = 2024, max_tokens= 2024)

#for the model to have memory
conversation_history_list = []

#max number of responses that the model remeber
#max_memory = 3


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
        				{"role": "system", "content": f"  O teu objetivo é formular uma resposta informativa que deve apenas abordar as seguintes noticias: {str_facebook}  . Notes: End your responses with '__' "},
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
        				{"role": "system", "content": f"  O teu objetivo é simplesmente dar a informação do estado to tempo e do ar descritas aqui: {new_tempo}  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	
	return model_tempo['choices'][0]['message']['content']






def get_general_information(prompt):

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





def get_bot_ultimate_response(prompt):


	model_output = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"O teu objetivo é interpretar o imput do utilizador e fazer uma tarefa, sinalizar a respostas entre as seguintes opções: XXXX se o input se refere a informações gerais sobre aveiro, YYYY se o input quer saber sobre notícias ou possiveis fatores que condicionem a condução em certas zonas da cidade, ZZZZ se é um pedido relacionado com eventos a decorrer na cidade, VVVVV se é um pedido de como esta o tempo na cidade, FFFF se o utilizador pede imformação do facebook, OOOO se nehum de outros pontos. Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"] #custume character to terminate generation or it goes forever...

		)

	
	response = model_output['choices'][0]['message']['content']

	final_response = ""


	if "XXXX" in response:
		final_response = get_general_information( response )
	elif "YYYY" in response:

		new_headers_list = get_nocicias_aveiro_news()

		final_response = get_relevant_topics_from_news(response, new_headers_list)
	elif "OOOO" in response:
		final_response = get_bot_assistant( response )
	elif "ZZZZ" in response:
		event_list =   get_eventos()

		final_response = get_relevant_topics_from_events(response, event_list)
	elif "VVVV" in response:
		str_tempo = get_tempo_scraping()

		final_response = get_tempo(response, str_tempo)
	elif "FFFF" in response:
		str_facebook = get_facebook_news()

		final_response = get_relevant_topics_from_facebook(response, str_facebook)

	else:
		final_response = "LLM interpretation was wrong or content of the imput is not valid" 
	
	return final_response







# #cicle to generate a conversation
# print("Beginning conversation")
# while True:

# 	#user input
# 	user_input = input("Your anwser (type 'terminate' to leave conversation ): ")

# 	#terminate conversation
# 	if user_input== "terminate":
# 		print("Terminating conversation")
# 		break

# 	else:

# 		#while len(conversation_history_list) > max_memory:
# 		#	conversation_history_list.pop(0)

# 		#conversation_history = ""

# 		#if len(conversation_history_list) > 0:
# 		#	conversation_history = ' '.join(conversation_history_list)


		


# 		#main llm agent
# 		model_output = llm.create_chat_completion(
#     	messages = [
#         				{"role": "system", "content": f"O teu objetivo é interpretar o imput do utilizador e fazer uma tarefa, sinalizar a respostas entre as seguintes opções: XXXX se o input se refere a informações gerais sobre aveiro, YYYY se o input quer saber sobre notícias ou possiveis fatores que condicionem a condução em certas zonas da cidade, ZZZZ se é um pedido relacionado com eventos a decorrer na cidade, VVVVV se é um pedido de como esta o tempo na cidade, FFFF se o utilizador pede imformação do facebook, OOOO se nehum de outros pontos. Notes: End your responses with '__' "},
#         				{
#            			 	"role": "user",
#             			"content": f"{user_input}"
#         			}
#     				]
#    		,stop=["__"] #custume character to terminate generation or it goes forever...

# 		)



# 		#print the response
# 		response = model_output['choices'][0]['message']['content']

# 		final_response = ""


# 		if "XXXX" in response:
# 			final_response = get_general_information( response )
# 		elif "YYYY" in response:

# 			new_headers_list = get_nocicias_aveiro_news()

# 			final_response = get_relevant_topics_from_news(response, new_headers_list)
# 		elif "OOOO" in response:
# 			final_response = get_bot_assistant( response )
# 		elif "ZZZZ" in response:
# 			event_list =   get_eventos()

# 			final_response = get_relevant_topics_from_events(response, event_list)
# 		elif "VVVV" in response:
# 			str_tempo = get_tempo_scraping()

# 			final_response = get_tempo(response, str_tempo)
# 		elif "FFFF" in response:
# 			str_facebook = get_facebook_news()

# 			final_response = get_relevant_topics_from_facebook(response, str_facebook)

# 		else:
# 			final_response = "LLM interpretation was wrong or content of the imput is not valid" 

# 		print("Model response:")
# 		print(final_response)

# 		#add user input and anwser to history
# 		#conversation_history_list.append(user_input)
# 		#conversation_history_list.append(response)


