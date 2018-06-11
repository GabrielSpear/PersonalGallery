from django.shortcuts import render, Http404
from .models import Photos

# Create your views here.

def home(request):
    image = Image.get_images()
    return render(request,'index.html',{"images":image})

def my_gallery(request):
    photos = Photos.objects.all()
    return render(request, 'gallery.html', {'photos':photos})

def single_photo(request, photo_id):
    photo = Photos.objects.get(id=photo_id)
    return render(request, 'photo.html', {'photo':photo})
