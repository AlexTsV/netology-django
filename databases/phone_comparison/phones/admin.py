from django.contrib import admin

from .models import Phone, Samsung, Xiaomi, Apple

# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    pass


class SamsungAdmin(admin.ModelAdmin):
    pass


class AppleAdmin(admin.ModelAdmin):
    pass


class XiaomiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Samsung, SamsungAdmin)
admin.site.register(Apple, AppleAdmin)
admin.site.register(Xiaomi, XiaomiAdmin)