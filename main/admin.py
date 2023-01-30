from django.contrib import admin
from .models import Chapter, Theme
class ChapterAdmin(admin.ModelAdmin):
    pass
class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug' : ('name',),}

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Theme, ThemeAdmin)
