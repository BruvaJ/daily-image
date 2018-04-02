from django.contrib.auth.forms import UserCreationForm
from .models import Subscriber
from django.contrib.auth import get_user_model
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # interest = Subscriber.interest
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
        student_kwargs = kwargs.copy()
        self.subscriber_form = SubscriberForm(*args, student_kwargs)
        self.fields.update(self.subscriber_form.fields)
        # print('init', kwargs)

    def save(self, *args, **kwargs):
        user = super(UserCreateForm, self).save()
        subscriber = Subscriber.objects.create(user=user, interest=self.cleaned_data['interest'])
        subscriber.save()


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ("interest",)
