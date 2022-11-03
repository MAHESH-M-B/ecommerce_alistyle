from django.urls import include,path
from rest_framework import routers
from .views import CategoryViewset


router=routers.DefaultRouter()
router.register(r'Category',CategoryViewset)

urlpatterns=[
    path('/api/category_api/',include(router.urls)),
]