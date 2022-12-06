from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=False)
    last_name = models.CharField(max_length=50,  null=True, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(default="Website_Enquiry", max_length=80)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email