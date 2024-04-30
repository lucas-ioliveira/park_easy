
class ParkEasyRepository:

    @staticmethod
    def repo_get_all_or_one_obj(model, pk=None):
        if pk:
            obj = model.objects.get(pk=pk)
            return obj
        else:
            obj = model.objects.filter(is_active=True)
            return obj


