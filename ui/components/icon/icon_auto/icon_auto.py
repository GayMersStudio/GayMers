
from typing import Any

from django.template import Context
from django_components import component


ICONS = {
    "none": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M10 18V21M14 20V21M21 12V13C21 15.2091 19.2091 17 17 17V21H7V17C4.79086 17 3 15.2091 3 13V12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12ZM10 10.5C10 11.6046 9.10457 12.5 8 12.5C6.89543 12.5 6 11.6046 6 10.5C6 9.39543 6.89543 8.5 8 8.5C9.10457 8.5 10 9.39543 10 10.5ZM18 10.5C18 11.6046 17.1046 12.5 16 12.5C14.8954 12.5 14 11.6046 14 10.5C14 9.39543 14.8954 8.5 16 8.5C17.1046 8.5 18 9.39543 18 10.5Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>',
    "search": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>'
}


@component.register("icon_auto")
class IconAuto(component.Component):
    template_name = "icon_auto.html"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context):
        icon = kwargs.get("icon")
        icon_key = icon if icon in ICONS else "none"

        return {
            "id": kwargs.get("id"),
            "fill": kwargs.get("fill", "none"),
            "stroke": kwargs.get("stroke", "none"),
            "class": kwargs.get("class", "none"),
            "content": ICONS[icon_key]
        }

