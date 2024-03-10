import factory
from faker import Faker

from other.models import OurContacts, PhoneNumbers, Schedule

fake = Faker()


class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule

    work_day = factory.Faker("word")
    start_work = factory.Faker("date_time")
    end_work = factory.Faker("date_time")


class PhoneNumbersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhoneNumbers

    number = factory.Faker("phone_number")


class OurContactsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OurContacts

    addres = factory.Faker("address")
    phone_number = factory.SubFactory(PhoneNumbersFactory)
