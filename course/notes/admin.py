from django.contrib import admin

# Register your models here.
from notes import models


class SectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Section, SectionAdmin)
