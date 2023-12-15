from django.db.models import Model, QuerySet
from django.forms import model_to_dict


class BaseRepository:
    model = None

    def __init__(self):
        self.base_qs = self.model.objects.all()

    def get_dict_qs(self, *exclude_fields) -> dict:
        data = []

        for m in self.qs:
            m_dict = dict()
            m_d = model_to_dict(m)
            for key, val in m_d.items():
                if key not in exclude_fields:
                    m_dict[key] = val
            data.append(m_dict)
        return {'res': data}
