import psycopg2

# Συνδεθείτε στη βάση δεδομένων
conn = psycopg2.connect(database="football", user="postgres", password="2110", host="localhost", port="5432")
cur = conn.cursor()

# Ορίστε τον player_id του επιθυμητού παίκτη
player_id = 10  # Αντικαταστήστε το με τον πραγματικό player_id

# Εκτελέστε το ερώτημα SQL
query = "SELECT ms.goals, ms.penalties, ms.yellow_cards, ms.red_cards, p.minutes_played, p.position " \
        "FROM matches m " \
        "JOIN matchstats ms ON m.match_id = ms.match_id " \
        "JOIN players p ON p.player_id = ms.player_id " \
        "WHERE p.player_id = %s"

cur.execute(query, (player_id,))

# Εμφανίστε τα αποτελέσματα
results = cur.fetchall()
for row in results:
    goals, penalties, yellow_cards, red_cards, minutes_played, position = row
    print(f"Γκολ: {goals}, Πέναλτι: {penalties}, Κίτρινες Κάρτες: {yellow_cards}, "
          f"Κόκκινες Κάρτες: {red_cards}, Λεπτά Αγώνα: {minutes_played}, Θέση: {position}")

# Κλείστε τη σύνδεση με τη βάση δεδομένων
cur.close()
conn.close()
