from django.urls import path
from .views.contact_views import *
from .views.menu_item_company import MenuAPIView
from .views.slider_views import SliderAPIView
from .views.menu_item_service import MenuItemServiceViewSet 
from .views.menuItem_product import ProductsViewSet


urlpatterns = [
    path("create/", create_contact),
    path("getcontact/", get_contact),
    path("getcontact/<int:pk>", get_contact_id),
    path("updatecontact/<int:pk>", update_contact),
    path("deletecontact/<int:pk>", delete_contact), 
    
    # class base
     path("menucompany_industries/", MenuAPIView.as_view()),
     path("menucompany_industries/<int:pk>/", MenuAPIView.as_view()),
     path("slider/", SliderAPIView.as_view()),
     path("slider/<int:pk>/", SliderAPIView.as_view()),
     path('menuservice/', MenuItemServiceViewSet.as_view()),
     path('menuservice/<int:pk>/', MenuItemServiceViewSet.as_view()),
     path("menuproduct/", ProductsViewSet.as_view()),
     path("menuproduct/<int:pk>/", ProductsViewSet.as_view()),

] 