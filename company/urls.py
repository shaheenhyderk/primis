from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CompanyLogin.as_view(), name='company_login'),
    path('questions/', views.CompanyQuestion.as_view(), name='company_login'),
]
