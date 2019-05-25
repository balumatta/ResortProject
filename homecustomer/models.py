from django.db import models


class CustomerFeedback(models.Model):
    cutomer_name = models.CharField(max_length=120, null=True, blank=True)
    customer_feedback = models.TextField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return self.cutomer_name


class StayConnected(models.Model):
    customer_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.customer_email
