from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="35" style="border-radius: 50%" />'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ['full_name', 'thumbnail', 'designation', 'created_date']
    list_display_links = ('full_name', 'thumbnail')

    class Meta:
        model = Team


admin.site.register(Team, TeamAdmin)
