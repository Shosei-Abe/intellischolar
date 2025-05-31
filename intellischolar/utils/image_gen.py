from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",  # dall-e-2 でも可
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url
