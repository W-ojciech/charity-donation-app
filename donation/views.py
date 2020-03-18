from django.shortcuts import render, redirect
from django.views import View

from donation.models import Donation, Category


class LandingPageView(View):
    def get(self, request):
        return render(request, "index.html")



class AddDonationView(View):
    def get(self, request):
        # donations = Donation.objects.all()
        # donations = list(donations)
        # number_of_donations = donations.count()
        return render(request, "form.html")
    # def post(self, request):
    #     return redirect(DonationConfirmedView)

class DonationConfirmedView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")



class LoginView(View):
    def get(self, request):
        return render(request, "login.html")



class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
