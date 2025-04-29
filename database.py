import sqlite3

def init_db(db_file="tokens.db"):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS tokens (pair_address TEXT PRIMARY KEY)')
        conn.commit()

def token_exists(pair_address, db_file="tokens.db"):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute('SELECT 1 FROM tokens WHERE pair_address = ?', (pair_address,))
        return c.fetchone() is not None

def add_token(pair_address, db_file="tokens.db"):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO tokens (pair_address) VALUES (?)', (pair_address,))
        conn.commit()
