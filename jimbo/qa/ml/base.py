from transformers import pipeline as transformers_pipeline
from typing import List, Union, Any
class QAModel:
    def __init__(self,**kwargs) -> None:
        self.models = {}
        

    def get_model(self, model_name: str) -> Any:
        """Factory to get models. Load requested model into self.models
        Args:
            model_name (str): model name
        Returns:
            None
        """
        if model_name == "question-answering":
            self.models['question-answering'] = transformers_pipeline(model_name)
            return

        raise NotImplementedError('This model does not exist')
      
    def load(self, model_name):
        if model_name in self.models:
            return self.models[model_name]

        self.get_model(model_name)
        return self.models[model_name]

    def predict(self,model_name,question,context):
      """
      main functionality of the model, answers a given question with a given context
      ARGS:
        model_name: str
        question: str
        context: str
      """
      try:
        if model_name not in self.models:
            print('loading new model ',model_name)
            self.get_model(model_name)

        return self.models[model_name](question = question, context = context)
      except Exception as err: 
        print("Error at predict ",str(err))

    def handle(self, model_name, queries, **kwargs):
        """Handle inference request, you can use this to 
            customize and add 
            - preprocessing 
            - prediction/inference
            - duration
            - postprocessing
        Args:
            model_name (Any): Spacy transformer model
            texts (List): Text to be processed
        """

        raise NotImplementedError('feature not implemented, use .predict for now')