"""Models for the poll tracking app."""
from django.db import models


class Candidate(models.Model):
    """Represents a Candidate who can be tied to QuestionResults."""
    name = models.CharField(max_length=100)


class Question(models.Model):
    """
    Represents a question asked within a poll - used to aggregate across polls.

    For horse race polls, we set up one question (e.g., "2020 Horse Race") and then include
    candidate IDs within the JSON data for each QuestionResult (see: QuestionResult).
    For questions like favorability, these could be asked of multiple Candidates, so we allow
    questions to be reused across these.
    """
    name = models.CharField(max_length=100)



class Pollster(models.Model):
    """Represents a Pollster that conducts Polls."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Poll(models.Model):
    """Represents a single Poll with one or more Questions."""
    pollster = models.ForeignKey(Pollster, on_delete=models.PROTECT)
    notes = models.TextField(blank=True, null=True)
    n_size = models.PositiveIntegerField()
    field_date_start = models.DateField()
    field_date_end = models.DateField()
    release_link = models.URLField()

    # define choices for the methodology
    METHODOLOGY_TYPES = (
        ("P", "Phone"),
        ("O", "Online"),
    )
    methodology = models.CharField(
        max_length=1,
        choices=METHODOLOGY_TYPES,
    )

    # define choices for the sample type
    SAMPLE_TYPES = (
        ("RV", "Registered Voters"),
        ("LV", "Likely Voters"),
        ("A", "Adults"),
    )
    sample = models.CharField(
        max_length=2,
        choices=SAMPLE_TYPES
    )



class QuestionResult(models.Model):
    """Represents the specific results for one question within a poll."""
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    data_json = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, blank=True, null=True)
