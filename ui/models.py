
from datetime import datetime
from django.db import models


class TimestampedModel(models.Model):
    id: str

    created_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Game(TimestampedModel):
    title: str = models.TextField()
    desc: str = models.TextField()
    pic: str = models.TextField()
    trailer: str = models.TextField(null=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"Game(@{self.title})"


class Gameslist(TimestampedModel):
    key: str = models.TextField(unique=True)
    title: str = models.TextField()

    games = models.ManyToManyField(
        to=Game,
        blank=True
    )

    def __str__(self):
        return f"GamesList(@{self.key})"
