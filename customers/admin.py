from django.contrib import admin

from .models import Customer, PostalAddress
# Register your models here.


@admin.register(PostalAddress)
class PostalAddresssAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'vat_id_number', 'creation_date', 'id']
