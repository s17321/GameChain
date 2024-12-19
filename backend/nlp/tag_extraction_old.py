def extract_tags(user_input: str) -> list[str]:
    """
    Prosta funkcja do ekstrakcji tagów z zapytania użytkownika.
    """
    # Przykładowy słownik słów kluczowych
    keywords = {
        "strzelanka": "shooter",
        "science-fiction": "sci-fi",
        "rpg": "role-playing",
        "fps": "first-person shooter",
        "gra": "game"
    }

    # Ekstrakcja słów kluczowych
    tags = []
    for word in user_input.lower().split():
        if word in keywords:
            tags.append(keywords[word])
    
    # Dodanie domyślnego taga
    if not tags:
        tags.append("general")

    return tags
