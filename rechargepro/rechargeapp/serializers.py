from rest_framework import serializers 
from .models import Recommended,HeroUnlimited,OtherPacks

class RecommendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommended
        fields = ['talktime','calls','SMS','validity','additional_benefit','price']


class HeroUnlimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroUnlimited
        fields = ['talktime','data','validity','additional_benefit','price']


class OtherPacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPacks
        fields = ['talktime','price']