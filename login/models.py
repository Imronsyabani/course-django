from django.db import models
from django.contrib.auth import hashers
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    password = models.TextField()
    is_user = models.BooleanField("Is User",default=True)

    def create_object(Object):
        hash_password = hashers.make_password(Object.password)
        data = User.objects.create(username=Object['username'],
                                    email=Object['email'],
                                        password= hash_password,
                                            is_user=True)
        return data