from park_easy.repository import ParkEasyRepository

class ParkEasyService:

    @staticmethod
    def service_get_all_or_one(model, app_serializer, pk=None, request=None):
        if pk:
            obj = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
            serializer = app_serializer(obj)
            return serializer
        if request:
            obj = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
            serializer = app_serializer(obj, data=request.data, partial=True)
            return serializer
        else:
            obj = ParkEasyRepository.repo_get_all_or_one_obj(model)
            serializer = app_serializer(obj, many=True)
            return serializer
    
    @staticmethod
    def service_post_or_update(request, obj=None, app_serializer=None):
        if obj:
            serializer = app_serializer(obj, data=request.data, partial=True)
            return serializer
        else:
            serializer = app_serializer(data=request.data)
            return serializer

    @staticmethod
    def service_del_one(model, pk):
        obj = ParkEasyRepository.repo_get_all_or_one_obj(model, pk)
        if obj:
            obj.is_active = False
            obj.save()