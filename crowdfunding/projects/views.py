from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer, ProjectUpdateSerializer, ProjectUpdateDetailSerializer
from django.http import Http404, HttpResponse
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly


class ProjectList(APIView):

    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
                # either someone has to be logged in or info is read only 

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

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404
        # just for detail view !!!

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance = project,
            data = data,
            partial = True
            # okay if request doesn't include every single field in model
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, pk):
        try:
            project_to_delete = self.get_object(pk)
            project_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Http404

class ProjectUpdatesList(APIView):

    # has to handle get, post requests which are the methods
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        updates = project.project_updates.all() 
        serializer = ProjectUpdateSerializer(updates, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ProjectUpdateSerializer(data=request.data)
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

class ProjectUpdateDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            updates = project.project_updates.all() 
            # serializer = ProjectUpdateDetailSerializer(updates)
            self.check_object_permissions(self.request, updates)
            return updates
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        update = self.get_object(pk)
        serializer = ProjectUpdateDetailSerializer(update)
        return Response(serializer.data)

    def put(self, request, pk):
        edit_update = self.get_object(pk)
        data = request.data
        serializer = ProjectUpdateDetailSerializer(
            instance = edit_update,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                # update to update request  ??
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

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

class PledgeDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly
        ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(
            instance = pledge,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
        # return Response(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                # update to update request  ??
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )