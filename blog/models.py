from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-title',]

    def __str__(self):
        return self.title 


class CustomerCall(models.Model):
    mobile = models.CharField(max_length=50, blank=True, help_text="Optional field")

    class Meta:
        verbose_name_plural = 'Customer Calls'

    def __str__(self):
        return self.mobile


class CustomerEmail(models.Model):
    email = models.CharField(max_length=100, blank=True, help_text="Optional field")

    class Meta:
        verbose_name_plural = 'Customer Emails'

    def __str__(self):
        return self.email
