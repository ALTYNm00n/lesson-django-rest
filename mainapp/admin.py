from django.contrib import admin

from mainapp.models import (
    User,UserAdmin,Participant,Organizer)

admin.site.register(User)
admin.site.register(UserAdmin)
admin.site.register(Participant)
admin.site.register(Organizer)