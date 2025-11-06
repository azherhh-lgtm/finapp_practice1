# %%
# filename: financial_bot.py
#pip install mistralai

from mistralai import Mistral

# Replace with your actual API key (not safe for sharing or production)
API_KEY = "NT55ZwCmmmuugK0WyIVsIXsMfNGi5Ju7"

client = Mistral(api_key=API_KEY)
MODEL = "mistral-large-latest"

system_prompt = """You are a helpful financial advisor assistant.
Provide advice on budgeting, investing, savings, and personal finance.
Keep answers clear and practical. Always mention this is educational, not professional financial advice."""

def chat_once(user_message: str) -> str:
    resp = client.chat.complete(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    print("Financial Bot (type 'exit' to quit)\n")
    while True:
        msg = input("You: ").strip()
        if msg.lower() in {"exit", "quit"}:
            break
        answer = chat_once(msg)
        print("Bot:", answer, "\n")



