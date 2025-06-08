from langchain.schema import HumanMessage, AIMessage
from .chatbot_config import llm, SYSTEM_PROMPT

def generate_response(user_query: str) -> str:
    messages = [
        SYSTEM_PROMPT,
        HumanMessage(content=user_query)
    ]
    response = llm.invoke(messages)
    return response.content