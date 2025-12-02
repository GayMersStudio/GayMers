
from django.contrib import admin
from .models import Game, Gameslist


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ("title", "desc", "price", "pic", "trailer")
    list_display = ('title', 'price')
    search_fields = ('title', )
    list_filter = ('created_at', )


@admin.register(Gameslist)
class GameslistAdmin(admin.ModelAdmin):
    fields = ("key", "title", "games")
    list_display = ('key', 'title')
    search_fields = ('key', 'title')
    list_filter = ('created_at', )
