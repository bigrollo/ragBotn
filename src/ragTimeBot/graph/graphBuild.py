
from langgraph.graph import START,END, MessagesState,StateGraph
from langgraph.prebuilt import tools_condition,ToolNode
from langgraph.graph.message import add_messages
from typing import TypedDict,Annotated,List
from src.ragTimeBot.state.state import State
from src.ragTimeBot.nodes.basic_chatbot_node import BasicChatbotNode



class graphBuilder:

    def __init__(self,model):
        self.llm=model
        self.graphBuilder=StateGraph(State)

    def getGraph(self):
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graphBuilder.add_node("chatBot",self.basic_chatbot_node.process)
        self.graphBuilder.add_edge(START,"chatBot")
        self.graphBuilder.add_edge("chatBot",END)
        return self.graphBuilder