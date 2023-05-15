import sqlite3

conn = sqlite3.connect('fashion.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS search
               (id INTEGER PRIMARY KEY, userinput TEXT, image TEXT, link TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS user_preferances
                     (preferance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     type TEXT NOT NULL,
                     price_range TEXT NOT NULL,
                     style TEXT NOT NULL,
                     gender TEXT NOT NULL,
                     size_id REAL NOT NULL,
                     FOREIGN KEY (size_id) REFERENCES size (size_id));''')

cur.execute('''CREATE TABLE IF NOT EXISTS database
                     (data_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     type TEXT NOT NULL,
                     price_range TEXT NOT NULL,
                     style TEXT NOT NULL,
                     gender TEXT NOT NULL,
                     size_id REAL NOT NULL,
                     FOREIGN KEY (size_id) REFERENCES size (size_id));''')

cur.execute('''CREATE TABLE IF NOT EXISTS size
                     (size_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     length_size INTEGER NOT NULL,
                     bust_size INTEGER NOT NULL,
                     shoulder INTEGER NOT NULL,
                     sleeve_size INTEGER NOT NULL);''')


cur.execute("INSERT INTO users (id) VALUES (2)")
cur.execute("INSERT INTO users (userinput) VALUES ('female, coat, S, beige, solid color')")
cur.execute("INSERT INTO stored_data (data) VALUES ('https://www.nudiejeans.com/product/ester-coat-beige?cjevent=aa1ccde3ee1e11ed8203a8210a18b8fa&utm_source=CJ&utm_medium=default&utm_campaign=Skimlinks&utm_content=100029023')")

cur.execute("UPDATE users SET id = 1 WHERE userinput = 'female, coat, S, beige, solid color'")


conn.commit()

print("Updated data:")
rows = cur.execute("SELECT * FROM users")
for row in rows:
    print(row)

conn.commit()

rows = cur.execute("SELECT * FROM users")
for row in rows:
    print(row)

conn.close()
