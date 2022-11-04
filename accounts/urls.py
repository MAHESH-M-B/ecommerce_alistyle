
from django.urls import path,include
from rest_framework import routers
from .views import AccountViewset

router=routers.DefaultRouter()
router.register(r'Account',AccountViewset)


urlpatterns = [
    path('api/Accounts_api/',include(router.urls)),
]
