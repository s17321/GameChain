from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.nlp.tag_extraction import extract_tags

# Inicjalizacja FastAPI
app = FastAPI(title="GameChain Backend API", version="0.1.0")

# Model danych - żądanie od użytkownika
class QueryRequest(BaseModel):
    user_input: str

# Model danych - odpowiedź
class QueryResponse(BaseModel):
    tags: list[str]

# Endpoint do analizy zapytania
@app.post("/analyze", response_model=QueryResponse)
async def analyze_query(request: QueryRequest):
    user_input = request.user_input

    if not user_input:
        raise HTTPException(status_code=400, detail="Zapytanie nie może być puste!")

    # Wywołanie funkcji NLP do ekstrakcji tagów
    tags = extract_tags(user_input)

    return QueryResponse(tags=tags)

# Uruchamianie serwera:
# uvicorn backend.main:app --reload
