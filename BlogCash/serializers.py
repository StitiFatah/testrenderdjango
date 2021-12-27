from rest_framework import serializers
from .models import TestImages


class TestImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestImages
        fields = "__all__"
