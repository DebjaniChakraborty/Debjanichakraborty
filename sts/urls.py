from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('cdc/', views.cdc, name='cdc'),
     path('index/', views.index, name='index'),
    
    path('answersubmit1/<int:pk>/<int:fk>', views.answersubmit1, name='answersubmit1'),
    path('answersubmit/<int:pk>/<int:fk>', views.answersubmit, name='answersubmit'),
     path('', views.index, name='index'),
    
     path('category/', views.category, name='category'),
     path('category1/', views.category1, name='category1'),
    path('adquestion/', views.adquestion, name='adquestion'),
    path('adquestion1/', views.adquestion1, name='adquestion1'),
    path('allquestion/', views.allquestion, name='allquestion'),
    path('allquestion1/', views.allquestion1, name='allquestion1'),
]
