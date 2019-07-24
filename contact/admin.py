from django.contrib import admin

from .models import Contact, Contact_CSV

to_register = [Contact, Contact_CSV]

admin.site.register(to_register)
