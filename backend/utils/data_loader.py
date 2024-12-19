import pandas as pd

def load_game_data(file_path: str) -> list[dict]:
    """
    Wczytuje dane gier z pliku CSV i zwraca listę słowników z tytułem i gatunkami gry.
    """
    df = pd.read_csv(file_path)

    # Wybieramy kolumny Title i Genres, usuwamy puste wartości
    games = df[['Title', 'Genres']].dropna()

    # Przekształcamy dane do listy słowników
    game_data = []
    for _, row in games.iterrows():
        genres = eval(row['Genres'])  # Zamiana stringa na listę (bezpiecznie, bo to własne dane)
        game_data.append({"title": row['Title'], "genres": genres})

    return game_data
