from rest_framework.response import Response
# from .models import
from rest_framework import status
from rest_framework.views import APIView
from company.models import Details, JobOpenings, AptitudeQuestions
from .serializers import JObOpeningSerializer, CompanyDetailSerializer, AptitudeQuestionsSerializer
import random


# Create your views here.

class CompanyOpenings(APIView):
    def get(self, request, id):
        detail = Details.objects.get(id=id)
        job_openings = JobOpenings.objects.filter(company_id=detail.id)
        aptitude_questions = AptitudeQuestions.objects.all()[:10]
        data = {
            "company": CompanyDetailSerializer(detail).data,
            "jobOpenings": JObOpeningSerializer(job_openings, many=True).data,
            "aptitudeQuestions": AptitudeQuestionsSerializer(aptitude_questions, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
