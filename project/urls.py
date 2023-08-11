
#from blog import views as blog_views # esse acrescentou

#from django.http import HttpResponse
#from django.urls import path
#from home import views as home_views # esse acrescentou



#defini a função para receber a request
#def my_view(request): #aqui a view recebeu o pedido do cliente
#    return HttpResponse('Uma mensagem para alguém especial') #aqui o servidor responde

from django.contrib import admin
from django.urls import include, path # include é para incluir um arquivo de url 

urlpatterns = [
    path('', include('home.urls')), # importa o arquivo URL DA HOME para isso usa o include.
    path('blog/', include('blog.urls')), # importa o arquivo URL DA HOME para isso usa o include.
    path('admin/', admin.site.urls), # padrão da administração do django
    ]
