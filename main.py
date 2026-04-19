import os
from openai import OpenAI

api_key = os.environ["GROQ_API_KEY"]

client = OpenAI(api_key = api_key, base_url="https://api.groq.com/openai/v1")

def main():
    print("Hello from travel-booking-agent!")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":"Hi, who are you?"}]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
