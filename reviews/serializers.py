from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_created_at(self, obj):
        # Format the date to the desired format
        return obj.created_at.strftime('%d.%m.%Y')
    