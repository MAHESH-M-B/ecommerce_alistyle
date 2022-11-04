from django.urls import include, path
from rest_framework import routers

from .views import Categoryviewset

router = routers.DefaultRouter()
router.register(r'Category', Categoryviewset)

urlpatterns = [
    path('api/category_api/', include(router.urls)),
]
