from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse
from . import forms
from django.shortcuts import render



class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("welcome")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        form.save()
        print('*'*50)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return render(self.request, 'goat_app/index.html')
