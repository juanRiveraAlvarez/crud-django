from django.urls import path
from tutorials import views

urlpatterns = [
        path('list',views.persona_list, name="list"),
        path('save',views.persona_save, name="save"),
        path('search/<int:pk>',views.search_persona, name="search"),
        path(r'^search/(?P<pk>[0-9]+)$',views.search_persona, name="search"),
        ]
