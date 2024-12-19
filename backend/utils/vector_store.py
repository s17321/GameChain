from sentence_transformers import SentenceTransformer
import chromadb
from backend.utils.data_loader import load_game_data

def init_vector_store():
    """
    Inicjalizacja ChromaDB oraz modelu SentenceTransformer.
    """
    client = chromadb.Client()
    collection = client.get_or_create_collection("game_tags")
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    return collection, embed_model

def populate_vector_store(file_path: str):
    """
    Wczytuje dane z CSV i zapisuje embeddingi gier do bazy ChromaDB.
    """
    collection, embed_model = init_vector_store()
    game_data = load_game_data(file_path)

    # Dodawanie gier do bazy
    for game in game_data:
        title = game['title']
        genres = " ".join(game['genres'])  # Łączymy gatunki jako jeden string
        description = f"{title} {genres}"

        embedding = embed_model.encode(description).tolist()
        collection.add(
            ids=[title],
            embeddings=[embedding],
            metadatas=[{"genres": genres}]
        )
    print("Baza wektorowa została zaktualizowana!")

if __name__ == "__main__":
    populate_vector_store("GameChain/data/games.csv")

def search_by_game_name(game_name: str) -> list[dict]:
    """
    Znajdź grę na podstawie nazwy i zwróć podobne gry.
    """
    collection, embed_model = init_vector_store()
    game_embedding = embed_model.encode(game_name).tolist()

    results = collection.query(query_embeddings=[game_embedding], n_results=5)
    return results



# Dodawanie gier do bazy
def add_game_to_vector_store(game_name: str, description: str, tags: list[str]):
    collection, embed_model = init_vector_store()
    embedding = embed_model.encode(" ".join(tags))
    collection.add(
        ids=[game_name],
        embeddings=[embedding],
        metadatas=[{"description": description}]
    )

# Znajdowanie podobnych gier
def search_similar_games(user_tags: list[str], top_k=3):
    collection, embed_model = init_vector_store()
    query_embedding = embed_model.encode(" ".join(user_tags))

    # Konwersja NumPy array na listę
    query_embedding = query_embedding.tolist()

    # Wykonanie zapytania
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results
