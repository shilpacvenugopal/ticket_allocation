from django.db import models
import uuid

class Employee(models.Model):
    class Meta:
        db_table = '"tickets_employee"'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=100)

class Ticket(models.Model):
    class Meta:
        db_table = '"tickets_details"'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket_number = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ticket_time = models.TimeField(null=True, blank=True)
    resolution_end_date = models.DateField(null=True, blank=True)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

class DutyRoster(models.Model):
    class Meta:
        db_table = '"tickets_duty_roster"'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    is_available = models.BooleanField(default=True)
    is_leave = models.BooleanField(default=False)

