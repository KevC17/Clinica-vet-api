from django.urls import path
from . import views

urlpatterns = [
    path('pets/list', views.pets_get_list),
    path('pets', views.pets_post_create),
    path('pets/<int:id>/', views.pets_get_by_id),
    path('pets/<int:id>/',views.pets_put),
    path('pets/<int:id>/',views.pets_delete)
]