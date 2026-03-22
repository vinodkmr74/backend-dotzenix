from django.urls import path
from .views.contact_views import *
from .views.menu_item_company import MenuAPIView
from .views.slider_views import SliderAPIView
from .views.menu_item_service import MenuItemServiceViewSet 
from .views.menuItem_product import ProductsViewSet
from .views.HeddingSunhedding import HeddingSunheddingAPIView
from .views.OurServiceCard import OurServiceCardViewSet
from .views.subitemOurservice import SubitemUpdateView
from .views.ProductCard import ProductCardViewSet
from .views.MissionVision import MissionVisionView
from .views.Satisfied import SatisfiedViewSet
from .views.OurExpertise import OurExpertiseViewSet
from .views.ExploreOur import ExploreOurViewSet

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
     path("heddingsunhedding/", HeddingSunheddingAPIView.as_view()),
     path("heddingsunhedding/<int:pk>/", HeddingSunheddingAPIView.as_view()),
     path("ourservicecard/",OurServiceCardViewSet.as_view()),
     path("ourservicecard/<int:pk>/",OurServiceCardViewSet.as_view()),
    #  path("subitems",OurServiceCardViewSet.as_view()),
    #  path("subitems/<int:pk>/",OurServiceCardViewSet.as_view()),
     path("subitems/<int:pk>/", SubitemUpdateView.as_view()),
     path("productcard/",ProductCardViewSet.as_view()),
     path("productcard/<int:pk>/",ProductCardViewSet.as_view()),
     path("missionvission/", MissionVisionView.as_view()),
     path("missionvission/<int:pk>/", MissionVisionView.as_view()),
     path("satisfied/", SatisfiedViewSet.as_view()),
     path("satisfied/<int:pk>/", SatisfiedViewSet.as_view()),
     path("ourexpertise/", OurExpertiseViewSet.as_view()),
     path("ourexpertise/<int:pk>/", OurExpertiseViewSet.as_view()),

     path("exploreour/", ExploreOurViewSet.as_view()),
     path("exploreour/<int:pk>/", ExploreOurViewSet.as_view()),

] 