import sqlite3
import os

print("Generating database...")
conn = sqlite3.connect('module.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS categories
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE)''')
c.execute('''CREATE TABLE IF NOT EXISTS files
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                size INTEGER DEFAULT 0,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id))''')

# insert all folders into categories table
for folder in os.listdir(os.getcwd()):
    if os.path.isdir(folder):
        c.execute("INSERT INTO categories (name) VALUES (?)", (folder,))
        conn.commit()
        category_id = c.lastrowid
        for file in os.listdir(folder):
            file_path = folder+'/'+file
            if os.path.isfile(file_path):
                c.execute("INSERT INTO files (name, size, category_id) VALUES (?, ?, ?)", (file, os.path.getsize(file_path), category_id))
                conn.commit()
    