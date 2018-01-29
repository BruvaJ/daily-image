from django.db import models

# Create your models here.
class Daily_Image(models.Model):
    up_votes = models.IntegerField(default=0, null=False)
    down_votes = models.IntegerField(default=0, null=False)
    first_published_date = models.DateTimeField(default=timezone.now, null=False)
    pixa_id = models.PositiveIntegerField(null=False)
    pixa_url = models.URLField(null=False)
    pixa_user = models.CharField(null=False)
    image = models.ImageField(null=False)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)
    #
    # def get_absolute_url(self):
    #     return reverse("post_detail",kwargs={'pk':self.pk})
    #
    #
    def __str__(self):
        return self.url
