from django.contrib import admin

from core.models import Appointment, Hospital, HospitalImage, HospitalVideo, Service, User

# Register your models here.
admin.site.register(Hospital)
admin.site.register(HospitalImage)
admin.site.register(HospitalVideo)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(User)