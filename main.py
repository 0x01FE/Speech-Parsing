import sqlite3 as sql
import sql_commands as sqlcmd

conn = sql.connect("words.db")



class SpeechParser:
	def __init__(self, name):
		self.name = name
		self.current_user = None
		
	def process_message(self, message):
		message = message.split(".")
		for sentence in message:
			sentence_words = sentence.split(" ")
			for word in sentence_words:
				word_data = sqlcmd.find_word(conn,word)
				question_flag = True
				for key in word_data:
					if word_data[key]:
						question_flag = False
				if question_flag:
					self.ask_question(word)


	def ask_question(self,word):
		print(f'I do not know {word}.')
		table = input(f'Is {word} a noun, verb, adjective, or adverb? ') + 's'
		associations = input(f'can you associate {word} for me? ')
		sqlcmd.add_word(conn,table,(word,associations))



Mel = SpeechParser("Mel")
while True:
	Mel.process_message(input())




















