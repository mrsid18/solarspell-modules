import sqlite3
import os

if os.path.exists('module.db'):
    print('Old database found, deleting...')
    os.remove('module.db')

print("Generating database...")
conn = sqlite3.connect('module.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS categories
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                parent_id INTEGER,
                path TEXT NOT NULL,
                FOREIGN KEY (parent_id) REFERENCES categories(id))''')
c.execute('''CREATE TABLE IF NOT EXISTS files
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                size INTEGER DEFAULT 0,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id))''')

# insert all folders into categories table
def generate_db(folder_name, folder_path, parent_id=None):
        if os.path.isdir(folder_path):
            c.execute("INSERT INTO categories (name, parent_id, path) VALUES (?, ?, ?)", (folder_name, parent_id, folder_path.replace(root_path, '')))
            conn.commit()
            category_id = c.lastrowid
            for file in os.listdir(folder_path):
                file_path = folder_path+'/'+file
                if os.path.isdir(file_path):
                    generate_db(file, file_path, category_id)
                elif os.path.isfile(file_path):
                    c.execute("INSERT INTO files (name, size, category_id) VALUES (?, ?, ?)", (file, os.path.getsize(file_path), category_id))
                    conn.commit()

root_path = os.getcwd()
for folder in os.listdir(os.getcwd()):
    generate_db(folder, os.getcwd()+"/"+folder)

conn.close()
print("Database generated.")
    