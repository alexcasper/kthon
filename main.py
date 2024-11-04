from update import get_students,retrieve_codewars 
from database import write_profile,write_update,create_team,add_player_to_team,get_teams, show_states, show_player_completions,show_team_players,update_team_score,update_team_name
import random,time

def make_players(players = get_students()):
    for player in players:
        write_profile(player)
        
def check_status(players = get_students(),iteration='0'):
    for player in players:
        user_data,chal_data = retrieve_codewars(player)
        if 'success' in chal_data and chal_data['success']==False:
          print(f'{player} not found')
          write_profile(player,{'status':'not found'})
        elif 'totalItems' in chal_data and chal_data['totalItems']==0:
          print(f'{player} found but no completions')
          write_profile(player,{'status':'not started'})
        elif 'codeChallenges' in user_data:
          print(f"retrieved for {player} - {user_data['codeChallenges']['totalCompleted']} completions")
          write_profile(player,{'status':'active'})
          print(chal_data)
          my_data = {'latest':[item[0] for item in chal_data]}
          print(my_data)
          write_update(player,iteration,data=my_data)
      

def create_teams():
    teams = []
    for team in range(0,9):
      teams.append(create_team(str(team)))
    return teams

def assign_teams(players = get_students(),teams = get_teams()):
    players_shuffled = players.copy()
    random.shuffle(players_shuffled)
    for index,player in enumerate(players_shuffled):
      add_player_to_team(player,teams[index%8])

def calculate_team_completions(teams = get_teams()):
    for team in teams:
        players = show_team_players(team)
        team_completions = []
        for player in players:
          team_completions += show_player_completions(player)
        print(team_completions)
        update_team_score(team,team_completions)

def roll_check_status(counter=0):
    while True:
        
        check_status(players = get_students(),iteration=str(counter))
        calculate_team_completions(teams = get_teams())
        counter+=1
        time.sleep(60)



roll_check_status(counter=0)
