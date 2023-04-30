from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ['id','username','password']
       extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
  

class MealSerializer(serializers.ModelSerializer):
    class Meta:
       model = Meal
       fields = ['id','title','description']
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
       model = Rating
       fields = ['id','meal','user','stars']