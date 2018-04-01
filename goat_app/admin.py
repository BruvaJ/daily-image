from django.contrib import admin

from goat_app.models import Daily_Image
from accounts.models import Subscriber

# Register your models here.
admin.site.register(Daily_Image)
admin.site.register(Subscriber)
