from django.contrib import admin

from .models import OurContacts, PhoneNumbers, Schedule

admin.site.register(Schedule)
admin.site.register(OurContacts)
admin.site.register(PhoneNumbers)
