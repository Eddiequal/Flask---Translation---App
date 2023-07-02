# user_queries.py

GET_USER_BY_USERNAME = ("""SELECT * FROM users WHERE username = %s """)

GET_USER_BY_ID = ("""SELECT * FROM users WHERE id = %s""")

INSERT_USER_INFO = ("""INSERT INTO users (username, password, email) VALUES (%s, %s, %s)""")

GET_USER_BY_EMAIL = ("""SELECT * FROM users WHERE email = %s""")
