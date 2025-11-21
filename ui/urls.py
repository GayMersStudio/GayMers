
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.default_top, name="main"),
    path('components/', include('django_components.urls'))
]
