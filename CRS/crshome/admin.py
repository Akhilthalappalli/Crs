from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(FIR)
admin.site.register(Feedback)
admin.site.register(Blocked)
admin.site.register(Notification)
