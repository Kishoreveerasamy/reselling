from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom user model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False)  # Allow duplicate usernames
    email = models.EmailField(unique=True)  # Use email as the unique login field

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# Ad model for property listings
class Ad(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)

    def __str__(self):
        return self.title
