from rest_framework import serializers
from candidate.models import PersonalDetails


class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = "__all__"
