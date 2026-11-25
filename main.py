import os 
from dotenv import load_dotenv
from openai import OpenAI

# load env virables from .env file
load_dotenv()
# initialize client
client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )
# send a request to the API
response = client.responses.create(
    model= "gpt-4.1-mini",
    input= "Explain Agentic AI in simple words"
)
# display the response
print(response.output_text)