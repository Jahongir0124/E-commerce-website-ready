from django.contrib import admin
from .models import *
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Customer)

