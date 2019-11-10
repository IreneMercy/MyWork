from django.shortcuts import render

def home(request):
    message="This is Mercy's portfolio"
    return render(request, 'index.html', {"message":message})
