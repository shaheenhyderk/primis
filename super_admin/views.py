from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from company.models import Details
from .serializers import AdminSerializer
from django.contrib import auth
import uuid
from django.contrib.auth.hashers import make_password


class AdminLogin(APIView):

    def post(self, request):
        user = auth.authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class AdminCompanies(APIView):

    def get(self, request):
        companies = Details.objects.all()
        return Response(AdminSerializer(companies, many=True).data)

    def post(self, request):
        password = make_password(request.data['password'])
        details = Details.objects.create(id=uuid.uuid1(), name=request.data['name'], username=request.data['username'],
                                         email=request.data['email'], phone=request.data['phone'], password=password)
        details.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id):
        detail = Details.objects.get(id=id)
        detail.delete()
        return Response(status=status.HTTP_200_OK)
