from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # ← これが .env を読み込む処理！

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_topic(topic):
    prompt = f"""
    Summarize the current research and applications related to the following topic in 3–5 sentences:
    Topic: {topic}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
