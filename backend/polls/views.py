from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PollSerializer
from .models import Poll

class PollView(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
