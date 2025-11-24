from typing import Any, Optional, Mapping

from django.template import Context
from django_components import component


@component.register("base")
class Base(component.Component):
    template_name = "base.html"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context) -> Optional[Mapping]:
        return {
            "blocks": kwargs.get("blocks", "none"),
        }
