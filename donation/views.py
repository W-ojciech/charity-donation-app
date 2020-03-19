from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from donation.models import Donation, Category, Institution



class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        number_of_donations = donations.count()
        list_1 = []
        for i in donations:
            list_1.append(i.institution_id)
        num_of_institutions_with_donation = list(set(list_1))
        fundations = Institution.objects.filter(type=0).order_by('name')
        non_governmental_organizations = Institution.objects.filter(type=1).order_by('name')
        local_collections = Institution.objects.filter(type=2).order_by('name')

        paginator = Paginator(non_governmental_organizations, 1)
        page = request.GET.get('page')
        non_governmental_organizations = paginator.get_page(page)
        return render(request, "index.html", {"number_of_donations": number_of_donations,
                                              "num_of_institutions_with_donation":
                                                  num_of_institutions_with_donation,
                                              "fundations": fundations,
                                              "non_governmental_organizations":
                                                  non_governmental_organizations,
                                              "local_collections": local_collections})



class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")
    def post(self, request):
        return redirect(DonationConfirmedView)

class DonationConfirmedView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")



class LoginView(View):
    def get(self, request):
        return render(request, "login.html")



class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
