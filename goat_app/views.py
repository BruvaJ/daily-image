from django.shortcuts import render
import os
from goat_website import settings

# Create your views here.
def index(request):
    return render(request, 'goat_app/index.html')

def gallery(request):
    images = os.listdir(os.path.join(settings.STATIC_DIR, "images/collection/"))
    return render(request, 'goat_app/gallery.html', context={'images': images})

def about(request):
    return render(request, 'goat_app/about.html')
