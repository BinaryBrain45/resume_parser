import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(text):
    prompt = f"Analyze this resume and suggest improvements:\n{text}"
    response = genai.generate(prompt)
    
    return response.text if response else "No suggestions available"
