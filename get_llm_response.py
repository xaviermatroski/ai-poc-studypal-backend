from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_model(provider, model_name):
    if provider == "groq":
        return ChatGroq(
            model=model_name,
            temperature=0.0,
            max_retries=2,
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def get_answer(question, provider, model_name):
    model = get_model(provider, model_name)
    answer = model.invoke(question)
    return answer.content

