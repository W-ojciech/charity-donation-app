"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from donation.views import LandingPageView, AddDonationView, LoginView, RegisterView, \
    DonationConfirmedView, user_list_view
from django.contrib.auth import views as auth_views
from donation_auth.admin import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='home'),
    path('add-donation/', AddDonationView.as_view(), name='donation'),
    path('login/', LoginView.as_view(), name='login'),
    # path("login/", auth_views.LoginView.as_view(template_name="login.html",
    #                                             authentication_form=UserLoginForm), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('donation-confirmed/', DonationConfirmedView.as_view(), name='donation-confirmed'),
    path('users/', user_list_view, name='users'),
]
