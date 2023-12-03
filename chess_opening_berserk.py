import berserk 
from datetime import datetime
import pandas as pd 


token = "lip_n4KvBbyt6oxi2DBmCKZY"
session = berserk.TokenSession(token)
client = berserk.Client(session=session)

def opening_times_played(user , op) -> str:
	start = berserk.utils.to_millis(datetime(2023, 11, 1))

	end = berserk.utils.to_millis(datetime(2023, 11, 26))

	games = list(client.games.export_by_player(user, since=start, until=end, max=1000))

	z = 0 

	print(len(games))

	opening = op

	for i in range(len(games)): 	    
	    game_id = games[i]['id']
	    s = client.games.export(game_id)
	    if op == s['opening']["name"]:
	        z = z + 1
	return z
def extract_stats(user):
	start = berserk.utils.to_millis(datetime(2023, 9, 1))
	end = berserk.utils.to_millis(datetime(2023, 12, 1))
	data_list = list(client.games.export_by_player(user, since=start, until=end, max=300))
	wins = 0
	losses = 0
	draws = 0
	for i in data_list:
		if i['status'] == "stalemate" or i['status'] == "draw" : draws += 1
		elif i['winner'] == "white" and i['players']['white']['user']['name'] == user : wins += 1
		else: losses += 1
	data = {'Result': ['Win', 'Draw', 'losses'],
            'Count': [wins,draws,losses]}
	df = pd.DataFrame(data)
	return df , data_list
def collect_speed(L , username):
    
    results = {'blitz': {"wins": 0, "draws": 0, "losses": 0}, 'rapid': {"wins": 0, "draws": 0, "losses": 0}, "classical": {"wins": 0, "draws": 0, "losses": 0}, "bullet": {"wins": 0, "draws": 0, "losses": 0}}

    
    for i in L:
        speed = i["speed"]
        if speed == "blitz":            
            if i['status'] == "stalemate" or i['status'] == "draw" : results["blitz"]["draws"] += 1
            elif i['winner'] == "white" and i['players']['white']['user']['name'] == username : results["blitz"]["wins"] += 1
            else: results["blitz"]["losses"] += 1
        elif speed == "rapid":
            if i['status'] == "stalemate" or i['status'] == "draw" : results["rapid"]["draws"] += 1
            elif i['winner'] == "white" and i['players']['white']['user']['name'] == username : results["rapid"]["wins"] += 1
            else: results["rapid"]["losses"] += 1
        elif speed == "classical":
            if i['status'] == "stalemate" or i['status'] == "draw" : results["classical"]["draws"] += 1
            elif i['winner'] == "white" and i['players']['white']['user']['name'] == username : results["classical"]["wins"] += 1
            else: results["classical"]["losses"] += 1
        elif speed == "bullet":
            if i['status'] == "stalemate" or i['status'] == "draw" : results["bullet"]["draws"] += 1
            elif i['winner'] == "white" and i['players']['white']['user']['name'] == username : results["bullet"]["wins"] += 1
            else: results["bullet"]["losses"] += 1
    
    qq = pd.DataFrame(results)
    qq = qq.T
    qq['total'] = qq['wins'] + qq['draws'] + qq['losses']
    return qq