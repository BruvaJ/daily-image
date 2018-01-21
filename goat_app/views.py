from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'goat_app/index.html')

def gallery(request):
    return render(request, 'goat_app/gallery.html')

def about(request):
    return render(request, 'goat_app/about.html')
