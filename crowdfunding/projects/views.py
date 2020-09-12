from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all() # list  of all projects available in database
        serializer = ProjectSerializer(projects, many=True) # get serializer, give it list of projects 
        return Response(serializer.data) # send all of serializer data

    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user) # save data to database
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectDetail(APIView):

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except:
            ProjectDetail.DoesNotExist
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)


class PledgeList(APIView):

    # has to handle get, post requests which are the methods
    def get(self, request):
        pledges = Pledge.objects.all() #get all pledges from database
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data) # return serializer from data

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )