# word_queries.py

GET_WORDS_BY_USER_ID = ("""SELECT * FROM words WHERE user_id=%s""")

INSERT_WORD_INFO = ("""INSERT INTO words (Definition, Meaning, user_id) VALUES (%s, %s, %s)""")

UPDATE_WORD_INFO = ("""UPDATE words SET Definition=%s, Meaning=%s WHERE id=%s""")

DELETE_WORDS_BY_USER_ID = ("""DELETE FROM words WHERE id=%s""")