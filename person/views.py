from django.shortcuts import render, Http404
from .models import Photos

# Create your views here.

def home(request):
    image = Image.get_images()
    return render(request,'index.html',{"images":image})
