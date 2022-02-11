from chatterbot import ChatBot  # Import "chatbot" from   # chatterbot package.

from chatterbot.trainers import ChatterBotCorpusTrainer  #Inorder to train our bot, we have  # to import a trainer package   # "ChatterBotCorpusTrainer"

chatbot=ChatBot('corona bot') #give name

trainer = ChatterBotCorpusTrainer(chatbot) #Create a new trainer for the chatbot

trainer.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations" ) #Now let us train our bot with multiple corpus

response = chatbot.get_response('What is your Number')
print(response)

response = chatbot.get_response('Who are you?')
print(response)
