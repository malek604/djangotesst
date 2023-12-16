from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'password')  # فیلدهایی که می‌خواهید در لیست نمایش داده شوند
    search_fields = ('email', 'username')  # فیلدهایی که می‌خواهید قابلیت جستجو داشته باشند

# ثبت مدل CustomUser با CustomUserAdmin مخصوص برای مدیریت بهتر در پنل ادمین
admin.site.register(CustomUser, CustomUserAdmin)
