from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.serializers import *
from api.models import *
from rest_framework import status
from rest_framework.viewsets import ViewSet
# Create your views here.

users=[
    {"id":1,"name":"John","phone":85950484940,"plan":"299 DUL"},
    {"id":2,"name":"Anugrah","phone":85950484941,"plan":"199 TT"},
    {"id":3,"name":"Arjun","phone":85950484942,"plan":"799 DUL"},
    {"id":4,"name":"Vyshnav","phone":85950484943,"plan":"1299 DUL"}
]
#localhost:8000/users - GET
#localhost:8000/users - POST -{'id'-5}

@api_view(["GET","POST"])
def getUsers(request,*args,**kwargs):
    if request.method=="GET":
        return Response(data=users)
    elif request.method=="POST":
        print(request.data)
        users.append(request.data)
        return Response(data=users)

@api_view(["GET","DELETE"])  
def getSpecificUser(request,*args,**kwargs):
    if request.method=="GET":
        uid=kwargs.get('id')
        user=[i for i in users if i["id"]==uid].pop()
        print(user)
        return Response(data=user)
    elif request.method=="DELETE":
        uid=kwargs.get('id')
        data=[i for i in users if i["id"]!=uid]
        return Response(data=data)

class AssignmentView(APIView):
    def post(self,request,**kwargs):
        jsondata=request.data
        dser=AssignmentSerializer(data=jsondata)
        if dser.is_valid():
            title=dser.validated_data.get("title")
            desc=dser.validated_data.get("description")
            ldate=dser.validated_data.get("last_date")
            Assignments.objects.create(title=title,description=desc,last_date=ldate)
            return Response(data={"msg":"Success"})
        return Response(data={"msg":dser.errors})
    def get(self,request):
        qs=Assignments.objects.all()
        ser=AssignmentSerializer(qs,many=True)
        return Response(data=ser.data)


class SpesificAssignmentView(APIView):
    def get(self,request,**kwargs):
        did=kwargs.get('id')
        full=Assignments.objects.get(id=did)
        serdata=AssignmentSerializer(full)
        return Response(data=serdata.data)
    
    def delete(self,request,**kwargs):
        did=kwargs.get('id')
        Assignments.objects.get(id=did).delete()
        qs=Assignments.objects.all()
        ser=AssignmentSerializer(qs,many=True)
        return Response(data=ser.data)
    def put(self,request,**kwargs):
        did=kwargs.get('id')
        full=Assignments.objects.get(id=did)
        serdata=AssignmentSerializer(data=request.data)
        if serdata.is_valid():
            title=serdata.validated_data.get('title')
            description=serdata.validated_data.get('description')
            ldate=serdata.validated_data.get('last_date')
            full.title=title
            full.description=description
            full.last_date=ldate
            full.save()
            return Response(data={'msg':"Updated"})
        return Response(data=serdata.errors)



class TeacherView(APIView):
    def post(self,request):
        dser=TeacherSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def get (self,request):
        data=Teacher.objects.all()
        ser=TeacherSerializer(data,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    
class SpeficTeacherView(APIView):
    def get (self,request,**kwargs):
        did=kwargs.get('id')
        dat=Teacher.objects.get(id=did)
        ser=TeacherSerializer(dat)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def delete (self,request,**kwargs):
        did=kwargs.get('id')
        dat=Teacher.objects.get(id=did).delete()
        full=Teacher.objects.all()
        ser=TeacherSerializer(full)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def put(self,request,**kwargs):
        did=kwargs.get('id')
        teach=Teacher.objects.get(id=did)
        desr=TeacherSerializer(data=desr.data,instance=teach)
        if desr.is_valid():
            desr.save()
            return Response(data=desr.data,status=status.HTTP_200_OK)
        return Response(data=desr.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class TeacherViewSet(ViewSet):
    def create(self,request):
        dser=TeacherSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        ser=TeacherSerializer(Teacher.objects.all(),many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def retrieve(self,request,pk=0):
        teach=Teacher.objects.get(id=pk)
        ser=TeacherSerializer(teach)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def update(self,request,pk=0):
        teach=Teacher.objects.get(id=pk)
        dser=TeacherSerializer(data=request.data,instance=teach)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=0):
        teach=Teacher.objects.get(id=pk)
        teach.delete()
        return Response(data={"msg":"Deleted"},status=status.HTTP_200_OK)
    
class TodoView(ViewSet):
    def create(self,request):
        dser=TodoSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def list(self,request):
        ser=TodoSerializer(Todo.objects.all(),many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def retrieve(self,request,pk=0):
        ser=TodoSerializer(Todo.objects.get(id=pk))
        return Response(data=ser.data,status=status.HTTP_200_OK)
    def update(self,request,pk=0):
        todo=Todo.objects.get(id=pk)
        dser=TodoSerializer(data=request.data,instance=todo)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=0):
        todo=Todo.objects.get(id=pk)
        todo.delete()
        return Response({"data":"Deleted"},status=status.HTTP_200_OK)