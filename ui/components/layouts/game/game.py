from typing import Any, Optional, Mapping

from django.template import Context
from django_components import component


@component.register("game")
class Game(component.Component):
    template_name = "game.html"
    css_file = "game.css"
    js_file = "game.js"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context) -> Optional[Mapping]:
        return {
            "title": kwargs.get("title", "Unknown game"),
            "pic": kwargs.get("pic", ""),
            "trailer": kwargs.get("trailer", ""),
            "desc": kwargs.get("desc", "no description"),
            "price": kwargs.get("price", "ERROR")
        }
