from django.urls import path
from super_admin import views

urlpatterns = [
    path('login/', views.AdminLogin.as_view(), name='admin_login'),
    path('company/', views.AdminCompanies.as_view(), name='admin_login'),
    path('company/<str:id>', views.AdminCompanies.as_view(), name='admin_login')
]
