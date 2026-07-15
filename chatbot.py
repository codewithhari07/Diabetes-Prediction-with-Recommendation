from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY
from rag import retrieve_context

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.2
)

def ask_ai(patient_data, prediction, question):

    context, sources = retrieve_context(question)

    prompt = f"""
You are an AI healthcare assistant.

Patient Information:

{patient_data}

Prediction:

{prediction}

Medical Context:

{context}

Question:

{question}

Instructions:

1. Use the provided medical context.
2. Explain in simple language.
3. Never prescribe medication.
4. Recommend consulting a doctor when appropriate.
"""

    response = llm.invoke(prompt)

    return response.content, sources