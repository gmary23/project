"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog import views as blog_views # esse acrescentou
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from home import views as home_views # esse acrescentou

# HTTP Request(requisição) <-> HTTP Response(O servidor responde)

#defini a função para receber a request
#def my_view(request): #aqui a view recebeu o pedido do cliente
#    return HttpResponse('Uma mensagem para alguém especial') #aqui o servidor responde

def home(request):
   # print('home')
    return HttpResponse('home1')

def blog(request):
    print('blog')
    return HttpResponse('blog')


urlpatterns = [
    path('', home_views.home),
    path('blog/', blog_views.blog),
    path('admin/', admin.site.urls),
    #path('blog/', my_view), #aqui nunca começa com "/", só termina. Aqui também coloca um argumento que nesse caso é a função que foi criada "my_view"
]
