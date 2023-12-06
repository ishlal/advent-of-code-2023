from typing import List

def parse_input(filename):
    res = []
    with open(filename) as f:
        all_games = []
        for line in f:
            title, games = line.split(":")
            gt, num = title.split()
            games.strip()
            ind_games = games.split(";")
            game = []
            game.append(int(num))
            for i in ind_games:
                tokens = i.split(",")
                cleaned_tokens = []
                for tok in tokens:
                    tok = tok.strip()
                    cleaned_tokens.append(tok)
                game.append(cleaned_tokens)
            all_games.append(game)
    return all_games
                



    return res