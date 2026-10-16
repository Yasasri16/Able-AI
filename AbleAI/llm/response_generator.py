import os
from groq import Groq
from llm.prompts import INPUT_CORRECTION_PROMPT, RESPONSE_PROMPT

def call_llm(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",  # Updated to an active model
        messages=[
            {"role": "system", "content": "You are a helpful assistive AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return completion.choices[0].message.content


def generate_response(user_input: str) -> dict:
    correction_prompt = INPUT_CORRECTION_PROMPT + f"\nUser input:\n{user_input}"
    corrected_input = call_llm(correction_prompt)

    response_prompt = RESPONSE_PROMPT.format(
        corrected_input=corrected_input.strip()
    )
    final_response = call_llm(response_prompt)

    return {
        "corrected_input": corrected_input.strip(),
        "response": final_response.strip()
    }

if __name__ == "__main__":
    test_input = "I gng doc"
    result = generate_response(test_input)

    print("Corrected Input:", result["corrected_input"])
    print("Final Response:", result["response"])