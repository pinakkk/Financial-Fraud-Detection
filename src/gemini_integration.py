# # Version 1.0.0 

# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load API key from .env
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Configure Gemini with the API key
# genai.configure(api_key=API_KEY)

# # Initialize the Gemini 1.5 Flash model
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# def get_explanation(transaction):
#     """
#     Send a transaction row to Gemini 1.5 Flash and get an explanation.
#     """
#     prompt = f"""
#     You are a financial fraud detection expert. Analyze the following transaction and explain whether it could be fraudulent:

#     Transaction Details:
#     {transaction.to_string()}

#     Respond concisely and clearly.
#     """

#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"Error generating explanation: {str(e)}"


# Version 2.0.0 
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API with your API key
genai.configure(api_key=API_KEY)

# Use the free-tier Gemini 1.5 Flash model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_explanation(transaction):
    """
    Send a transaction row to Gemini 1.5 Flash and get an explanation.
    """
    prompt = f"""
    You are a financial fraud detection expert. Analyze the following transaction and explain in a clear and concise manner whether it could be fraudulent.

    Transaction Details:
    {transaction.to_string()}

    Provide your response in bullet points if necessary.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
