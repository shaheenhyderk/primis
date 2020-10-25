from rest_framework.response import Response
from .models import Details, JobOpenings, QuestionIndex, SpecificQuestions, AptitudeQuestions
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
import uuid
from candidate.serializers import SpecificQuestionsSerializer


# Create your views here.

class CompanyLogin(APIView):
    def post(self, request):
        company = Details.objects.filter(email=request.data['email']).first()
        if company is not None:
            if check_password(request.data['password'], company.password):
                return Response({"companyId": company.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class CompanyQuestion(APIView):
    def get(self, request, id):
        data_list = []
        job_openings = JobOpenings.objects.filter(company_id=id)
        for x in job_openings:
            question_index = QuestionIndex.objects.filter(job_opening_id=x.id).values('question_id')
            question_index_list = []
            for y in question_index:
                question_index_list.append(y["question_id"])
            specific_questions = SpecificQuestions.objects.filter(pk__in=question_index_list)[:3]
            sub_data = {
                "jobOpeningId": x.id,
                "jobOpeningTitle": x.name,
                "questions": SpecificQuestionsSerializer(specific_questions, many=True).data
            }
            data_list.append(sub_data)
        return Response(data_list, status=status.HTTP_200_OK)

    def post(self, request):
        job_opening = JobOpenings.objects.create(id=uuid.uuid1(), name=request.data['jobOpening'],
                                                 company_id=request.data['companyId'])
        job_opening.save()
        for x in request.data['questions']:
            specific_question = SpecificQuestions.objects.create(id=uuid.uuid1(), question=x['question'],
                                                                 choice1=x['choice1'], choice2=x['choice2'],
                                                                 choice3=x['choice3'], choice4=x['choice4'],
                                                                 answer=x['answer'])
            specific_question.save()
            question_index = QuestionIndex.objects.create(id=uuid.uuid1(), job_opening_id=job_opening.id,
                                                          question_id=specific_question.id)
            question_index.save()
        return Response(status=status.HTTP_200_OK)


class CompanyQuestionEdit(APIView):
    def post(self, request):
        x = request["question"]
        specific_question = SpecificQuestions.objects.create(id=uuid.uuid1(), question=x['question'],
                                                             choice1=x['choice1'], choice2=x['choice2'],
                                                             choice3=x['choice3'], choice4=x['choice4'],
                                                             answer=x['answer'])
        specific_question.save()
        question_index = QuestionIndex.objects.create(id=uuid.uuid1(), job_opening_id=request["jobOpeningId"],
                                                      question_id=specific_question.id)
        question_index.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id):
        specific_question = SpecificQuestions.objects.get(id=id)
        specific_question.delete()
        question_index = QuestionIndex.objects.get(question_id=id)
        question_index.delete()
        return Response(status=status.HTTP_200_OK)


class CompanyDashboard(APIView):
    def get(self, request, id):
        return Response(status=status.HTTP_200_OK)