from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
import os
from goat_website import settings
from goat_app.models import Daily_Image, Subscriber
from goat_app.forms import SubscriberForm
import random

# Create your views here.
def index(request):
    form = SubscriberForm
    return render(request, 'goat_app/index.html', context={'form': form})

def gallery(request):
    # return render(request, 'goat_app/gallery.html', context={'images': getGoatImages()})
    return render(request, 'goat_app/gallery.html', context={'images': Daily_Image.objects.all()})

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

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Subscriber.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    else:
        new_subscriber = Subscriber(email = email)
        # new_subscriber.save()
    return JsonResponse(data)
