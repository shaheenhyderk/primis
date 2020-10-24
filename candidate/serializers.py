from rest_framework import serializers
from company.models import JobOpenings, Details, AptitudeQuestions


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
