from rest_framework import serializers
from company.models import Details


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id', 'name', 'username', 'email', 'phone')
