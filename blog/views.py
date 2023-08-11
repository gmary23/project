from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    return render(
        request,
        'blog/index.html' # manda renderizar o arquivo que está dentro do templates
        ) 


def exemplo(request):
    print('Exemplo do blog')
    return render(
        request,
        'blog/exemplo.html' # manda renderizar o arquivo que está dentro do templates
        ) 

