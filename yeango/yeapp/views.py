from django.shortcuts import render

def index(request):
  return render(request, 'yeapp/home.html')

def contact(request):
  return render(request, 'yeapp/basic.html', {'content':['Gaan we niet doen he, nee he.','hihi']})