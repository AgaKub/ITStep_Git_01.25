from django.urls import path, include
from .import views
from django.views.generic import TemplateView
from rest_framework import routers
from .views import KategoriaViewSet

from .views import ProduktyViewSet

router = routers.DefaultRouter()


router.register(r"produkty", views.ProduktyViewSet)
router.register(r"kategoria", views.KategoriaViewSet)
router.register(r"zamowienia", views.ZamowienieViewSet)
router.register(r'pozycje-zamowienia', views.PozycjaZamowieniaViewset)


urlpatterns = [path("hello/", views.powitanie, name="hello"),
               path("info/", views.wyswietl_info, name="info"),
               path("witaj1/", views.witaj, name="witaj1"),
               #path("produkty/", views.lista_produktow, name="produkty"),
               path("o_nas/", TemplateView.as_view(template_name="mojaaplikacja/o_nas.html"),name="o_nas"),
               path("kontakt/", views.kontakt, name='kontakt'),
               path("rejestracja/", views.rejestracja, name='rejestracja'),
               path("produkty/", views.ProduktList.as_view(), name="lista_produktow"),
               path("produkty/", views.ProduktDetail.as_view(), name="produkt-detail"),
               #path("produkty/", views.produkt_list, name="lista_produktow"),
               #path("produkty/<int:pk>", views.produkt_detail, name="produkt-detail")
               path('kategoria/<int:pk/', views.KategoriaDetail.as_view(), name='kategoria-detail'),
               path("", include(router.urls)),




]
