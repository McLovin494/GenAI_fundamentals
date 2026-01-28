from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="AIzaSyBKAzXGm8leNeeFr_tT7IWkcPB4LiIa_rk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in maths and only and only ans math realted questions.If the query is not related to math do not ans it and say sorry",
        },
        # set the background controlled proper prompting
        {
            "role": "user",
            "content": "Hey, Can u code a python programm that says hello world",
        },
    ],
)

print(response.choices[0].message.content)
