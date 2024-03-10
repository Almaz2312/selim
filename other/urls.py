from django.urls import path

from .views import OurContactsList, PhoneNumberList, ScheduleList

urlpatterns = [
    path("schedule/", ScheduleList.as_view()),
    path("phone_number/", PhoneNumberList.as_view()),
    path("our_contacts/", OurContactsList.as_view()),
]
