import sqlite3
from database.users import get_password_hash
from database.queries import insert_user_query, create_user_query

user = (1, "test", "test@test.com", "admin", get_password_hash("test"))

conn = sqlite3.connect("kidscamp.db")

cursor = conn.cursor()
cursor.execute(create_user_query)
cursor.execute(insert_user_query, user)

conn.commit()
conn.close()