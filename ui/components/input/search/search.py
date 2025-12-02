
from django_components import component


@component.register("search")
class Search(component.Component):
    template_name = "search.html"
    js_file = "search.js"
