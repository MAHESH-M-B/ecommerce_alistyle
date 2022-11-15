from django.urls import include, path
from rest_framework import routers

from .views import StoreViewset
from store import views
router = routers.DefaultRouter()
router.register(r'Category', StoreViewset)

urlpatterns = [
    path('api/store_api/', include(router.urls)),
    path('store/',views.store,name='store'),
    path('store/<slug:category_slug>/',views.store,name='product_by_category')
]
