from park_easy.repository import ParkEasyRepository
from cars.serializers import CarSerializer

class CarService:

    @staticmethod
    def service_get_all_or_one_cars(model, pk=None, request=None):
        if pk:
            car = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
            serializer = CarSerializer(car)
            return serializer
        if request:
            car = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
            serializer = CarSerializer(car, data=request.data, partial=True)
            return serializer
        else:
            cars = ParkEasyRepository.repo_get_all_or_one_obj(model)
            serializer = CarSerializer(cars, many=True)
            return serializer
    
    @staticmethod
    def service_post_or_update_car(request, car=None):
        if car:
            serializer = CarSerializer(car, data=request.data, partial=True)
            return serializer
        else:
            serializer = CarSerializer(data=request.data)
            return serializer

    @staticmethod
    def service_del_one_car(model, pk):
        car = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
        if car:
            car.is_active = False
            car.save()