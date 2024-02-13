from common.models import Image
from common.repositories import MetaRepository, ImageRepository


class ImageService:
    repository = ImageRepository

    @classmethod
    def create_image(cls, image: dict):
        image = cls.repository.save_model(**image)
        return image


class MetaService:
    repository = MetaRepository
    @classmethod
    def create_meta(cls, meta: dict):
        seo_image = ImageService.create_image(meta.image)


