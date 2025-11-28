from flask import Flask
import pymysql

# Connexion à une base MySQL avec des valeurs DIFFERENTES de l'examen
connection = pymysql.connect(
    host="127.0.0.1",
    user="admin",
    password="root",
    database="eval",
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection:
        with connection.cursor() as cursor:
            # Exemple : création d'une table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produits (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(255),
                    prix DECIMAL(10,2)
                )
            """)

            # Exemple : insertion d'une ligne
            cursor.execute(
                "INSERT INTO produits (nom, prix) VALUES (%s, %s)",
                ("Clavier mécanique", 79.99)
            )
            connection.commit()

            # Exemple : sélection
            cursor.execute("SELECT * FROM produits")
            result = cursor.fetchall()

            print("Résultat de la requête SELECT :")
            for row in result:
                print(row)

except Exception as e:
    print("Erreur :", e)

app = Flask(__name__)
@app.route("/")
def hello_world():
    return f"<p>Hello World!</p>"

@app.route("/health")
def health():
    return {'status':'ok'}

if __name__  == "__main__":
    app.run("0.0.0.0", port=5000)
