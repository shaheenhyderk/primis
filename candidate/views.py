from rest_framework.response import Response
# from .models import
from rest_framework import status
from rest_framework.views import APIView
from company.models import Details, JobOpenings, AptitudeQuestions, QuestionIndex, SpecificQuestions
from .serializers import JObOpeningSerializer, CompanyDetailSerializer, AptitudeQuestionsSerializer, \
    SpecificQuestionsSerializer
from .models import PersonalDetails, AptitudeResult, SkillResult
import random
import uuid


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

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        experience_marks = int(request.data["experience"]) / 20 * 20
        correct_aptitude = 0
        for x in request.data["aptitudeQuestions"]:
            if x["correct"]:
                correct_aptitude += 1
        aptitude_marks = correct_aptitude / len(request.data["aptitudeQuestions"]) * 10
        aptitude_marks_percent = correct_aptitude / len(request.data["aptitudeQuestions"]) * 100
        correct_skill = 0
        for x in request.data["aptitudeQuestions"]:
            if x["correct"]:
                correct_skill += 1
        skill_marks = correct_skill / len(request.data["skillQuestions"]) * 70
        skill_marks_percent = correct_skill / len(request.data["skillQuestions"]) * 100
        total_marks = experience_marks + aptitude_marks + skill_marks
        personal_details = PersonalDetails.objects.create(id=uuid.uuid1(), company_id=request.data["companyId"], name=request.data["name"],
                                                          email=request.data["email"], phone=request.data["phone"],
                                                          qualification=request.data["qualification"],
                                                          job_opening_id=request.data["jobOpeningId"],
                                                          experience=int(request.data["experience"]),
                                                          project=request.data["project"],
                                                          why_hire_you=request.data["whyHireYou"], status='Pending',
                                                          aptitude_result=aptitude_marks_percent,
                                                          skill_result=skill_marks_percent, total_result=total_marks)
        personal_details.save()

        for x in request.data["aptitudeQuestions"]:
            aptitude_result = AptitudeResult.objects.create(id=uuid.uuid1(), user_id=personal_details.id,
                                                            question_id=x["questionId"], question=x["questionId"],
                                                            answer=x["answer"], correct=x["correct"])
            aptitude_result.save()

        for x in request.data["skillQuestions"]:
            skill_result = SkillResult.objects.create(id=uuid.uuid1(), user_id=personal_details.id,
                                                      question_id=x["questionId"], question=x["questionId"],
                                                      answer=x["answer"], correct=x["correct"])
            skill_result.save()

        return Response(SpecificQuestionsSerializer(status=status.HTTP_200_OK))
