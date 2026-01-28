from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AIzaSyBKAzXGm8leNeeFr_tT7IWkcPB4LiIa_rk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
response = client.chat.completions.create(
    model="gemini-2.5-flash", messages=[{"role": "user", "content": "Hey There"}]
)

print(response.choices[0].message.content)
