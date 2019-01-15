from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homepage.html')

def contact(request):
    return render(request, 'mainApp/basic.html',
                  {'values': ['If you have any questions, ask me:',
                  '(050) 123-45-67', 'example@mail.com']})
