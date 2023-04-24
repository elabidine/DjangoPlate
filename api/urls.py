from django.urls import path
from django.conf.urls import include
from .views import RatingViewset, MealViewset
from rest_framework import routers



router = routers.DefaultRouter()
router.register('meals', MealViewset)
router.register('rating', RatingViewset)
urlpatterns = [
    path('', include(router.urls))
]
