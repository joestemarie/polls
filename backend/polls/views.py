from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PollSerializer, QuestionResultSerializer
from .models import Poll, QuestionResult

class PollView(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


@api_view(["GET"])
def question_result_list(request, poll_id):
    """Get all the question results for a single poll."""
    this_poll = Poll.objects.get(id=poll_id)
    question_results = QuestionResult.objects.filter(poll=this_poll)
    serializer = QuestionResultSerializer(question_results, many=True)
    return Response(serializer.data)
