from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CompanyLogin.as_view(), name='company_login'),
    path('questions/', views.CompanyQuestion.as_view(), name='company_login'),
    path('question/add/', views.CompanyQuestionEdit.as_view(), name='company_question_add'),
    path('question/<str:id>/', views.CompanyQuestionEdit.as_view(), name='company_question_delete'),
    path('<str:id>/questions/', views.CompanyQuestion.as_view(), name='company_login'),
    path('<str:id>/dashboard/', views.CompanyQuestion.as_view(), name='company_login'),
]
