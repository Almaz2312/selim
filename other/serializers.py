from rest_framework.serializers import ModelSerializer

from .models import OurContacts, PhoneNumbers, Schedule


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class OurContactsSerializer(ModelSerializer):
    class Meta:
        model = OurContacts
        fields = "__all__"


class PhoneNumbersSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = "__all__"
