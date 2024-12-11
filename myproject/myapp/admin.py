from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Seller, Ticket, SoldTicket

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_seller')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Seller)
admin.site.register(Ticket)
admin.site.register(SoldTicket)
