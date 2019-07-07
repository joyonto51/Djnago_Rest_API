from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models import Attendance


class SelectClassSectionView(APIView):
    def get(self, request, *args, **kwargs):
        class_list = ['One', 'Two', 'Three', 'Four', 'Five']

        data = {'classes': class_list,}

        return Response(data)

class TakeAttendanceView(APIView):
    def get(self, request, *args, **kwargs):
        class_name = request.GET.get('class_name')

        students = Attendance.objects.filter(school_class=class_name)
        student_data = []

        for student in students:
            data = {
                'name': student.name,
                'roll': student.roll,
                'attendance': student.attendance,
            }
            student_data.append(data)

        data = {'students': student_data,}

        return Response(data)

    def post(self, request, *args, **kwargs):
        data = request.data
        request.session['data'] = data['data']

        print("\n========= Student Data ==========\n")

        for student in data['data']:
            Attendance.objects.filter(roll=student['roll']).update(attendance=student['attendance'])

            print(student['name'], " Roll:", student['roll'], " Attendance:", student['attendance'])
            print("---------------------------------------------")

        return Response("Okay It's worked!!")
