
from src.ragTimeBot.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot logic implementation.
    """
    def __init__(self,model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """

        print(state['messages'])
       

        return {"messages":self.llm.invoke(state['messages'])}