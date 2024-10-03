from llama_cpp import Llama

# Load the model
model_path = "C:/UNIVERSIDADE/Meta-Llama-3.1-8B-Instruct-Q6_K.gguf"
llm = Llama(model_path=model_path, chat_format="llama-2")

conversation_history_list = []

#max number of responses that the model remeber
max_memory = 10

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

		while len(conversation_history_list) > max_memory:
			conversation_history_list.pop(0)

		conversation_history = ""

		if len(conversation_history_list) > 0:
			conversation_history = ' '.join(conversation_history_list)


		model_output = llm.create_chat_completion(
    	messages = [
        				{"role": "system", "content": f"You are an objective assistant that helps in any topic. Conversation history: {conversation_history} . Notes: End your responses with '__' "},
        				{
           			 	"role": "user",
            			"content": f"{user_input}"
        			}
    				]
   		,stop=["__"] #custume character to terminate generation or it goes forever...

		)

		#print the response
		response = model_output['choices'][0]['message']['content']
		print("Model response:")
		print(response)

		#add user input and anwser to history
		conversation_history_list.append(user_input)
		conversation_history_list.append(response)