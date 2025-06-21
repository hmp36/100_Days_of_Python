from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    message_count = Message.objects.count()
    user_count = User.objects.count()
    return render(request, 'dashboard.html', {
        'message_count': message_count,
        'user_count': user_count,
    })