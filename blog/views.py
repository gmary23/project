from django.shortcuts import HttpResponse
# from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    return HttpResponse('blog do app - testando')

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo- testando')

def geila(request):
    print('testando uma view')
    return HttpResponse('Uhuuuuummm..deu certo')
