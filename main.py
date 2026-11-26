import os 
from dotenv import load_dotenv
from openai import OpenAI
from util import add, subtract, multiply, divide
from agent import tools
import json

# load env virables from .env file
load_dotenv()
# initialize client
client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
# Part1: simple request
# Get the question from the user 
question = input("What do you want to ask the AI tutor?")
# send a request to the API
response = client.responses.create(
    model= "gpt-4.1-mini",
    input= question
)
# display the response
print(response.output_text)

# part 2: Tool calling
# define available tools for tool calling
# idea behind tool calling: let the LLM know what funcs we have in our program and 
# then the LLM calls these functions when needed, ex: when the user asks what's 1 plus 1..
available_tools = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# try to ask the model -> the model might return a func call
response = client.responses.create(
    model="gpt-4.1-mini", 
    input= "What is 15 plus 25 minus 24", 
    tools= tools
)
tool_outputs = []
print(response.output)
for item in response.output:
    if item.type == "function_call": 
        tool_name = item.name
        if tool_name not in available_tools:
            raise ValueError(f"Unknown tool: {tool_name}")
        arguments = json.loads(item.arguments) #load json obj into python dict
        function_to_call = available_tools[tool_name]
        result = function_to_call(**arguments)
        tool_output = {
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": str(result)
        }
        tool_outputs.append(tool_output)
if tool_outputs:
    final_response = client.responses.create(
        model="gpt-4.1-mini", 
        previous_response_id= response.id,
        input=tool_outputs
    )
    print(final_response.output_text)