import sqlite3

conn = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/example.db",
    isolation_level=None,
)
print(conn.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall())
