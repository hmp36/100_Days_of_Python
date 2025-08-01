"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views  # Add this import at the top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # <-- Add this line
    path('about/', views.about, name='about'),  # <-- Add this line
    path('services/', views.services, name='services'),  # <-- Add this line
    path('contact/', views.contact, name='contact'),  # <-- Add this line
    path('faq/', views.faq, name='faq'),  # <-- Add this line
    path('api/greeting/', views.api_greeting, name='api_greeting'),  # <-- Add this line
    path('api/messages/', views.api_messages, name='api_messages'),  # <-- Add this line
    # other app-specific URLs
]
