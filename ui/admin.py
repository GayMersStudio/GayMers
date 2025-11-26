from django.contrib import admin
from .models import Game


@admin.register(Game)
class MyModelAdmin(admin.ModelAdmin):
    fields = ("title", "desc", "price", "pic", "trailer")
    list_display = ('title', 'price')
    search_fields = ('title', )
    list_filter = ('created_at', )
