from django.db import models
from accounts.models import User


class LearningModule(models.Model):
    DIFFICULTY_CHOICES = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    content = models.TextField()

    is_completed = models.BooleanField(default=False)
    retry_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.user.email}"


class ModuleTest(models.Model):
    module = models.OneToOneField(LearningModule, on_delete=models.CASCADE)
    questions = models.JSONField()  # MCQs
    pass_percentage = models.IntegerField(default=60)

    def __str__(self):
        return f"Test for {self.module.topic}"


class ModuleTestAttempt(models.Model):
    module = models.ForeignKey(LearningModule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    score = models.IntegerField()
    percentage = models.FloatField()
    passed = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
