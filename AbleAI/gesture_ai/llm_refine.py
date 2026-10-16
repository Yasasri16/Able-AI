import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_text(tokens):
    prompt = f"""
    Convert these sign language tokens into a clear English sentence:

    {' '.join(tokens)}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(refine_text(["doctor", "appointment"]))
