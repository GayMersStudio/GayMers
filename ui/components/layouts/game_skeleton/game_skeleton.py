
from django_components import component


@component.register("game_skeleton")
class GameSkeleton(component.Component):
    template_name = "game_skeleton.html"
