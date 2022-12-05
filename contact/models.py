from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(default="Website_Enquiry", max_length=80)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email