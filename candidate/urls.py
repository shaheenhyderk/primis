from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/', views.CompanyOpenings.as_view(), name='company_opening'),
    path('job-opening/<str:id>/', views.CandidateQuestions.as_view(), name='company_opening'),
    path('submit/', views.CandidateSubmit.as_view(), name='company_opening'),
]
