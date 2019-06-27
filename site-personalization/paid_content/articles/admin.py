from django.contrib import admin
from .models import Article, Profile


class ArticleAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, ProfileAdmin)
