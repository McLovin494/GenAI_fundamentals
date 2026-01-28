from openai import OpenAI
from dotenv import load_dotenv

# ZERO SHOT PROMPTING IS DIRECTLY GIVING INSTRUCTIONS TO THE MODEL
load_dotenv()
client = OpenAI(
    api_key="your api key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
SYSTEM_PROMPT = "You ans only coding related queries and you do not answer anything else. If user asks anything other than coding just say sorry"
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        # set the background controlled proper prompting
        {
            "role": "user",
            "content": "Hey, Can u translate the word hello to hindi",
        },
    ],
)
print(response.choices[0].message.content)
