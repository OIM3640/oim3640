from openai import OpenAI

client = OpenAI()

messages = []
print("Hello, we finally meet! What service would you like me to provide next?")
system_message = input("Human says: ")
messages.append(
    {
        "role": "system",
        "content": system_message,
    }
)
print("\n")

print(
    "Okay, got it! I will serve you well.\n"
    + "Now please chat with me!\n"
    + "Remember, when you're annoyed, please say 'goodbye'."
)

while True:
    print("\n")
    message = input("Human says: ")
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )

    completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    reply = completion.choices[0].message.content
    print(f"ChatGPT says: {reply}")

    if message.lower() == "goodbye":
        break
