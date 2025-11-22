

from django.template import Context
from django_components import component


@component.register("welcome_card")
class Welcome_card(component.Component):
    template_name = "welcome_card.html"

    

