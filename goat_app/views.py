from django.shortcuts import render
import os
from goat_website import settings
import random

# Create your views here.
def index(request):
    return render(request, 'goat_app/index.html')

def gallery(request):
    return render(request, 'goat_app/gallery.html', context={'images': getGoatImages()})

def about(request):
    return render(request, 'goat_app/about.html')

def surprise_goat(request):
    images = getGoatImages()
    image = images[random.randrange(0, len(images))]
    return render(request, 'goat_app/surprise_goat.html', context={'image': image})


def getGoatImages():
    images = []
    for f in os.listdir(os.path.join(settings.STATIC_DIR, "images/collection/")):
        print(os.path.join("images/collection/", f))
        images.append(os.path.join("images/collection/", f))
    return images
