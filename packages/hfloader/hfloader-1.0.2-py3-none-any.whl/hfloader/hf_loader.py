import transformers

'''
Finds the HuggingFace AutoClass that is needed for loading the model
'''
def find_auto_class(model_name, verbose=False):
	config = transformers.AutoConfig.from_pretrained(model_name)                     #  Loads the config of the model from the HuggingFace transformers package

	try:                                                                             #  Try statement to ensure that all errors will be handeled
		architecture = config.architectures[0]                                       #  Gets the architecture of the model


		if architecture.find("For") != -1:                                           #  Checks to see if model contains keyword 'For' 
			architecture = "AutoModel" + architecture[architecture.find("For"):]     #  If so, then it replaces everything before the keyword with 'AutoModel'	
		elif architecture.find("Model") != -1:                                       #  Checks to see if the model contains the keyword 'Model'
			architecture = "AutoModel" + architecture[architecture.find("Model"):]   #  If so, then it replaces everything before the keyword with 'AutoModel'
		else:
			raise Exception("Architecture is not recognized by the package")         #  Raise an exception is neither keyword is found
	

		return architecture                                                          #  Returns the correct AutoClass model as a string


	except Exception as e:                                                           #  Handles an error should it occur
		if verbose: print(e)                                                         #  If verbosity is desired, it will print the error
		print("Model architecture was not found or model has been depreciated")      #  Custom error saying that the models architecture was not found or has been depreciated 
		exit()                                                                       #  Exits the script


'''
Loads the HuggingFace Tokenizer and Model
'''
def load_model(model_name, verbose=False):
	print("Loading Model")                                                           #  Output for user


	try:                                                                             #  Try statement to ensure that all errors will be handeled
		auto_class = getattr(transformers, find_auto_class(model_name, verbose))     #  Get the AutoClass associated with the model, and get that associated attribute function from the transformers package

	except Exception as e:                                                           #  Handles an error should it occur
		if verbose: print(e)                                                         #  If verboisty is desired, it will print the error
		print("Invalid model architecture or model has been depreciated")            #  Custom error saying that the models architecture is invalid or depreciated
		exit()                                                                       #  Exits the script


	tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)               #  Loads the tokenizer from HuggingFace Model Hub
	print("Loaded tokenizer")                                                        #  Output for user
	
	model = auto_class.from_pretrained(model_name)       #  Loads the model from HuggingFace Model Hub
	print("Loaded Model")                                                            #  Output for user


	return tokenizer, model                                                          #  Returns the tokenizer and model