from django.db import models

from django.contrib.auth.models import User


# create table mpesaRequest(merchant_id, checkout_id, res_code, res_text, msg, ref, trans_dec, phone, trans_date)
class mpesaRequest(models.Model):
    merchant_id = models.CharField(max_length=50)
    checkout_id = models.CharField(max_length=50)
    res_code = models.IntegerField()
    res_text = models.CharField(max_length=150)
    msg = models.CharField(max_length=150)
    ref = models.CharField(max_length=150)
    trans_dec = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    trans_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Checkout id: {self.checkout_id} by {self.phone}"


class MpesaPayments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt = models.CharField(max_length=20, primary_key=True)
    merchant_id = models.CharField(max_length=50, blank=True, null=True, default="")
    checkout_id = models.CharField(max_length=50, blank=True, null=True, default="")
    res_code = models.IntegerField(blank=True, null=True, default=0)
    res_text = models.CharField(max_length=150, blank=True, null=True, default="")
    amount = models.FloatField(blank=True, null=True, default=0.0)
    phone = models.CharField(max_length=13, blank=True, null=True, default="")
    trans_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return f"Paid {self.amount} for user '{self.user}'"
