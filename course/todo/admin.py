from django.contrib import admin

from todo import models


class TodoAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Todo, TodoAdmin)
