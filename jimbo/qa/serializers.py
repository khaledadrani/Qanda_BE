from django.core import serializers
import json 

def get_model_fields(model):
    return [f.name for f in model._meta.get_fields()]

class JsonSerializer:
    def __init__(self,model):
        self.serialize = serializers.serialize #this returns a json string
        self.format = "json"
        self.model = model 

    def serialize_data(self,queryset,fields=None,verbose=True):
        if not fields: 
            fields = get_model_fields(self.model)

        serialized = self.serialize(format=self.format,fields=fields,queryset=queryset)
        serialized = json.loads(serialized) #this returns a json dict object
        if verbose:
            print('serialized ',serialized)
        return [item['fields'] for item in serialized]



