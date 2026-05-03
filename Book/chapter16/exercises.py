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

print(conn.execute("SELECT * FROM cats LIMIT 3").fetchall())
print(conn.execute("SELECT rowid,name FROM cats").fetchall())
print(conn.execute("SELECT * FROM cats ORDER BY name asc").fetchall())

all_cats = conn.execute("SELECT * FROM cats ORDER BY name asc")
for cat in all_cats:
    print(f"Name: {cat[0]}, Birthdate: {cat[1]}, Fur: {cat[2]}, Weight: {cat[3]}")

import pprint

pprint.pprint(
    conn.execute("SELECT * FROM cats WHERE fur = 'black' ORDER BY name ASC").fetchall()
)

conn.execute("CREATE INDEX idx_name ON cats (name)")
conn.execute("DROP INDEX idx_name")

conn.execute("CREATE INDEX idx_birthdate ON cats (birthdate)")
conn.execute("DROP INDEX idx_birthdate")

conn.execute("UPDATE cats SET fur = 'black' WHERE name = 'Perseo'")
conn.execute("UPDATE cats SET weight_kg = 10")

# It may seem silly to have a superfluous WHERE 1 at the end of your query, but it lets you avoid dangerous bugs that could easily wipe out real data.
conn.execute('UPDATE cats SET name = "Goku" where name = "Zophie"')
conn.execute("DELETE FROM cats where rowid = 2")

# Connection with roll back
conn.execute("BEGIN")

# conn.execute("INSERT INTO cats VALUES ('Socks', '2022-04-04', 'white', 4.2)")
# conn.execute("INSERT INTO cats VALUES ('Fluffy', '2022-10-30', 'gray', 4.5)")

# conn.rollback()
conn.commit()

backup_conn = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/backup.db",
    isolation_level=None,
)

conn.backup(backup_conn)

# conn.execute("ALTER TABLE cats RENAME TO felines")

# conn.execute("ALTER TABLE cats ADD COLUMN is_loved INTEGER DEFAULT 1")
# conn.execute("ALTER TABLE cats RENAME COLUMN fur TO description")
# conn.execute("ALTER TABLE cats DROP COLUMN is_loved")

conn.execute(
    "CREATE TABLE IF NOT EXISTS vaccinations (vaccine TEXT, date_administered TEXT, administered_by TEXT, cat_id INTEGER, FOREIGN KEY(cat_id) REFERENCES cats(rowid)) STRICT"
)

# conn.execute("INSERT INTO vaccinations VALUES ('rabies', '2023-06-06', 'Dr. Echo', 1)")
# conn.execute("INSERT INTO vaccinations VALUES ('Felv', '2023-06-06', 'Dr. Echo', 1)")

print(conn.execute("SELECT * FROM vaccinations").fetchall())

# In-memory database
memory_db_conn = sqlite3.connect(":memory:", isolation_level=None)
memory_db_conn.execute("CREATE TABLE test (name TEXT, number REAL)")
memory_db_conn.execute("INSERT INTO test VALUES ('foo', 3.14)")
file_db_conn = sqlite3.connect("test.db", isolation_level=None)
memory_db_conn.backup(file_db_conn)

# Loading database into in-memory
file_db_conn = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/example.db"
)
memory_db_conn = sqlite3.connect(":memory:", isolation_level=None)
file_db_conn.backup(memory_db_conn)
print(memory_db_conn.execute("SELECT * FROM cats").fetchall())

# Database to queries
conn = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/example.db",
    isolation_level=None,
)
with open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/database_queries.txt",
    "w",
) as file_obj:
    for line in file_db_conn.iterdump():
        file_obj.write(line + "\n")
