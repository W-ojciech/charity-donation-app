from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import View
from donation.models import Donation, Category, Institution
from django.contrib.auth import authenticate, login, get_user_model
from donation_auth.models import User
from django.urls import reverse_lazy
from donation_auth import admin



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

        paginator = Paginator(non_governmental_organizations, 5)
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
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories,
                                            'institutions': institutions})
    def post(self, request):
        categories_checked = request.POST.getlist("categories")
        bags_quantity = request.POST.get("bags")
        institution_checked = Institution.objects.get(pk=request.POST.get('organization'))
        address = request.POST.get("address")
        phone_number = request.POST.get("phone")
        city = request.POST.get("city")
        postcode = request.POST.get("postcode")
        pick_up_date = request.POST.get("data")
        pick_up_time = request.POST.get("time")
        pick_up_comment = request.POST.get("more_info")
        user = User.objects.get(pk=request.user.id)
        new_donation = Donation.objects.create(
            quantity=bags_quantity,
            institution=institution_checked,
            address=address,
            phone_number=phone_number,
            city=city,
            zip_code=postcode,
            pick_up_date=pick_up_date,
            pick_up_time=pick_up_time,
            pick_up_comment=pick_up_comment,
            user=user
        )
        new_donation.save()
        for category in categories_checked:
            new_donation.categories.add(category)
        return render(request, "form-confirmation.html")

class DonationConfirmedView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")



class LoginView(View):
    def get(self, request):
        form = admin.UserLoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        form = admin.UserLoginForm()
        if user is None:
            message = 'User does not exist'
            try:
                User.objects.get(email=email)
            except Exception:
                return render(request, 'login.html', {'form': form, 'message': message})
            else:
                message = 'Password is incorrect'
            return render(request, 'login.html', {'form': form, 'message': message})
        login(request, user)
        return render(request, 'index.html')




class RegisterView(View):
    def get(self, request):
        form = admin.AddUserForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = admin.AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('login')
        return render(request, 'register.html', {'form': form})



class UserPageView(View):
    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        donations = Donation.objects.filter(user=request.user.id)
        return render(request, 'user_page.html', {'user': user, 'donations': donations})
