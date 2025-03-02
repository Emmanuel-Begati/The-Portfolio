from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'website/index.html')   

def home1 (request):
    return render(request, 'website/home1.html')

def home2 (request):
    return render(request, 'website/home2.html')

def home3 (request):
    return render(request, 'website/home3.html') 

def home4 (request):
    return render(request, 'website/home4.html')

def home5 (request):
    return render(request, 'website/home5.html')

def home6 (request):
    return render(request, 'website/home6.html')
