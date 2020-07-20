from django.contrib.auth.backends import BaseBackend
from .models import User
from django.db.models import Q


class MyLoginBack(BaseBackend):
    def authenticate(self, request, **kwargs):
        '''

        :param request:
        :param kwargs:
        :return:
        '''
        username = kwargs['username']
        password = kwargs['password']
        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(telphone=username)).first()
        if user:
            b = user.check_password(password)
            if b:
                return user
            else:
                return None
        else:
            return None

