from generation.rag_chain import generate_answer

response = generate_answer(
    "What is Q2 revenue?",
    "Q2 revenue is 120000 dollars."
)

print(response)