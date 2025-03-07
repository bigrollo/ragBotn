
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class groqLLMobj():

    def __init__(self,model,api_key):
        self.model = model
        self.api_key=api_key

    def getLLM(self):
        llm = ChatGroq(model=self.model)
        return llm
