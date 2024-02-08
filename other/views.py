from django.shortcuts import render
from rest_framework import generics  # type: ignore

from .models import OurContacts, PhoneNumbers, Schedule
from .serializers import (
    OurContactsSerializer,
    PhoneNumbersSerializer,
    ScheduleSerializer,
)


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class PhoneNumberList(generics.ListAPIView):
    queryset = PhoneNumbers.objects.all()
    serializer_class = PhoneNumbersSerializer


class OurContactsList(generics.ListAPIView):
    queryset = OurContacts.objects.all()
    serializer_class = OurContactsSerializer
