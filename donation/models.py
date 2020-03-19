from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Category name')



INSTITUTIONS_TYPES = (
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna")
)
class Institution(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Institution name')
    description = models.TextField(max_length=256)
    type = models.IntegerField(choices=INSTITUTIONS_TYPES, default=0)
    categories = models.ManyToManyField(Category)



class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
