from django.db import models
from django.utils import timezone

# Create your models here.
class Daily_Image(models.Model):
    up_votes = models.IntegerField(default=0, null=False)
    down_votes = models.IntegerField(default=0, null=False)
    first_published_date = models.DateTimeField(default=timezone.now, null=False)
    pixa_id = models.PositiveIntegerField(null=False)
    pixa_url = models.URLField(null=False, max_length=100)
    pixa_user = models.CharField(null=False, max_length=255)
    image_path = models.ImageField(null=False, upload_to='daily_images', max_length=100, unique=True)

    def get_latest():
        return Daily_Image.objects.latest('first_published_date')

    def vote(has_liked, id):
        chosen = Daily_Image.objects.get(pk=id)
        print(has_liked)
        if(has_liked == True):
            print('up')
            chosen.up_votes = chosen.up_votes + 1
        else:
            print('down')
            chosen.up_votes = chosen.up_votes - 1
        chosen.save()
        return

    # TODO:
    # not yet used. Could be nice alternative to all the different file paths in settings
    @staticmethod
    def get_directory():
        return 'daily_images'

    def __str__(self):
        return self.image_path.url


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    interest = models.CharField(max_length=10)
    subscription_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
