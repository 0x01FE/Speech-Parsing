CREATE TABLE verbs (
	word TEXT PRIMARY KEY UNIQUE NOT NULL,
	associations TEXT
);
CREATE TABLE nouns (
	word TEXT PRIMARY KEY UNIQUE NOT NULL,
	associations TEXT
);
CREATE TABLE adjectives (
	word TEXT PRIMARY KEY UNIQUE NOT NULL,
	associations TEXT
);
CREATE TABLE  adverbs (
	word TEXT PRIMARY KEY UNIQUE NOT NULL,
	associations TEXT
);
CREATE TABLE people (
	person_name TEXT PRIMARY KEY UNIQUE NOT NULL,
	standing INTEGER NOT NULL,
	associations TEXT
);
CREATE TABLE memory (
	event_name TEXT PRIMARY KEY NOT NULL,
	persons TEXT,
	associations TEXT
);
