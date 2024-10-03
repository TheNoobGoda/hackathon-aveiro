#import the llama.cpp pakage 
from llama_cpp import Llama
#load model
llm = Llama(model_path="T.E-8.1.i1-Q6_K.gguf", chat_format="llama-2", n_ctx = 2024, max_tokens= 2024)

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


def get_relevant_topics_from_events(prompt, new_headers_list): ####### preciso alterar
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



def get_relevant_topics_from_news(prompt, new_headers_list): ###### preciso alterar
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






def get_general_information(prompt):
	informacao_aveiro = "(Informação geral) - Aveiro é uma cidade portuguesa, capital do Distrito de Aveiro, na sub-região de Aveiro, na antiga província da Beira Litoral, pertencendo à região do Centro. A cidade possui 62.653 habitantes em 2021 e é sede do Município de Aveiro, que tem uma área total de 197,58 km², 80.978 habitantes em 2021 e uma densidade populacional de 410 hab./km², subdividido em 10 freguesias. O município é limitado a norte pelo município da Murtosa, a nordeste por Albergaria-a-Velha, a leste por Águeda, a sul por Oliveira do Bairro, a sudoeste por Vagos e por Ílhavo e a oeste com o Oceano Atlântico. A cidade é um importante centro urbano, portuário, ferroviário, universitário e turístico. Fica situada a cerca de 63 km a noroeste de Coimbra, 70 km a sul do Porto e 255 km de Lisboa. (história) - Fruto da crise dinástica de 1383–1385, deu-se em Aveiro uma escaramuça entre tropas castelhanas e cavaleiros portugueses da Ordem de Cristo. Junto ao que é hoje a vila de Eixo, 120 cavaleiros comandados por João Cabral enfrentaram uma pequena expedição conjunta de tropas castelhanas com um total de 250 soldados, incluindo cerca de 210 peões e uma mistura de 40 cavaleiros e besteiros, entre eles o galego Juan de Batista. Na manhã de 17 de outubro de 1384, ocorreu a escaramuça, resultando numa vitória decisiva portuguesa. O padre da paróquia fez o sumário da batalha e, embora provavelmente exagerado, afirmou que morreram 46 castelhanos e apenas 7 portugueses. No final do dia, as tropas castelhanas remanescentes bateram em retirada, refugiando-se junto ao que é hoje Vilar Formoso, para mais tarde se juntarem ao exército de Juan I de Castela. Em finais do século XVI e princípios do século XVII, a instabilidade da comunicação entre a Ria e o mar levou ao fecho do canal, impedindo o uso do porto e criando condições de insalubridade devido à estagnação das águas da lagoa. Esses fatores resultaram numa grande diminuição do número de habitantes, muitos dos quais emigraram, fundando póvoas piscatórias ao longo da costa portuguesa, o que provocou uma grave crise económica e social. Curiosamente, durante essa fase de recessão, foi construído, em plena dominação filipina, um dos mais notáveis templos de Aveiro: a Igreja da Misericórdia. Em 1759, por Alvará Real de 11 de abril, D. José I elevou Aveiro a cidade, poucos meses depois de condenar por traição o seu último duque, título criado em 1547 por D. João III. Aveiro foi feita Oficial da Ordem Militar da Torre e Espada, do Valor, Lealdade e Mérito a 29 de março de 1919, e Membro-Honorário da Ordem da Liberdade a 23 de março de 1998. Foi também um dos principais portos envolvidos na pesca do bacalhau durante o período ditatorial. (geografia) - É um município territorialmente descontínuo, visto que compreende algumas ilhas fluviais na Ria de Aveiro e uma porção da península costeira, na freguesia de São Jacinto, com quase 25 km de extensão, que fecha a ria a ocidente. O município tem limites terrestres e aquáticos através da ria com Ílhavo e Murtosa. Faz ainda fronteira com Albergaria-a-Velha, Oliveira do Bairro, Vagos e Águeda. (gastronomia e locais de interece) - Aveiro oferece uma rica variedade de pontos de interesse em diversas categorias. Entre os monumentos e o patrimônio cultural, destacam-se a Sé de Aveiro (Igreja de São Domingos), uma catedral com arquitetura barroca e uma história rica; o Museu de Aveiro (Museu de Santa Joana), um antigo convento dedicado à princesa Santa Joana, com coleções de arte sacra; a Igreja da Misericórdia, uma bela igreja com interiores decorados com azulejos que retratam cenas bíblicas; a Capela de São Gonçalinho, famosa pela festa onde se atiram cavacas do telhado; o Teatro Aveirense, um teatro histórico que continua a receber espetáculos de música, dança e teatro; e a Estação de Comboios de Aveiro, conhecida pelos painéis de azulejos que ilustram cenas da cidade. Na categoria de zonas comerciais e shoppings, o Forum Aveiro destaca-se como um centro comercial ao ar livre, com lojas, restaurantes e uma vista magnífica sobre os canais. O Mercado Manuel Firmino é um mercado tradicional onde se encontram produtos frescos e locais, enquanto a Avenida Dr. Lourenço Peixinho é a principal artéria da cidade, repleta de lojas, cafés e restaurantes. O Glicínias Plaza, por sua vez, é um grande centro comercial com cinemas, lojas de grandes marcas e opções variadas de restauração. No que diz respeito à comida típica de Aveiro, os Ovos Moles são o doce mais emblemático, feito de gemas de ovo e açúcar, envolto em hóstia. Outros pratos típicos incluem as Tripas de Aveiro, uma massa doce recheada com ovos moles; as Enguias, servidas em caldeirada ou fritas; o Bacalhau à Lagareiro, assado no forno com batatas e azeite; e o Arroz de Marisco, um prato de sabor especial devido à proximidade da Ria de Aveiro. Entre as atividades e experiências mais marcantes, os passeios de Moliceiro nos canais permitem explorar a cidade de uma forma única. As Salinas de Aveiro oferecem visitas guiadas, onde é possível aprender sobre a extração de sal e até tomar um banho nas águas salinas. A visita ao Ecomuseu Marinha da Troncalhada explora a história das salinas, enquanto a observação de aves na Ria de Aveiro é ideal para os amantes da natureza. A cidade também oferece uma extensa ciclovia, promovendo o uso de bicicletas como forma de explorar Aveiro de maneira sustentável. Zonas de interesse natural e lazer incluem a Ria de Aveiro, com sua biodiversidade rica e beleza natural; o Jardim Infante Dom Pedro, um grande parque no centro da cidade ideal para relaxar; a Costa Nova, famosa pelas casas coloridas (palheiros) e suas belas praias; a Praia da Barra, que abriga o farol mais alto de Portugal; e a Reserva Natural das Dunas de São Jacinto, um espaço protegido perfeito para explorar a flora e fauna locais. O Parque Infante D. Pedro é outro espaço verde icónico da cidade, excelente para passeios e atividades ao ar livre. A Universidade de Aveiro, conhecida pela arquitetura contemporânea, também merece uma visita. Outros pontos de interesse incluem a Fábrica Centro Ciência Viva, um museu interativo de ciência ótimo para famílias e curiosos; o Centro de Congressos de Aveiro, que recebe eventos culturais e empresariais; o Museu da Vista Alegre, em Ílhavo, dedicado à famosa fábrica de porcelana; e o Farol da Barra, o mais alto de Portugal, que oferece uma vista panorâmica incrível. "

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
        				{"role": "system", "content": f"  Tu és um assistente, que tem o objetivo de auxiliar o user em qualquer pedido  . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{prompt}"
        			}
    				]
   		,stop=["__"]
		)
	return model_3['choices'][0]['message']['content']

