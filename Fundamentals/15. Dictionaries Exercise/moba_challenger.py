players_pool = {}
player_by_points = {}

while True:
    line = input()
    if line == "Season end":
        break

    if "->" in line:
        player, position, skill = line.split(" -> ")
        skill = int(skill)

        if player not in players_pool:
            players_pool[player] = {position: skill}

        elif position not in players_pool[player]:
            players_pool[player][position] = skill

        if skill > players_pool[player][position]:
            players_pool[player][position] = skill

    if " vs " in line:
        player1, player2 = line.split(" vs ")
        if player1 in players_pool and player2 in players_pool:
            player1_total_skill = sum(players_pool[player1].values())
            player2_total_skill = sum(players_pool[player2].values())
            common_positions = set(players_pool[player1]).intersection(set(players_pool[player2]))
            if common_positions:
                if player1_total_skill > player2_total_skill:
                    del players_pool[player2]
                elif player2_total_skill > player1_total_skill:
                    del players_pool[player1]

# player_by_points = {}
# for user, position in players_pool.items():
#     for pos, skill in position.items():
#         if user in player_by_points:
#             player_by_points[user] += skill
#         else:
#             player_by_points[user] = skill
#
#
# for individual_user, individual_point in sorted(player_by_points.items(), key=lambda x: (-x[1], x[0])):
#     print(f"{individual_user}: {individual_point} skill")
#     for key, value in sorted(players_pool[individual_user].items(), key=lambda x: (-x[1], x[0])):
#         print(f"- {key} <::> {value}")

sorted_players = sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, positions in sorted_players:
    total_skill = sum(positions.values())
    print(f"{player}: {total_skill} skill")
    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")