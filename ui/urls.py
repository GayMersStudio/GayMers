
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('welcome', views.welcome, name="welcome"),
    path('api/v1/lists', views.GamesListView.as_view()),
    path('api/v1/search', views.SearchView.as_view()),
    path('components/', include('django_components.urls'))
]
