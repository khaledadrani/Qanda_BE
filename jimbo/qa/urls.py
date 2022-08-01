from django.urls import path

from . import views

app_name = 'api/v0'

urlpatterns = [
    path('', views.index_json, name='index'),
    path('qa',views.qa,name='qa'),
    #path('qa/form',views.qa_form,name='qa_form'),
    path('qa/questions/<int:id>',views.question,name='question_id'),
    path('qa/questions/<int:id>/question',views.question_question,name='question_id_question'),
    path('qa/questions/<int:id>/answer',views.question_answer,name='question_id_answer'),
    path('qa/questions/<int:id>/context',views.question_context,name='question_id_context')
    
]