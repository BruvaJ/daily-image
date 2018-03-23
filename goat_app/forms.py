from django.forms import ModelForm
from goat_app.models import Subscriber

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'interest']
