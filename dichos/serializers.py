from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dicho


class DichoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'creator', 'saying', 'translation', 'category'
        )
        model = Dicho
