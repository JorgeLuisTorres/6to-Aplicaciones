import sqlite3

DATABASE_NAME = "torneo_robotica.db"

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inscriptos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_robot TEXT NOT NULL,
            nombre_piloto TEXT NOT NULL,
            escuela TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()