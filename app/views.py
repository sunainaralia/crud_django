from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class AddAndChangeUser(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "success": True,
                    "msg": "User data is posted successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

    def get(self, request, pk=None, format=None):
        if pk is None:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
            return Response(
                {
                    "success": True,
                    "msg": "All user data is retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            try:
                data = User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise Http404
            serializer = UserSerializer(data)
            return Response(
                {
                    "success": True,
                    "msg": "User is retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

    def patch(self, request, pk, format=None):
        try:
            data = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "msg": "User information is changed successfully",
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request, pk, format=None):
        try:
            data = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        data.delete()
        return Response(
            {"success": True, "msg": "User is deleted successfully"},
            status=status.HTTP_200_OK,
        )
