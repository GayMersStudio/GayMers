
from django_components import component


@component.register("tab")
class Tab(component.Component):
    template_name = "tab.html"
    js_file = "tab.js"
