from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact



class ContactAdmin(admin.ModelAdmin):

    readonly_fields = ('first_name', 'last_name', 'email','date', 'subject', 'message')

    fields = ('first_name', 'last_name', 'email','date', 'subject', 'message')

    list_display = ('first_name', 'last_name', 'email','date')

    ordering = ('-date',)

admin.site.register(Contact, ContactAdmin)