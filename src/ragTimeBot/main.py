import streamlit as st

from src.ragTimeBot.ui.load_ui import loadScreen
from src.ragTimeBot.llms.groqLLM import groqLLMobj
from src.ragTimeBot.graph.graphBuild import graphBuilder
from langgraph.checkpoint.memory import MemorySaver
from src.ragTimeBot.state.state import State

def loadChatbot():
    
    ## Load Streamlit Interface
    ui = loadScreen("My First Langgraph Chatbot")

    ## Load the screen
    userInterface = ui.loadStreamInterface()
    # Declare Thread object

    # Create Memory Object
    memory=MemorySaver()
    thread = {"configurable": {"thread_id": "1"}}
    ## Load Chat Window Info
    # Add text area

    chatQuestion =st.chat_input("Enter your question here")       
    # In LLM Call establish Model connect
    selected_model=userInterface["llmDrop"]
    selected_groq_model= userInterface['selected_groq_model']
    selected_api_key=userInterface['llmApikey']

    llmModel = groqLLMobj(selected_groq_model,selected_api_key)
    # Create model to be called
    myModel=llmModel.getLLM()
    theGraph = graphBuilder(myModel)
    myGraph= theGraph.getGraph()
    theFinalGraph = myGraph.compile(checkpointer=memory,debug=True)


    if chatQuestion:
        if selected_model!="" and selected_groq_model!="":
            # Build the Graph
 
            # Create Graph Stream
            events = theFinalGraph.stream({'messages':("user",chatQuestion)},thread,stream_mode="values")

            for event in events:
                #print(event["messages"])
                #with st.chat_message("assistant"):
                 #   st.write(event["messages"])
                with st.chat_message("assistant"):
                    st.write(event["messages"][-1].content)
