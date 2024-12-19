from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

def load_llm():
    model_name = "google/flan-t5-large"  # Prosty model, można podmienić na inny
    pipe = pipeline("text2text-generation", model=model_name, max_length=50)
    return HuggingFacePipeline(pipeline=pipe)

def extract_tags(user_input: str) -> list[str]:
    """
    Użycie LangChain + Hugging Face LLM do ekstrakcji tagów z zapytania użytkownika.
    """
    llm = load_llm()
    prompt = (
        "Extract only the relevant keywords (tags) from the user input. "
        "Focus on categories like game type, gameplay style, and themes. "
        "Respond in a list of keywords separated by commas.\n"
        f"User Input: {user_input}"
    )
    response = llm.invoke(prompt)  # Zamiast przestarzałego __call__

    # Przykład odpowiedzi: "shooter, multiplayer, competitive"
    tags = [tag.strip() for tag in response.split(",") if tag.strip()]
    return tags
