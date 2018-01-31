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

    def __str__(self):
        return self.url
