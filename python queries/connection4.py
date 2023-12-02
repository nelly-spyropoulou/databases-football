import psycopg2

# Σύνδεση στη βάση δεδομένων
conn = psycopg2.connect(
    host="localhost",
    database="football",
    user="postgres",
    password="2110"
)

# Εκτέλεση της ερώτησης SQL
desired_team = "ERMIS"  # Αντικαταστήστε με την επιθυμητή ομάδα
query = """
    SELECT
        home_wins AS home_wins,
        away_wins AS away_wins,
        home_losses AS home_losses,
        away_losses AS away_losses,
        home_draws AS home_draws,
        away_draws AS away_draws
    FROM
        teams
    WHERE
        name = %(team)s
"""

# Εκτέλεση της ερώτησης SQL με παράμετρο την επιθυμητή ομάδα
cursor = conn.cursor()
cursor.execute(query, {'team': desired_team})

# Ανάκτηση των αποτελεσμάτων
result = cursor.fetchone()

# Εκτύπωση της αγωνιστικής εικόνας της ομάδας
print("Στατιστικά της ομάδας,",desired_team)
print("Νίκες Εντός:", result[0])
print("Νίκες Εκτός:", result[1])
print("Ήττες Εντός:", result[2])
print("Ήττες Εκτός:", result[3])
print("Ισοπαλίες Εντός:", result[4])
print("Ισοπαλίες Εκτός:", result[5])
print("Συνολικοί Αγώνες:", result[0]+result[1]+result[2]+result[3]+result[4]+result[5])
print("Αγώνες Εντός:", result[0]+ result[2]+result[4])
print("Αγώνες Εκτός:", result[1]+ result[3]+result[5])
print("Συνολικές Νίκες:", result[0]+result[1])
print("Συνολικές Ήττες:", result[2]+ result[3])
print("Συνολικές Ισοπαλίες:", result[4]+result[5])
# Κλείσιμο της σύνδεσης
cursor.close()
conn.close()