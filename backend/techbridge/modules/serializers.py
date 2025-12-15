from rest_framework import serializers
from .models import LearningModule, ModuleTest


class LearningModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningModule
        fields = "__all__"


class ModuleTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleTest
        fields = "__all__"
