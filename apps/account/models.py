from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # save current date time when the model is updated 
    updated = models.DateTimeField(auto_now=True)
    point = models.IntegerField(default=0)
    transaction_password = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username.capitalize()




