from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/images')
    age = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.user.username