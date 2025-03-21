import sqlite3

class EntrepriseModel:
    def __init__(self):
        self.conn = sqlite3.connect('registre_commerce.db')  # SQLite uses a file for the database
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS entreprises (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nom_Entreprise TEXT NOT NULL,
            Num_Registre TEXT NOT NULL UNIQUE,
            Adresse TEXT,
            Email TEXT,
            Telephone TEXT,
            Date_inscription TEXT,  -- SQLite stores dates as TEXT
            Secteur_Activite TEXT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ajouter_entreprise(self, nom, num_registre, adresse, email, telephone, date_inscription, secteur_activite):
        query = """
        INSERT INTO entreprises (Nom_Entreprise, Num_Registre, Adresse, Email, Telephone, Date_inscription, Secteur_Activite)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (nom, num_registre, adresse, email, telephone, date_inscription, secteur_activite))
        self.conn.commit()

    def rechercher_entreprise(self, critere):
        query = """
        SELECT * FROM entreprises
        WHERE Nom_Entreprise LIKE ? OR Num_Registre LIKE ?
        """
        self.cursor.execute(query, (f"%{critere}%", f"%{critere}%"))
        return self.cursor.fetchall()

    def supprimer_entreprise(self, entreprise_id):
        query = """
        DELETE FROM entreprises
        WHERE Id = ?
        """
        self.cursor.execute(query, (entreprise_id,))
        self.conn.commit()

    def lire_entreprises(self):
        query = "SELECT * FROM entreprises"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
