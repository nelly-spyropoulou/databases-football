import psycopg2


host = 'localhost'
database = 'football'
user = 'postgres'
password = '2110'


connection = psycopg2.connect(host=host, database=database, user=user, password=password)


def get_goals_and_penalties(match_id):
    with connection.cursor() as cursor:
        query = "SELECT ms.time_of_event, p.last_name, p.first_name " \
                "FROM matchstats ms " \
                "JOIN players p ON ms.player_id = p.player_id " \
                "WHERE ms.match_id = %s AND (ms.goals > 0 OR ms.penalties > 0)"
        cursor.execute(query, (match_id,))
        result = cursor.fetchall()
        if result:
            return result
        else:
            return "No goals or penalties found for the given match."


match_id = 233  
result = get_goals_and_penalties(match_id)
if isinstance(result, str):
    print(result)
else:
    for event in result:
        event_time = event[0]
        player_name = event[1]
        print(f"{event_time} - {player_name}")


connection.close()
