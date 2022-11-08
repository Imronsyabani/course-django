from django.db import models
from django.contrib.auth import hashers
from django.utils.translation import gettext_lazy as _
import logging
logger = logging.getLogger(__name__)
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=60)
    password = models.TextField()
    is_user = models.BooleanField("Is User",default=True)

    def create_object(Object):
        hash_password = hashers.make_password(Object['password'])
        data = User.objects.create(username=Object['username'],
                                    email=Object['email'],
                                        password= hash_password,
                                            is_user=True)
        return data
    
    def _valid_login(email,password):
        get_user_object = User.objects.filter(email__exact=email)
        try:
            if get_user_object and hashers.check_password(password,get_user_object[0].password):
                return True
            else:
                return False
        except Exception as e:
            logger.warning(e)
