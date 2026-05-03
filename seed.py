import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM events")
db.execute("DELETE FROM comments")

user_count = 1000
event_count = 10**5
comment_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username) VALUES (?)",
               ["user" + str(i)])

for i in range(1, event_count + 1):
    user_id=random.randint(1, user_count)
    description=random.randint(1,comment_count)
    db.execute("INSERT INTO events (event_name, date_time, description, user_id) VALUES (?,datetime('now'),?,?)",
               ["event" + str(i), description,user_id])

for i in range(1, comment_count + 1):
    user_id = random.randint(1, user_count)
    event_id = random.randint(1, event_count)
    db.execute("""INSERT INTO comments (content, user_id, event_id)
                  VALUES (?, ?, ?)""",
               ["comment" + str(i), user_id, event_id])

db.commit()
db.close()