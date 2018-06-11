from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image

# Create your views here.

def home(request):
    image = Image.get_images()
    return render(request,'index.html',{"images":image})
