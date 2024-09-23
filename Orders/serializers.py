from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    quote_items = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Quote
        fields = ['company', 'status', 'quote_items']