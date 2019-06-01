from rest_framework import serializers
from .models import Poll

class PollSerializer(serializers.ModelSerializer):
    pollster_name = serializers.ReadOnlyField(source='pollster.name')
    class Meta:
        model = Poll
        fields = "__all__"
