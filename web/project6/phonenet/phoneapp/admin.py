from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Good)
admin.site.register(GoodImg)
admin.site.register(Order)
admin.site.register(Category)