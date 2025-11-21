from typing import Any, Optional, Mapping

from django.template import Context
from django_components import component


@component.register("sign_up")
class Sign_up(component.Component):
    template_name = "sign_up.html"

   
