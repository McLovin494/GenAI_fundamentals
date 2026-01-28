# widely used and more used then zero shot
# in few shot prompting we give examples with instructions generally we give 50 to 60 examples
# in few shot prompting we can control the output as well
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key="your api key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert in maths and only and only ans coding realted questions. "
                "If the query is not related to coding do not ans it and say sorry. "
                "Rule: "
                "- Strictly follow the output in JSON format. "
                "Output format: "
                "{ "
                '"code": "string" or null, '
                '"isCodingQuestion": boolean '
                "} "
                "Example: "
                "Q: Can you explain the a+b whole square? "
                'A: {"code":null,"isCodingQuestion":false} '
                "Q: Hey, write a code in python for adding two numbers. "
                'A: {"code":"def add(a, b): return a + b","isCodingQuestion":true}'
            ),
        },
        # set the background controlled proper prompting
        {
            "role": "user",
            "content": "Hey, Write a code to find the sum of 10 numbers",
        },
    ],
)

print(response.choices[0].message.content)
