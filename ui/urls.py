
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.default_top, name="main"),
    path('welcome', views.welcome, name="welcome"),
    path('sign_up', views.welcome, name="sign_up"),
    path('components/', include('django_components.urls'))
]
