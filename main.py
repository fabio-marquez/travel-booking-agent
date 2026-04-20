import os
from openai import OpenAI
from pydantic import BaseModel

api_key = os.environ["GROQ_API_KEY"]

client = OpenAI(api_key = api_key, base_url="https://api.groq.com/openai/v1")

def SimpleCallingLLM():

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":"You are a helpful assistant named Llama"},
            {"role":"user","content":"Hi, who are you?"}
        ]
    )

    response = completion.choices[0].message.content
    print(response)
    return

class Greeting(BaseModel):
    name: str
    role: str

def StructuredOutput():

    completion = client.chat.completions.parse(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role":"system","content":"You are a helpful assistant named Llama"},
            {"role":"user","content":"Hi, who are you?"}
        ],
        response_format=Greeting
    )

    response = completion.choices[0].message.parsed
    model_name = response.name
    model_role = response.role
    print(f"Model Name: {model_name}, Model Role: {model_role}")
    return

def main():
    print("Hello from travel-booking-agent!")
    
    #SimpleCallingLLM()
    StructuredOutput()

if __name__ == "__main__":
    main()
