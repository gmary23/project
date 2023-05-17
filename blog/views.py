from django.shortcuts import HttpResponse
# from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    return HttpResponse('blog do app')
