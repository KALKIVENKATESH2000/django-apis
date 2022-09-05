from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Employees_List),
    path('add/', views.employees_add),
    path('update/<str:pk>/', views.employees_update),
    path('delete/<str:pk>/', views.employee_delete),

]