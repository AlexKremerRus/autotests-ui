import pytest

from components.courses.create_course_form_component import CourseFormParams
from pages.courses.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.courses.create_course_page import CreateCoursePage

course_form_params_empty = CourseFormParams(
    title='',
    description='',
    estimated_time='',
    max_score='0',
    min_score='0'
)

course_form_params_tests = CourseFormParams(
    title='Playwright',
    description='Playwright',
    estimated_time='2 weeks',
    max_score='100',
    min_score='10'
)

course_form_params_tests_for_edit = CourseFormParams(
    title='Alex',
    description='Alex course',
    estimated_time='3 weeks',
    max_score='200',
    min_score='20'
)

course_form_params_tests_for_edit_post = CourseFormParams(
    title='Test A',
    description='Test A course',
    estimated_time='4 weeks',
    max_score='250',
    min_score='25'
)

card_params_tests = CheckVisibleCourseCardParams(
    index=0,
    title=course_form_params_tests.title,
    max_score=course_form_params_tests.max_score,
    min_score=course_form_params_tests.min_score,
    estimated_time=course_form_params_tests.estimated_time
)

card_params_tests_for_edit = CheckVisibleCourseCardParams(
    index=0,
    title=course_form_params_tests_for_edit.title,
    max_score=course_form_params_tests_for_edit.max_score,
    min_score=course_form_params_tests_for_edit.min_score,
    estimated_time=course_form_params_tests_for_edit.estimated_time
)

card_params_tests_for_edit_post = CheckVisibleCourseCardParams(
    index=0,
    title=course_form_params_tests_for_edit_post.title,
    max_score=course_form_params_tests_for_edit_post.max_score,
    min_score=course_form_params_tests_for_edit_post.min_score,
    estimated_time=course_form_params_tests_for_edit_post.estimated_time
)

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar.check_visible()

        create_course_page.image_upload_widget.check_visible()
        create_course_page.create_course_form.check_visible(course_form_params_empty)

        create_course_page.create_course_exercises_toolbar.check_visible()

        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_upload=True)

        create_course_page.create_course_form.fill(course_form_params_tests)
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(card_params_tests)

    def test_edit_course(self, create_course_page:CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar.check_visible()

        create_course_page.image_upload_widget.check_visible()
        create_course_page.create_course_form.check_visible(course_form_params_empty)

        create_course_page.create_course_exercises_toolbar.check_visible()

        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/cat.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_upload=True)

        create_course_page.create_course_form.fill(course_form_params_tests_for_edit)
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(card_params_tests_for_edit)

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(course_form_params_tests_for_edit_post)
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(card_params_tests_for_edit_post)

        # Комментарий - вопрос для Никиты
        # 1 - я использую дата класс - но тут лучше наверно уже использовать функцию - которая генерит данные и выплевывает объекта типа дата класс - чтобы не было хардкода именно данных
        # 2 - по факту я использую шаги из кейса создания курса - могу ли я просто вызвать функцию test_create_course ?
