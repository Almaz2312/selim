import pytest

from other.factories import OurContactsFactory, PhoneNumbersFactory, ScheduleFactory


@pytest.mark.django_db
def test_schedule_factory():
    schedule_instance = ScheduleFactory()

    assert schedule_instance is not None
    assert schedule_instance.work_day
    assert schedule_instance.start_work
    assert schedule_instance.end_work


@pytest.mark.django_db
def test_phone_numbers_factory():
    phone_numbers_instance = PhoneNumbersFactory()

    assert phone_numbers_instance is not None
    assert phone_numbers_instance.number


@pytest.mark.django_db
def test_our_contacts_factory():
    our_contacts_instance = OurContactsFactory()

    assert our_contacts_instance is not None
    assert our_contacts_instance.addres
    assert our_contacts_instance.phone_number is not None
