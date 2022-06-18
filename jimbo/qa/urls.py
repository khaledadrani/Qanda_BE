from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qa',views.question_answering,name='qa')
    #path('show_request',views.show_request, name='show_request')
]