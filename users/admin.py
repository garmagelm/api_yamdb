from django.apps import apps
from django.contrib import admin

models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active',)
    empty_value_display = '-пусто-'
