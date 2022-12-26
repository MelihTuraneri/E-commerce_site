from django.urls import path
from laptops import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/laptops/MSI


urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.site_search_view),
    path("msearch/", views.site_msearch_view),
    path("mahone", views.mahone, name="mahone"),
    path("ascsorted", views.ascsorted, name="ascsortedsite"),
    path("descsorted", views.descsorted, name="descsortedsite"),
    path("home/<str:id>", views.laptop_details, name="laptopdetails"),
    path("mahone/<str:id>", views.mahone_details, name="mahonedetails"),
    path("mmarka/<str:marka_liste>", views.Mmarka_listesi, name="mmarkafilter"),
    path("marka/<str:marka_liste>", views.Marka_listesi, name="markafilter"),
    path("islemci/<str:islemci_liste>", views.Islemci_listesi, name="islemcifilter"),
    path("os/<str:os_liste>", views.Os_listesi, name="osfilter"),
    path("size/<str:size_liste>", views.Size_liste, name="sizefilter"),
    path("site/<str:site_liste>", views.Site_liste, name="sitefilter"),
    path("puan/", views.puan, name="puansite")
    #path("marka/<str:marka_liste>/islemci/<str:islemci_liste>", views.Islemci_listesi, name="islemcifilter")
]