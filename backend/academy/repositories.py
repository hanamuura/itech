from django.db.models import QuerySet

from academy.models import Promotion, Course
from common.repositories import BaseRepository


class PromotionRepository(BaseRepository):
    model = Promotion


class CourseRepository(BaseRepository):
    model = Course
