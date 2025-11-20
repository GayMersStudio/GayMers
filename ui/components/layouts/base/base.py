
from django_components import component


@component.register("base")
class Base(component.Component):
    template_name = "base.html"
