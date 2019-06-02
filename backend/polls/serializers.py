from rest_framework import serializers
from .models import Poll, QuestionResult

class PollSerializer(serializers.ModelSerializer):
    pollster_name = serializers.ReadOnlyField(source='pollster.name')
    class Meta:
        model = Poll
        fields = "__all__"



class QuestionResultSerializer(serializers.ModelSerializer):
    question_text = serializers.ReadOnlyField(source="question.name")
    candidate_name = serializers.ReadOnlyField(source="candidate.name")
    class Meta:
        model = QuestionResult
        fields = "__all__"
