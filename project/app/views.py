from django.shortcuts import render
from django.http import HttpResponse   
# Create your views here.
def contact(request):
    return HttpResponse("Contact")

def index(request):
    return render(request, 'index.html')