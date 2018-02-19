from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
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
        images.append(os.path.join("images/collection/", f))
    return images

class ImageList(ListView):
    model = Daily_Image


class ImageDetail(DetailView):
    model = Daily_Image

    def get_object(self):
        # Call the superclass
        object = super().get_object()
        # Record the last accessed date
        if(object.first_published_date == Daily_Image.get_latest().first_published_date):
            object.votable = True
        # Return the object
        return object


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Subscriber.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'
    else:
        new_subscriber = Subscriber(email = email)
        new_subscriber.save()
    return JsonResponse(data)

def goat_vote(request):
    has_liked = int(request.GET.get('hasLiked', None))
    id = request.GET.get('id', None)
    boolean_has_liked = True if (has_liked == 1) else False
    Daily_Image.vote(boolean_has_liked, id)
    return HttpResponse(status=204)
