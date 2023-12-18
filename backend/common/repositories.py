from django.db.models import Model, QuerySet
from django.forms import model_to_dict


class BaseRepository:
    model = None

    def __init__(self):
        if self.model is None:
            raise NotImplementedError
        self.base_qs = self.model.objects

    def get_values(self, *values: str) -> QuerySet[tuple]:
        return self.base_qs.all().values(*values)

    def get_values_list(self, *values: str) -> QuerySet[tuple]:
        return self.base_qs.all().values_list(*values, flat=True)

    def get_all(self):
        return self.base_qs.all()
