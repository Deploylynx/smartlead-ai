from transformers import pipeline

# lightweight free AI model
generator = pipeline("text-generation", model="distilgpt2")

def generate_message(lead):
    prompt = f"""
Write a professional client outreach message.

Client Name: {lead['name']}
Company: {lead['company']}
Requirement: {lead['need']}

Message:
"""

    result = generator(prompt, max_length=120, num_return_sequences=1)

    text = result[0]["generated_text"]

    return text