
import streamlit as st
from src.ragTimeBot.ui.uiConfig import Config


class loadScreen():

    def __init__(self,botName):
        self.botName= botName
        self.userControls={}


    def loadStreamInterface(self):

        st.set_page_config(page_title=self.botName,layout="wide")
        st.header("Marc's Langgraph Chatbot")
    
        # Load Config File
        theConfig = Config()
        availModels = theConfig.get_models()
        groqOptions = theConfig.get_groq_model_options()

        with st.sidebar:
            # LLM selection
            self.userControls["llmDrop"] = st.selectbox("Select LLM", availModels)
            self.userControls["selected_groq_model"] = st.selectbox("Select Model",groqOptions)
            self.userControls["llmApikey"] = st.text_input("Enter GROQ API Key")
                
        return self.userControls
