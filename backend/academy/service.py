from academy.repositories import CourseRepository


class CourseService:
    repository = CourseRepository

    @classmethod
    def create_course(cls, course_obj):

