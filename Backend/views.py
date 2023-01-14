from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import meeting,ugSenator,pgSenator,facultyExecutivebodie,studentExecutivebodie,upcomingEvent
from .serializers import meetingSerializer,ugSenatorSerializer,pgSenatorSerializer,facultyExcecutiveSerializer,studentExcecutiveSerializer,upComingSerializer
from rest_framework.decorators import api_view
# Create your views here.


# class meetingList(APIView):
def home(request):
    response= requests.get('http://127.0.0.1:8001/faculty/?format=json').json()
    response1 =requests.get('http://127.0.0.1:8001/student/?format=json').json()
    return render(request,'main/home.html',{'response':response,'response1':response1})
    



def Senate(request):
    res2=requests.get('http://127.0.0.1:8001/ugsenator/?format=json').json()
    response3=requests.get('http://127.0.0.1:8001/pgsenator/?format=json').json()
    return render(request,'main/Senate.html',{'res2':res2,'response3':response3})


def minutes(request):
    res3=requests.get('http://127.0.0.1:8001/meeting/?format=json').json()
    return render(request,'main/minutes.html',{'res3':res3})


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

@api_view(["GET"])
def getupComing(request):
        upComings=upcomingEvent.objects.all()
        serializer=upComingSerializer(upComings, many=True)
        return Response(serializer.data)

