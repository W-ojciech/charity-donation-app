from django.contrib.auth.forms import PasswordChangeForm
from donation_auth.models import User


class UserEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'
