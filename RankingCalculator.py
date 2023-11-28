import numpy as np
from Team import Team
from RecordGenerator import *

first_half_season_record = np.array([])

def winrate(team):
    team_total = team.win + team.lose
    return team.win / team_total if team_total != 0 else 0

def find_one_first_half_season_champion(teams):
    result = 0
    for i in range(len(teams)):
        if winrate(teams[i]) > winrate(teams[result]):
            result = i
    global first_half_season_record
    first_half_season_record = teams
    return result

def find_all_first_half_season_champion(teams):
    champions = []
    champion_winrate = 0
    for i in range(len(teams)):
        winrate_i = winrate(teams[i])
        if winrate_i >= champion_winrate:
            champion_winrate = winrate_i
            champions.append(i)
    global first_half_season_record
    first_half_season_record = teams
    return champions

def find_one_playoff_teams(teams, first_half_season_champion):
    second_half_season_record = gen_second_half_season_record(teams, first_half_season_record)
    second_half_season_champion = 0
    for i in range(len(teams)):
        if winrate(second_half_season_record[i]) > winrate(second_half_season_record[second_half_season_champion]):
            second_half_season_champion = i

    playoff_teams = np.zeros(len(teams))
    playoff_teams[first_half_season_champion] = 1
    playoff_teams[second_half_season_champion] = 1
    sorted_record = sorted(teams, key=lambda x:(x.win / (x.win + x.lose) if x.win + x.lose != 0 else 0))
    # print(first_half_season_champion)
    # print(second_half_season_champion)
    if first_half_season_champion == second_half_season_champion:
        count = 1
        for i in range(len(sorted_record)):
            if i != first_half_season_champion:
                playoff_teams[i] = 1
                count += 1
                if count == 3:
                    # print(playoff_teams)
                    return playoff_teams
    else:
        count = 2
        for i in range(len(sorted_record)):
            if i != first_half_season_champion and i != second_half_season_champion:
                playoff_teams[i] = 1
                # print(playoff_teams)
                return playoff_teams

def find_all_playoff_teams(teams, first_half_season_champions):
    second_half_season_record = gen_second_half_season_record(teams, first_half_season_record)
    second_half_season_champions = []
    second_champion_winrate = 0
    for i in range(len(teams)):
        team_i_total = second_half_season_record[i].win + second_half_season_record[i].lose
        team_i_winrate = second_half_season_record[i].win / team_i_total if team_i_total != 0 else 0
        if team_i_winrate >= second_champion_winrate:
            second_champion_winrate = team_i_winrate
            second_half_season_champions.append(i)

    playoff_teams = np.zeros(len(teams))
    sorted_record = sorted(teams, key=lambda x:(x.win / (x.win + x.lose) if x.win + x.lose != 0 else 0))

    for first_half_season_champion in first_half_season_champions:
        for second_half_season_champion in second_half_season_champions:
            playoff_teams[first_half_season_champion] = 1
            playoff_teams[second_half_season_champion] = 1
            # print(first_half_season_champion)
            # print(second_half_season_champion)
            if first_half_season_champion == second_half_season_champion:
                count = 1
                for i in range(len(sorted_record)):
                    if i != first_half_season_champion:
                        playoff_teams[i] = 1
                        count += 1
                        if count == 3:
                            break
            else:
                count = 2
                for i in range(len(sorted_record)):
                    if i != first_half_season_champion and i != second_half_season_champion:
                        playoff_teams[i] = 1
                        break
    # print(playoff_teams)
    return playoff_teams