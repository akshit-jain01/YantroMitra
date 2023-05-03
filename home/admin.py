from django.contrib import admin
from .models import Notifications, Associations, Memories

# Register your models here.

admin.site.register(Associations)
admin.site.register(Notifications)
admin.site.register(Memories)

