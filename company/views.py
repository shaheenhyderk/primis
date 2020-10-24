from rest_framework.response import Response
from .models import Details, JobOpenings, QuestionIndex, SpecificQuestions, AptitudeQuestions
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
import uuid
import xlrd


# Create your views here.

class CompanyLogin(APIView):
    # def get(self, request):
    #     path = "D:\shahe\Downloads\Aptitude.xlsx"
    #     wb = xlrd.open_workbook(path)
    #     sheet = wb.sheet_by_index(0)
    #     for i in range(15, 17):
    #         aptitude_questions = AptitudeQuestions.objects.create(id=uuid.uuid1(), question=str(sheet.cell_value(i, 0)),
    #                                                               choice1=str(sheet.cell_value(i, 1)),
    #                                                               choice2=str(sheet.cell_value(i, 2)),
    #                                                               choice3=str(sheet.cell_value(i, 3)),
    #                                                               choice4=str(sheet.cell_value(i, 4)),
    #                                                               answer=str(sheet.cell_value(i, 5)))
    #         aptitude_questions.save()
    #
    #     return Response(status=status.HTTP_200_OK)

    def post(self, request):
        company = Details.objects.filter(email=request.data['email']).first()
        if company is not None:
            if check_password(request.data['password'], company.password):
                return Response({"companyId": company.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class CompanyQuestion(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

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
