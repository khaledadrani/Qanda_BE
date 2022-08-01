from django.shortcuts import render
import json

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from qa.ml.base import QAModel
# from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from qa.models import Problem
from qa.serializers import JsonSerializer
import traceback
import sys
import pickle

#https://docs.djangoproject.com/en/4.0/intro/tutorial03/

baker = QAModel()
model_name = 'question-answering'
json_serializer = JsonSerializer(Problem)


def index(request):
    latest_question_list = list(Problem.objects.order_by('id'))[-5:]
    # output = '<br>'.join([q.question for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('qa/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index_json(request):

    print("request ",str(type(request)),request)

    print("request header ACCEPT ",request.headers['Accept'])

    return JsonResponse(
        {'message':"Basic question answering is here! Testing if it works!",
        'request':str(request.body),
        'Accept':str(request.headers['Accept'])
        })

def question(request,id):
    if request.method == "GET":
        response_data = dict()
        try:
            response_data['result'] = json_serializer.serialize_data([Problem.objects.get(pk=id)])[0]
            return JsonResponse(response_data)
        except Problem.DoesNotExist as err:
            message = 'Item not found'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 404
            return response
        except Exception as err:
            message = 'Internal Server Error'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 500
            return response
    else:
        print('Invalid METHOD')
        resp = JsonResponse({'error':'Invalid METHOD'})
        resp.status_code = 400
        return resp

copydict = lambda dct, *keys: {key: dct[key] for key in keys}

def question_question(request,id):
    if request.method == "GET":
        response_data = dict()
        try:
            response_data['result'] = json_serializer.serialize_data([Problem.objects.get(pk=id)])[0]
            response_data['result'] = copydict(response_data['result'],'question')
            return JsonResponse(response_data)
        except Problem.DoesNotExist as err:
            message = 'Item not found'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 404
            return response
        except Exception as err:
            message = 'Internal Server Error'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 500
            return response
    else:
        print('Invalid METHOD')
        resp = JsonResponse({'error':'Invalid METHOD'})
        resp.status_code = 400
        return resp

def question_context(request,id):
    if request.method == "GET":
        response_data = dict()
        try:
            response_data['result'] = json_serializer.serialize_data([Problem.objects.get(pk=id)])[0]
            response_data['result'] = copydict(response_data['result'],'context')
            return JsonResponse(response_data)
        except Problem.DoesNotExist as err:
            message = 'Item not found'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 404
            return response
        except Exception as err:
            message = 'Internal Server Error'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 500
            return response
    else:
        print('Invalid METHOD')
        resp = JsonResponse({'error':'Invalid METHOD'})
        resp.status_code = 400
        return resp

def question_answer(request,id):
    if request.method == "GET":
        response_data = dict()
        try:
            response_data['result'] = json_serializer.serialize_data([Problem.objects.get(pk=id)])[0]
            response_data['result'] = copydict(response_data['result'],'answer')
            return JsonResponse(response_data)
        except Problem.DoesNotExist as err:
            message = 'Item not found'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 404
            return response
        except Exception as err:
            message = 'Internal Server Error'
            print(message,str(err))
            response = JsonResponse({'error':message})
            response.status_code = 500
            return response
    else:
        print('Invalid METHOD')
        resp = JsonResponse({'error':'Invalid METHOD'})
        resp.status_code = 400
        return resp

# @csrf_exempt 
def qa(request):
    try:
        print('request in question answering',request.body)
        print('request headers ',request.headers)

        if request.method == 'GET':
            print("GET METHOD SELECTED")
            queryset = Problem.objects.all()
            result = json_serializer.serialize_data(queryset)
            
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


def qa_form(request):
    try:
        

        if request.method == 'GET':
            print("GET METHOD SELECTED")
            
            question = request.POST['question']
            context = request.POST['context']
            answer = baker.predict(model_name=model_name, question=question, context=context)
            print('predicted answer ',answer)
            problem = Problem(question=question,context=context,answer=answer,model_name=model_name)
            print('problem at hand ',problem)
            problem.save()
            result = serializers.serialize("json", [problem])
            
            return HttpResponseRedirect(reverse('api/v0:question_id', args=(problem.id,)))
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
