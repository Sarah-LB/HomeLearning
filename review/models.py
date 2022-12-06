from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class UserReview(models.Model):
    """
    A model to allow users to read and post product reviews
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.subject
