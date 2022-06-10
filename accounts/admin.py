from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

# Register your models here.

# to see all info in admin panel we need to below class also because we mase custom user  
class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(CustomUser,CustomUserAdmin)