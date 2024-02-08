from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # type: ignore


class Schedule(models.Model):
    work_day = models.CharField(max_length=500)  # type: ignore
    start_work = models.DateTimeField()  # type: ignore
    end_time = models.DateTimeField()  # type: ignore

    def __str__(self) -> str:
        return self.work_day


class PhoneNumbers(models.Model):
    number = PhoneNumberField()

    class Meta:
        verbose_name = "PhoneNumbers"
        verbose_name_plural = "PhoneNumbers"

    def __str__(self) -> str:
        return f"{self.number}"


class OurContacts(models.Model):
    addres = models.CharField(max_length=500)  # type: ignore
    phone_number = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE)  # type: ignore

    def __str__(self) -> str:
        return f"{self.addres}"


class Meta:
    verbose_name = "OurContacts"
    verbose_name_plural = "OurContacts"
