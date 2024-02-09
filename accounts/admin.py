from django.contrib import admin
from .models import Address, Porfile, ContactNumbers

# Register your models here.

admin.site.register(Address)
admin.site.register(Porfile)
admin.site.register(ContactNumbers)

