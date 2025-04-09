from park_easy.settings import MINUTES_PARKING_30, MINUTES_PARKING_60
from park_easy.settings import VALUE_PARKING_30, VALUE_PARKING_60, VALUE_PARKING_ADD_HOUR

from django.utils import timezone
from datetime import timedelta


class ParkEasyRepository:

    @staticmethod
    def repo_get_all_or_one_obj(model, pk=None):
        if pk:
            obj = model.objects.get(pk=pk)
            return obj
        else:
            obj = model.objects.filter(is_active=True)
            return obj

    @staticmethod
    def repo_vacancie_occupied(model):
        vacancies_id = 1
        vacancies = model.objects.filter(id=vacancies_id).first()
        if vacancies:
            total_vacancies = vacancies.total_number_vacancies
            if vacancies.vacancies_occupied is not None:
                vacancies.vacancies_occupied = int(vacancies.vacancies_occupied + 1)
                vacancies.vacancies_free = int(total_vacancies - 1)
                return vacancies.save()

    @staticmethod
    def repo_vacancie_free(model):
        vacancies_id = 1
        vacancies = model.objects.filter(id=vacancies_id).first()
        if vacancies:
            total_vacancies = vacancies.total_number_vacancies
            if vacancies.vacancies_occupied is not None:
                vacancies.vacancies_occupied = int(vacancies.vacancies_occupied - 1)
                vacancies.vacancies_free = int(total_vacancies + 1)
                return vacancies.save()

    @staticmethod
    def repo_calculates_amount_payable(obj):
        entry = obj.entry
        output = timezone.now()

        total_time = output - entry

        if total_time <= timedelta(minutes=MINUTES_PARKING_30):
            amount_payable = VALUE_PARKING_30
        elif total_time <= timedelta(minutes=MINUTES_PARKING_60):
            amount_payable = VALUE_PARKING_60
        else:
            amount_payable = amount_payable + VALUE_PARKING_ADD_HOUR

        obj.total_time = str(total_time)
        obj.amount_payable = str(amount_payable)
        obj.output = output
