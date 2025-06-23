from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    message_count = Message.objects.count()
    user_count = User.objects.count()
    recent_messages = Message.objects.order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {
        'message_count': message_count,
        'user_count': user_count,
        'recent_messages': recent_messages,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})