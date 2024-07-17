from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import UserSerializer, MenuSerializer, BookingSerializer


def index(request):
    "This function is just for return the index web page"
    return render(request, 'index.html', {})


class UserView(APIView):

    """
    This class handle POST request
    for creating/register new user
    """
    def post(self, request):
        """
        This method create new user
        """

        valid_data = UserSerializer(data=request.data)

        if valid_data.is_valid():
            user = valid_data.create(validated_data=valid_data)

            if user:

                return Response(valid_data.data, status=status.HTTP_201_CREATED)

        return Response(valid_data._errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        This method will return a list
        with every user registered
        """
        users = User.objects.all()

        users_serialized = UserSerializer(users, many=True)

        return Response(users_serialized.data, status=status.HTTP_200_OK)


# Create your views here. 
class MenuItemsView(ListCreateAPIView):
    """This class handles the GET and POST methods
    for menu entity"""
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """This class Handles the GET, PUT and DELETE methods
    for menu entity"""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    """This class handles differents HTTP
    methods for the booking entity"""
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
