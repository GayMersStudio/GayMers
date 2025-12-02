from typing import Any, Optional, Mapping

from django.template import Context
from django_components import component


@component.register("tab")
class Tab(component.Component):
    template_name = "tab.html"
    js_file = "tab.js"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context) -> Optional[Mapping]:
        return {
            "target": kwargs.get("target", ""),
        }
