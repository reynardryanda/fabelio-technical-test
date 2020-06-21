from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mst-product', views.MSTProductViewSet,basename='mst-product')
router.register(r'trx-product', views.TRXProductViewSet,basename='trx-product')

urlpatterns = [
    path('', include(router.urls)),
]