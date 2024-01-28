import json

from django.http import JsonResponse
from django.views import View

from academy.models import Promotion
from academy.repositories import PromotionRepository
from academy.views import get_academy_promotions


class AdminPromotionsView(View):
    def get(self, request):
        return JsonResponse({})

    def post(self, request):
        data = json.loads(request.body)

        promotion = Promotion()

        promotion.name = data['name']
        promotion.description = data['description']
        promotion.dt_start = data['dt_start']
        promotion.dt_end = data['dt_end']
        promotion.image_id = data['image_id']
        promotion.meta_id = data['meta_id']

        promotion_repo = PromotionRepository(promotion)
        promotion_repo.save_model()
