from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Form Submission"
            message = form.cleaned_data['message']
            from_email = form.cleaned_data.get('email', 'webmaster@localhost')
            send_mail(
                subject,
                message,
                from_email,
                ['your@email.com'],  # Replace with your real email
            )
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

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