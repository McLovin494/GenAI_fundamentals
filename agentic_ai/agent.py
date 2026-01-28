# think before generating the response in chain of thought prompting we want llms to think and ans
from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class LLMOuputFormat(BaseModel):
    step: str = Field(
        ..., description="The ID of the step. Example:PLAN, OUTPUT,TOOL etc"
    )
    content: Optional[str] = Field(
        None, description="The optional string content for the step"
    )
    tool: Optional[str] = Field(None, description="The ID of the tool called")
    input: Optional[str] = Field(None, description="Input params for the tool ")


load_dotenv()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key="your key here",
)


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    else:
        return "Something went wrong"


available_tools = {"get_weather": get_weather}

SYSTEM_PROMPT = """
You are an expert AI assistant that follows a structured reasoning process internally.
You MUST output only valid JSON as specified.
You work on START,PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT
You can also call a tool if required from list of available tools 
for every tool call wait for the observe step which is the output from the called tool
Rules:
- Strictly Follow the given JSON output format
- Only run one step at a time
- The sequence of steps is START (where user gives an input), PLAN (That can be multiple times ) and OUTPUT (which is goinf to the displayed to the user)
Output JSON format:
{"step":"START" | "PLAN"|"OUTPUT|TOOL ","content":"string":"tool":"string":"input":"string"}
Available Tools:
- get_weather(city:str): Takes city name as an input string and returns the weather info about the city 
Example 1:
START: Hey, Can you solve 2+3*5/10
PLAN:{"step":"PLAN":"content":"looking at the problem w should solve this using BODMAS method"}
PLAN:{"step":"PLAN":"content:"Yes, The BODMAS is correct thing to be done here"}
PLAN:{"step":"PLAN":"content":"first we must multiply 2*5 which is 15"}
PLAN:{"step":"PLAN":"content":"Now the equation is 2+15/10"}
PLAN:{"step":"PLAN":"content":"We must perform the divide that is 15/10=1.5"}
PLAN:{"step":"PLAN":"content":"Now the new equation is 2+1.5 2.5"}
PLAN:{"step":"PLAN":"content":"Now finally perfom the add"}
PLAN:{"step":"PLAN":"content":"Great, we have solved an finally left with 2.5 as ans"}
PLAN:{"step":"OUTPUT":"content":"3.5 "}

Example 2:
START: What is the weather of Delhi?
PLAN:{"step":"PLAN":"content":"Seems like user is interested in getting weather of Delhi in India"}
PLAN:{"step":"PLAN":"content:"Let's see if we have any available tool from the list of available tools"}
PLAN:{"step":"PLAN":"content":"Great, we have get_weather tool available for this query"}
PLAN:{"step":"PLAN ":"content":"I need to call get_weather tool for Delhi as input for city"}
PLAN:{"step":"TOOL":"tool":"get_weather":"input":"delhi"}
PLAN:{"step":"OBSERVE":"content":"The the temperature of delhi is cloudy with 20 C"}
PLAN:{"step":"PLAN":"content":"Great I got the weather info about delhi"}
PLAN:{"step":"OUTPUT ":"content":"The current weather in delhi is 20C with cloudy sky"}
 
"""
message_history = [{"role": "system", "content": SYSTEM_PROMPT}]
while True:
    user_query = input("👉🏻")
    message_history.append({"role": "user", "content": user_query})
    print("\n\n\n\n\n\n\n")
    while True:
        # Fixed: Pass the Pydantic model class directly, not wrapped in a dict
        response = client.beta.chat.completions.parse(
            model="gemini-2.5-flash",
            response_format=LLMOuputFormat,
            messages=message_history,
        )
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = response.choices[0].message.parsed

        print(parsed_result)
        if parsed_result.step == "START":
            print("🔥", parsed_result.content)
            continue
        if parsed_result.step == "TOOL":
            tool_called = parsed_result.tool
            tool_input = parsed_result.input
            tool_response = available_tools[tool_called](tool_input)
            print(
                f"Tool called-{tool_called} on input-{tool_input}, Result{tool_response}"
            )
            message_history.append(
                {
                    "role": "developer",
                    "content": json.dumps(
                        {
                            "step": "OBSERVE",
                            "tool": tool_called,
                            "input": tool_input,
                            "output": tool_response,
                        }
                    ),
                }
            )
            continue
        if parsed_result.step == "PLAN":
            print("🧠 ", parsed_result.content)
            continue
        if parsed_result.step == "OUTPUT":
            print("🤖 ", parsed_result.content)
            break

    print("\n\n\n\n\n\n\n")
