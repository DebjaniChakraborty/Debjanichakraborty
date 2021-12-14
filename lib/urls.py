"""lib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sts import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
   
    
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('signout/', views.signout,name='signout'),
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('cdc/', views.cdc, name='cdc'),
    path('index/', views.index, name='index'),
   
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('category1/', views.category1, name='category1'),
    path('adquestion/', views.adquestion, name='adquestion'),
    path('adquestion1/', views.adquestion1, name='adquestion1'),
    path('allquestion/', views.allquestion, name='allquestion'),
    path('allquestion1/', views.allquestion1, name='allquestion1'),
    path('answersubmit/<int:pk>/<int:fk>', views.answersubmit, name='answersubmit'),
    path('answersubmit1/<int:pk>/<int:fk>', views.answersubmit1, name='answersubmit1'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
