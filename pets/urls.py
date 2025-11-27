from django.urls import path
from . import views

urlpatterns = [
    path('pets/list', views.pets_get_list),
    path('pets', views.pets_post_create),
    path('pets/<int:id>/', views.pets_get_by_id),
    path('pets/<int:id>/update',views.pets_put),
    path('pets/<int:id>/delete',views.pets_delete),
    path('pets/tratamientos/dosis-total',views.pets_daily_dose),
    path('pets/mascotas/control-peso',views.pets_weight_control)
]