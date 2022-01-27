import sqlite3 as sql

def update_database_schema(conn):
	user_input = input("Are you sure you want to do this? (Y/N)\n")
	if user_input.lower() == "y":
		c = conn.cursor()
		with open("schema.sql",'r') as f:
			c.executescript(f.read())
			
def print_db(conn):
	c = conn.cursor()
	c.execute("SELECT name FROM sqlite_master WHERE type='table';")
	print(c.fetchall())
	
def find_word(conn,word):
	response = {}
	c = conn.cursor()
	c.execute("SELECT * FROM verbs WHERE word = :word",{"word" : word})
	response["verb"] = c.fetchall()
	c.execute("SELECT * FROM nouns WHERE word = :word",{"word" : word})
	response["noun"] = c.fetchall()
	c.execute("SELECT * FROM adjectives WHERE word = :word",{"word" : word})
	response["adjective"] = c.fetchall()
	c.execute("SELECT * FROM adverbs WHERE word = :word",{"word" : word})
	response["adverb"] = c.fetchall()
	return response

def add_word(conn,table,word):
	##input word must be a tuple of WORD and ASSOCIATIONS
	##table should be verbs, nouns, adjectives, or adverbs
	c = conn.cursor()
	if table == "nouns":
		c.execute("INSERT INTO nouns VALUES (:word,:associations)",{"associations" : word[1], "word" : word[0]})
	elif table == "verbs":
		c.execute("INSERT INTO verbs VALUES (:word,:associations)",{"associations" : word[1], "word" : word[0]})
	elif table == "adverbs":
		c.execute("INSERT INTO adverbs VALUES (:word,:associations)",{"associations" : word[1], "word" : word[0]})
	elif table == "adjectives":
		c.execute("INSERT INTO adjectives VALUES (:word,:associations)",{"associations" : word[1], "word" : word[0]})
	conn.commit()
	
def update_word(conn,table,word):
	##input word must be a tuple of WORD and ASSOCIATIONS
	##table should be verbs, nouns, adjectives, or adverbs
	c = conn.cursor()
	c.execute("UPDATE :table\nSET associations = :associations\nWHERE word = :word",{"table" : table, "associations" : word[1], "word" : word[0]})
	
