from django.contrib import admin
from django.urls import path
from donation.views import LandingPageView, AddDonationView, LoginView, RegisterView, \
    DonationConfirmedView, UserPageView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),

    path('', LandingPageView.as_view(), name='home'),
    path('add-donation/', AddDonationView.as_view(), name='donation'),
    path('donation-confirmed/', DonationConfirmedView.as_view(), name='donation-confirmed'),

    path('user-page/', UserPageView.as_view(), name='user-page'),
    path('user-edit/', UserEditView.as_view(), name='user-edit'),
]
