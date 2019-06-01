from django.contrib import admin
from .models import Candidate, Question, Pollster, Poll, QuestionResult

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Question)
admin.site.register(Pollster)
admin.site.register(Poll)
admin.site.register(QuestionResult)
