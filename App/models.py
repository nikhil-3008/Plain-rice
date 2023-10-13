from django.db import models
from django.conf import settings

class Investment(models.Model):
    investment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    prize = models.IntegerField()
    time = models.IntegerField()
    total_amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

class Investor(models.Model):
    investor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    prize = models.IntegerField()
    total_amount = models.IntegerField(default=0)  


    def __str__(self):
        return self.name


