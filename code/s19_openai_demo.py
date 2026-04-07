from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI()

conversation = [
    {
        "role": "system",
        "content": (
            "You are an AI tutor for business students. "
            "Explain ideas clearly, use practical business examples, "
            "and suggest simple next steps students can try."
        ),
    }
]

print("Business AI Chatbot is ready. Type 'exit' to stop.")

while True:
    user_message = input("You: ").strip()
    if user_message.lower() in {"exit", "quit"}:
        print("Bot: Thanks for chatting. Keep exploring AI in business!")
        break
    if not user_message:
        continue

    conversation.append({"role": "user", "content": user_message})

    response = client.responses.create(
        model="gpt-5-nano",
        input=conversation,
    )

    bot_message = response.output_text.strip()
    print(f"Bot: {bot_message}")
    conversation.append({"role": "assistant", "content": bot_message})

