from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': MessageForm(), 'success': True})
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def dashboard(request):
    message_count = Message.objects.count()
    user_count = User.objects.count()
    recent_messages = Message.objects.order_by('-created_at')[:5]
    return render(request, 'dashboard.html', {
        'message_count': message_count,
        'user_count': user_count,
        'recent_messages': recent_messages,
    })