# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    print(settings.SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA)
    return render(request, 'home.html')
