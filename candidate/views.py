from rest_framework.response import Response
# from .models import
from rest_framework import status
from rest_framework.views import APIView
from company.models import Details, JobOpenings, AptitudeQuestions, QuestionIndex, SpecificQuestions
from .serializers import JObOpeningSerializer, CompanyDetailSerializer, AptitudeQuestionsSerializer, \
    SpecificQuestionsSerializer
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


class CandidateQuestions(APIView):
    def get(self, request, id):
        question_index = QuestionIndex.objects.filter(job_opening_id=id).values('question_id')
        question_index_list = []
        for x in question_index:
            question_index_list.append(x["question_id"])
        specific_questions = SpecificQuestions.objects.filter(pk__in=question_index_list)
        return Response(SpecificQuestionsSerializer(specific_questions, many=True).data, status=status.HTTP_200_OK)


class CandidateSubmit(APIView):
    def post(self, request):
        return Response(SpecificQuestionsSerializer(status=status.HTTP_200_OK))
