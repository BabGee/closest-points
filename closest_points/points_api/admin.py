from django.contrib import admin

from points_api.models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ('x', 'y')

admin.site.register(Point, PointAdmin)
