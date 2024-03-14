from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Ticket,Employee,DutyRoster
from datetime import datetime

class TicketAPIView(APIView):
    def post(self,request):
        # Create tickets
        try:
            ticket_obj=Ticket.objects.create(
                ticket_number=request.data['ticket_number'],
                description =request.data.get('description'),
                resolution_end_date =request.data['resolution_end_date'],
                ticket_time = request.data['ticket_time']
                 )
            # function for automatically allocate the ticket
            self.allocate_ticket(ticket_obj)
            return Response({'id':ticket_obj.id,"message":"Successfully Created Ticket"},status=200)
        except:
            return Response({'error': 'Something went wrong and check db connection'}, status=400)

    def get(self,request):
        # Get ticket details
        try:
            ticket_obj=Ticket.objects.all().values()
            return Response({"ticket_obj":ticket_obj},status=200)
        except:
            return Response({'error': 'Something went wrong and check db connection'}, status=400)

    def put(self,request,id):
        try:
            if not Ticket.objects.filter(id=id).first():
                return Response({"message":"Data not Found"},status=400)
            Ticket.objects.filter(id=id).update(
                ticket_number=request.data.get('ticket_number'),
                description =request.data.get('description'),
                resolution_end_date =request.data.get('resolution_end_date'),
                ticket_time=request.data['ticket_time']

            )
            return Response({'id':id,"message":"Successfully Updated Ticket"},status =200)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket object does not exist and check db connection'}, status=400)
    def delete(self, request, id):
        try:
            Ticket.objects.get(id=id).delete()
            return Response({"message":"Deleted ticket Successfully"}, status=200)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket object does not exist and check db connection'}, status=400)

    def allocate_ticket(self, ticket):
        print("allocate")
        current_date = ticket.creation_date.date()
        # based on duty roster get the available employees and order by shift time
        available_employees = DutyRoster.objects.filter(date=current_date, is_available=True,is_leave=False).order_by(
            'shift_start')
        for employee in available_employees:

            #check if the employee have ticket already
            if not Ticket.objects.filter(creation_date=current_date, assigned_employee=employee.employee).exists():
                left_time=employee.shift_start.hour - employee.shift_end.hour
                print(left_time)
                print(ticket.ticket_time.date())
                print(ticket.ticket_time.hour)
                print("assigning a ticket")
                ticket.assigned_employee = employee.employee
                ticket.save()
                employee.is_available = False
                employee.save()
                return
        #  reset availability if all user have tickets
        DutyRoster.objects.filter(date=current_date).update(is_available=True)
        return self.allocate_ticket(ticket)


class EmployeeAPIView(APIView):

    def post(self,request):
        try:
            employee_obj=Employee.objects.create(
                employee_name=request.data['employee_name'],
                address =request.data.get('address'),
                employee_number =request.data['employee_number']
                 )
            return Response({'id':employee_obj.id,"message":"Successfully Created Employee"},status=200)
        except:
            return Response({'error': 'Something went wrong and check db connection'}, status=400)

    def get(self,request):
        try:
            employee_obj = Employee.objects.all().values()
            return Response({"employee_obj": employee_obj}, status=200)
        except:
            return Response({'error': 'Something went wrong and check db connection'}, status=400)

class DutyRosterAPIView(APIView):
    def post(self,request):
        try:
            duty_roster_obj=DutyRoster.objects.create(
                employee_id=request.data['employee'],
                date=request.data['date'],
                is_available =request.data['is_available'],
                shift_start=request.data.get('shift_start'),
                shift_end=request.data['shift_end'],
                is_leave=request.data['is_leave']
                 )
            return Response({'id':duty_roster_obj.id,"message":"Successfully Created DutyRoster"},status=200)
        except:
            return Response({'error': 'Something went wrong and check db connection'}, status=400)


class DashboardAPIView(APIView):
    def get(self,request):
        date_param = request.query_params.get('date')
        if date_param:
            date = datetime.strptime(date_param, '%Y-%m-%d').date()
        else:
            date = datetime.now().date()
        duty_roster = DutyRoster.objects.filter(date=date).order_by('shift_start')
        employees_data = []
        for duty in duty_roster:
            employee_data = {
                'name': duty.employee.employee_name,
                'start_time': duty.shift_start,
                'end_time': duty.shift_end,
                'availability': duty.is_available,
                'on_leave':duty.is_leave,
                'allocated_tickets': Ticket.objects.filter(assigned_employee=duty.employee,
                                                           creation_date__date=date)
            }
            employees_data.append(employee_data)
        return render(request, 'dashboard.html', {'employees_data': employees_data,'date':date})


