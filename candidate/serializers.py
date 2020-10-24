from rest_framework import serializers
from company.models import JobOpenings, Details, AptitudeQuestions, SpecificQuestions


class JObOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpenings
        fields = ('id', 'name')


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('name',)


class AptitudeQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AptitudeQuestions
        fields = "__all__"


class SpecificQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificQuestions
        fields = "__all__"
