from django.contrib import admin
from .models import Settings, DeliveryFee

# Register your models here.

admin.site.register(Settings)
admin.site.register(DeliveryFee)
