from django.contrib import admin
from .models import UserReview

# Register your models here.


class (admin.ModelAdmin):

    readonly_fields = ('user', 'product',
                       'date', 'updated',
                       'title', 'content')

    fields = ('user', 'product',
                'date', 'updated',
                'title', 'content')

    list_display = ('user', 'product',
                       'date', 'updated',
                       'title')

    ordering = ('-date', 'product', 'user')


admin.site.register(UserReview, UserReviewAdmin)