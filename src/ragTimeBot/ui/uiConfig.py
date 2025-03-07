
import yaml

class Config:
    def __init__(self):
        with open('./src/ragTimeBot/ui/uiConfig.yaml', 'r') as file:
            groqOptions = yaml.safe_load(file)
            self.models =groqOptions["availModels"]
            self.config=groqOptions["groqOptions"]
            

    def get_models(self):
        return self.models

    def get_groq_model_options(self):
        return self.config


