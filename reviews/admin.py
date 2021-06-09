from django.apps import apps
from django.contrib import admin

models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('score', 'pub_date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date',)
