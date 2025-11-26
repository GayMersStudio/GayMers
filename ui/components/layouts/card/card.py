from typing import Any, Optional, Mapping

from django.template import Context
from django_components import component


@component.register("card")
class Card(component.Component):
    template_name = "card.html"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context) -> Optional[Mapping]:
        card_type = kwargs.get("type", "base")

        return {
            "type": card_type,
            "class": kwargs.get("class", ""),
            "onclick": kwargs.get("onclick", ""),
        }
