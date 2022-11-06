from django.urls import include, path
from rest_framework import routers

from .views import StoreViewset

router = routers.DefaultRouter()
router.register(r'Category', StoreViewset)

urlpatterns = [
    path('api/store_api/', include(router.urls)),
]
