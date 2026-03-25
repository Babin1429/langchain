from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

prompt=PromptTemplate.from_template(
    "Explain the concept of {topic} in simple terms."
)
chain=prompt | llm
n= input("Enter a topic to explain: ")
response=chain.invoke({"topic": n})
print(response)
