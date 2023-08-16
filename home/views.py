from django.shortcuts import render # atalhos que tem a função de renderizar o html

# Criando sua view aqui.
def home(request):
    print('home')

    return render(
        request,
        'global/base.html' # manda renderizar o arquivo que está dentro do templates
        ) 
