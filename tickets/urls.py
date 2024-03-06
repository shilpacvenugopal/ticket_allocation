from django.urls import path
from .views import TicketAPIView, EmployeeAPIView, DutyRosterAPIView,DashboardAPIView
urlpatterns = [
    path('ticket/', TicketAPIView.as_view()),
    path('ticket/<uuid:id>/', TicketAPIView.as_view()),
    path('employee/', EmployeeAPIView.as_view(),name='employee_create'),
    path('duty_roster/', DutyRosterAPIView.as_view()),

    path('dashboard/', DashboardAPIView.as_view()),

]

