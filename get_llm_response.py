from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.0,
    max_retries=2,
)

def get_answer(question):
    answer = model.invoke(question)
    return answer.content

