from django.db import models
from django.conf import settings

# Create your models here.

class Investment(models.Model):
    investment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    prize = models.IntegerField()
    time = models.IntegerField()
    # risk = models.IntegerField(choices=INTEREST_RATE, default=LOW)
    total_amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


