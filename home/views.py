from django.http import HttpResponse
#from django.shortcuts import render

# Criando sua view aqui.
def home(request):
    print('home')
    return HttpResponse('home do app Geila') # página principal
