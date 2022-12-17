from django.contrib import admin
from vamsiele.models import users

# Register your models here.
class usersAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Mobile', 'Message']
admin.site.register(users, usersAdmin)
