from django.shortcuts import render
import json

from django.http import HttpResponse,JsonResponse
from qa.ml.models import QAModel
# from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from qa.models import Problem

import traceback
import sys

baker = QAModel()
model_name = 'question-answering'
baker.load(model_name)

def index(request):

    return JsonResponse({'message':"basic question answering is here!",'request':str(request.body)})


# @csrf_exempt 
def question_answering(request):
    try:
        print('request in question answering',request.body)
        print('request headers ',request.headers)

        if request.method == 'GET':
            print("GET METHOD SELECTED")
            # for p in Problem.objects.all():
            #     print('entry ',p)
            result = serializers.serialize("json", Problem.objects.all(),fields=('question','context','answer','model_name'))
            print('result ',result)
            return JsonResponse({'response':result})

        elif request.method == 'POST':
            print("POST METHOD SELECTED")
            data = json.loads(request.body)
            question = data['question']
            context = data['context']
            answer = baker.predict(model_name=model_name, question=question, context=context)
            print('predicted answer ',answer)
            problem = Problem(question=question,context=context,answer=answer,model_name=model_name)
            print('problem at hand ',problem)
            problem.save()
            result = serializers.serialize("json", [problem])
            print("DATA ",data)
            return JsonResponse({'response':result})
        else:
            print('Invalid METHOD')
            resp = JsonResponse({'error':'Invalid METHOD'})
            resp.status_code = 400
            return resp
    except Exception as err: 
        print('INTERNAL SERVER ERROR: ',str(err))
        traceback.print_exc()
        resp = JsonResponse({'error':'Internal Server Error'})
        resp.status_code = 500
        return resp
