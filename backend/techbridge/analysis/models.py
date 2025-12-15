from django.db import models
from accounts.models import User


class Question(models.Model):
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text[:50]


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options"
    )
    text = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.text} ({self.score})"


class PersonalityResult(models.Model):
    LEARNING_LEVELS = (
        ("slow", "Slow Learner"),
        ("average", "Average Learner"),
        ("fast", "Fast Learner"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="personality_result"
    )
    total_score = models.IntegerField()
    learning_level = models.CharField(
        max_length=20,
        choices=LEARNING_LEVELS
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.learning_level}"
