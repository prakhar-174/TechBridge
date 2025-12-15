from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Question, Option, PersonalityResult
from .serializers import QuestionSerializer
from .services import calculate_learning_level


class QuestionListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.prefetch_related("options").order_by("order")
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class SubmitPersonalityTestAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        answers = request.data.get("answers", [])
        total_score = 0

        for ans in answers:
            option = Option.objects.get(
                id=ans["option_id"],
                question_id=ans["question_id"]
            )
            total_score += option.score

        learning_level = calculate_learning_level(total_score)

        PersonalityResult.objects.update_or_create(
            user=request.user,
            defaults={
                "total_score": total_score,
                "learning_level": learning_level
            }
        )

        profile = request.user.profile
        profile.learning_rate = learning_level
        profile.save()

        request.user.onboarding_stage = 3
        request.user.save()

        return Response({
            "message": "Test submitted successfully",
            "learning_level": learning_level,
            "score": total_score
        })