#cicle to generate a conversation
print("Beginning conversation")
while True:
	#user input
	user_input = input("Your anwser (type 'terminate' to leave conversation ): ")

	#terminate conversation
	if user_input== "terminate":
		print("Terminating conversation")
		break
	else:
		#while len(conversation_history_list) > max_memory:
		#	conversation_history_list.pop(0)

		#conversation_history = ""

		#if len(conversation_history_list) > 0:
		#	conversation_history = ' '.join(conversation_history_list)

		#main llm agent
		model_output = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"O teu objetivo é interpretar o input do utilizador e fazer uma tarefa, sinalizar a respostas entre as seguintes opções: XXXX se o input se refere a informações gerais sobre aveiro, YYYY se o input quer saber de possiveis eventos recentes, noticias ou possiveis fatores que condicionem a condução em certas zonas da cidade, ZZZZ se é um pedido relacionado com eventos a decorrer na cidade, VVVVV se é um pedido de como está o tempo na cidade, OOOO se nehum de esses pontos. Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{user_input}"
        			}
    				]
   		,stop=["__"] #custom character to terminate generation or it goes forever...

		)
		
		#print the response
		response = model_output['choices'][0]['message']['content']

		final_response = ""

		if "XXXX" in response:
			final_response =
		elif "YYYY" in response:
			final_response =
		elif "OOOO" in response:
			final_response = 
		elif "ZZZZ" in response:
			final_response = 
		elif "VVVV" in response:
			final_response = 
		else:
			final_response = "LLM interpretation was wrong or content of the imput is not valid" 

		#print("Model response:")
		#print(response)

		#add user input and anwser to history
		#conversation_history_list.append(user_input)
		#conversation_history_list.append(response)


