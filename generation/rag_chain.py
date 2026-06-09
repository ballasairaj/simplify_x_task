import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

from generation.prompt import PROMPT

load_dotenv()

llm = ChatMistralAI(
    model="mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0
)

def generate_answer(query, context):

    prompt = PROMPT.format(
        context=context,
        question=query
    )

    response = llm.invoke(prompt)

    return response.content