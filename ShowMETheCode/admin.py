from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Category, Material, Color, Accessory

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock', 'is_available', 'discount', 'colored_name', 'created_at')
    list_filter = ('brand', 'category', 'material', 'color', 'is_available', 'created_at')
    search_fields = ('name', 'description', 'brand__name', 'category__name', 'material__name', 'color__name')
    ordering = ('-created_at',)
    list_editable = ('price', 'stock', 'discount', 'is_available')
    date_hierarchy = 'created_at'

    def colored_name(self, obj):
        return format_html('<span style="color: #{};">{}</span>',
                           obj.color.name if obj.color else '000', obj.name)
    colored_name.short_description = 'Name'


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Accessory, AccessoryAdmin)
