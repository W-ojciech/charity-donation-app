from django import forms
from donation.models import Donation


class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'






# from donation_auth.models import User
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#
#
# class UserLoginForm(AuthenticationForm):
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'placeholder': 'Email', 'autofocus': True}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'placeholder': 'Password', 'autocomplete': 'current-password'}))


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'placeholder': 'Email', 'autofocus': True}))
#     password1 = forms.CharField(
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
#                                           'placeholder': 'Hasło'}),
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}),
#     )
#
#     class Meta:
#         model = User
#         fields = ("email", "password1", "password2")


