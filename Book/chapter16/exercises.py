import sqlite3

conn = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/example.db",
    isolation_level=None,
)
# print(conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall())

# conn.execute("INSERT INTO cats VALUES ('Perseo', '1997-01-24', 'orange', 10)")

# # Fuck hackers
# cat_name = "Ranger"
# cat_birthday = "1990-12-12"
# fur_color = "black"
# cat_weight = 12
# conn.execute(
#     "INSERT INTO cats VALUES (?,?,?,?)",
#     [
#         cat_name,
#         cat_birthday,
#         fur_color,
#         cat_weight,
#     ],
# )

print(conn.execute("SELECT * FROM cats").fetchall())
print(conn.execute("SELECT rowid,name FROM cats").fetchall())
print(conn.execute("SELECT * FROM cats ORDER BY name asc").fetchall())

all_cats = conn.execute("SELECT * FROM cats ORDER BY name asc")
for cat in all_cats:
    print(f"Name: {cat[0]}, Birthdate: {cat[1]}, Fur: {cat[2]}, Weight: {cat[3]}")

import pprint

pprint.pprint(
    conn.execute("SELECT * FROM cats WHERE fur = 'black' ORDER BY name ASC").fetchall()
)
