from django.contrib import admin
from .models import Product, Category, UserReview

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'age_range',
        'price',
        'rating',
        'image',
    )

    order = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class UserReviewAdmin(admin.ModelAdmin):

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