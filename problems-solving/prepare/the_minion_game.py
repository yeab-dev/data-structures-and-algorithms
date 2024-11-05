def minion_game(string: str):
    players_with_score = {"Kevin": 0, "Stuart": 0}
    vowels = ["A", "E", "I", "O", "U"]
    for c in range(len(string)):
        if not (string[c] in vowels):
            players_with_score["Stuart"] += len(string) - c

        if(string[c] in vowels):
            players_with_score["Kevin"] += len(string) - c
    
    winner = max(players_with_score.keys(), key=players_with_score.get)
    if players_with_score["Kevin"] == players_with_score["Stuart"]:
        print("Draw")
    else:
        print(winner, players_with_score[winner])
