from django.contrib import admin
from .models import Category, Wrapper, Topping, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(IceCream, IceCreamAdmin)

admin.site.register(Category)
admin.site.register(Wrapper)
admin.site.register(Topping)
