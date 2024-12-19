# GameChain - System Rekomendacji Gier Wideo

**GameChain** to aplikacja do rekomendowania gier wideo na podstawie analizy zapytań użytkownika w języku naturalnym. Wykorzystuje NLP oraz modele językowe (LLM) do ekstrakcji tagów uzyskanych dzięki LangChain'om i dopasowania ich do danych w bazie. 

## Wymagania systemowe

- Python 3.11
- Conda (opcjonalnie)

---

## Konfiguracja projektu

### 1. Klonowanie repozytorium.
Skopiuj repozytorium na swój komputer

### 2. Utworzenie środowiska wirtualnego. - (Opcjonalne)
Utwórz środowisko wirtualne:

conda create --name GameChain python=3.10
conda activate GameChain

### 3. Instalacja zależności.
Zainstaluj wymagane pakiety z requirements.txt:

pip install -r requirements.txt

### 3. Uruchomienie projektu.
# Backend (FastAPI)
Uruchom backend API na serwerze Uvicorn:

uvicorn backend.main:app --reload
Domyślnie aplikacja działa na http://127.0.0.1:8000.

# Frontend (Streamlit)
Uruchom frontend w Streamlit:

streamlit run frontend/app.py
Frontend będzie dostępny pod adresem http://localhost:8501