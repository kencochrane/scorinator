from rest_framework import serializers
from .models import ProjectScore, ScoreAttribute, ProjectScoreAttribute


class ScoreAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreAttribute


class ProjectScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectScore


class ProjectScoreAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectScoreAttribute
