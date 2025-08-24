from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def predictions(request):
    return render(request, 'predictions.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def insights(request):
    return render(request, 'insights.html')

def about(request):
    return render(request, 'about.html')



