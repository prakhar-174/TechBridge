from django.urls import path
from .views import QuestionListAPI, SubmitPersonalityTestAPI

urlpatterns = [
    path("questions/", QuestionListAPI.as_view()),
    path("submit/", SubmitPersonalityTestAPI.as_view()),
]
