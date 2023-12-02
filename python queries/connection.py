import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="football",
    user="postgres",
    password="2110"
)

def get_coaches_of_match(match_id, team_name):
    with conn.cursor() as cursor:
        query = "SELECT c.first_name || ' ' || c.last_name AS coach_name " \
                "FROM public.matches m " \
                "JOIN public.teams t ON m.home_team = t.name OR m.away_team = t.name " \
                "JOIN public.coaches c ON t.team_id = c.team_id " \
                "WHERE m.match_id = %s AND t.name = %s"
        cursor.execute(query, (match_id, team_name))
        results = cursor.fetchall()
        if results:
            coaches = [result[0] for result in results]
            return "Coaches: " + ", ".join(coaches)
        else:
            return "No coaches found for the given match."

match_id = 52
team_name = "PAOK MANDRAS"
result = get_coaches_of_match(match_id, team_name)
print(result)

conn.close()
