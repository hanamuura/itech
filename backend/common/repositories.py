from django.db.models import Model, QuerySet
from django.forms import model_to_dict

from common.models import Image, Meta


class BaseRepository:
    model = None

    def __init__(self, instance=None):
        if self.model is None:
            raise NotImplementedError
        self.base_qs = self.model.objects
        self.instance = instance

    def get_values(self, *values: str) -> QuerySet[tuple]:
        return self.base_qs.all().values(*values)

    def get_values_list(self, *values: str) -> QuerySet[tuple]:
        return self.base_qs.all().values_list(*values, flat=True)

    def get_all(self):
        return self.base_qs.all()

    def get_single(self, **kwargs):
        return self.base_qs.filter(**kwargs).first()

    def save_model(self, **kwargs):
        self.base_qs.save(**kwargs)


class ImageRepository(BaseRepository):
    model = Image


class MetaRepository(BaseRepository):
    model = Meta
