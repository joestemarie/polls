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

    def __str__(self):
        return self.name



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

    GEOGRAPHY_CHOICES = (
        ("US", "National"),
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("DC", "Dist. of Columbia"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
    )
    geography = models.CharField(
        max_length=2,
        choices=GEOGRAPHY_CHOICES
    )

    METHODOLOGY_TYPES = [
        ('Phone', (
            ("LC", "Live Caller"),
            ("IV", "IVR"),
            )
        ),
        ("Online", (
            ("WS", "Web Survey"),
            )
        )
    ]
    methodology = models.CharField(
        max_length=2,
        choices=METHODOLOGY_TYPES,
    )

    SAMPLE_METHODS = (
        ("LS", "Listed"),
        ("RD", "Random-digit Dialing"),
        ("PL", "Panel")
    )
    sample_method = models.CharField(
        max_length=2,
        choices=SAMPLE_METHODS
    )

    SAMPLE_TYPES = (
        ("RV", "Registered Voters"),
        ("LV", "Likely Voters"),
        ("A", "Adults"),
    )
    sample = models.CharField(
        max_length=2,
        choices=SAMPLE_TYPES
    )

    def __str__(self):
        return "{} - {} ({} - {})".format(
            self.pollster.name,
            self.geography,
            self.field_date_start,
            self.field_date_end
        )



class QuestionResult(models.Model):
    """Represents the specific results for one question within a poll."""
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    data_json = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT, blank=True, null=True)
