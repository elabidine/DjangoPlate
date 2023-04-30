from django.urls import path
from django.conf.urls import include
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('meals', MealViewset)
router.register('rating', RatingViewset)
urlpatterns = [
    path('', include(router.urls))
]
