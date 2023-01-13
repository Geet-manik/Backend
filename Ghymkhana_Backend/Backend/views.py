from django.shortcuts import render
 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import meeting,ugSenator,pgSenator,facultyExecutivebodie,studentExecutivebodie
from .serializers import meetingSerializer,ugSenatorSerializer,pgSenatorSerializer,facultyExcecutiveSerializer,studentExcecutiveSerializer
from rest_framework.decorators import api_view
# Create your views here.


# class meetingList(APIView):
@api_view(["GET"])
def getmeeting(request):
        meetings=meeting.objects.all()
        serializer=meetingSerializer(meetings, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def getugSenator(request):
        ugSenators=ugSenator.objects.all()
        serializer=ugSenatorSerializer(ugSenators, many=True)
        return Response(serializer.data)

      
@api_view(["GET"])
def getpgSenator(request):
        pgSenators=pgSenator.objects.all()
        serializer=pgSenatorSerializer(pgSenators, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def getfacultyExecutivebodie(request):
        facultyExecutives=facultyExecutivebodie.objects.all()
        serializer=facultyExcecutiveSerializer(facultyExecutives, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def getstudentExecutivebodie(request):
        studentExecutives=studentExecutivebodie.objects.all()
        serializer=studentExcecutiveSerializer(studentExecutives, many=True)
        return Response(serializer.data)