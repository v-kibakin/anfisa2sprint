from django.contrib import admin
from .models import Category, Wrapper, Topping, IceCream


class IceCreamAdmin(admin.ModelAdmin):
    ...


admin.register(IceCream, IceCreamAdmin)

admin.site.register(Category)
admin.site.register(Wrapper)
admin.site.register(Topping)
