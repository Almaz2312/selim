from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from .models import OurContacts, PhoneNumbers, Schedule
from .views import OurContactsList, PhoneNumberList, ScheduleList


class NewsTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        schedule = [
            Schedule(
                work_day="monday",
                start_work="2024-02-04,08:00",
                end_time="2024-02-04,16:00",
            ),
            Schedule(
                work_day="monday",
                start_work="2023-02-04 08:00:00",
                end_time="2023-02-04 16:00:00",
            ),
        ]
        Schedule.objects.bulk_create(schedule)

    def test_list(self):
        request = self.factory.get("api/v1/schedule/")
        view = ScheduleList.as_view()
        response = view(request)

        # print(response.data)

        assert response.status_code == 200


class NumbersTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        phone = [
            PhoneNumbers(number="+996559951309"),
            PhoneNumbers(number="+9960559951009"),
        ]
        PhoneNumbers.objects.bulk_create(phone)

    def test_list(self):
        request = self.factory.get("api/v1/phone_numbers/")
        view = PhoneNumberList.as_view()
        response = view(request)

        # print(response.data)

        assert response.status_code == 200


class OurContactsListTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.phone_number = PhoneNumbers.objects.create(number="+9960559591009")
        our_contact = [
            OurContacts(addres="Bishkek", phone_number=self.phone_number),
            OurContacts(addres="Tokmok", phone_number=self.phone_number),
        ]
        OurContacts.objects.bulk_create(our_contact)

    def test_list(self):
        request = self.factory.get("api/v1/our_contacts/")
        view = OurContactsList.as_view()
        response = view(request)

        # print(response.data)

        assert response.status_code == 200
