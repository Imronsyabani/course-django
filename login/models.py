from django.db import models
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth import hashers
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
import logging
logger = logging.getLogger(__name__)


class DetailUser(models.Model):
    related_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_user = models.BooleanField("Is User",default=True)

    def create_object(Object):
        hash_password = hashers.make_password(Object['password'])
        try:
            data = User.objects.create(username=Object['username'],
                                        email=Object['email'],
                                        password = hash_password,
                                    )
            DetailUser.objects.create(related_user=data, is_user=True)
        except Exception as e:
            logger.warning(e)
            return e
        return data
    
    def _valid_login_admin(email,password):
        get_user_object = DetailUser.objects.get(
                                Q(related_user__is_staff=True) | Q(related_user__is_superuser=True),
                                    related_user__email=email)
        try:
            if get_user_object and hashers.check_password(password,get_user_object.related_user.password):
                return True
            else:
                return False
        except Exception as e:
            logger.warning(e)

    def _valid_login_user(email,password):
        get_user_object = DetailUser.objects.filter(is_user__exact=True, related_user__email=email)
        try:
            if get_user_object and hashers.check_password(password,get_user_object[0].related_user.password):
                return True
            else:
                return False
        except Exception as e:
            logger.warning(e)

