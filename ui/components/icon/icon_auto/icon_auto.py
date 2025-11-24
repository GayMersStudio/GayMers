
from typing import Any

from django.template import Context
from django_components import component


ICONS = {
    "none": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M10 18V21M14 20V21M21 12V13C21 15.2091 19.2091 17 17 17V21H7V17C4.79086 17 3 15.2091 3 13V12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12ZM10 10.5C10 11.6046 9.10457 12.5 8 12.5C6.89543 12.5 6 11.6046 6 10.5C6 9.39543 6.89543 8.5 8 8.5C9.10457 8.5 10 9.39543 10 10.5ZM18 10.5C18 11.6046 17.1046 12.5 16 12.5C14.8954 12.5 14 11.6046 14 10.5C14 9.39543 14.8954 8.5 16 8.5C17.1046 8.5 18 9.39543 18 10.5Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>',
    "search": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M11 6C13.7614 6 16 8.23858 16 11M16.6588 16.6549L21 21M19 11C19 15.4183 15.4183 19 11 19C6.58172 19 3 15.4183 3 11C3 6.58172 6.58172 3 11 3C15.4183 3 19 6.58172 19 11Z" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g>',
    "windows": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M0 36.357L104.62 22.11l.045 100.914-104.57.595L0 36.358zm104.57 98.293l.08 101.002L.081 221.275l-.006-87.302 104.494.677zm12.682-114.405L255.968 0v121.74l-138.716 1.1V20.246zM256 135.6l-.033 121.191-138.716-19.578-.194-101.84L256 135.6z"></path></g>',
    "mac": '<g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M273.81 52.973C313.806.257 369.41 0 369.41 0s8.271 49.562-31.463 97.306c-42.426 50.98-90.649 42.638-90.649 42.638s-9.055-40.094 26.512-86.971zM252.385 174.662c20.576 0 58.764-28.284 108.471-28.284 85.562 0 119.222 60.883 119.222 60.883s-65.833 33.659-65.833 115.331c0 92.133 82.01 123.885 82.01 123.885s-57.328 161.357-134.762 161.357c-35.565 0-63.215-23.967-100.688-23.967-38.188 0-76.084 24.861-100.766 24.861C89.33 608.73 0 455.666 0 332.628c0-121.052 75.612-184.554 146.533-184.554 46.105 0 81.883 26.588 105.852 26.588z"></path></g>'
}
VIEWBOXES = {
    "windows": "-0.5 0 257 257",
    "mac": "-56.24 0 608.728 608.728"
}


@component.register("icon_auto")
class IconAuto(component.Component):
    template_name = "icon_auto.html"

    def get_template_data(self, args: Any, kwargs: Any, slots: Any, context: Context):
        icon = kwargs.get("icon")
        icon_key = icon if icon in ICONS else "none"

        return {
            "fill": kwargs.get("fill", "none"),
            "stroke": kwargs.get("stroke", "none"),
            "class": kwargs.get("class", "none"),
            "viewbox": VIEWBOXES.get(icon_key, "0 0 24 24"),
            "content": ICONS[icon_key]
        }

