from rest_framework import viewsets
from .models import Meal,Rating
from .serializers import MealSerializer,RatingSerializer


class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
# Create your views here.
