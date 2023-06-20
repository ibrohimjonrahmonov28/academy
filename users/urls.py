from django.urls import path
from . import views
urlpatterns = [
    path("",views.get_shop ,name="mainpage"),
    path("shops/<int:shop_id>/",views.get_category,name="shops"),
    path("barber/<int:barber_id>/",views.get_barber,name="barbers"),
    path("add",views.get_add,name="add" ),

    ]
