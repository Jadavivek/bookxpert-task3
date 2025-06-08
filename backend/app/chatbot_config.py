import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage

# Set Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCWg8CZXzRuLrLCHw_0NF8-Jw21zha7iNM"

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# System prompt config
SYSTEM_PROMPT = SystemMessage(
    content="You are a chef who can create recipes using any ingredients provided by the user. Respond concisely and clearly."
)