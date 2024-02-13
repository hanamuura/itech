import base64

from pydantic import ValidationError

from academy.models import Course
from academy.repositories import CourseRepository
from academy.schemas import CourseSchema


class CourseService:
    repository = CourseRepository()

    @classmethod
    def encode_image(cls):
        with open('images.jpg', 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string

    @classmethod
    def patch(cls, new_data: dict, course_id: int):
        old_course: Course = cls.repository.get_single(id=course_id)
        old_course.name = new_data.get('name', old_course.name)
        old_course.discount = new_data.get('discount', old_course.discount)
        old_course.price = new_data.get('price', old_course.price)
        old_course.block_content = new_data.get('block_content', old_course.block_content)
        old_course.image = new_data.get('image', old_course.image)
        old_course.meta = new_data.get('meta', old_course.meta)
        try:
            schema = CourseSchema.model_validate(old_course).model_dump()
            old_course.save()
            return schema
        except ValidationError:
            return {}
